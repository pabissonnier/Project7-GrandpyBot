import parssing as script

# Test instances creation
test_datas_management = script.Parssing()


class TestParssing:
    QUESTION = "Bonjour, je voudrais l'adresse de Zara à Paris 15 s'il vous plait, merci !"
    FILTERED_SENTENCE = 'zara+paris+15'
    FIRST_WORD = "zara"

    def test_get_main_words(self):
        assert script.Parssing.get_main_words(test_datas_management, self.QUESTION) == self.FILTERED_SENTENCE

    def test_wiki_first_word(self):
        assert script.Parssing.wiki_firstword(test_datas_management, self.FILTERED_SENTENCE) == self.FIRST_WORD
