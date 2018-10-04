# mal_score_prediction

mal_score_prediction is a python app that predicts scores of your PTW, dropped, on-hold, and watching in your mal list.

## Installation
You should either use git clone or direct zip download.
Both should work.

### Dependencies
* python (preferably python 3)
* pandas
* xgboost
* bayes_opt (BayesianOptimization)
* sklearn
* mal_scraper
* tkinter, html, requests (should be already installed with python)

To install those follow this:

`xcode-select --install`

`/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

`brew install python3`

`pip install pandas`

`pip3 install xgboost`

`pip install bayesian-optimization`

`pip install -U scikit-learn`

`pip install mal-scraper`

## Usage
To launch app, please set the "mal_score_prediction" folder as working directory using Terminal or cmd.

Then type `python main.py` to launch app.

This is the application window.

![alt text](https://i.imgur.com/qVEKsYc.jpg)

Please fill all parameters before clicking "Start Prediction".

### Parameters
* Username: please type username here
* Consumption status check list: check whichever you want to include in prediction. Default is "All".
* Minimum No.- Genre: the minimum number of anime required to stay as a feature. There is no default value, so please type something. Ex: if value is 4, then all genres with less than 4 entries will be "Other".
* Minimum No.- Studio: the minimum number of anime required to stay as a feature. There is no default value, so please type something. Ex: if value is 10, then all studio with less than 10 entries will be "Other".
* Rounds: the number of model trainings. larger is better, but it can take long time.
* Label Result: it creates another final result with consumption status labeled. Default is "Yes".

### Recommended Values for Parameters
* Username: please don't type more than one. Stored data must be erased if different username is typed.
* Consumption status check list: unless you have strong preferences, "All" is recommended.
* Minimum No.- Genre: 5~15 is recommended range. small value suits smaller list size (<200), and large value suits larger list size (>700)
* Minimum No.- Studio: 10~20 is recommended range. small value suits smaller list size (<200), and large value suits larger list size (>700)
* Rounds: 3 is recommended. larger is better, but run time can be concerning.
* Label Result: "Yes" is recommended unless only one of consumption status is selected.

## Manual Customization and Optimization
To optimize parameters, please check the individual "result.csv". If you found one that suits your expectations, then find the corresponding "params.csv" file. Then move "params.csv" to the "params" folder.

Corresponding files have same number. Ex: "result3.csv", "params3.csv"

For genre and studio customization, please edit "anime_train_test_creation.py" manually. You can specify which studio should be kept even if the entry numbers are lower than minimum no. that you set.

## Cautions
Please don't run the program for more than 1 username. It can corrupt all the data.

You can run the program for different username if you create empty "data" and "data/params" folders. Though it's not recommended if you do not understand the process of the program well.

Also, if Terminal output "TypeError", just click "Start Prediction" again. This is one issue that I haven't solved yet.

If you think the program is not running well type `ctrl+c` or `cmd+c` to stop the program. The program saves important information in the middle of process, so don't worry about quitting program can affect the result.
