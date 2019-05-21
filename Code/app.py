"""
This file is part of the flask+d3 Hello World project.
"""
import numpy as np
import sys
import pandas as pd
import json
import flask
from collections import defaultdict
import os
from file_paths import *
import pickle
from constants import *
from nltk.corpus import wordnet
import word_processing
import os

app = flask.Flask(__name__)

data_context = None
scope = {'genre' : 'all', 'decade' : 'all'}

if __name__ == '__main__':
    port = 8001

    # Open a web browser pointing at the app.
    os.system("open http://localhost:{0}".format(port))

    # Set up the development server on port 8000.
    app.debug = True
    app.run(port=port)


#Utility Functions

@app.route("/")
def index():
    global data_context, scope
    """
    When you request the root path, you'll get the hierarchy.html template.

    """
    data_context = get_home(None)
    scope = {'genre' : 'all', 'decade' : 'all'}
    return flask.render_template("hierarchy.html")


@app.route("/wordcloud")
def word_cloud():
    global data_context

    return flask.render_template("wordcloud.html", data=json.dumps(data_context['wordcloud'], indent=4))

@app.route("/bargraph")
def bar_graph():
    global data_context

    return flask.render_template("bargraph.html", data=json.dumps(data_context['bar_chart'], indent=4));


@app.route("/wordtrend")
@app.route("/wordtrend/urgent/<string:word>")
def word_trend(word=''):
    global data_context
    if word:
        keywords = [word] + word_processing.get_similar_words(word, count=2)
        result = {}
        for keyword in keywords:
            result[keyword] = word_processing.get_word_trend(keyword)
        return flask.render_template("wordtrend.html", data=json.dumps(result, indent=4))
    print ('Received Request')
    return flask.render_template("wordtrend.html", data=json.dumps(data_context['line_chart'], indent=4))

@app.route("/navbar")
def navbar():
    return flask.render_template("navbar.html")


@app.route("/load_data/<string:search>", methods=['GET','POST'])
def load_context(search):
    global scope, data_context

    if search in genres:
        if not scope['decade'] == 'all':
            search = {'genre' : search, 'decade' : scope['decade']}
        else:
            search = {'genre' : search}
        scope['genre'] = search['genre']
        
    elif search in decades:
        if not scope['genre'] == 'all':
            search = {'decade' : search, 'genre' : scope['genre']}
        else:
            search = {'decade' : search}
        scope['decade'] = search['decade']
    data_context = get_home(search)
    result = {'OKAY' : "Good job section"}
    return json.dumps(result, indent=4)
    



@app.route("/line")
def line():
    return flask.render_template("line_chart.html")

@app.route("/similarity")
def similarity():
    return flask.render_template("similarity.html")


def get_home(search):
        
    if not search:
        result = {}
        with open(all_json_file) as af:
            data = json.loads(af.read())
        result['wordcloud'] = data['wordcloud']
        result['bar_chart'] = data['bar_chart']
        result['line_chart'] = data['line_chart']
        return result


    with open(home_json_file) as hf:
        home_data = json.loads(hf.read())

    wordcloud = home_data['wordcloud']
    bar_chart = home_data['bar_chart']
    line_chart = home_data['line_chart']


    result = {}


    if len(search) == 2:

        genre = search['genre']
        decade = search['decade']

        result['wordcloud'] = wordcloud[decade][genre]
        result['bar_chart'] = bar_chart[decade][genre]
        result['line_chart'] = line_chart[decade][genre]
    
    elif 'genre' in search:
        print (search, scope)
        genre = search['genre']
        
        wc_dict = defaultdict(int)
        for decade in wordcloud:
            for word in wordcloud[decade][genre]:
                wc_dict[word] += 1

        result['wordcloud'] = wc_dict

        bc_dict = defaultdict(int)
        for decade in bar_chart:
            bc_dict[decade] += bar_chart[decade][genre]

        result['bar_chart'] = bc_dict

        lc_dict = {}
        top_keyword = sorted(wc_dict.items(), key=lambda x: -x[1])[0][0]
        top_keys = [top_keyword] + word_processing.get_similar_words(top_keyword, count=2)

        for word in top_keys:
            lc_dict[word] = word_processing.get_word_trend(word)
        
        result['line_chart'] = lc_dict


    return result
    

@app.route("/data")
@app.route("/data/<string:word>")
def data(word=""):
    
    mode = 'year'
    trend_file = os.path.join(word_trend_dir, word + '_' + mode + '_count.json')

    if os.path.exists(trend_file):
        with open(trend_file) as infile:
            data = infile.read()
    else:
        data = word_processing.get_word_trend(word)
        with open(trend_file, 'w') as outfile:
            outfile.write(data)

    return data



@app.route("/hierarchy")
def hierarchy():
    with open("data/hierarchy_data.json", 'r') as infile:
        data = json.load(infile)
    return json.dumps(data)

# @app.route("/wordcloud")
# @app.route("/wordcloud/<string:type>")
# def data_wordcloud(type=""):
#     with open("data/"+type+"_keys_count.json", 'r') as infile:
#         data = json.load(infile)
#     return json.dumps(data)

# @app.route("/scatterplot")
# def data_scatter():
#     with open("data/similarity.json", 'r') as infile:
#         data = json.load(infile)
#     return json.dumps(data)