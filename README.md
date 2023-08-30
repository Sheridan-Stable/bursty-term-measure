# A Statistical Significance Testing Approach for Measuring Term Burstiness with Applications to Domain-Specific Term Extraction

This repository contains computer code for reproducing the results described in the manuscript “A Statistical Significance Testing Approach for Measuring Term Burstiness with Applications to Domain-Specific Term Extraction”. ArXiv preprint link: TBA

## Getting Started

Clone this repository by running the command

```
git clone https://github.com/paul-sheridan/bursty-term-measure.git
```

and `cd` into the repository root folder `bursty-term-measure`.

### Running Python Code

Most repository code is written in Python 3 in a Jupyter Notebook environment. While there are multiple ways to run a repository Jupyter Notebook, here is one way to do it:
```
python3 -m venv .
source bin/activate
pip install -r requirements.txt
jupyter notebook
deactivate
```

### Running R Code

Run repository R code by opening associated R Markdown files in RStudio.

## Data

### GENIA Term Corpus Data

Create a folder called `bursty-term-measure/genia/0-raw-data`. Download the GENIA Term corpus version 3.02 file `GENIAcorpus3.02.tgz` from the GENIA ([download page](http://www.geniaproject.org/genia-corpus/term-corpus "GENIA Project Homepage")). Extract the `GENIAcorpus3.02.xml` XML file and place it in the `bursty-term-measure/genia/0-raw-data` folder.

#### Preprocessing

Go to such and such folder...

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
