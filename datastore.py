
import random
class Datastore():

    def __init__(self):
        #pobieranie słowa z słownika
        with open("słownik.txt", encoding="utf-8") as word_file:
            self.words = word_file.read().splitlines()

    def get_word(self):
        word = ""
        while len(word) < 3:
            word = random.choice(self.words)
        return word
