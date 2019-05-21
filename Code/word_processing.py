import pickle
from collections import defaultdict
from nltk.corpus import wordnet
from gensim.models.word2vec import Word2Vec
import gensim.downloader as api
from file_paths import *
from constants import decade_key, decade_order
import json
import os


if os.path.exists(w2v_model_file):
    print ('Found existing word2vec model')
    w2v_model = pickle.load(open(w2v_model_file, 'rb'))
else:
    print ('No existing word2vec model')
    corpus = api.load('text8')
    print ('training')
    w2v_model = Word2Vec(corpus)
    pickle.dump(w2v_model, open(w2v_model_file, 'wb'))
    print ('model saved at', w2v_model_file)


def get_similar_words(word, count=3):

    if w2v_model.wv.vocab:
        similar_words = [pair[0] for pair in w2v_model.wv.most_similar(word)[:count]]
        return similar_words
    return []



def generate_synonyms(word):
    
    synsets = wordnet.synsets(word)

    for synset in synsets:
        for lemma in synset.lemmas():
            name = lemma.name()
            if '_' in name:
                continue
            yield name



def get_synonyms(word, limit=3):

    synonyms = set()
    count = 3
    generator = generate_synonyms(word)
    while len (synonyms) != limit:
        try:
            synonyms.add(next(generator))
        except StopIteration:
            break
    return synonyms



def pack_trend_result(trend, counts, mode):
    
    # print(counts)
    threshold = 10
    per_k = 1000
    result = []
    if mode == 'decade':
        for decade in decade_order:
            if counts[decade] < threshold:
                print ('reducing')
                trend[decade] /= per_k
            result.append({ decade_key[decade] :  trend[decade] * per_k / counts[decade] })
    elif mode == 'year':
        for label, count in sorted(trend.items(), key=lambda x: int(x[0])):
            if counts[label] < threshold:
                print ('reducing')
                count /= 1000
            result.append({ label : count * per_k / counts[label] })
    else:
        for key in trend:
            result.append({ key : trend[key] * per_k / counts[key] })

    return result



def get_word_trend(word, mode='year'):

    trend_file = os.path.join(word_trend_dir, word + '_' + mode + '_count.json')
    if os.path.exists(trend_file):
        with open(trend_file) as tf:
            trend = json.loads(tf.read())[word]
    else:
    
    # print("----------------------------------------"+word+"------------------------------------------")
        lyrics = pickle.load(open(lyrics_file, 'rb'))
        labels = pickle.load(open(labels_file, 'rb'))[mode]

        trend_dict = defaultdict(int)
        val_counts = defaultdict(int)

        for lyric, label in zip(lyrics, labels):
            words = lyric.split()
            trend_dict[label] += words.count(word)
            val_counts[label] += 1
        print('Counts collected')

        trend = pack_trend_result(trend_dict, val_counts, mode)
        print ('Saving file at', trend_file)
        with open(trend_file, 'w') as tf:
            tf.write(json.dumps({ word : trend }, indent=4))
    
    return trend

    # result = { word : pack_trend_result(trend_dict, val_counts, mode) }
    # print('Sending counts')
    # return json.dumps(result, indent=4, sort_keys=True)



def context_trend_search(word, context, mode='year'):
    
    context_label = list(context.keys())[0]
    context_value = context[context_label]

    lyrics = pickle.load(open(lyrics_file, 'rb'))
    labels = pickle.load(open(labels_file, 'rb'))
    context_labels = labels[context_label]
    mode_labels = labels[mode]
    
    del labels

    trend_dict = defaultdict(int)
    val_counts = defaultdict(int)

    for lyric, con_label, mode_label in zip(lyrics, context_labels, mode_labels):
        if con_label != context_label:
            continue
        trend_dict[mode_label] += 1
        val_counts[mode_label] += 1

    result = { word : pack_trend_result(trend_dict, val_counts, mode) }
    print ('Sending counts')
    return json.dumps(result, indent=4)



