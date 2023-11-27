# encoding=gbk
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import sqlalchemy

text = urlopen("http://python.org/community/jobs").read()
print(text)
soup = bs(text,features="html.parser")
# print(soup('a'))
jobs =set()

for header in soup('h3'):
	print(header)
	links = header('a','reference')
	if not links: continue
	link = links[0]
	jobs.add('%s,(%s)'%(link.string,link['href']))
	print(link)


print('\n'.join(sorted(jobs,key=lambda s : s.lower())))