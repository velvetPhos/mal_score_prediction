import pandas as pd
import time
from jikanscrap import get_data
import numpy as np

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
        'School',
        'Yaoi',
        'Yuri',
        'Shounen Ai',
        'Hentai']

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


type = ['TV', 'Movie', 'OVA', 'Special', 'ONA', 'Music_type']

source = ['Manga', 'Novel', 'Original', 'Lightnovel', 'Visualnovel', 'Game', 'Other_source']

data_cols = ['name', 'id_ref', 'score', 'mean', 'rank', 'popularity', 'members', 'fav/members', 'rank/pop', 'year', 'fav', 'ep', 'notDone']

data_cols = data_cols + type + source + genres + studio

def create_df():
    df = pd.DataFrame()

    for c in data_cols:
        df[c] = 0
    for c in genres:
        df[c] = 0

    df.to_csv('data/data.csv')


create_df()
