#-*-coding:utf8
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://qbadmin:qianbase@10.14.40.152:26287/qianbase'
db = SQLAlchemy(app)

# User model
class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(50), nullable=False)
	email = db.Column(db.String(150))
	password_hash = db.Column(db.String(128))
	is_superuser = db.Column(db.Boolean, default=False)

	@property
	def password(self):
		raise AttributeError('password is not a readable attribute')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

# Authentication decorators
def login_required(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		if 'logged_in' not in session:
			flash('You need to be logged in to view this page.')
			return redirect(url_for('login'))
		return f(*args, **kwargs)
	return decorated_function

def superuser_required(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		if 'is_superuser' not in session or not session['is_superuser']:
			flash("You need superuser privileges to view this page.")
			return redirect(url_for('index'))
		return f(*args, **kwargs)
	return decorated_function

# Routes for authentication
@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		user = User(
			username=request.form['username'],
			email=request.form['email'],
			password_hash=request.form['password'],
		    is_superuser=request.form['is_superuser']
		)
		db.session.add(user)
		db.session.commit()
		flash('Registration successful. Please log in.')
		return redirect(url_for('login'))
	return render_template('register.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
# 	if request.method == 'POST':
# 		user = User.query.filter_by(username=request.form['username']).first()
# 		print(user.verify_password(request.form['password']))
# 		if user is not None and user.verify_password(request.form['password']):
# 			session['logged_in'] = True
# 			session['is_superuser'] = user.is_superuser
# 			session['username'] = user.username
# 			return redirect(url_for('dashboard'))
# 		else:
# 			flash('Invalid username or password.')
# 	return render_template('login.html')



# @app.route('/login', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		user = User.query.filter_by(username=request.form['username']).first()
		if user is not None and user.verify_password(request.form['password']):
			print("123455")
			session['logged_in'] = True
			session['is_superuser'] = user.is_superuser
			session['username'] = user.username
			flash('You are now logged in.', 'success')
			return redirect(url_for('index'))
		else:
			flash('Invalid username or password.', 'danger')
	return render_template('login.html')


@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	session.pop('is_superuser', None)
	session.pop('username', None)
	flash('You have been logged out.')
	return redirect(url_for('index'))

# Routes for user management
@app.route('/show')
@login_required
def index():
	users = User.query.all()
	return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
@superuser_required
def add_user():
	username = request.form['username']
	email = request.form['email']
	new_user = User(username=username, email=email, password=request.form['password'])
	db.session.add(new_user)
	db.session.commit()
	flash('New user added successfully.')
	return redirect(url_for('index'))

@app.route('/delete/<int:id>')
@superuser_required
def delete_user(id):
	user_to_delete = User.query.get_or_404(id)
	db.session.delete(user_to_delete)
	db.session.commit()
	flash('User deleted successfully.')
	return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['POST'])
@superuser_required
def update_user(id):
	user_to_update = User.query.get_or_404(id)
	user_to_update.username = request.form['username']
	user_to_update.email = request.form['email']
	db.session.commit()
	flash('User updated successfully.')
	return redirect(url_for('index'))





@app.route('/dashboard')
@login_required
def dashboard():
	# 此处可以根据用户角色调整显示的内容
	if session.get('is_superuser'):
		users = User.query.all()  # 如果是超级用户，展示所有用户列表
	else:
		users = None  # 如果不是超级用户，不展示用户列表
	# return render_template('dashboard.html', users=users)
	return render_template('index.html', users=users)




@app.route('/add_user', methods=['GET', 'POST'])
@superuser_required
def add_user_form():
	if request.method == 'POST':
		# 处理添加用户的逻辑
		pass
	return render_template('add_user.html')



# Run the Flask app
if __name__ == '__main__':
	# db.create_all()
	app.run(debug=True)
