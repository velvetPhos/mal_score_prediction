# mal_score_prediction

mal_score_prediction is a python app that predicts scores of your PTW, dropped, on-hold, and watching in your mal list.

This program uses the data fetched from Jikan API, and it is the vital part of the program.

## Installation
You should either use git clone or direct zip download.
Both should work.

### Dependencies
* python3
* pandas
* xgboost
* bayes_opt (BayesianOptimization)
* sklearn
* lxml
* tkinter, time, requests (should be already installed with python)

To install those follow this:

`xcode-select --install` (only for mac users)

install anaconda python (https://docs.continuum.io/anaconda/install/)

`pip install xgboost` or `conda install -c conda-forge xgboost`

`pip install bayesian-optimization`

## Usage
To launch app, please set the "mal_score_prediction/anime_prediction_app" folder as working directory using Terminal or cmd.

Then type `python main.py` to launch app.

This is the application window.

![alt text](https://i.imgur.com/MOKsPSQ.jpg)

Please fill all parameters before clicking "Start Prediction".

Result will be in "data" folder, and name would be "final_data.csv" or "final_data_labeled.csv".

### Parameters
* Username: please type username here
* Rounds: the number of model trainings. larger is better, but it can take long time.

### Recommended Values for Parameters
* Username: please don't type more than one. Stored data must be erased if different username is typed.
* Rounds: Only increase 1 at time since Bayesian Optimazation would output only one unique parameter each run. First run should be 1. Rounds number should always be 1 ~ (no. of stored parameters + 1).

## Manual Customization and Optimization
To optimize parameters, please check the individual "result.csv". If you found one that suits your expectations, then find the corresponding "params.csv" file. Then move "params.csv" to the "params" folder.

Corresponding files have same number. Ex: "result3.csv", "params3.csv"

## Cautions
Please don't run the program for more than 1 username. It can corrupt all the data.

You can run the program for different username if you create empty "data" and "data/params" folders. Though it's not recommended if you do not understand the process of the program well.

If you think the program is not running well type `ctrl+c` to interrupt the program. The program saves important information in the middle of process, so don't worry about quitting program can affect the result.
