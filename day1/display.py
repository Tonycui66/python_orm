# --*-- coding:utf8 --*--
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/show-file')
def show_file():
	file_content = ''
	with open('./bmsql.txt', 'r') as file:  # 替换为你的文件路径
		file_content = file.read()
	return render_template('display_file.html', content=file_content)

if __name__ == '__main__':
	app.run(debug=True)