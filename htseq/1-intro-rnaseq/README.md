# Introduction to Single-Cell RNA-seq

An introductory assignment covering the full single-cell RNA-seq analysis pipeline:
quality control, cell filtering, normalization, dimensionality reduction, clustering,
manual cell-type annotation, differential expression, and result export.

## Resources

- 📖 **Single-Cell Best Practices** (primary reference): https://www.sc-best-practices.org/
- 📖 **Scanpy documentation**: https://scanpy.readthedocs.io/
- 📖 **AnnData documentation**: https://anndata.readthedocs.io/

## Getting started

This repository uses [pixi](https://pixi.sh) for environment management.

```bash
# Install pixi (if not already installed)
curl -fsSL https://pixi.sh/install.sh | bash

# Install all dependencies and launch the notebook
pixi run notebook
```

If you want to use pixi from vscode, the easiest solution I found was to create a pixi kernel, which can then be loaded via the kernel selection tool in vscode. The kernel created when running the command below is called pixi_scrna_intro.
```
pixi run install-kernel
```

## Assignment

Open `assignment.ipynb` and work through the sections in order:

| Section | Topic |
|---------|-------|
| 0 | Imports |
| 1 | Load Data |
| 2 | Quality Control (QC) |
| 3 | Cell & Gene Filtering |
| 4 | Normalization & Feature Selection |
| 5 | Dimensionality Reduction & Clustering |
| 6 | Marker Gene Visualization |
| 7 | Manual Cell Type Annotation |
| 8 | Differential Expression |
| 9 | Save Results |

The test data object (`*.h5ad`) is provided in the `data/` folder and must **not** be committed.

## Submission

Commit **only** these files:

1. `assignment.ipynb` — your completed notebook
2. `obs.tsv` — `adata.obs` exported as tab-separated text (must contain `manual_celltype_labels`)
3. `de_results.csv` — differential expression results

Do **not** commit `.h5ad`, `.h5`, or other large binary data files.

## Automated testing
You can check whether you 

```bash
pixi run test
```

The test suite checks:
- `obs.tsv` is present, tab-separated, and contains a `manual_celltype_labels` column
  with non-empty labels for every cell
- A DE results CSV with the expected columns is present
- The notebook contains the required analysis steps in the correct order

