# A Statistical Significance Testing Approach for Measuring Term Burstiness with Applications to Domain-Specific Term Extraction

This repository contains computer code for reproducing the results described in the manuscript “A Statistical Significance Testing Approach for Measuring Term Burstiness with Applications to Domain-Specific Terminology Extraction”. ArXiv preprint link: TBA

## Getting Started

Clone this repository by running the command

```
git clone https://github.com/paul-sheridan/bursty-term-measure.git
```

and `cd` into the repository root folder `bursty-term-measure`.

### Running Python Code

Repository code is written in Python 3 in a Jupyter Notebook environment. While there are multiple ways to run a repository Jupyter Notebook, here is one way to do it:
```
python3 -m venv .
source bin/activate
pip install -r requirements.txt
jupyter notebook
deactivate
```

## Data

### GENIA Term Corpus Data

We downloaded the GENIA Term corpus version 3.02 file `GENIAcorpus3.02.tgz` from the GENIA Project homepage ([download page](http://www.geniaproject.org/genia-corpus/term-corpus "GENIA Project Homepage")). The extracted `GENIAcorpus3.02.xml` XML file is located in the `genia/0-raw-data` folder.

#### Preprocessing

To preprocess the GENIA data, open and run the `bursty-term-measure/genia/1-preprocessing/preprocessing-script.ipynb` Jupyter Notebook. After applying a variety of preprocessing steps to the data, the notebook outputs three files to the `genia/0-data-preprocessed` folder:

- `GENIAcorpus3.02-doc-ids.csv` (CSV): Article Ids.
- `GENIAcorpus3.02-keywords.tsv` (TSV): Mapping of lexical units to semantic classes.
- `GENIAcorpus3.02-preprocessed.json` (JSON): Abstract texts after preprocessing.

The particular preprocessing steps are described in the notebook.

### Stop Words

## GENIA Numerical Experiments

### IDF vs. ICF Plot

### Bursty Score Calculation

### Perfromance Evaluation

## Citation
If you find anything useful please cite our work using:
```
@misc{SarriaHurtado2023,
  author = {Samuel Sarria Hurtado and Todd Mullen and Paul Sheridan},
  title = {A Statistical Significance Testing Approach for Measuring Term Burstiness with Applications to Domain-Specific Term Extraction},
  year = {2023},
  eprint = {arXiv:xxxx.xxxxx}
}
```
