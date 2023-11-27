from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://qbadmin:qianbase@10.14.40.152:26287/qianbase'
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(50), nullable=False)
	email = db.Column(db.String(150))

@app.route('/')
def index():
	users = User.query.all()
	return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add_user():
	username = request.form['username']
	email = request.form['email']
	new_user = User(username=username, email=email)
	db.session.add(new_user)
	db.session.commit()
	return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_user(id):
	user_to_delete = User.query.get_or_404(id)
	db.session.delete(user_to_delete)
	db.session.commit()
	return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['POST'])
def update_user(id):
	user_to_update = User.query.get_or_404(id)
	user_to_update.username = request.form['username']
	user_to_update.email = request.form['email']
	db.session.commit()
	return redirect(url_for('index'))

if __name__ == '__main__':
	# db.create_all()
	app.run(debug=True)
