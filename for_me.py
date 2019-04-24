from extraction import Extraction
from parssing import Parssing


# Instances creation
datas_extraction = Extraction()
datas_management = Parssing()

question = "zzzzzz"
filtered_sentence = Parssing.get_main_words(datas_management, question)
url_googleaddress = Extraction.get_urladdress(datas_extraction, filtered_sentence)
googleapi_data = Extraction.get_googleapi_data(datas_extraction, url_googleaddress)
lat = Extraction.get_lat(datas_extraction, googleapi_data)
lng = Extraction.get_lng(datas_extraction, googleapi_data)

print(lat, lng)







