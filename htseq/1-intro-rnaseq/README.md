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
