# A Heuristic Approach to Term Dispersion Quantification with Applications to Domain-Specific Terminology Extraction

This repository contains computer code for reproducing the results described in the manuscript “A Statistical Significance Testing Approach for Measuring Term Burstiness with Applications to Domain-Specific Terminology Extraction”.

## Getting Started

Clone this repository by running the command
```
git clone https://github.com/sheridan-stable/bursty-term-measure.git
```
and `cd` into the repository root folder `bursty-term-measure`.

## Running Repository Code

Repository code is written in Python 3.11 in a Jupyter Notebook environment. While there are multiple ways to run a repository Jupyter Notebook, here is one way to do it:

From the command line, create a virtual environment:
```
python3.11 -m venv .
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

### GENIA Term Coprus Data

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

## GENIA Term Coprus Numerical Experiment Tables

### GENIA Term Corpus Summary Statistics

To reproduce the GENIA Term corpus summary statistics of Table 3 from the manuscript, run the relevalnt code blocks in the `genia/2-tables/tables.ipynb` notebook. Data used fof the table is output to the `genia/3-tables/table-3` folder.

### Term Dispersion Measure Evaluation

To reproduce performance evaluation results from Tables 5-7 and Tables A1-A3 from the manuscript, run the relevalnt code blocks in the `genia/2-tables/tables.ipynb` notebook. This will generate mean P@k, R@k, and F1@k scores together with standard deviations for the IDF, ICF, Chi-square test, Church Gale (CG), Irvine and Callison-Burch (ICB), Derivation of Proportions (DoP), and Residual ICF (RICF) term dispersion measures. Data used for the tables is output directly to the `genia/2-tables/table-x` folders, where `x=5,6,7,a1,a2,a3`.

To reproduce the RBO similarity score results from Tables 8 and 9, run the relevalnt code blocks in the `genia/3-tables/tables.ipynb` notebook. Data used for the tables is output directly to the `genia/2-tables/table-8` and `genia/2-tables/table-9` folders, respectively.

### Stopwords Exploratory Analysis

Run the relevant code blocks in the `genia/2-tables/tables.ipynb` notebook to reproduce the results of the stopwords analysis in Tables 10 and 11 from the manuscript. Data used for the tables is output directly to the `genia/2-tables/table-10` and `genia/2-tables/table-11` folders, respectively.

## GENIA Term Coprus Numerical Experiment Figures

Manuscript figures were generated in R. Associated R Notebooks may be run in R Studio.

### IDF vs. ICF Scatterplot

Run the `genia/2-figure/figure-1/figure-1.Rmd` R Markdown notebook to generate the scatterplot of Figure 1 from the manuscript.

### Baseline Measures vs. RICF Scatterplots

Run the `genia/2-figure/figure-2/figure-2.Rmd` R Markdown notebook to generate the scatterplots of Figure 2 from the manuscript.

## Citation
If you find anything useful please cite our work using:
```
@misc{SarriaHurtado2026,
  author = {Samuel Sarria Hurtado and Paul Sheridan and Todd Mullen and Uyen Lai and Taku Onodera and Gurjit S. Randhawa and Aitazaz A. Farooque},
  title = {A Heuristic Approach to Term Dispersion Quantification with Applications to Domain-Specific Terminology Extraction},
  year = {2026},
  eprint = {arXiv:XXXX.XXXXX}
}
```
