"""
prepare_data.py

Step 1 of the candy classification practical:
- Detect the black backing paper (not just the biggest square that fits)
- Crop the RGB photo to that square
- Convert the crop to grayscale
- Save both versions for use in napari

Expected layout:
    project/
    |-- data_raw/         put your .jpg photos here
    |-- data_cropped/     created by this script
    |-- data_grayscale/   created by this script

Run with:
    pixi run python prepare_data.py
"""

from pathlib import Path

import numpy as np
from skimage import io, color, img_as_ubyte
from skimage.filters import threshold_otsu
from skimage.transform import resize

RAW_DIR = Path("data_raw")
CROP_DIR = Path("data_cropped")
GRAY_DIR = Path("data_grayscale")


def detect_black_square_bbox(img_rgb: np.ndarray, dark_row_col_frac: float = 0.05):
    """Find the bounding box of the black square backing paper.

    Assumes the paper is noticeably darker than the outer mat/background.
    Any row/column with at least `dark_row_col_frac` fraction of dark pixels
    is considered part of the square (this tolerates candies/sugar covering
    parts of the paper -- the gaps between them are still dark).

    Returns (top, bottom, left, right), cropped to an exact square window
    centered on the detected box.
    """
    gray = color.rgb2gray(img_rgb)
    thresh = threshold_otsu(gray)
    dark_mask = gray < thresh

    row_frac = dark_mask.mean(axis=1)
    col_frac = dark_mask.mean(axis=0)
    row_idx = np.where(row_frac > dark_row_col_frac)[0]
    col_idx = np.where(col_frac > dark_row_col_frac)[0]

    if row_idx.size == 0 or col_idx.size == 0:
        raise ValueError(
            "Could not detect a dark square -- try adjusting "
            "dark_row_col_frac or check the photo's lighting."
        )

    top, bottom = int(row_idx.min()), int(row_idx.max())
    left, right = int(col_idx.min()), int(col_idx.max())

    # Force an exact square (photos are rarely pixel-perfect), centered on
    # the detected box rather than stretching/skewing it.
    h, w = bottom - top, right - left
    side = min(h, w)
    cy, cx = (top + bottom) // 2, (left + right) // 2
    top, left = cy - side // 2, cx - side // 2
    bottom, right = top + side, left + side
    return top, bottom, left, right


def main():
    CROP_DIR.mkdir(exist_ok=True)
    GRAY_DIR.mkdir(exist_ok=True)

    paths = sorted(RAW_DIR.glob("*.jpg"))
    if not paths:
        print(f"No .jpg files found in {RAW_DIR.resolve()}")
        return

    for path in paths:
        img_rgb = io.imread(path)  # (H, W, 3) uint8

        # 1) crop to the detected black square
        top, bottom, left, right = detect_black_square_bbox(img_rgb)
        cropped = img_rgb[top:bottom, left:right]
        cropped = resize(
            cropped,
            (224, 224, 3),
            anti_aliasing=True,
            preserve_range=True,
        ).astype(np.uint8)

        io.imsave(CROP_DIR / path.name, cropped)

        # 2) grayscale (rgb2gray returns float 0-1, convert back to uint8)
        gray = img_as_ubyte(color.rgb2gray(cropped))

        io.imsave(GRAY_DIR / path.name, gray)

        print(
            f"{path.name}: {img_rgb.shape} -> square "
            f"rows[{top}:{bottom}] cols[{left}:{right}]"
        )


if __name__ == "__main__":
    main()
