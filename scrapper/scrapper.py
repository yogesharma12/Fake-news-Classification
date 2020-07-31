import feedparser as fp
import json
import newspaper
from newspaper import Article
from time import mktime
from datetime import datetime

LIMIT = 50

data = {}
data['newspapers'] = {}

# Load JSON file with news sites
with open('NewsPapers.json') as data_file:
    companies = json.load(data_file)

count = 1

# Iterate through each news company
for company, value in companies.items():
    
    
    print("Downloading articles from ", company)
    paper = newspaper.build(value['link'], memoize_articles = False)

    newsPaper = {
            			"link": value['link'],
            			"articles": []
            	}

    noneTypeCount = 0
    for content in paper.articles:
            if count > LIMIT:
                    break

            try:
            	content.download()
            	content.parse()
            except Exception as e:
            	print(e)
            	print("continuing...")
            	continue

            if content.publish_date is None:
            	print(count,"article has date of type none")
            	noneTypeCount = noneTypeCount + 1;
            	if noneTypeCount>10:
            		print("aborting...")
            		noneTypeCount=0
            		break
            	count = count + 1
            	continue

            article = {}

            article['title'] = content.title
            article['text'] = content.text
            article['link'] = content.url
            article['author'] = content.authors

            newsPaper['articles'].append(article)
            count = count + 1

            if count%12 == 0:
            	print(count, "articles downloaded from", company)

            noneTypeCount = 0

                


    count = 1
    data['newspapers'][company] = newsPaper

try:
    fname = 'scraped_articles.json'
    print('saving articles . . . in {}'.format(fname))
    with open(fname, 'w') as outfile:
        json.dump(data, outfile)
except Exception as e: print(e)