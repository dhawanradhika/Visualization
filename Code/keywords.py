from collections import defaultdict
import numpy as np
import re
import pickle
import json
from nltk.corpus import stopwords
from file_paths import *
from constants import *

def get_keywords(document):
    tokens = document.split()

    distribution = defaultdict(list)

    for i, token in enumerate(tokens):
        distribution[token].append(i)
    
    distances = {}
    means = {}
    std_devs = {}

    for token in distribution:
        token_distribution = distribution[token]
        occurrences = len(token_distribution)
        if occurrences < 2:
            continue

        distances[token] = np.zeros((occurrences - 1))

        mean = 0
        for i in range(occurrences - 1):
            dist = token_distribution[i + 1] - token_distribution[i]
            distances[token][i] = dist
            mean += dist

        means[token] = mean / occurrences
        distances[token] = distances[token] / mean
        std_devs[token] = np.std(distances[token])

    dev_list = []
    for token in std_devs:
        dev_list.append((token, std_devs[token]))
    
    dev_list = sorted(dev_list, key=lambda x: -x[1])[:4]

    return dev_list


def preprocess(text):

    
    no_punct = re.compile('[-\“”`",\.!\$:;#\n\?]\(\)')
    stops = stopwords.words('english')
    appending = [word.replace('\'', '') for word in stops]
    stops += appending
    stops += ['im', 'ill', 'ive', 'know', '[chorus]']
    processed = re.sub(no_punct, ' ', text.lower()).replace('  ', ' ')
    words = [word for word in processed.split() if word not in stops]
    return ' '.join(words)



lyrics = pickle.load(open(lyrics_file, 'rb'))
labels = pickle.load(open(labels_file, 'rb'))

decades = labels['decade']
genres = labels['genre']

del labels

keywords = {}
print ('Finding keywords')
for decade, genre, lyric in zip(decades, genres, lyrics):
    if genre == 'not available' or genre == 'other':
        continue

    processesed = preprocess(lyric)
    keys = get_keywords(processesed)
    if genre not in keywords:
        keywords[genre] = {}
    if decade not in keywords[genre]:
        keywords[genre][decade] = defaultdict(int)
    for key in keys:
        keywords[genre][decade][key[0]] += 1



print ('Writing keywords')

pickle.dump(keywords, open(keywords_file, 'wb'))
