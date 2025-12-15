import nltk
import numpy as np
from nltk.stem.porter import PorterStemmer

# Initialize the NLTK stemmer
stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_text, vocabulary):
    tokenized_sentence = [stem(w) for w in tokenized_text]
    bag = np.zeros(len(vocabulary), dtype=np.float32)
    for idx, word in enumerate(vocabulary):
        if word in tokenized_sentence:
            bag[idx] = 1.0
    return bag
