import pytest
import app as script

question = "Bonjour, je voudrais l'adresse de Zara à Paris 15 s'il vous plait, merci !"

url_googleaddress = "https://maps.googleapis.com/maps/api/place/textsearch/json?" \
                    "query=zara+paris+15&key=AIzaSyA1C5CCM7bcXC-Tg8U-az-vmRlRwymj3b0"


def test_get_main_words():
    assert script.get_main_words(question) == "zara+paris+15"


def test_get_googleapi_data():
    assert type(script.get_googleapi_data(url_googleaddress)) == dict


def test_answer():
    assert type(script.answer) == str


def test_address():
    assert type(script.address) == str


def test_map():
    assert type(script.map) == str


def test_wiki():
    assert type(script.wiki) == str
