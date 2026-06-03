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
| `data/read_counts.tsv` | Raw gene-level count matrix (genes × samples, tab-separated) |
