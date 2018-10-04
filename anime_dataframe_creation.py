import mal_scraper
import pandas as pd
import time
from webscrap import get_data

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


noOldFile = True

def create_df(username, ignore_consumption):

    # checks if there's usable old data
    try:
        old_df = pd.read_csv('data/data.csv')
        noOldFile = False
    except:
        pass

    # this part can create minor unintentional error. I'll fix this later
    while(True):
        try:
            alist = mal_scraper.get_user_anime_list(username)
            break
        except:
            pass

    temp_dict = {}

    col = list(alist[0].keys())
    for c in col:
        temp_dict[c] = []

    for anime in alist:
        for c in col:
            temp_dict[c].append(anime[c])

    df = pd.DataFrame(data=temp_dict)

    if not noOldFile:
        old_df = old_df.drop('name', axis=1).drop('score', axis=1)
        df = df.merge(old_df, on='id_ref', how='left')
        df = df.drop('Unnamed: 0', axis=1)

    df['consumption_status'] = df['consumption_status'].apply(lambda a: str(a)[18:])

    df = df.drop('is_rewatch', axis=1).drop('progress', axis=1).drop('start_date', axis=1).drop('finished_date', axis=1)

    df.to_csv('data/alist.csv')

    #['consuming', 'completed', 'on_hold', 'dropped', 'backlog']

    train = df[df['score'] > 0]
    test = df[df['score'] == 0]

    test = test[test['consumption_status'] != 'completed']

    # removes unneeded consumption status
    if len(ignore_consumption) > 0:
        for c in ignore_consumption:
            test = test[test['consumption_status'] != c]

    train = train.reset_index()
    test = test.reset_index()

    df = pd.concat([train, test])

    df = df.drop('index', axis=1)

    df = df.drop('consumption_status', axis=1)

    data_cols = ['mean', 'rank', 'popularity', 'members', 'studio', 'type', 'year', 'source', 'genres', 'fav', 'ep']

    if noOldFile:
        df['notDone'] = True
        for c in data_cols:
            df[c] = None
        for c in genres:
            df[c] = 0
    else:
        df.loc[df['notDone'].isnull(), 'notDone'] = True

    # This process can take upto 2 hours,
    # but it saves the process so teminating process in middle is fine
    while (df[df['notDone']].shape[0] > 0):
        timeout = time.time() + 60*3

        for animeId in df[df['notDone']]['id_ref'].values:
            if time.time() > timeout:
                break
            try:
                temp = get_data(animeId)
                for c in data_cols:
                    if c == 'genres' and temp[c] != None:
                        for g in temp[c]:
                            df.loc[df['id_ref'] == animeId, g] = 1
                    else:
                        df.loc[df['id_ref'] == animeId, c] = temp[c]

                df.loc[df['id_ref'] == animeId, 'notDone'] = False
            except:
                pass

        df.to_csv('data/data.csv')
        timeout = time.time() + 60
        while(True):
            if time.time() > timeout:
                break


    df.to_csv('data/data.csv')

    print('Finished dataframe creation')
