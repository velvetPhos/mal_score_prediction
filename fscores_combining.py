import pandas as pd

def combine_fscores(rounds):
    rounds = 3
    fscores = {}

    for n in range(rounds):
        temp = pd.read_csv('data/fscores{}.csv'.format(n))
        name = 'Y{}'.format(n)
        temp = temp.drop('Unnamed: 0', axis=1).rename({'Y': name}, axis=1)

        fscores[n] = temp

    combined = fscores[0]
    for n in range(1, rounds):
        temp = fscores[n]
        if (combined.shape[0] > temp.shape[0]):
            combined = combined.merge(temp, on='X', how='left')
        else:
            combined = temp.merge(combined, on='X', how='left')

    combined = combined.fillna(0)

    combined['mean'] = 0
    for n in range(rounds):
        name = 'Y{}'.format(n)
        combined['mean'] = combined['mean'] + combined[name]

    combined['mean'] = combined['mean']/rounds

    final = combined[['X', 'mean']].rename({'X': 'features','mean': 'feature importance'}, axis=1).sort_values('feature importance', ascending=False)

    final.to_csv('data/final_fscores.csv')

    print('Finished fscores combining')
