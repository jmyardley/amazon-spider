Scrapy project in Python using virtualenv, pymongo. 

Items are scraped in reviewspider.py and inserted in pipelines.py. 

With mongod running on localhost, cd into amazonspider and run "scrapy crawl reviewspider" from terminal.

Potential future fixes: add conditional so that the correct "title" span is scraped from global (foreign language) reviews instead of the hidden title.

