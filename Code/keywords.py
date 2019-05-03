from collections import defaultdict
import numpy as np
import re
from nltk.corpus import stopwords

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
        if occurrences == 1:
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
    
    dev_list = sorted(dev_list, key=lambda x: -x[1])

    for el in dev_list:
        print(el[0])


def preprocess(text):
    
    no_punct = re.compile('[-\“”`"\',\.!\$:;#\n\?]')
    stops = stopwords.words('english')
    processed = re.sub(no_punct, ' ', text.lower()).replace('  ', ' ')
    words = [word for word in processed.split() if word not in stops]
    return ' '.join(words)

with open('doc.txt') as df:
    text = preprocess(df.read())
    get_keywords(text)
