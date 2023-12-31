# Watson
My personal AI workflow using the Kaggle competition "Contradictory, My Dear Watson"

You may test the finished model out at https://huggingface.co/spaces/MutualAbsorb/Watson-App

## Installation
* Clone the repo to your local machine.
* Setup a clean Anaconda environment with `Python 3.11.4`.
* Data must be ingested into a PostgreSQL database for the scripts to work correctly.
  * Create a new schema named `watson`.
  * Create 2 tables named `train` and `test` with the following columns:
    * `train`

    ![image](https://github.com/DillonWall/Watson/assets/49173127/8a7481b1-3299-48cd-a382-b3f5783fade9)

    * `test`
   
    ![image](https://github.com/DillonWall/Watson/assets/49173127/00e04972-6c02-4aae-a709-6f2b5ab5c410)

  * Import the CSV files from the `1_CSV_Data` folder into the `train` and `test` tables with their respective data.
 
    ![image](https://github.com/DillonWall/Watson/assets/49173127/b0272712-19e0-424d-bd1a-e9b36c7e0197)

* For EDA to work properly, you must create a new `2_EDA\sensitive_info.py` file similar to `2_EDA\sensitive_info.py.example` except with connection info for your postgres database.
 
## Usage
### EDA (Exploratory Data Analysis)
Simply run the Jupyter notebook `2_EDA\watson_eda.ipynb`; it should also take care of setting up your Anaconda environment as needed.

## Status

## Screenshots
