from flask_sqlalchemy import  SQLAlchemy
from flask import Flask, render_template


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://qbadmin:qianbase@10.14.40.152:26287/qianbase'
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)

	def __repr__(self):
		return f'<User {self.username}>'

@app.route('/')
def index():
	users = User.query.all()
	return render_template('index.html', users=users)


if __name__ == '__main__':
    app.run()
