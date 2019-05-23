CSE 564
Analysis of Social Trends through Lyrics
Kritik Mathur (111986679) and Radhika Dhawan (112074050)

Problem
It is a universally accepted fact that songs are a reflection of the society[1]. Different music caters to different people across different eras, oftentimes defining an era as well. We analyse lyrics of music across 5 decades to get an understanding of social trends and how contemporary gets impacted by societal changes and major events.

This kind of analysis has its uses in:
Marketing and advertising industry: It can be used in writing marketing slogan or copywriter specific to different target customers. 
Music Industry: It can be helpful to music producers to know how the trend of music is changing with time.
Analysing changes in social behaviors of people and relating those to major events in the history.

Background
The techniques for text analysis we’ll be applying are
Keyword Extraction
Since songs have a different structure than sentences, in the sense they generally don’t have complete sentences and the order of the words is more flexible than in normal texts, common keyword extraction methods like RAKE[2] won’t be well suited for this. Hence, we’ll be experimenting with a couple of lyrical topic detection techniques [3][4]
Document to Vector
To find similarities in songs, genres, or artists, we need to convert text 
	data into vectors. Some common approaches for document-to-vector that we will be trying are tf-idf, bag-of-words, BERT.

Sentiment Analysis
	Different genres often have different sentiment associated with them and this information can be a useful characteristic in getting a hint of the general sentiment at the time that genre was popular. We’ll use SentiWordNet[5] for the aforementioned task.

Approach
Text Analysis:
Keyword extraction
Top words - Finding the popular words/phrases in the songs using the approaches mentioned previously and visualizing using word cloud.  
Gender wise - Finding the most popular words used by a particular gender.
Similarity
Get a high dimensional vector representation of each artist (bag of words, tfidf)
Reduce the vectors to 2 dimensions and show them on a scatter plot
Cluster the obtained points to find groups of artists that write similar songs (k-means)
Prediction
Use the vectors generated in 2 to mathematically model the task of predicting artist and genre of a new song.
We’ll also explore unsupervised sentiment and aggression analysis on the lyrics using Senti WordNet
Word use trends in each genre and decade.

Visualizations: 
We are going to use HTML, Javascript (d3.js for charts) and CSS for visualization and analysis of data further: 
Word Cloud: To visualize the top keywords extracted, we will be creating a word cloud as in the picture below. 
           

We will also have dropdown menus to choose between:
Top words by all the artists
Top words by male artists
Top words by female artists

2. ScatterPlot: We will be creating a scatter plot for visualizing the similarity of artists: the closer the vector of artists, the similar their lyrics should be.
3. LineChart: 
For k-means clustering of artists, we would need to optimize the value of k, using an elbow chart.
We will also draw a line chart for visualizing the change in sentiments of lyrics in past decades. 
4. BarChart: After sentiment and aggression analysis, we would draw barcharts to for the comparison of sentiments and male and female artists.

Datasets
362,237 lyrics from MetroLyrics.com[7]: There are around 380,000+ lyrics in the data set from 18,230 different artists from 12 different genres arranged by year. 
Various fields in the dataset: 
Index: Index of the dataset
Song: Name of the song 
Year: Year of the release
Artist: Name of the singer
Genre: Genre to which the song belongs 
Lyrics: Complete lyrics of the song

All the news[13]
The publications include the New York Times, Breitbart, CNN, Business Insider, the Atlantic, Fox News, Talking Points Memo, Buzzfeed News, National Review, New York Post, the Guardian, NPR, Reuters, Vox, and the Washington Post. Sampling wasn't quite scientific; I chose publications based on my familiarity of the domain and tried to get a range of political alignments, as well as a mix of print and digital publications. By count, the publications break down accordingly:
The data primarily falls between the years of 2016 and July 2017, although there is a not-insignificant number of articles from 2015, and a possibly insignificant number from before then.

Song lyrics from 6 musical genre[12] 
There are two datasets artists-data.csv and lyrics-data.csv, both have data on six musical genres:
Rock
Hip Hop
Pop music
Sertanejo (Basically the Brazilian version of Country Music)
Funk Carioca (Originated 60s US Funk, a completely different genre in Brazil nowadays)
Samba (Typical Brazilian music)
Decade
Number of Songs
60s
1
70s
4496
80s
3874
90s
11285
00s
190847
10s
151718

