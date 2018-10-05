import pandas as pd

def adjust_df(ignore_consumption):
    df = pd.read_csv('data/data.csv')
    train = df[df['score'] > 0]
    test = df[df['score'] == 0]
    # removes unneeded consumption status
    if len(ignore_consumption) > 0:
        for c in ignore_consumption:
            test = test[test['consumption_status'] != c]

    train = train.reset_index()
    test = test.reset_index()

    df = pd.concat([train, test])

    df = df.drop('consumption_status', axis=1).drop('Unnamed: 0', axis=1).drop('index', axis=1)

    df.to_csv('data/working_data.csv')
