import itchat
from itchat.content import *

def GetWei1():
	# 登录微信
	itchat.auto_login(hotReload=True)

	# 获取公众号列表
	official_accounts = itchat.search_mps()

	# 选择要下载文章的公众号
	official_account = None
	for account in official_accounts:
		print(account)
		if account['NickName'] == '公众号名称':
			official_account = account
			break

	if official_account is None:
		print('未找到指定公众号')
	else:
		# 获取公众号的历史消息
		messages = itchat.get_mps_history(official_account['UserName'])

		# # 下载文章
		for message in messages:
			if isinstance(message, TEXT):
				print('文章内容：', message['Text'])
				# 保存文章到本地文件
				with open('articles.txt', 'a', encoding='utf-8') as f:
					f.write(message['Text'] + '')

if __name__ == '__main__':
	GetWei1()