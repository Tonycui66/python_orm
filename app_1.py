from flask import Flask, render_template
from requests import request
import subprocess
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/run_program', methods=['POST'])
def run_program():
	program_name = request.form['program_name']
	output = subprocess.check_output([program_name])
	return output.decode('utf-8')

if __name__ == '__main__':
	app.run()