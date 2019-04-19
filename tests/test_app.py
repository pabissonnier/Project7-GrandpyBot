import app as script
import urllib.request
from io import BytesIO
import json


question = "Bonjour, je voudrais l'adresse de Zara à Paris 15 s'il vous plait, merci !"

url_googleaddress = "https://maps.googleapis.com/maps/api/place/textsearch/json?" \
                    "query=zara+paris+15&key=AIzaSyA1C5CCM7bcXC-Tg8U-az-vmRlRwymj3b0"

googleapi_data = {
   "html_attributions" : [],
   "results" : [
      {
         "formatted_address" : "15 Rue Linois, 75015 Paris, France",
         "geometry" : {
            "location" : {
               "lat" : 48.848095,
               "lng" : 2.2822566
            },
            "viewport" : {
               "northeast" : {
                  "lat" : 48.84966402989272,
                  "lng" : 2.283917729892722
               },
               "southwest" : {
                  "lat" : 48.84696437010727,
                  "lng" : 2.281218070107278
               }
            }
         },
         "icon" : "https://maps.gstatic.com/mapfiles/place_api/icons/shopping-71.png",
         "id" : "ba608eddd1f071af7c24e8f765304512e17c876d",
         "name" : "Zara",
         "opening_hours" : {
            "open_now" : True
         },
         "photos" : [
            {
               "height" : 4032,
               "html_attributions" : [
                  "\u003ca href=\"https://maps.google.com/maps/contrib/105757222043428747568/photos\"\u003eA Google User\u003c/a\u003e"
               ],
               "photo_reference" : "CmRaAAAAjQ6om6rWO_3XLo4Xy3AKTor2nUdDOiCKZlCgfgjjseWCLqQp1yic-19qQswTf1_67t2ucoLuvNcGilgXOCR_hyVqeWPdLdcUbsDj0XBcl0JVmm59QM-FOyGAXmhNe7S4EhCC12bBUT7tA6PqhYbdjRk3GhQZsW-4VXiZ-kNa6S0ZD68giNQ4hQ",
               "width" : 3024
            }
         ],
         "place_id" : "ChIJnfcR6QVw5kcR5uegoEFI5n8",
         "plus_code" : {
            "compound_code" : "R7XJ+6W Paris, France",
            "global_code" : "8FW4R7XJ+6W"
         },
         "price_level" : 2,
         "rating" : 3.7,
         "reference" : "ChIJnfcR6QVw5kcR5uegoEFI5n8",
         "types" : [ "clothing_store", "store", "point_of_interest", "establishment" ],
         "user_ratings_total" : 197
      }
   ],
   "status" : "OK"
}


def test_get_main_words():
    assert script.get_main_words(question) == "zara+paris+15"


def test_get_googleapi_data(monkeypatch):
    def mockreturn(request):
        return BytesIO(json.dumps(googleapi_data).encode())

    monkeypatch.setattr(urllib.request, "urlopen", mockreturn)
    assert script.get_googleapi_data(url_googleaddress) == googleapi_data


def test_get_address():
    assert script.get_address(googleapi_data) == "15 Rue Linois, 75015 Paris, France"


def test_get_lat():
    assert script.get_lat(googleapi_data) == 48.848095


def test_get_lng():
    assert script.get_lng(googleapi_data) == 2.2822566




