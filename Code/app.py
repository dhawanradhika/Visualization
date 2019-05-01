"""
This file is part of the flask+d3 Hello World project.
"""
import numpy as np
import sys
import itertools
import time
from pathlib import Path
import pandas as pd
import json
import flask


#-------------------------------------------------------------------------
# Setting paths for data files
#base_path="./data/"
#song_data=base_path+"songs.csv"
#-------------------------------------------------------------------------
# Loading Data Files
#df = pd.read_csv(song_data)
#columns = df.columns
#df.columns = ['attr-'+str(i) for i in range(1,len(df.columns)+1)]
#-------------------------------------------------------------------------
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
