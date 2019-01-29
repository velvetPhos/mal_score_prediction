import mal_scraper
import pandas as pd


def get_alist(username):
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

    df['consumption_status'] = df['consumption_status'].apply(lambda a: str(a)[18:])

    df = df[['id_ref', 'score', 'consumption_status']]
    df.to_csv('data/alist.csv')

    print('Finished fetching alist')
