# mal_score_prediction

mal_score_prediction is a python app that predicts scores of your PTW, dropped, on-hold, and watching in your mal list.

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

`xcode-select --install`

`/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

`brew install python3`

`pip install pandas`

`pip3 install xgboost`

`pip install bayesian-optimization`

`pip install -U scikit-learn`

`pip install lxml`

## Usage
To launch app, please set the "mal_score_prediction" folder as working directory using Terminal or cmd.

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
* Rounds: 3 is recommended. larger is better, but run time can be concerning.

## Manual Customization and Optimization
To optimize parameters, please check the individual "result.csv". If you found one that suits your expectations, then find the corresponding "params.csv" file. Then move "params.csv" to the "params" folder.

Corresponding files have same number. Ex: "result3.csv", "params3.csv"

## Cautions
Please don't run the program for more than 1 username. It can corrupt all the data.

You can run the program for different username if you create empty "data" and "data/params" folders. Though it's not recommended if you do not understand the process of the program well.

If you think the program is not running well type `ctrl+c` to interrupt the program. The program saves important information in the middle of process, so don't worry about quitting program can affect the result.
