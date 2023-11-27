import io

import bs4
import requests
from PIL import Image,ImageSequence
from bs4 import BeautifulSoup
import os,sys

def download_links(num):
	url = f"https://xkcd.com/{num}/info.0.json"
	resp = requests.get(url)
	data = resp.json()
	# print(data)
	links = data.get("img")
	print(links)
	return links


def create_index():
	index = {}
	for num in range(1,10):
		links = download_links(num)
		index[num] = links
	return index


def search_links(query):
	index = create_index()
	results =[]
	for num,links in index.items():
		if query in links:
			results.append(f"https://xkcd.com/{num}/")
	return results


def list_links():
	index = create_index()
	results =[]
	for num,links in index.items():
		results.append(links)
	return results
def show(url):
	resp = requests.get(url)
	data = resp.content
	image = Image.open(io.BytesIO(data))
	image.show()

def show_byte(url,num):
	# resp = requests.get(url)
	# data = resp.content
	# frames  = list(ImageSequence.Iterator(Image.open(io.BytesIO(data))))
	# for frame in frames:
	# 	frame.show()
	resp = requests.get(url)
	data = resp.content
	with open("%s%s"%(str(num),os.path.splitext(url)[1]),"wb") as f:
		f.write(data)
	print("%s%s download finished"%(str(num),os.path.splitext(url)[1]))
	# image = Image.open(io.BytesIO(data))
	# image.show()
	# image.close()

def list_show(url):
	results = list_links()
	# frames = []
	for url in results:
		resp = requests.get(url)
		data = resp.content
		buffer = io.BytesIO(data)
		frames  = list(ImageSequence.Iterator(buffer))

		for frame in frames:
			frame.show(closing=True)



def down_image(url):
	resp = requests.get(url)
	# print(resp.text)
	# print(resp.content)
	soup = BeautifulSoup(resp.text,"html.parser")
	img_tags = soup.find_all("img")
	for i in img_tags:
		suburl = i.get("src")
		if not suburl.startswith("http"):
			suburl=url+suburl
		print(suburl)


if __name__ == '__main__':
	# print(os.path.splitext("https://imgs.xkcd.com/comics/barrel_cropped_(1).jpg"))
	# sys.exit()
    index = create_index()
    for key,value in index.items():
	    print(key,value.strip(),"\n")
	    # show_byte(value,key)
	    # time.sleep(30)
	# # down_image("https://www.cockroachlabs.com/")
