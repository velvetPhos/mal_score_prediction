from lxml import html
import requests

def get_data(id_ref):

    dic = {}

    keys = ['mean', 'rank', 'popularity', 'members', 'studio', 'type', 'year', 'source', 'genres', 'fav', 'ep']

    for k in keys:
        dic[k] = None

    page = requests.get('https://myanimelist.net/anime/{}'.format(id_ref))
    tree = html.fromstring(page.content)

    mean = tree.xpath('//div[@data-title="score"]/text()')
    dic['mean'] = float(mean[0].replace(' ','').replace('\n', ''))

    rank = tree.xpath('//span[@class="numbers ranked"]/strong/text()')
    dic['rank'] = int(rank[0][1:])

    popularity = tree.xpath('//span[@class="numbers popularity"]/strong/text()')
    dic['popularity'] = int(popularity[0][1:])

    members = tree.xpath('//span[@class="numbers members"]/strong/text()')
    dic['members'] = int(members[0].replace(',',''))

    studio = tree.xpath('//span[@class="information studio author"]/a/text()')
    if len(studio) > 0:
        dic['studio'] = studio[0]

    type = tree.xpath('//div[.//span[@class="dark_text"] and .//text()[contains(., \'Type:\')]]/text()')
    type = list(filter(lambda a: a!='', list(map(lambda a: a.replace('\n', '').replace(' ', ''), type))))
    if len(type) == 0:
        type = tree.xpath('//div[.//span[@class="dark_text"] and .//text()[contains(., \'Type:\')]]/a/text()')
        type = list(filter(lambda a: a!='', list(map(lambda a: a.replace('\n', '').replace(' ', ''), type))))
    if len(type) != 0:
        dic['type'] = type[0]

    year = tree.xpath('//div[.//span[@class="dark_text"] and .//text()[contains(., \'Aired:\')]]/text()')
    year = list(filter(lambda a: a!='', list(map(lambda a: a.replace('\n', '').replace(' ', ''), year))))[0]
    if len(year) <= 4:
        dic['year'] = int(year)
    else:
        dic['year'] = int(year[year.index(',')+1:year.index(',')+5])

    source = tree.xpath('//div[.//span[@class="dark_text"] and .//text()[contains(., \'Source:\')]]/text()')
    dic['source'] = list(filter(lambda a: a!='', list(map(lambda a: a.replace('\n', '').replace(' ', ''), source))))[0]

    dic['genres'] = tree.xpath('//div[.//span[@class="dark_text"] and .//text()[contains(., \'Genres:\')]]/a/text()')

    fav = tree.xpath('//div[.//span[@class="dark_text"] and .//text()[contains(., \'Favorites:\')]]/text()')
    dic['fav'] = int(list(filter(lambda a: a!='', list(map(lambda a: a.replace('\n', '').replace(' ', ''), fav))))[0].replace(',', ''))

    ep = tree.xpath('//div[.//span[@class="dark_text"] and .//text()[contains(., \'Episodes:\')]]/text()')
    try:
        dic['ep'] = int(list(filter(lambda a: a!='', list(map(lambda a: a.replace('\n', '').replace(' ', ''), ep))))[0])
    except:
        pass

    return dic
