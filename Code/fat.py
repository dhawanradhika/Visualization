from constants import *
from file_paths import *
import pickle
import json
from collections import defaultdict, OrderedDict
import numpy as np
from word_processing import *

def fat_by_gen():
    lyrics = pickle.load(open(lyrics_file, 'rb'))
    labels = pickle.load(open(labels_file, 'rb'))

    genres = np.unique(labels['genre'])


    keywords = pickle.load(open(keywords_file, 'rb'))


    result = {}
    print ('Making wordcloud')
    wordcloud = []
    key_freq = defaultdict(int)
    for decade in keywords:
        for genre in keywords[decade]:
            for word in keywords[decade][genre]:
                key_freq[word[0]] += keywords[decade][genre][word]

    sorte = sorted(key_freq.items(), key=lambda x: -x[1])[:100]
    wordcloud = dict(sorte)

    print ('Making bar chart')
    bar_chart = {}
    for genre in genres:
        if genre == 'not available' or genre == 'other':
            continue
        bar_chart[genre] = labels['genre'].count(genre)

    print ('Making line chart')
    line_chart = {}
    top_key = sorte[0][0]
    similars = get_similar_words(top_key, count=2)

    words = [top_key] + similars

    for word in words:
        trend = get_word_trend(word)
        # print (word)
        line_chart[word] = json.loads(trend)[word]

    # line_chart = json.dumps(line_chart, indent=4)

    print ('Saving')
    result['wordcloud'] = wordcloud
    result['bar_chart'] = bar_chart
    result['line_chart'] = line_chart

    with open('fat.json', 'w') as ff:
        ff.write(json.dumps(result, indent=4))



def fat_by_decade():

    label_decades = pickle.load(open(labels_file, 'rb'))['decade']
    label_genres = pickle.load(open(labels_file, 'rb'))['genre']
    
    decades = np.unique(label_decades)
    genres = np.unique(label_genres)

    print ('Making bar chart')
    bar_chart = OrderedDict()
    wordcloud = OrderedDict()
    line_chart = OrderedDict()
    
    for decade in decade_order:
        bar_chart[decade_key[decade]] = OrderedDict()
        wordcloud[decade_key[decade]] = OrderedDict()
        line_chart[decade_key[decade]] = OrderedDict()
        for genre in genres:
            if genre == 'not available' or genre == 'other':
                continue
            bar_chart[decade_key[decade]][genre] = 0
            wordcloud[decade_key[decade]][genre] = defaultdict(int)
            line_chart[decade_key[decade]][genre] = {}
    
    for decade, genre in zip(label_decades, label_genres):
        if genre == 'not available' or genre == 'other':
            continue
        bar_chart[decade_key[decade]][genre] += 1
        

    keywords = pickle.load(open(keywords_file, 'rb'))
    for genre in keywords:
        if genre == 'not available' or genre == 'other':
            continue
        for decade in keywords[genre]:
            dec_key = decade_key[decade]
            for word in keywords[genre][decade]:
                wordcloud[dec_key][genre][word] += keywords[genre][decade][word]

    for decade in wordcloud:
        for genre in wordcloud[decade]:
            if genre == 'not available' or genre == 'other':
                continue
            gen_dict = wordcloud[decade][genre]
            sorte = sorted(gen_dict.items(), key=lambda x: -x[1])
            gen_dict = dict(sorte[:100])
            wordcloud[decade][genre] = gen_dict

            if not sorte:
                continue
            words = [sorte[0][0]] + get_similar_words(sorte[0][0])

            for word in words:
                line_chart[decade][genre][word] = json.loads(get_word_trend(word))[word]

    result = {}
    print ('Saving')
    result['wordcloud'] = wordcloud
    result['bar_chart'] = bar_chart
    result['line_chart'] = line_chart

    with open('fat_decadewise.json', 'w') as ff:
        ff.write(json.dumps(result, indent=4))


fat_by_decade()