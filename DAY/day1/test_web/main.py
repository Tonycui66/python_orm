import psycopg2.extras
from flask import request
import cgi, sys
form = cgi.FieldStorage()

conn = psycopg2.connect(database='qianbase', user='qbadmin', password='qianbase',port=26287,host='10.14.40.152')
curs = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
## 主页发布的展示方法
def format_show(message,children):  # 创建递归函数
    str1=""
    str1 +='''<h5><a href="view?id=%(id)i">%(sender)s：%(subject)s</a></h5>''' % message
    str1 +='''<font size="2">{}</font>'''.format(message['text'])
    try:
        kids = children[message['id']]
    except KeyError:
        pass
    else:
        str1 +='<blockquote>'
        for kid in kids:
            format_show(kid)
        str1 +='</blockquote>'
    return str1


## 主页发布
def Message():
    str1 ='''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>123456</title>
</head>
<body>
    <h3>5678</h3>
'''
    sql = 'select * from messages'
    curs.execute(sql)
    messages = curs.fetchall()
    top_level = []
    children = {}
    for message in messages:
        parrent_id = message['reply_to']
        if parrent_id is None:
            top_level.append(message)
        else:
            children.setdefault(parrent_id, []).append(message)

    for message in top_level:  # 遍历顶级消息列表
        str1+=format_show(message,str1=str1,children=children)  # 调用递归函数

    str1 +='''
<hr/>
<a href="edit"><font size="2">send</font></a>
</body>
</html>
'''
    return str1


def view():
    # id = form.getvalue('id') # 获取URL中的id参数
    id = request.args.get('id')
    # id=3
    str1 = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>view</title>
</head>
<body>
'''
    try:
        print(id)
        id = int(id)  # 将id转换为整数类型
    except:  # 如果转换异常
        print('无效的消息id！')
        sys.exit()  # 退出脚本执行

    sql = 'select * from messages where id=%i' % id
    curs.execute(sql)
    rows = curs.fetchall()
    if not rows:  # 如果没有查询结果
        print('消息不存在！')
        sys.exit()  # 退出脚本执行
    row = rows[0]  # 获取查询结果中的第一个字典
    print(row)
    str1 +='''
<p>
<h5>%(subject)s</h5>
<font size="2">%(sender)s</font></br>
<pre>%(text)s</pre>
</p>
<hr/>
<a href="/"><font size="2">first</font></a>|
<a href="edit?reply_to=%(id)s"><font size="2">replay</font></a>
</body>
</html>
''' % row
    return str1


## save 的内部实现方法
def quote(string):  # 定义处理单引号的函数
    if string:  # 如果不是空值或None值
        return string.replace("'", "''")  # 将单引号替换为两个单引号
    else:
        return string
## save的实现
def save():
    str1 = ""

    subject = quote(form.getvalue('subject'))  # 获取字段值并进行单引号处理
    sender = quote(form.getvalue('sender'))  # 获取字段值并进行单引号处理
    reply_to = form.getvalue('reply_to')
    text = quote(form.getvalue('text'))  # 获取字段值并进行单引号处理
    print(subject,sender,reply_to,text)

    if reply_to is not None:  # 如果有被回复消息的id
        try:
            reply_to = int(reply_to)  # 将id转换为整数类型
        except:  # 如果转换异常
            str1 = '''
            <font size="2" color="red">not message</font>
            <hr/>
            <a href="edit?reply_to=%s"><font size="2">restart edit</font></a>
            ''' % reply_to
            sys.exit()  # 退出脚本执行
    if not (subject and sender and text):  # 如果有任何一个字段值为空值或者None值
        str1 +='''
        <font size="2" color="red">input</font>
        <hr/>
        <a href="/"><font size="2">first</font></a>
        '''
    else:  # 如果是符合要求的输入
        if reply_to is None:  # 如果是回复消息
            sql = "insert into messages(subject,sender,text) values('%s','%s','%s')" % (subject, sender, text)
        else:  # 如果是新发布消息
            sql = "insert into messages(subject,sender,reply_to,text) values('%s','%s','%i','%s')" % (
                subject, sender, reply_to, text)
        curs.execute(sql)
        conn.commit()
        str1 +='''
        <font size="2" color="green">success</font>
        <hr/>
        <a href="/"><font size="2">return</font></a>
        '''
    return str1

def edit():
    reply_to = form.getvalue('reply_to')  # 获取被回复消息的id
    print(reply_to)
    subject = ''  # 创建标题变量

    str1 ='''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <title>edit message</title>
    </head>
    <body>
    <form action="save" method="post">
    ''' # 创建HTML基本代码并添加表单
    if reply_to is not None:  # 如果获取到被回复消息的id
        try:
            reply_to = int(reply_to)  # 将id转换为整数类型
        except:  # 如果转换发生异常
            print('无法回复该消息！')
            sys.exit()  # 退出脚本执行
        else:  # 如果id可用
            str1 += '    <input type="hidden" value="%s" name="reply_to"/>' % reply_to  # 将被回复消息id写入表单元件值
            sql = 'select subject from messages where id=%i' % reply_to  # 通过被回复消息id查询被回复消息的标题
            curs.execute(sql)
            subject = curs.fetchone()[0]  # 将查询到的标题存入变量
            if not subject.startswith('reply: '):  # 如果标题开头没有“回复：”字样
                subject = 'reply: ' + subject  # 为标题添加“回复：”字样

    str1 += '''
        <b><font size="2">subject: </font></b><br/>
        <input type="text" value="%s"  style="width:240px" name="subject"/><br/>
        <b><font size="2">author: </font></b><br/>
        <input type="text"  style="width:240px" name="sender"/><br/>
        <b><font size="2">edit content: </font></b><br/>
        <textarea rows="5" cols="50" style="width:240px" name="text"></textarea><br/>
        <input type="submit" value="send">
    </form>
    <hr/>
    <a href="/"><font size="2">first</font></a>
    </body>
    </html>
    ''' % subject
    return str1

if __name__ == '__main__':
    print(edit())