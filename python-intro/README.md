# Part 1: Python intro

This folder contains introductory Python notebooks.

If you are completely new to Python, follow the steps below exactly.

## 1) Install Conda (one-time setup)

You need a package manager called **Conda**.

Recommended: install **Miniforge** (lightweight Conda):
- https://github.com/conda-forge/miniforge

After installation, open a new terminal and check:

```bash
conda --version
```

If you see a version number, you are ready.

Optional (faster): install **Mamba** after creating your Conda setup:

```bash
conda install -n base -c conda-forge mamba
```

Then check:

```bash
mamba --version
```

## 2) Clone the repository from GitHub

If you do not have the files yet, run:

```bash
git clone https://github.com/bionetslab/compbiol.git
```

This creates a local folder named `compbiol`.

## 3) Open a terminal in the cloned repository

Go into the cloned repository and then into `python-intro`:

```bash
cd compbiol
cd python-intro
```

## 4) Create the teaching environment

Run this command once:

```bash
conda env create -f environment.yml
```

If you installed Mamba, you can use this faster equivalent command:

```bash
mamba env create -f environment.yml
```

This installs Python and all libraries needed by the notebooks.

## 5) Activate the environment

Activate it every time you start working:

```bash
conda activate python-intro
```

Your terminal prompt should now show `(python-intro)`.

Note: activation is the same for Conda and Mamba.

## 6) Launch JupyterLab

Start JupyterLab from inside `python-intro`:

```bash
jupyter lab
```

A browser tab should open automatically.

Then open notebooks in this order:
1. `1_first_steps.ipynb`
2. `2_data_handling.ipynb`
3. `3_functions_and_classes.ipynb`
4. `4_visualization_with_seaborn.ipynb`
5. `5_reproducible_Python.ipynb`
6. `project_tcga_brca.ipynb`

## 7) Run cells

Inside each notebook:
- Click the first code cell.
- Press **Shift+Enter** to run it.
- Continue cell-by-cell from top to bottom.

## 8) Next session: start again quickly

From the repository root:

```bash
cd python-intro
conda activate python-intro
jupyter lab
```

## Troubleshooting

### `conda: command not found`
- Close and reopen terminal after installing Miniforge.
- If needed, restart your computer once so shell settings are refreshed.

### `mamba: command not found`
Install Mamba into base environment:

```bash
conda install -n base -c conda-forge mamba
```

### Environment already exists
If you changed `environment.yml`, recreate environment:

```bash
conda env remove -n python-intro
conda env create -f environment.yml
```

Mamba equivalent for recreate:

```bash
mamba env remove -n python-intro
mamba env create -f environment.yml
```

### Kernel is not the right one
In JupyterLab, switch kernel to **python-intro**.

### Stop JupyterLab
Back in the terminal, press **Ctrl+C**.
