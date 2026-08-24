# A Heuristic Approach to Term Dispersion Quantification with Applications to Domain-Specific Terminology Extraction

This repository contains computer code for reproducing the results described in the manuscript “A Heuristic Approach to Term Dispersion Quantification with Applications to Domain-Specific Terminology Extraction” (currently under review with Natural Language Processing - Cambrige University Press).

## Getting Started

Clone this repository by running the command
```
git clone https://github.com/sheridan-stable/bursty-term-measure.git
```
and `cd` into the repository root folder `bursty-term-measure`.

## Running Repository Code

Repository code is written primarily in Python 3.11 in a Jupyter Notebook environment. While there are multiple ways to run a repository Jupyter Notebook, here is one way to do it:

From the command line, create and configure a virtual environment:
```
# 1. Create a virtual environment.
python3.11 -m venv .

# 2. Activate your virtual environment.
# On Mac/Linux:
source bin/activate
# On Windows:
venv\Scripts\activate

# 3. Add your environment to Jupyter.
python -m ipykernel install --user --name=myenv --display-name "Python (myenv)"

# 4. Install required packages.
pip install -r requirements.txt

# 5. Launch a Jupyter Notebook server in your default web browser and open a Jupyter Notebook of interest.
jupyter notebook

# 6. Close down the the virtual environment once you are done.
deactivate
```


## Data

### GENIA Coprus

