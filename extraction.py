# -*- coding: utf-8 -*-
import urllib.request
import json
import wikipedia


class Extraction:
    """ Class for the datas extraction"""
    def __init__(self):
        pass

    def get_urladdress(self, filtered_sentence):
        """ Get the url to display address"""
        url_googleaddress = "https://maps.googleapis.com/maps/api/place/textsearch/json?" \
                    "query={0}&key=AIzaSyA1C5CCM7bcXC-Tg8U-az-vmRlRwymj3b0".format(filtered_sentence)
        return url_googleaddress

    def get_urlmap(self, filtered_sentence, lat, lng):
        """ Get the url to display map"""
        url_googlemap = "https://maps.googleapis.com/maps/api/staticmap?center={0}&zoom=13" \
                    "&size=400x300&maptype=roadmap" \
                    "&key=AIzaSyA1C5CCM7bcXC-Tg8U-az-vmRlRwymj3b0" \
                    "&format=png&visual_refresh=true" \
                    "&markers=color:red%7C{1},{2}".format(filtered_sentence, lat, lng)
        return url_googlemap

    def get_googleapi_data(self, url_googleaddress):
        googleapi_json = urllib.request.urlopen(url_googleaddress)
        googleapi_read = googleapi_json.read()
        googleapi_data = json.loads(googleapi_read.decode("utf-8"))
        return googleapi_data

    def get_address(self, googleapi_data):
        for items in googleapi_data["results"]:
            address_location = items["formatted_address"]
            return address_location

    def get_lat(self, googleapi_data):
        for items in googleapi_data["results"]:
            lat = items["geometry"]["location"]["lat"]
            return lat

    def get_lng(self, googleapi_data):
        for items in googleapi_data["results"]:
            lng = items["geometry"]["location"]["lng"]
            return lng

    def wiki_datas(self, first_word):
        wikipedia.set_lang('fr')
        sentence_wiki = wikipedia.summary(first_word, sentences=1)
        return sentence_wiki

    def wiki_link(self, first_word):
        link_wiki_api = wikipedia.page(first_word).url
        link_wiki = """<a href='{0}'>Si tu veux en savoir plus</a>""".format(link_wiki_api)
        return link_wiki