Data Cleaning
Before we can use the data for the above mentioned tasks, we need to perform the following preprocessing:
Disregard rows with empty fields for tasks related to that particular field
Remove duplicate rows
Get rid of extra spaces
Remove stop words
Remove punctuations
Make all the words case-uniform
Normalize shorthands (like ain’t to is not) 

Dashboard
The dashboard comprises of a sunburst detailing the distribution of our dataset. It’s first layer is divided by decades and the second by genres. As suggested by TA Ayush, we have added the year-wise trend for words on the dashboard.
The figure shows the first look of the home page which will be changed according to user's choice.
Linking:
On changing the decade in the hierarchical cluster, all the charts start displaying data for that particular decade.
On changing the genre in the bar graph, the word cloud displays popular words for that genre. 
The area chart shows the decade wise trend of the most popular word for that particular genre.

                                    

Zoomable Hierarchical Clustering[8]: For a better understanding of data we are using, instead of plain old table, we chose to visualize the data in the form of a zoomable hierarchical cluster.
The home page contains the description of data in the form of a hierarchical cluster. The number of songs in each cluster are displayed on hovering over the part in the visualization.



The innermost circle represents the total number of songs. The middle circle displays the category and number of songs in each decade ranging from 1960s to 2010s. The outermost circle represents the songs in various genres in every decade. For example: In the figure above, the current mouse hovers over the part of songs in folk genre in 1970s.

Area line graph: On loading the dashboard initially, the area graph shows year wise trend of the word the maximum count. Upon choosing the genre from the bar graph, it shows the trend of the top most word from that genre.

                        

Bar graph: The bar graph on the dashboard represents number of songs in each genre. On initial loading of the bar graph it shows the number of songs from each decade. On choosing the decade from the hierarchical cluster, the total number of songs of that particular decade are shown in each Genre bar.
                            


Extracting Keywords[4]: Instead of taking the words that occur more frequently, we extract ‘keywords’ from the songs. Keywords are defined as words that exhaustively convey what the song is about. We used the fact that such words occur in clusters, thus have high variance in their position. These words are extracted as follows:
Remove stopwords (is, the, a, they etc.)
Make a list of positions for each word.
From the list created in step 2, make one that contains the distances in occurrences of each word.
Next step is to find the standard deviation of the list obtained in step 3. Since, it can be affected by the frequency, we normalize the said list with its mean
Now we calculate the standard deviation of each word. The ones that are more important will occur in clusters, and thus have a higher standard deviation


Song: In Dreams, by Ben Howard
Keywords given by the algorithm
Always a riddle in the world she says
Always a riddle inside my head
Always a thing to wonder the way we come to be
Oh it's a big old place for me, yeah it's a big old world indeed
Everyone is killing me and everything conspires
Oh in dreams I have watched it spin
Seen a violent crack of atoms were all that comes in
Oh in dreams I have lain in sin
Just to be the cracked and the cared for
How can I ask, ask for more?
Always a riddle in the world she says
Always a riddle inside my head
Always a thing to wonder in the way we come to be
Oh it's a big old place for me yeah
It's a big old world indeed
Kicking my heels and wondering how I've been here so long
Oh in dreams I have watched it spin
Seen a violent crack of atoms were all that comes in
Oh in dreams I saw Aesop's kin
Just a carcass of a man, I belong inside his skin
Mmmm mmmmm mmmm
Where to, where to begin?
I live alone, I live a lonely life without you
And I may be troubled but I'm gracious in defeat
Oh I may be troubled but I'm gracious in defeat


riddle
big
old
always
dreams
oh
world
inside
says
head
thing
wonder
way
come
place
yeah






Categorized Animated Word Clouds[9]: The popular words page contains a dropdown that lets us choose between genre and decade. After choosing the category from dropdown, various dropdowns belonging to that particular category start displaying each for an interval of 4 seconds. For example: The figure below displays two screenshots of different times displaying popular words from two different genres.
         

Classification
There is another tab separate from the dashboard where you can type in the lyrics of a song

Radar Chart: The radar chart shows the possibility of the lyric searched to the 7 genres. As it can be seen in the example below, the lyric searched is very close to metal and pop and the closest to that metal.
 
                        
Year wise Trend


Area Graph: The yearwise trends page can be navigated to from the navigation bar or clicking on the year-wise trend graph from the dashboard. This page contains a text box where we can enter the word to be searched. Upon clicking on the search button, the pattern of the word from year 1970 to 2010 can be seen. 

