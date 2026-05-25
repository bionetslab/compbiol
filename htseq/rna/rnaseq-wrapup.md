# Mini-project
## Step 1: (optional) Download data from GEO (GSE231587)
It could make sense to go to the GEO website once, to check out how it looks and where to obtain the data.

This step is time consuming and requires a powerful computer, so if you don't have the time, just try to find out 
- what GEO is.
- what the SRA is.
- download data using fetchNGS (nf-co.re) pipeline (one sample).

## Step 2: (optional) preprocess the data using nfcore/scrnaseq
nf-co.re/scrnaseq

## Step 3: Do cell type annotation.
The data is already preprocessed. You can download the data using the link provided here. The dataset is from a study on Multiple sclerosis lesions in the brain. You can look at this paper https://www.neurology.org/doi/10.1212/NXI.0000000000200213 for further information on the study.

## Step 3.0 Look at the data
1. Which cell types do you find? Look at the paper to see which ones are annotated?
2. How was the data annotated?
3. 
## Step 3.1 Quality control
Perform standard QC. Check
- Mitochondrial content
- Ribosomal Content
- Number of cells and genes
- Doublets
- Ambient RNA?
  

## Step 3.2 Annotate the clusters
- Use two complementary methods.
The preprocessed dataset can be found at: https://zenodo.org/records/17733765/files/snRNA.tar.gz?download=1

## Step 4: Pseudobulking (new) and differential expression
- Run differential expression analysis for the pseudobulked expression datasets. Pseudobulking refers to simply summing up the counts from a sample to create a pseudobulk sample. As an example, given that we have 3 patients where we sequenced 5 celltypes each. We can aggregate those to 5 pseudobulk samples per patient, one for each celltype. Then, we can use DESeq2 on the psudobulked samples. We use psuedobulking to overcome the problem of 'pseudoreplication' which arises because the cells from one sample are heavily correlated. However, statistical test often assume independece of the samples. In order to avoid spurious results, we aggregate the data to sample level.
- You can pick one or two conditions to compare, because there are many possibilities to do comparisons given the data. (e.g. compare two celltypes, or compare two conditions within the same cell type)

## Step 5: Run downstream analysis:
### 5.1 Run gene set enrichment analysis on the results of the differential expression analysis
- Recall what an overrepresentation test is
- You can use tools like gprofiler (https://biit.cs.ut.ee/gprofiler/gost) on the web or GSEApy using a script

### 5.2. Are the interactions between the celltypes in the dataset
- Recall how Liana+ computes the p-values for interactions between cell types.
- You can use tools like LIANA+ to find interactions between celltypes (https://liana-py.readthedocs.io/en/latest/)

## 5.3 Gene regulatory networks
- Choose a dataset to compute a GRN for. You can use SCENIC to infer the network, you can even use SCENI+ when downloading the data ATAC data from zendod: https://zenodo.org/records/17733765/files/snATAC.tar.gz?download=1 Otherwise you can also use GRNboost2 https://arboreto.readthedocs.io/en/latest/algorithms.html Pick one celltype and potentially subsample the cells to make the tool run faster, if it takes too long. YOu can also preselect genes, to choose only highly expressed ones.

## 5.4. Find another downstream analysis for scRNASeq or bulk data and run it on the data
- Which method did you choose and why?
- What are the results.

## 6 Evaluate you results.
- Are your results in line with known biology?
- Are there unexpected findings.
- What can you easily explain, what is difficult?
- 
