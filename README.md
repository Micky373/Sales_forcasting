# Sales_forcasting

## Live demo to the project result

- [Streamlit](#)

**Table of content**

- [Sales Forcating](#Sales-forcating)
  - [Overview](#overview)
  - [Requirements](#requirements)
  - [Install](#install)
  - [Data](#data)
  - [Features](#features)
    - [Data Exploration](#data-exploration)
    - [Scripts](#scripts)
    - [Test](#test)

## Overview

The aim of this project is to predict the sales six weeks ahead across all the stores of the Rossman Pharmaceutical company using Machine and Deep Learning. The different factors affecting the sales are: promotions, competitions, school-state holiday, seasonality, and locality.

## Requirements
  Python 3.5 and above, Pip and MYSQL
  The visualization are made using plotly

## Install
```
git clone https://github.com/Micky373/Sales_forcasting.git
cd Sales_forcating
pip install -r requirements.txt
```

## Data
  - The data used in the project is generated automatically by Rossman Pharmaceutical company.
  - The data is [here](https://drive.google.com/file/d/1EgqYG4gN3GKtMhmPala81dEsFpFVm97j/view?usp=sharing) 

## Features

### Data Exploration
  - Data cleaning is done in the data_cleaning.ipynb
  
### Scripts
 - All the scripts used by the notebooks are inside the scripts folder.

### Test
 - Tests for the scripts are inside the tests folder.

### Travis CI
  - The file .travis.yml contains the configuration for Travis.
