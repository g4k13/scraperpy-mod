# -*- coding: utf-8 -*-
from . import helpers
import os, sys, pymongo, requests, bs4, json, pdb, feedparser, datetime
from pymongo import MongoClient

def postToMongo(dbname, tablename, document, mongourl):
    client = MongoClient(mongourl)
    db = client[dbname]
    db[tablename].insert_one(document)


def getBBCArabic(mongourl):
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
    postToMongo('bbcarabicscrape', 'scrapes', results, mongourl)


def getBBCArabicRSS(mongourl):
    rssurl = "http://feeds.bbci.co.uk/arabic/rss.xml"
    data = feedparser.parse(rssurl)
    results = {'title': data.feed.title, 'link': data.feed.link, 'data': data.entries, 'time': datetime.datetime.now().strftime("%I:%M%p %B %d, %Y")}
    for entry in data.entries:
        postToMongo('bbcarabicrss', 'articles', entry, mongourl)
