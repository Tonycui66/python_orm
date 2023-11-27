import re
import collections



index = collections.defaultdict(dict)

WORD_RE = re.compile(r'\w+')
filename = '../../vector.py'
if __name__ == '__main__':
	# print(index)
    print(index)
    index.default_factory = list
    print(index)
    del index.default_factory
    print(index)
    index.default_factory = list
    print(index)
    with open(filename,encoding='utf-8') as fp:
	    for lineno,line in enumerate(fp,1):
		    for match in WORD_RE.finditer(line):
			    word = match.group()
			    column_no = match.start()+1
			    index[word].append((lineno,column_no))
	# for word in index:
	# 	print(word,index[word])
    print(index)
    # for word in sorted(index,key=str.upper):
	#     print(word,index[word])