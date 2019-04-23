import extraction as script
import urllib.request
from io import BytesIO
import json


# Test instances creation
test_datas_extraction = script.Extraction()


class TestExtraction:
    FILTERED_SENTENCE = 'zara+paris+15'
    FIRST_WORD = "zara"
    ADDRESS = "15 Rue Linois, 75015 Paris, France"
    URL_GOOGLEADDRESS = "https://maps.googleapis.com/maps/api/place/textsearch/json?" \
                    "query=zara+paris+15&key=AIzaSyA1C5CCM7bcXC-Tg8U-az-vmRlRwymj3b0"
    URL_GOOGLEMAP = "https://maps.googleapis.com/maps/api/staticmap?center=zara+paris+15&zoom=13" \
                    "&size=400x300&maptype=roadmap" \
                    "&key=AIzaSyA1C5CCM7bcXC-Tg8U-az-vmRlRwymj3b0" \
                    "&format=png&visual_refresh=true" \
                    "&markers=color:red%7C48.848095,2.2822566"
    LAT = 48.848095
    LNG = 2.2822566
    GOOGLE_API_DATAS = {
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
    WIKI_SENTENCE = "Zara est la chaîne de magasins de vêtements de mode pour enfant et pour " \
                    "adultes principale du groupe espagnol Inditex qui possède aussi les marques Zara Home, " \
                    "Massimo Dutti, Bershka, Pull and Bear, Stradivarius, Kiddy's class, Lefties, Uterqüe, " \
                    "ainsi que Oysho."

    WIKI_LINK = "<a href='https://fr.wikipedia.org/wiki/Zara_(v%C3%AAtements)'>Si tu veux en savoir plus</a>"

    def test_get_urladdress(self):
        assert script.Extraction.get_urladdress(test_datas_extraction, self.FILTERED_SENTENCE) == \
               self.URL_GOOGLEADDRESS

    def test_get_urlmap(self):
        assert script.Extraction.get_urlmap(test_datas_extraction, self.FILTERED_SENTENCE, self.LAT, self.LNG) == \
               self.URL_GOOGLEMAP

    def test_get_googleapi_data(self, monkeypatch):
        def mockreturn(request):
            return BytesIO(json.dumps(self.GOOGLE_API_DATAS).encode())

        monkeypatch.setattr(urllib.request, "urlopen", mockreturn)
        assert script.Extraction.get_googleapi_data(test_datas_extraction, self.URL_GOOGLEADDRESS) == \
               self.GOOGLE_API_DATAS

    def test_get_address(self):
        assert script.Extraction.get_address(test_datas_extraction, self.GOOGLE_API_DATAS) == self.ADDRESS

    def test_get_lat(self):
        assert script.Extraction.get_lat(test_datas_extraction, self.GOOGLE_API_DATAS) == self.LAT

    def test_get_lng(self):
        assert script.Extraction.get_lng(test_datas_extraction, self.GOOGLE_API_DATAS) == self.LNG

    def test_wiki_datas(self):
        assert script.Extraction.wiki_datas(test_datas_extraction, self.FIRST_WORD) == self.WIKI_SENTENCE

    def test_wiki_link(self):
        assert script.Extraction.wiki_link(test_datas_extraction, self.FIRST_WORD) == self.WIKI_LINK
