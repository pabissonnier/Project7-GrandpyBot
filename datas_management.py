# -*- coding: utf-8 -*-
import json
import urllib.request
import wikipedia



def get_summary(place):
    print(wikipedia.summary(place, sentences=1))

get_summary('los angeles')
