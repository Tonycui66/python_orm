import psycopg2.extras

conn = psycopg2.connect(database='qianbase', user='qbadmin', password='qianbase',port=26287,host='10.14.40.152')
curs = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  # 参数是以字典形式获取查询结果

print('''
<!DOCTYPE html>
<html lang="zh_cn">
<head>
    <meta charset="gbk">
    <title>我的论坛</title>
</head>
<body>
    <h3>小楼帅哥的第一个BBS</h3>
''')

sql = 'select * from messages'
curs.execute(sql)
messages = curs.fetchall()
top_level = []  # 保存父级消息的列表
children = {}  # 保存子级消息的字典

for message in messages:  # 遍历返回的消息列表
	parrent_id = message['reply_to']  # 获取消息元组中的reply_to列
	if parrent_id is None:  # 如果不是回复的消息
		top_level.append(message)  # 添加到父级消息列表
	else:
		children.setdefault(parrent_id, []).append(message)  # 否则以被回复消息的序号为键添加回复消息到值的列表


def format_show(message):
	print('<h5>{}.{}：{}</h5>'.format(message['id'], message['sender'], message['subject']))  # 输出父级消息内容
	print('<font size="2">{}</font>'.format(message['text']))
	try:
		kids = children[message['id']]  # 根据父级消息id从子级消息字典中查找所有子级消息
	except KeyError:
		pass
	else:
		print('<blockquote>')
		for kid in kids:  # 遍历找到的消息列表
			format_show(kid)  # 递归进行下一级消息的处理
		print('</blockquote>')


print('<p>')
for message in top_level:  # 遍历父级消息
	format_show(message)  # 调用递归函数进行多级遍历

print('''
</p>
</body>
</html>
''')