We downloaded the GENIA corpus version 3.02 file `GENIAcorpus3.02.tgz` from the GENIA Project homepage ([download page](http://www.geniaproject.org/genia-corpus/term-corpus "GENIA Project Homepage")). The extracted `GENIAcorpus3.02.xml` XML file is located in the `genia/0-raw-data` folder.

To preprocess the GENIA data, open and run the `bursty-term-measure/genia/1-preprocessing/preprocessing.ipynb` Jupyter Notebook. After applying a variety of preprocessing steps to the data, the notebook outputs three files to the `genia/1-preprocessing` folder:

- `GENIAcorpus3.02-doc-ids.csv` (CSV): Article Ids
- `GENIAcorpus3.02-keywords.tsv` (TSV): Mapping of lexical units to semantic classes
- `GENIAcorpus3.02-preprocessed.json` (JSON): Abstract texts after preprocessing
- `GENIAcorpus3.02-preprocessed-no-lex.json` (JSON): Abstract texts after preprocessing with `_lex` postfixes stripped

The particular preprocessing steps are described in the notebook.

### BC5CDR Coprus

We downloaded the BC5CDR corpus from the `bigbio/bc5cdr` Hugging Face repository ([download page](https://huggingface.co/datasets/bigbio/bc5cdr)).

To preprocess the BC5CDR data, open and run the `bursty-term-measure/bc5cdr/1-preprocessing/preprocessing.ipynb` Jupyter Notebook. After applying a variety of preprocessing steps to the data, the notebook outputs three files to the `bc5cdr/1-preprocessing` folder:

- `bc5cdr-keywords.tsv` (TSV): Mapping of lexical units to semantic classes
- `bc5cdr-preprocessed.json` (JSON): Abstract texts after preprocessing
- `bc5cdr-preprocessed-no-lex.json` (JSON): Abstract texts after preprocessing with `_lex` postfixes stripped

### Common Stopwords

We compiled a list of 989 English stopwords by pooling stopwords from

- The nltk 3.8.1 Python library (179 stopwords)
- The Terrier IR Platform (733 stopwords, [download page](https://www.kaggle.com/datasets/rowhitswami/stopwords?resource=download "Kaggle: All English Stopwords (700+)")) stored locally at `genia/0-raw-data/terrier-stopwords.txt` 
- MyISAM (543 stopwords, [download page](https://dev.mysql.com/doc/refman/8.0/en/fulltext-stopwords.html "12.9.4 Full-Text Stopwords: Stopwords for MyISAM Search Indexes")) stored locally at `genia/0-raw-data/myisam-stopwords.txt` 

The subset of 417 (out of 989) stopwords occurring in the GENIA data is used in an exploratory analysis described below. No preprocessing is required.

## Toy Example

To reproduce the toy example results of Table 4, run the `toy-example/toy-example-table.ipynb` notebook.

## Experimental Results

### Corpus Summary Statistics

To reproduce the GENIA corpus summary statistics of Table 3 from the manuscript, run the relevant code blocks in the `genia/2-tables/tables.ipynb` notebook. Data used for the table is output to the `genia/3-tables/table-3` folder.

To reproduce the BC5CDR corpus summary statistics of Table 4 from the manuscript, run the relevant code blocks in the `bc5cdr/2-tables/tables.ipynb` notebook. Data used for the table is output to the `bc5cdr/3-tables/table-3` folder.

### Terminology Extraction Experimental Evaluation

To reproduce GENIA corpus performance evaluation results from Tables 6-8 and Tables A1-A4 from the manuscript, run the relevant code blocks in the `genia/2-tables/tables.ipynb` notebook. This will generate mean P@k, R@k, and F1@k scores together with standard deviations for the IDF, ICF, Chi-square test, Church Gale (CG), Irvine and Callison-Burch (ICB), Derivation of Proportions (DoP), and Residual ICF (RICF), KeyBERT, and KeyLLM methods. Data used for the tables is output directly to the `genia/2-tables/table-x` folders, where `x=6,7,8,a1,a2,a3,a4`.

To reproduce the GENIA corpus RBO similarity score results from Tables 9 and 10, run the relevant code blocks in the `genia/3-tables/tables.ipynb` notebook. Data used for the tables is output directly to the `genia/2-tables/table-9` and `genia/2-tables/table-10` folders, respectively.

To reproduce BC5CDR corpus performance evaluation results from Tables 13-15 and Tables A5-A8 from the manuscript, run the relevant code blocks in the `bc5cdr/2-tables/tables.ipynb` notebook. This will generate mean P@k, R@k, and F1@k scores together with standard deviations for the IDF, ICF, Chi-square test, Church Gale (CG), Irvine and Callison-Burch (ICB), Derivation of Proportions (DoP), and Residual ICF (RICF), KeyBERT, and KeyLLM methods. Data used for the tables is output directly to the `bc5cdr/2-tables/table-x` folders, where `x=13,14,15,a5,a6,a7,a8`.

To reproduce the BC5CDR corpus RBO similarity score results from Tables 16 and 17, run the relevant code blocks in the `bc5cdr/3-tables/tables.ipynb` notebook. Data used for the tables is output directly to the `bc5cdra/2-tables/table-16` and `bc5cdr/2-tables/table-17` folders, respectively.

### Stopwords Exploratory Analysis

For GENIA, run the relevant code blocks in the `genia/2-tables/tables.ipynb` notebook to reproduce the results of the stopwords analysis in Tables 11 and 12 from the manuscript. Data used for the tables is output directly to the `genia/2-tables/table-11` and `genia/2-tables/table-12` folders, respectively.

For BC5CDR, run the relevant code blocks in the `genia/2-tables/tables.ipynb` notebook to reproduce the results of the stopwords analysis in Tables 18 and 19 from the manuscript. Data used for the tables is output directly to the `bc5cdr/2-tables/table-18` and `bc5cdr/2-tables/table-19` folders, respectively.

## Figures

Manuscript figures were generated in R. Associated R Notebooks may be run in R Studio.

### IDF vs. ICF Scatterplot

For GENIA, run the `genia/2-figure/figure-1a/figure-1a.Rmd` R Markdown notebook to generate the scatterplot of Figure 1a from the manuscript.

For BC5CDR, run the `bc5cdr/2-figure/figure-1b/figure-1b.Rmd` R Markdown notebook to generate the scatterplot of Figure 1b from the manuscript.

### Baseline Methods vs. RICF Scatterplots

For GENIA, run the `genia/2-figure/figure-2/figure-2.Rmd` R Markdown notebook to generate the scatterplots of Figure 2 from the manuscript.

For BC5CDR, run the `bc5cdr/2-figure/figure-3/figure-3.Rmd` R Markdown notebook to generate the scatterplots of Figure 3 from the manuscript.

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
