# NGS Quality Control Pipeline (Snakemake)

## Overview

This project implements an automated **Next-Generation Sequencing (NGS) Quality Control pipeline** using Snakemake.
It performs read trimming, quality assessment, and aggregated reporting in a reproducible workflow.

---

## Features

* Automated workflow using **Snakemake**
* Read trimming using **fastp**
* Quality check using **FastQC**
* Aggregated report generation using **MultiQC**
* Reproducible and scalable pipeline

---

## Tools Used

* Snakemake
* fastp
* FastQC
* MultiQC
* Conda (environment management)

---

## Project Structure

```
NGS-Pipeline/
│── data/                  # Input FASTQ files (ignored in Git)
│── results/               # Output files (ignored in Git)
│── workflow/
│    └── Snakefile        # Main workflow
│── config/
│    └── config.yaml      # Sample configuration
│── .gitignore
│── README.md
```

---

## Installation

### 1. Clone repository

```
git clone https://github.com/your-username/NGS-Pipeline.git
cd NGS-Pipeline
```

### 2. Create environment

```
conda create -n ngs_pipeline_env -c conda-forge -c bioconda snakemake fastp multiqc -y
conda activate ngs_pipeline_env
```

---

## Usage

### Run the pipeline

```
snakemake -j 1
```

### Force complete rerun

```
snakemake --forceall
```

---

## Output

* Trimmed FASTQ files → `results/fastp/`
* FastQC reports → `results/fastqc/`
* MultiQC report → `results/multiqc/multiqc_report.html`

---

## Input Data

Raw FASTQ files are not included due to size limitations.

You can use test data from:

* https://www.ebi.ac.uk/ena/browser/home

Place files in:

```
data/sample1_R1.fastq.gz
data/sample1_R2.fastq.gz
```

---

## Workflow Summary

1. Input FASTQ files
2. Trimming with fastp
3. Quality check with FastQC
4. Aggregation using MultiQC

---

## Future Improvements

* Add alignment step (BWA)
* Add variant calling (GATK)
* Support multiple samples via config file
* Docker/Singularity integration

---

## Author

Rishikesh Indraguru
M.Sc Bioinformatics

---


This pipeline is developed as part of a bioinformatics learning and portfolio project.
