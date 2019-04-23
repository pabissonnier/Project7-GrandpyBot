# -*- coding: utf-8 -*-
import json


class Parssing:
    """ Parssing datas for extraction """
    def get_main_words(self, question):
        question = question.lower()

        word_tokens = question.split()

        with open('stopwords.json', encoding='utf-8') as json_file:
            stopwords = json.load(json_file)

            filtered_list = [w for w in word_tokens if not w in stopwords]

            filtered_sentence = '+'.join(filtered_list)
            return filtered_sentence

    def wiki_firstword(self, filtered_sentence):
        words_list = filtered_sentence.split('+')
        first_word = words_list[0]
        return first_word


