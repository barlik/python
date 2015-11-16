#!/bin/env python
from bs4 import BeautifulSoup
from urllib import request
from sys import argv

def get_youtube_channel_id(url):
    req = request.urlopen(url)
    data = req.read()
    soup = BeautifulSoup(data, 'html.parser')
    return soup.meta.findNext(itemprop='channelId')['content']

if __name__ == "__main__":
    if argv[1]:
        print ('https://www.youtube.com/feeds/videos.xml?channel_id=' + get_youtube_channel_id(argv[1]))

