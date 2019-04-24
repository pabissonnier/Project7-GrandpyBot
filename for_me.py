from extraction import Extraction
from parssing import Parssing


# Instances creation
datas_extraction = Extraction()
datas_management = Parssing()

question = "zara paris"
link = Extraction.wiki_link(datas_extraction, "colette")

print(link)







