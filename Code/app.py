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
from flask import request


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

@app.route("/genres")
def genre_dashboard():
    return flask.render_template("genres.html")

@app.route("/navbar")
def navbar():
    return flask.render_template("navbar.html")

@app.route("/genre_similarity")
def genre_similarity():
    return flask.render_template("genre_similarity.html")

@app.route("/home_word_compare")
def home_word_compare():
    return flask.render_template("home_word_compare.html")

@app.route("/genre_wordcloud", methods=['GET','POST'])
def genre_wordcloud():
    genre = ""
    decade = ""
    if request.method == 'POST':
        genre = request.form.get("genre")
        decade = request.form.get("decade")
        return flask.render_template("genre_wordcloud.html", value=genre, decade=decade)
    else:
        return flask.render_template("genre_wordcloud.html", value=genre, decade=decade)

@app.route("/genre_bargraph", methods=['GET','POST'])
def genre_bargraph():
    if request.method == 'POST':
        decade = request.form.get("decade")
        return flask.render_template("genre_bargraph.html", decade=decade)
    else:
        return flask.render_template("genre_bargraph.html")

@app.route("/genre_wordtrend")
def genre_wordtrend():
    return flask.render_template("genre_wordtrend.html")

@app.route("/data")
@app.route("/data/<string:word>")
def data(word=""):
    print("---------------------------"+word+"---------------------")
    if os.path.exists("data/"+word+"_count.json"):
        with open("data/"+word+"_count.json", 'r') as infile:
            data = json.load(infile)
    else:
        data = getWordTrend(word)
        with open("data/"+word+'_count.json', 'w') as outfile:
            json.dump(data, outfile)
    return json.dumps(data)

@app.route("/hierarchy")
def hierarchy():
    with open("data/hierarchy_data.json", 'r') as infile:
        data = json.load(infile)
    return json.dumps(data)

@app.route("/data-compare")
def data_compare():
    with open("data/home_word_compare.json", 'r') as infile:
        data = json.load(infile)
    return json.dumps(data)

@app.route("/wordcloud")
@app.route("/wordcloud/<string:decade>")
@app.route("/wordcloud/<string:decade>/<string:genre>")
def data_wordcloud(decade="",genre=""):
    with open("data/decade_keys_count.json", 'r') as infile:
        data = json.load(infile)
    if(decade!=""):
        data = data[decade]
    return json.dumps(data)

@app.route("/scatterplot")
def data_scatter():
    with open("data/hiphop_metal.json", 'r') as infile:
        data = json.load(infile)
    return json.dumps(data)

@app.route("/genre/bargraph/")
@app.route("/genre/bargraph/<string:decade>")
def genrebargraph(decade=""):
    print("INSIDE")
    if(decade!=""):
        print(decade)
    with open("data/genre_"+decade.strip()+"_counts.json", 'r') as infile:
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
