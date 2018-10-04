import pandas as pd

def create_train_test(genre_lim, studio_lim):
    df = pd.read_csv('data/data.csv')

    genres = ['Historical',
                'Drama',
                'Shoujo',
                'Adventure',
                'Seinen',
                'Fantasy',
                'Josei',
                'Slice of Life',
                'Mystery',
                'Dementia',
                'Thriller',
                'Psychological',
                'Space',
                'Sci-Fi',
                'Police',
                'Samurai',
                'Supernatural',
                'Music',
                'Military',
                'Vampire',
                'Sports',
                'Martial Arts',
                'Shoujo Ai',
                'Cars',
                'Kids',
                'Parody',
                'Romance',
                'Super Power',
                'Demons',
                'Horror',
                'Magic',
                'Shounen',
                'Game',
                'Mecha',
                'Comedy',
                'Ecchi',
                'Harem',
                'Action',
                'School']

    df = df.drop('Unnamed: 0', axis=1).drop('id_ref', axis=1).drop('notDone', axis=1).drop('genres', axis=1)
    df['fav/members'] = df['fav'] / df['members']
    df['rank/pop'] = df['rank'] / df['popularity']

    df.loc[df['source']=='Webmanga', 'source'] = 'Manga'
    df.loc[df['source']=='Book', 'source'] = 'Novel'
    df.loc[df['source']=='Picturebook', 'source'] = 'Other'
    df.loc[df['source']=='Unknown', 'source'] = 'Other'
    df.loc[df['source']=='4-komamanga', 'source'] = 'Manga'
    df.loc[df['source']=='Music', 'source'] = 'Other'
    df.loc[df['source']=='Cardgame', 'source'] = 'Other'
    df.loc[df['source']=='Game', 'source'] = 'Other'


    df['Other_genre'] = 0

    df['Sports'] = df['Sports'] + df['Martial Arts']
    df['Supernatural'] = df['Supernatural'] + df['Super Power']

    genres.remove('Martial Arts')
    genres.remove('Super Power')

    df = df.drop('Martial Arts', axis=1)
    df = df.drop('Super Power', axis=1)
    df.loc[df['Supernatural'] > 1, 'Supernatural'] = 1

    ignore_genres = []

    for g in genres:
        if (df[g].values.sum() < genre_lim):
            ignore_genres.append(g)

    # please uncomment and modify this part if you want to customize
    # keep_genres = []
    # ignore_genres = set(ignore_genres) - set(keep_genres)

    for g in ignore_genres:
        df['Other_genre'] = df['Other_genre'] + df[g]
        df = df.drop(g, axis=1)

    df.loc[df['Other_genre'] > 1, 'Other_genre'] = 1

    df.loc[df['studio'].isnull(), 'studio'] = 'Other'

    studios = df.groupby(by='studio').count().reset_index()[['studio', 'name']]

    small_studios = studios.loc[studios['name'] < studio_lim, 'studio'].values

    # please uncomment and modify this part if you want to customize
    # keep_studios = []

    ignore_studios = set(small_studios)  # -set(keep_studios)

    for s in ignore_studios:
        df.loc[df['studio'] == s, 'studio'] = 'Other'

    cat_cols = ['studio', 'type', 'source']

    df = pd.concat([df, pd.get_dummies(df[cat_cols]) ], axis=1)

    for c in cat_cols:
        df = df.drop(c, axis=1)

    df.columns

    df[df['score'] >0].to_csv('data/train.csv')

    df[df['score'] == 0].to_csv('data/test.csv')

    print('Finished train and test creation')
