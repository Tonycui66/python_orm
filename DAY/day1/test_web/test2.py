
from DAY.day1.test_web.util import *
import os
from flask import Flask,render_template

app = Flask(__name__)
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/edit')
def edit():
	return render_template('edit.html')


@app.route('/save')
def save():
	return render_template('save.html')


@app.route('/view')
def view():
	Html.gen_view_html
	return render_template('view.html',html_files=['save.html'])
if __name__ == '__main__':
    Html = GenHtml()
    Html.gen_save_html
    Html.gen_edit_html
    Html.gen_view_html
    app.run()

