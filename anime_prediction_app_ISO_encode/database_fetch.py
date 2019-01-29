import pandas as pd
import time
from jikanscrap import get_data
import numpy as np

studio = ['8bit',
    'A-1 Pictures',
    'AIC',
    'APPP',
     'Artland',
     'Asahi Production',
     'Bee Train',
     'Bones',
     "Brain's Base",
     'CloverWorks',
     'CoMix Wave Films',
     'Daume',
     'David Production',
     'Diomedea',
     'Doga Kobo',
     'Fuji TV',
     'Gainax',
     'GoHands',
     'Gonzo',
     'Graphinica',
     'Hal Film Maker',
     'Imagin',
     'J.C.Staff',
     'Khara',
     'Kinema Citrus',
     'Kyoto Animation',
     'LIDENFILMS',
     'Lerche',
     'MAPPA',
     'Madhouse',
     'Manglobe',
     'Mushi Production',
     'Nippon Animation',
     'OLM',
     'Oh! Production',
     'Orange',
     'P.A. Works',
     'Palm Studio',
     'Passione',
     'Polygon Pictures',
     'Production I.G',
     'Production IMS',
     'Radix',
     'Satelight',
     'Science SARU',
     'Seven',
     'Shaft',
     'Shuka',
     'Silver Link.',
     'Studio 3Hz',
     'Studio 4Â°C',
     'Studio Deen',
     'Studio Gallop',
     'Studio Ghibli',
     'Studio Gokumi',
     'Studio Hibari',
     'Studio Pierrot',
     'Studio Rikka',
     'Sunrise',
     'SynergySP',
     'TMS Entertainment',
     'TYO Animations',
     'Tatsunoko Production',
     'Telecom Animation Film',
     'Tezuka Productions',
     'Toei Animation',
     'Tokyo Movie Shinsha',
     'Trigger',
     'White Fox',
     'Wit Studio',
     'Xebec',
     'Zexcs',
     'feel.',
     'ufotable',
     'Other']


def update_data():
    df = pd.read_csv('data/data.csv', encoding="ISO-8859-1").drop('Unnamed: 0', axis=1)

    for mal_id in list(df[df['notDone'] == True]['id_ref'].values):
        timeout = time.time() + 2

        temp = get_data(mal_id)

        if len(temp)>1:
            df.loc[df['id_ref'] == mal_id, 'name'] = temp['title']
            df.loc[df['id_ref'] == mal_id, 'mean'] = temp['score']
            df.loc[df['id_ref'] == mal_id, 'rank'] = temp['rank']
            df.loc[df['id_ref'] == mal_id, 'popularity'] = temp['popularity']
            df.loc[df['id_ref'] == mal_id, 'members'] = temp['members']
            df.loc[df['id_ref'] == mal_id, 'fav'] = temp['favorites']
            df.loc[df['id_ref'] == mal_id, 'ep'] = temp['episodes']

            try:
                df.loc[df['id_ref'] == mal_id, 'year'] = temp['aired']['from'][:4]
            except:
                df.loc[df['id_ref'] == mal_id, 'year'] = 0


            if temp['source'] == 'Manga' or temp['source'] == 'Webmanga' or temp['source'] == '4-komamanga':
                df.loc[df['id_ref'] == mal_id, 'Manga'] = 1

            if temp['source'] == 'Original':
                df.loc[df['id_ref'] == mal_id, 'Original'] = 1

            if temp['source'] == 'Book' or temp['source'] == 'Novel':
                df.loc[df['id_ref'] == mal_id, 'Novel'] = 1

            if temp['source'] == 'Lightnovel':
                df.loc[df['id_ref'] == mal_id, 'Lightnovel'] = 1

            if temp['source'] == 'Visualnovel':
                df.loc[df['id_ref'] == mal_id, 'Visualnovel'] = 1

            if temp['source'] == 'Game' or temp['source'] == 'Cardgame':
                df.loc[df['id_ref'] == mal_id, 'Game'] = 1

            if temp['source'] == 'Picturebook' or temp['source'] == 'Unknown' or temp['source'] == 'Music':
                df.loc[df['id_ref'] == mal_id, 'Other_source'] = 1

            df.loc[df['id_ref'] == mal_id, 'fav/members'] = temp['favorites'] / temp['members']
            df.loc[df['id_ref'] == mal_id, 'rank/pop'] = temp['favorites'] / temp['popularity']

            if temp['type'] == 'Music':
                df.loc[df['id_ref'] == mal_id, 'Music_type'] = 1
            else:
                df.loc[df['id_ref'] == mal_id, temp['type']] = 1

            studio_array = []
            for s in temp['studio']:
                studio_array.append(s['name'])

            for s in studio_array:
                if s in set(studio):
                    df.loc[df['id_ref'] == mal_id, s] = 1
                else:
                    df.loc[df['id_ref'] == mal_id, 'Other'] = 1

            genre_array = []
            for g in temp['genre']:
                genre_array.append(g['name'])

            for g in genre_array:
                df.loc[df['id_ref'] == mal_id, g] = 1

            df.loc[df['id_ref'] == mal_id, 'notDone'] = False

        else:
            df = df[df['id_ref'] != mal_id]
        print(len(list(df[df['notDone'] == True]['id_ref'].values)))
        df.to_csv('data/data.csv')
        while(time.time() <= timeout):
            pass


    df.to_csv('data/data.csv')

    print('Finished updating data')
