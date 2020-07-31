# Fake-news-Classification
using Multinomial Naive Bayes Classifier and TF-IDF

# ABSTRACT    
This Project comes up with the applications of NLP (Natural Language Processing) techniques for detecting the 'fake news' (misleading news stories that comes from the non-reputable sources).Only by building a model based on a (Term Frequency Inverse Document Frequency) tfidf  matrix, (word tallies relative to how often they’re used in other articles in your dataset) can only get you so far. But these models do not consider the important qualities like word ordering and context. 

This project includes assembling a dataset of both fake and real news and employ a Naive Bayes classifier in order to create a model to classify an article into fake or real based on its words and phrases.

# OBJECTIVE
The main objective is to detect the fake news, which is a text classification problem. It is needed to build a model that can differentiate between “Real” news and “Fake” news

## REQUIREMENTS
1. Python
2. Numpy
3. Pandas
4. newspaper 
5. json
6. NLTK
7. sklearn 

## Directories
1. data_cleaning 
    1.1 cleaning_helper.py
2. notebooks
    2.1 read_json_and_clean.ipynb
    2.2 train_test_model.ipynb
3. savedFiles
    3.1 cleaned_df.pkl
    3.2 dirty_df.pkl
4. scrapper
    4.1 NewsPapers.json
    4.2 scraped_articles.json
    4.3 scrapper.py
5. to extract fake news sites
    5.1 fakenewssites.csv
    5.2 forfakenews.ipynb
    
## Various Stages 
1. Data Collection
2. Data preprocessing 
3. Preprocessing the Text
4. Classification + model selection
5. Validation of Model
    
    
## First Step - DATA COLLECTION

First of all find the reliable news sources for 'Real News' and unreliable news sources to gather 'Fake News' .
Create a json file "NewsPapers.json" Put the links of all reliable sources first and then put links for fake news.
Build a web scrapper for scrapping news articles from the links given in "NewsPapers.json" and store the articles in "scraped_articles.json".

## Second Step - Data preprocessing



