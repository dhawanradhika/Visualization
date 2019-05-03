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
    When you request the root path, you'll get the index.html template.

    """
    with open (decade_wise_json) as dwj:
        return flask.render_template('index.html', zooming)
    return flask.render_template("index.html", )

@app.route("/word_cloud")
def scatter():
    return flask.render_template("word_cloud.html")

@app.route("/line")
def line():
    return flask.render_template("line_chart.html")

@app.route("/data")
@app.route("/data/<string:word>")
def data(word=""):
    print("---------------------------"+word+"---------------------")
    if os.path.exists("data/"+word+"_count.json"):
        with open("data/"+word+"_count.json", 'r') as infile:
            data = json.load(infile)
    else:
        line_data = getWordTrend(word)
        with open(word+'_count.json', 'w') as outfile:
            json.dump(data, outfile)
    return json.dumps(data)

if __name__ == "__main__":
    import os

    port = 8000

    # Open a web browser pointing at the app.
    os.system("open http://localhost:{0}".format(port))

    # Set up the development server on port 8000.
    app.debug = True
    app.run(port=port)
