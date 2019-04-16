import pytest
import app as script


def test_get_main_words():
    question = "Bonjour, je voudrais l'adresse de Burger King à Paris 14 s'il vous plait, merci !"
    assert script.get_main_words(question) == "burger+king+paris+14"


def test_get_googleapi_data():
    url_googleaddress = "https://maps.googleapis.com/maps/api/place/textsearch/json?" \
                    "query=burger+king+paris+14&key=AIzaSyA1C5CCM7bcXC-Tg8U-az-vmRlRwymj3b0"
    assert type(script.get_googleapi_data(url_googleaddress)) == dict
