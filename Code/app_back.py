"""
This file is part of the flask+d3 Hello World project.
"""
import numpy as np
import sys
import pandas as pd
import json
import flask
from collections import defaultdict


# def word_count(mode, mode_val, word):

#     if mode == 'decade':
#         lookup = pickle.load(open(decade_file, 'rb'))
#         mode_val = int(mode_val)
#     elif mode == 'genre':
#         lookup = pickle.load(open(genre_file, 'rb'))
#     elif mode == 'artist':
#         lookup = pickle.load(open(artist_file, 'rb'))
#     else:
#         lookup = pickle.load(open(year_file, 'rb'))
#         mode_val = int(mode_val)

#     look_in = pickle.load(open('organized_corpus/labels.pk', 'rb'))[mode]
#     lyrics = pickle.load(open('organized_corpus/lyrics.pk', 'rb'))

#     count = defaultdict(int)
#     for lyric, val in zip(lyrics, look_in):
#         count[val] += lyrics.split().count(word)

#     return count

#Utility Functions

#Get the trend of a word for line chart
def getWordTrend(word):
    print("----------------------------------------"+word+"------------------------------------------");

# ------------------------------------------------------------------
app = flask.Flask(__name__)


@app.route("/")
def index():
    """
    When you request the root path, you'll get the hierarchy.html template.

    """
<<<<<<< HEAD
    with open (decade_wise_json) as dwj:
        return flask.render_template('index.html', zooming)
    return flask.render_template("index.html", )
=======
    return flask.render_template("hierarchy.html")
>>>>>>> 5a64a6f8febc98c96604f2fd969edf99309aa5a0

@app.route("/word_cloud")
def word_cloud():
    return flask.render_template("word_cloud.html")

@app.route("/line")
def line():
    return flask.render_template("line_chart.html")

@app.route("/similarity")
def similarity():
    return flask.render_template("similarity.html")

@app.route("/data")
@app.route("/data/<string:word>")
def data(word=""):
    print("---------------------------"+word+"---------------------")
    if os.path.exists("data/"+word+"_count.json"):
        with open("data/"+word+"_count.json", 'r') as infile:
            data = json.load(infile)
    else:
        line_data = getWordTrend(word)
        with open("data/"+word+'_count.json', 'w') as outfile:
            json.dump(data, outfile)
    return json.dumps(data)

@app.route("/hierarchy")
def hierarchy():
    with open("data/hierarchy_data.json", 'r') as infile:
        data = json.load(infile)
    return json.dumps(data)

@app.route("/wordcloud")
@app.route("/wordcloud/<string:type>")
def data_wordcloud(type=""):
    with open("data/"+type+"_keys_count.json", 'r') as infile:
        data = json.load(infile)
    return json.dumps(data)

@app.route("/scatterplot")
def data_scatter():
    with open("data/similarity.json", 'r') as infile:
        data = json.load(infile)
    return json.dumps(data)

if __name__ == "__main__":
    import os

    port = 8000

    # Open a web browser pointing at the app.
    os.system("open http://localhost:{0}".format(port))

    # Set up the development server on port 8000.
    app.debug = True
    app.run(port=port)