Similarity in Genres

Getting vectors for Songs[10],[11]: The two methods used to find vectors for each song are (i) Tf-Idf, and (ii) Doc2Vec.

Tf-Idf vectors were limited to a size of 5000 and preliminary 2-class classification on an unoptimized SGD classifier resulted in an accuracy of 88%. We are yet to experiment with Doc2Vec.

The vectors obtained from Tf-Idf were reduced to 2 dimensions using MDS (distance metric = Euclidean) and plotted on a scatter plot using d3.

Scatter Plot: The last tab displays a scatter plot of artists to visualize the similarity between the artists. The artists that are placed together in the scatter plot have similar lyrics. The following graph shows the scatter plot for songs in two genres Hip-Hop and Metal.

Demo
Youtube:  
Github: https://github.com/dhawanradhika/Visualization/tree/master/Code

Challenges Faced

Size of the Data: Due to a large number of lyrics in our dataset, we constantly ran into memory issues and had to downsize our data at most steps. Currently, we train vectors on a cloud machine that has 32GB RAM.
Class Imbalance: Number of songs from the decades 60s-90s are so few, they barely add up to be 1/5th of the songs from 00s. Also, a large proportion of songs are from the genre ‘Rock’ (100k+).


Timeline

Week 
Project Work
Week 1 [April 8 - April 15]
Brainstorming project ideas.
Final Project decided and proposed. 
Week 2 [April 16 - April 22]
Data collection and preprocessing.
Data analysis for word count in each genre and decade. 
Data analysis for year wise trend for each word.
Week 3 [April 23 - April 28]


Completion of home page, year wise words trends, similarity of artists and popular words page with the visualizations. 
Similarity Vector of lyrics between artists.
Preliminary Genre Classification using SGD Classifier.
Genre wise keyword analysis.
Week 4 [April 29 - May 5]
Project preliminary report submission.
Similarity Vector of lyrics between decades and genres.
Scatter plots for the similarity vectors.
Week 5 [May 6 - May 12]
Sentiment and aggression analysis of data. 
Prediction model for predicting artist and genre of a new song.
Week 6 [May 13 - May 21]
Final Poster and report submission.


Future Work
Display a list of news events observed relevant to the pattern observed in the yesr-wise trend of lyrics. 
Analysis of songs in different languages and culture.
Text analysis on other types of writing like novels, essays, news articles, public notices, etc.

References
[1]. Longhurst, B., & Bogdanović, D. (2014). Popular music & society (3rd ed.). Cambridge: Polity Press
[2]. Rose, Stuart & Engel, Dave & Cramer, Nick & Cowley, Wendy. (2010). Automatic Keyword Extraction from Individual Documents. 10.1002/9780470689646.ch1
[3]. Kleedorfer, Florian, Peter Knees and Tim Pohle. “Oh Oh Oh Whoah! Towards Automatic Topic Detection In Song Lyrics.” ISMIR (2008)
[4]. Apoorva G., Mathur K., Mamidi R. (2018). What is this Song About?: Identification of Keywords in Bollywood Lyrics, 19th International Conference on Computational Linguistics and Intelligent Text Processing.
[5]. Baccianella, Stefano & Esuli, Andrea & Sebastiani, Fabrizio. (2010). SentiWordNet 3.0: An Enhanced Lexical Resource for Sentiment Analysis and Opinion Mining.. Proceedings of LREC. 10
[6]. Jonathan Yu. (2017). D3 Word Cloud. 
[7]. 362,237 lyrics from MetroLyrics.com (https://www.kaggle.com/gyani95/380000-lyrics-from-metrolyrics)
[8]. Andreas Dewes. (2015). Hierarchical Pie Chart
[9]. Joe Whitfield-Seed. (2018). Animated d3 word cloud
[10]. Ramos, J.E. (2003). Using TF-IDF to Determine Word Relevance in Document Queries.
[11]. Quoc Le, Tomas Mikolov (2014). Distributed Representations of Sentences and Documents. Proceedings of the 31st International Conference on Machine Learning, PMLR 32(2):1188-1196
[12]. https://www.kaggle.com/neisse/scrapped-lyrics-from-6-genres
[13]. https://www.kaggle.com/snapcrack/all-the-news

