import pandas as pd


def merge_alist():
    alist = pd.read_csv('data/alist.csv').drop('Unnamed: 0', axis=1)

    df = pd.read_csv('data/data.csv').drop('Unnamed: 0', axis=1)

    columns = df.columns


    ids = set(alist['id_ref'].values) - set(df['id_ref'].values)

    remove_ids = set(df['id_ref'].values) - set(alist['id_ref'].values)

    for mal_id in ids:
        temp = pd.DataFrame(columns=columns)
        temp['id_ref'] = [mal_id]
        temp['notDone'] = True
        df = df.append(temp)

    for mal_id in remove_ids:
        df = df[df['id_ref'] != mal_id]

    for mal_id in set(df['id_ref'].values):
        df.loc[df['id_ref'] == mal_id, 'score'] = alist.loc[alist['id_ref'] == mal_id, 'score'].values[0]

    df.to_csv('data/data.csv')

    print('Finished merging alist')
