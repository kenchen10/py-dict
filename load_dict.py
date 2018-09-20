import json
import os, sys
from word_manipulations import *

def load_words():
    #Import words_dictionary.json and convert to a python dictionary
    try:
        filename = os.path.dirname(sys.argv[0]) + "words_dictionary.json"
        with open(filename, "r") as english_dictionary:
            valid_words = json.load(english_dictionary)
            return valid_words
    except Exception as e:
        return str(e)

def find_word(dictionary):
    #Find words that are in the dictionary with a letter removed
    new_list = []
    for word in removed_list:
        if binarySearch(word, dictionary)[1]:
            new_list = new_list + [dictionary[binarySearch(word, removed_list)[0]]]
    return new_list

if __name__ == '__main__':
    word_dict = load_words() #Dictionary of words
    word_list = (list(word_dict)) #List of all English words
    removed_list = remove_first_list(word_list) #All English words without the first letter
