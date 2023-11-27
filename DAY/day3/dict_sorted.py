# tag : DIALCODES[]
# dial codes of the top 10 populous countries

DIAL_CODES = [
	(86,'China'),
	(91,'India'),
	(1,'United States'),
	(62,'Indonesia'),
	(55,'Brazil'),
	(92,'Pakistan'),
	(880,'Bangladesh'),
	(234,'Nigeria'),
	(7,'Russia'),
	(81,'Japan'),
]

if __name__ == '__main__':
    d1 = dict(DIAL_CODES)
    print(d1.keys())
    d2 = dict(sorted(DIAL_CODES,key=lambda x : x[0]))
    print(d2.keys())
    d3 = dict(sorted(DIAL_CODES))
    print(d3.keys())
    print(sorted(DIAL_CODES,key=lambda x :x[0],reverse=True))
    print(DIAL_CODES.sort(key=lambda x:x[0],reverse=True))
    print(DIAL_CODES)
    print(list(map(lambda x:"%d%s"%x,DIAL_CODES)))
    print("end")
