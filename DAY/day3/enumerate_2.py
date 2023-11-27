import re

WORD_RE = re.compile(r'\w+')

if __name__ == '__main__':
	filename = "../../vector.py"
	index = {}
	with open(filename, encoding='utf-8') as fp:
		for lineno, line in enumerate(fp, 1):
			print(lineno,line)
			for match in WORD_RE.finditer(line):
				word = match.group()
				column_no = match.start() + 1
				occurence = index.get(word, [])
				occurence.append((lineno, column_no))
				index[word] = occurence

	for word in index:
		print(word, index[word])
