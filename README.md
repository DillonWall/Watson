# Watson
I am creating my personal AI workflow using the Kaggle competition "Contradictory, My Dear Watson"

## Installation
* Clone the repo to your local machine.
* (recommended) Setup a clean Anaconda environment with Python 3.11.
* Data must be ingested into a PostgreSQL database for the scripts to work correctly.
  * Create a new schema named `watson`
  * Import the CSV files from the `1_CSV Data` folder into tables in the watson schema named `train` and `test` with their respective data.
* For EDA to work properly, you must create a new `2_EDA\sensitive_info.py` file such as the `2_EDA\sensitive_info.py.example` file except with connection info for your postgres database.
 
## Usage
### EDA (Exploratory Data Analysis)
Simply run the Jupyter notebook `2_EDA\watson_eda.ipynb`; it should also take care of setting up your Anaconda environment as needed.

## Status

## Screenshots
