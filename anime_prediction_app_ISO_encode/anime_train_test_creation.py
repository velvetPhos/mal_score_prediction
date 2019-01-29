import pandas as pd


def create_train_test():
    df = pd.read_csv('data/data.csv', encoding="ISO-8859-1")


    df = df.drop('Unnamed: 0', axis=1)



    df[df['score'] >0].to_csv('data/train.csv')

    df[df['score'] == 0].to_csv('data/test.csv')

    print('Finished train and test creation')
