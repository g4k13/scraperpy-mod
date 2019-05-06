# -*- coding: utf-8 -*-
from . import helpers
import sys, requests, bs4, json, pdb

def getBBCArabic(filename=None):
    sourceName = "BBC Arabic"
    sourceUrl = 'http://www.bbc.com/arabic'
    res = requests.get(sourceUrl)
    res.raise_for_status()
    bbcsoup = bs4.BeautifulSoup(res.text, features="html.parser")
    headlines = bbcsoup.select('a.title-link')
    results = {sourceName : {'root': sourceUrl, 'data': []}}
    count = 0
    for line in headlines:
        results[sourceName]['data'].append({'text': line.getText(), 'href': line.get('href')})
        count += 1

    if filename:
        lineFile = open(filename, 'w')
        lineFile.write(json.dumps(results, ensure_ascii=False))
        lineFile.close()

    return json.dumps(results, ensure_ascii=False)

