# A Statistical Significance Testing Approach for Measuring Term Burstiness with Applications to Domain-Specific Terminology Extraction

This repository contains computer code for reproducing the results described in the manuscript “A Statistical Significance Testing Approach for Measuring Term Burstiness with Applications to Domain-Specific Terminology Extraction”. ArXiv preprint link: https://arxiv.org/abs/2310.15790

## Getting Started

Clone this repository by running the command
```
git clone https://github.com/sheridan-stable/bursty-term-measure.git
```
and `cd` into the repository root folder `bursty-term-measure`.

## Running Repository Code

Repository code is written in Python 3 in a Jupyter Notebook environment. While there are multiple ways to run a repository Jupyter Notebook, here is one way to do it:

From the command line, create a virtual environment:
```
python3 -m venv .
source bin/activate
pip install -r requirements.txt
```

Launch a Jupyter Notebook server in your default web browser
```
jupyter notebook
```
and open a Jupyter Notebook of interest.

Remeber to close down the the virtual environment
```
deactivate
```
once you are done.

## Data

### GENIA Data

We downloaded the GENIA Term corpus version 3.02 file `GENIAcorpus3.02.tgz` from the GENIA Project homepage ([download page](http://www.geniaproject.org/genia-corpus/term-corpus "GENIA Project Homepage")). The extracted `GENIAcorpus3.02.xml` XML file is located in the `genia/0-raw-data` folder.

To preprocess the GENIA data, open and run the `bursty-term-measure/genia/1-preprocessing/preprocessing.ipynb` Jupyter Notebook. After applying a variety of preprocessing steps to the data, the notebook outputs three files to the `genia/1-preprocessing` folder:

- `GENIAcorpus3.02-doc-ids.csv` (CSV): Article Ids
- `GENIAcorpus3.02-keywords.tsv` (TSV): Mapping of lexical units to semantic classes
- `GENIAcorpus3.02-preprocessed.json` (JSON): Abstract texts after preprocessing

The particular preprocessing steps are described in the notebook.

### Common Stopwords

We compiled a list of 989 English stopwords by pooling stopwords from

- The nltk 3.8.1 Python library (179 stopwords)
- The Terrier IR Platform (733 stopwords, [download page](https://www.kaggle.com/datasets/rowhitswami/stopwords?resource=download "Kaggle: All English Stopwords (700+)")) stored locally at `genia/0-raw-data/terrier-stopwords.txt` 
- MyISAM (543 stopwords, [download page](https://dev.mysql.com/doc/refman/8.0/en/fulltext-stopwords.html "12.9.4 Full-Text Stopwords: Stopwords for MyISAM Search Indexes")) stored locally at `genia/0-raw-data/myisam-stopwords.txt` 

The subset of 417 (out of 989) stopwords occurring in the GENIA data is used in an exploratory analysis described below. No preprocessing is required.

## GENIA Data Numerical Experiments

### IDF vs. ICF Plot

Run the `genia/2-figure/figure-1.ipynb` notebook to generate the plot of Figure 1 from the manuscript.

### Term Burstiness Score Evaluation

To reproduce performance evaluation results from Table 4 from the manuscript, run the `genia/3-tables/tables.ipynb` notebook. This will generate the IDF, ICF, Chi-square test, Church Gale (CG), Irvine and Callison-Burch (ICB), Derivation of Proportions (DOP), Chi-square test, and Resicual ICF (RICF) term burstiness scores. Data used for the table is output directly to the `genia/3-tables` folder.

### Stopwords Exploratory Analysis

Run the `genia/3-tables/tables.ipynb` notebook to reproduce the results of the stopwords analysis in Tables 5 and 6 from the manuscript. Data used for the tables is output directly to the `genia/3-tables` folder.

## Citation
If you find anything useful please cite our work using:
```
@misc{SarriaHurtado2023,
  author = {Samuel Sarria Hurtado and Todd Mullen and Taku Onodera and Paul Sheridan},
  title = {A Statistical Significance Testing Approach for Measuring Term Burstiness with Applications to Domain-Specific Terminology Extraction},
  year = {2023},
  eprint = {arXiv:2310.15790}
}
```
