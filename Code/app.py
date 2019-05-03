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

#Utility Functions

#Get the trend of a word for line chart
def get_word_trend(word, mode='year'):
    
    print("----------------------------------------"+word+"------------------------------------------")
    lyrics = pickle.load(open(lyrics_file, 'rb'))
    labels = pickle.load(open(labels_file, 'rb'))[mode]

    trend_dict = defaultdict(int)
    val_counts = defaultdict(int)

    for lyric, label in zip(lyrics, labels):
        words = lyric.split()
        trend_dict[label] += words.count(word)
        val_counts[label] += 1
    print('Counts collectedss')

    result = []
    for label, count in sorted(trend_dict.items(), key=lambda x: int(x[0])):
        result.append({ label : count * 1000 / val_counts[label] })
    result = { word : result }
    print('Sending counts')
    return json.dumps(result, indent=4, sort_keys=True)
    




app = flask.Flask(__name__)


@app.route("/")
def index():
    """
    When you request the root path, you'll get the hierarchy.html template.

    """
    return flask.render_template("hierarchy.html")

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

    trend_file = os.path.join(word_trend_dir, word + '_count.json')

    if os.path.exists(trend_file):
        with open(trend_file) as infile:
            data = infile.read()
    else:
        data = get_word_trend(word)
        with open(trend_file, 'w') as outfile:
            outfile.write(data)

    return data



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
