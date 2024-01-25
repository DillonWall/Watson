# Watson
This repo is my personal attempt at the Kaggle competition "Contradictory, My Dear Watson".

This competition is a long-standing community discussion about training NLP models for the purpose of detecting contradiction and entailment in multilingual text. 

I achieved a 68% validation accuracy by using transfer learning with the BERT base multilingual model. Technologies used include Python, PyTorch, PostgreSQL, Transformers, scikit-learn, pandas, numpy, matplotlib, and others.

---

## Contents
* [Motivation](#motivation)
* [Quick Start](#quick-start)
* [Local Install / Usage](#local-install--usage)
  * [Step 1: Data Ingestion](#step-1-data-ingestion)
  * [Step 2: EDA (Exploratory Data Analysis)](#step-2-eda-exploratory-data-analysis)
  * [Step 3: Model Training](#step-3-model-training)
  * [Step 4: Huggingface Spaces](#step-4-huggingface-spaces)
* [Contributing](#contributing)

---

## Motivation
Due to my interest in AI and having past experience (see [Sentize](https://github.com/DillonWall/Sentize)), I wanted to create an complete workflow involving all the necessary steps to train an AI model from the ground up.
This workflow includes:
- Importing data to a database (PostgreSQL)
- EDA (Exploratory Data Ananlysis)
- Training the model
- Publishing the model (Huggingface Spaces)
<div align="right">[ <a href="#contents">↑ Back to top ↑</a> ]</div>

---

## Quick Start
Test the finished model out at https://huggingface.co/spaces/MutualAbsorb/Watson-App

Check out the submission on Kaggle at https://www.kaggle.com/code/dillonwall/watson-bert-pytorch
<div align="right">[ <a href="#contents">↑ Back to top ↑</a> ]</div>

---

## Local Install / Usage
### Step 1: Data Ingestion
* Clone the repo to your local machine.
* Setup a clean Anaconda/Mamba environment with `Python 3.11.4`.
* Data must be ingested into a PostgreSQL database for the scripts to work correctly.
  * Create a new schema named `watson`.
  * Create 2 tables named `train` and `test` with the following columns:
    * `train`

    ![image](https://github.com/DillonWall/Watson/assets/49173127/8a7481b1-3299-48cd-a382-b3f5783fade9)

    * `test`
   
    ![image](https://github.com/DillonWall/Watson/assets/49173127/00e04972-6c02-4aae-a709-6f2b5ab5c410)

  * Import the CSV files from the `1_CSV_Data` folder into the `train` and `test` tables with their respective data.
 
    ![image](https://github.com/DillonWall/Watson/assets/49173127/b0272712-19e0-424d-bd1a-e9b36c7e0197)
 
### Step 2: EDA (Exploratory Data Analysis)
* For EDA to work properly, you must create a new `2_EDA\sensitive_info.py` file similar to `2_EDA\sensitive_info.py.example` except with connection info for your postgres database.

Simply run the Jupyter notebook `2_EDA\watson_eda.ipynb`; it should also take care of setting up your Python environment as needed.

### Step 3: Model Training
Again, just run and follow the `3_Model\model_training.ipynb`.

### Step 4: Huggingface Spaces
Setup your own Space on Huggingface. Feel free to reference my repository as an example for setting up, which can be found at https://huggingface.co/spaces/MutualAbsorb/Watson-App/tree/main

<div align="right">[ <a href="#contents">↑ Back to top ↑</a> ]</div>

---

## Contributing
I would love to collaborate on this project together with you!

You can help me out by:
* Checking out the list of [open issues](https://github.com/DillonWall/Watson/issues?q=is%3Aissue+is%3Aopen+) where I need help.
* If you need new features, please open a [new issue](https://github.com/DillonWall/Watson/issues) or start a [discussion](https://github.com/DillonWall/Watson/discussions).
* When creating a pull request, kindly consider the time it takes for reviewing and testing, and maintain proper coding style.
* If you wish to use this project commercially, kindly [contact me](https://github.com/DillonWall). 

Please [![Star Watson](https://img.shields.io/github/stars/DillonWall/Watson.svg?style=social&label=Star%20Watson)](https://github.com/DillonWall/Watson/) to support growth!


<div align="right">[ <a href="#contents">↑ Back to top ↑</a> ]</div>
