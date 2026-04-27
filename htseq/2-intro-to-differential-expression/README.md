# Introduction to Differential Expression Analysis

A hands-on tutorial covering bulk RNA-seq differential expression analysis with
**PyDESeq2**, followed by a comparison to the nf-core `differentialabundance` pipeline.

## Resources

- 📖 **PyDESeq2 documentation**: https://pydeseq2.readthedocs.io/
- 📖 **DESeq2 paper** (Love *et al.*, 2014): https://doi.org/10.1186/s13059-014-0550-8
- 📖 **nf-core differentialabundance**: https://nf-co.re/differentialabundance
- 📖 **nf-core getting started**: https://nf-co.re/docs/usage/getting_started/introduction

## Getting started

This tutorial uses [pixi](https://pixi.sh) for environment management.

```bash
# Install pixi (if not already installed)
curl -fsSL https://pixi.sh/install.sh | bash

# Install all dependencies and launch the notebook
pixi run notebook
```

If you want to use pixi from VS Code, create a pixi kernel first:

```bash
pixi run install-kernel
```

The kernel created by the command above is called `pixi_de_intro` and can be
selected via the kernel-selection tool in VS Code.

## Data

Supply the data files in the `data/` folder before opening the notebook:

| File | Description |
|------|-------------|
| `data/counts.tsv` | Raw gene-level count matrix (genes × samples, tab-separated) |
| `data/metadata.tsv` | Sample metadata (samples × variables, tab-separated). Must contain a `condition` column. |

> **Note:** Large data files are excluded by `.gitignore` and must **not** be committed.

## Tutorial sections

Open `tutorial.ipynb` and work through the sections in order:

| Section | Topic |
|---------|-------|
| 0 | Imports |
| 1 | Load count matrix and metadata |
| 2 | Pre-processing: filter low-count genes |
| 3 | Run PyDESeq2 (model fitting, Wald test, results) |
| 4 | Visualize results (MA plot, volcano plot, heatmap) |
| 5 | Export results |
| 6 | nf-core `differentialabundance` pipeline |

Section 6 is split into three steps:

| Step | Description |
|------|-------------|
| 6 — Step 1 | Install Nextflow and a container engine |
| 6 — Step 2 | Understand the required input files for the pipeline |
| 6 — Step 3 | Run the pipeline and compare its output to your manual analysis |

## Results

At the end of the session you will have produced:

1. `output/de_results.csv` — full DE results table from PyDESeq2
2. `output/de_results_significant.csv` — significant DE genes only
3. `output/ma_plot.png`, `output/volcano_plot.png`, `output/heatmap_top_de_genes.png` — figures
4. `nfcore_run/results/` — nf-core pipeline output (after running Step 3)
