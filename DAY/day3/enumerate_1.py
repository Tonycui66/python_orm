# import os
import re


if __name__ == '__main__':
    # WORD_RE = re.compile(r'\w+')
    # filename= "../../vector.py"
    # index = {}
    # with open(filename,encoding='utf-8') as fp:
    #     for line_no,line in enumerate(fp,1):
    #         print(line_no,line)
    #         for match in WORD_RE.finditer(line):
    #             word = match.group()
    #             column_no = match.start()+1
    #             location = (line_no,column_no)
    #             index.setdefault(word,[]).append(location)
	#
    # print(index)
    # for match in WORD_RE.finditer("中国 123"):
    #     print(match)
    #     print(match.span())
    #     print(match.start())
    #     print(match.group(0))
    # print("中国 123"[0:2])
    a={1:'a',2:'b'}
    # print(a.update(a.fromkeys([3,4],10)))
    a.update(dict.fromkeys([3,4],20))
    print(a)
    print("123123")
