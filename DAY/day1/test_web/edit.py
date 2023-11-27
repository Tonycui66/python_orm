import sys, cgi, psycopg2.extras

form = cgi.FieldStorage()
reply_to = form.getvalue('reply_to')  # 获取被回复消息的id
subject = ''  # 创建标题变量

print('''
<!DOCTYPE html>
<html lang="zh_cn">
<head>
    <meta charset="gbk">
    <title>编辑消息</title>
</head>
<body>
<form action="save.py" method="post">
''')  # 创建HTML基本代码并添加表单
if reply_to is not None:  # 如果获取到被回复消息的id
    try:
        reply_to = int(reply_to)  # 将id转换为整数类型
    except:  # 如果转换发生异常
        print('无法回复该消息！')
        sys.exit()  # 退出脚本执行
    else:  # 如果id可用
        print('    <input type="hidden" value="%s" name="reply_to"/>' % reply_to)  # 将被回复消息id写入表单元件值
        conn = psycopg2.connect(database='myproject_db', user='opython', password='opython')
        curs = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        sql = 'select subject from messages where id=%i' % reply_to  # 通过被回复消息id查询被回复消息的标题
        curs.execute(sql)
        subject = curs.fetchone()[0]  # 将查询到的标题存入变量
        if not subject.startswith('回复：'):  # 如果标题开头没有“回复：”字样
            subject = '回复：' + subject  # 为标题添加“回复：”字样

print('''
    <b><font size="2">主题：</font></b><br/>
    <input type="text" value="%s"  style="width:240px" name="subject"/><br/>
    <b><font size="2">作者：</font></b><br/>
    <input type="text"  style="width:240px" name="sender"/><br/>
    <b><font size="2">编辑内容：</font></b><br/>
    <textarea rows="5" cols="50" style="width:240px" name="text"></textarea><br/>
    <input type="submit" value="发布">
</form>
<hr/>
<a href="main.py"><font size="2">返回首页</font></a>
</body>
</html>
''' % subject)
