import requests
from bs4 import BeautifulSoup
def GetWei():
	# 公众号文章列表页的 URL

	# url = 'https://mp.weixin.qq.com/s?__biz=MzIyOTM4MjU5MQ==&mid=2247483654&idx=1&sn=5a455e60805e6e060e1f3d5044586f82&chksm=9b78b288b8444e48745f6b207b058f20a3585928e45e3f840b10050584064a6e650f7f6a14e&scene=21#rd'
	# url = "https://mp.weixin.qq.com/s/8dIURpHmIqIU0CAvm6-elg"
	url = "https://mp.weixin.qq.com/s/yp-lvB9A5dVBrsBT3XkICA"
	# 发送 GET 请求获取文章列表页的 HTML 页面
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')

	# 解析文章列表信息
	print(soup)
	articles = soup.find_all('div', {'class': 'media'})
	print(articles)
	# 获取每篇文章的详细信息页面的 URL
	for article in articles:
		print(article)
		title = article.find('div', {'class': 'media-left'}).text.strip()
		link = article.find('a')['href']
		print(title, link)

		# 获取文章详细信息页面的 HTML 页面
		article_url = 'https://mp.weixin.qq.com' + link
		article_response = requests.get(article_url)
		article_soup = BeautifulSoup(article_response.text, 'html.parser')

		# 解析文章内容信息
		content = article_soup.find('div', {'class': 'rich_media-content'}).text.strip()

		# 将文章内容信息保存到本地文件中
		with open(title + '.txt', 'w', encoding='utf-8') as f:
			f.write(content)
	print("end")

if __name__ == '__main__':
    GetWei()