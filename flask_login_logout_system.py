# Program : A very basic Login Logout System using Python Flask and MySQL database
# Programmed By : Suman Gangopadhyay
# Email ID : linuxgurusuman@gmail.com
# URL : https://www.linkedin.com/in/sumangangopadhyay/
# Date : 7-Nov-2018
# Language : Python 3.5
# Framework : Flask
# Caveats : Using MySQL database. Please create the database and the table before using the program. See line 24 to 29
# Copyright © 2018 Suman Gangopadhyay

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, logout_user, login_required, LoginManager, UserMixin

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:suman@localhost/php_mysqli'
app.config['SECRET_KEY'] = 'happy_diwali'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

class login_system(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    user = db.Column(db.String(20), unique=True)
    password  = db.Column(db.String(20))
    visible = db.Column(db.Integer)

@login_manager.user_loader
def load_user(user_id):
    return login_system.query.get(int(user_id))

@app.route('/')
def index():
    user = login_system.query.filter_by(user='suman').first()
    login_user(user)
    return "SUCCESS : You are logged in"


@app.route('/admin')
@login_required
def admin():
    return "This is the home page of Suman the Administrator"

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return "You are now successfully logged out !"


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)