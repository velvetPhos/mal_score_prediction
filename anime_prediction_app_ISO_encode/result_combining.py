import pandas as pd

def combine_results(rounds):
    res = {}

    for n in range(rounds):
        temp = pd.read_csv('data/result{}.csv'.format(n), encoding="ISO-8859-1")
        name = 'prediction{}'.format(n)
        temp = temp.drop('Unnamed: 0', axis=1).rename({'prediction': name}, axis=1)

        res[n] = temp[['id_ref', name]]


    combined = res[0]
    combined['mean'] = 0

    for n in range(1, rounds):
        combined = combined.merge(res[n], on='id_ref')

    for n in range(rounds):
        name = 'prediction{}'.format(n)
        combined['mean'] = combined['mean'] + combined[name]

    combined['mean'] = combined['mean']/rounds

    final = combined[['id_ref', 'mean']].rename({'mean': 'prediction'}, axis=1).sort_values('prediction', ascending=False)

    alist = pd.read_csv('data/alist.csv', encoding="ISO-8859-1")[['name', 'id_ref']]

    final = final.merge(alist, on='id_ref')

    final.to_csv('data/final_data.csv', encoding="ISO-8859-1")

    print('Finished result combining')
