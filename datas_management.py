# -*- coding: utf-8 -*-
import json
import urllib.request

url_wiki = "https://fr.wikipedia.org/w/api.php?action=query&prop=extracts&exintro" \
                   "&titles=Albert%20Einstein&format=json"

wiki_json = urllib.request.urlopen(url_wiki)
wiki_read = wiki_json.read()
wiki_data = json.loads(wiki_read.decode("utf-8"))

for items in wiki_data["query"]['pages']['extract']:
    print(items)
