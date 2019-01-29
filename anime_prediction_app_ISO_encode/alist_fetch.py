from lxml import html
import requests
import re
import json
import pandas as pd

def get_alist(username):
    status_convert = {1:'watching', 2:'completed', 3:'on-hold', 4:'dropped', 5:'plan to watch', 6:'plan to watch'}

    id_ref = []
    score = []
    status = []
    name = []
    num = 1

    while (True):
        page = requests.get('https://api.jikan.moe/v3/user/{}/animelist/all/{}'.format(username, num))
        tree = html.fromstring(page.content)



        text = tree.xpath('text()')[0]

        print('https://api.jikan.moe/v3/user/{}/animelist/all/{}'.format(username, num))

        text = json.loads(text)


        text = text['anime']

        if len(text) == 0:
            break

        for anime in text:
            id_ref.append(anime['mal_id'])
            score.append(anime['score'])
            status.append(status_convert[anime['watching_status']])
            name.append(anime['title'])

        if len(text) == 0:
            break

        num = num + 1

    data = {'name':name, 'id_ref':id_ref, 'score':score, 'consumption_status':status}

    df = pd.DataFrame(data=data)

    df.to_csv('data/alist.csv')

    print('Finished alist fetching')
