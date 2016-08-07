# Script for title synonymity

1) Download meta info about articles from RSS sources specified in rss_sources.txt

2) Store titles, urls and rss source in DB

3) Get name entities for each title

4) Group titles by entities


ToDo:

5) Count clause synonymity for each pair

6) Group by both scores


## Has to be installed:

1) Python packages

- feedparser
- nltk (see www.nltk.org/install.html)

2) Other:
 
- Stanford NER (see http://nlp.stanford.edu/software/CRF-NER.shtml or http://www.nltk.org/api/nltk.tag.html#module-nltk.tag.stanford) 

