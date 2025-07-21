#!/usr/bin/python3
from flask import Flask, redirect, render_template, request, url_for, session

app=Flask(__name__)

app.secret_key='whoareyou'

#dummy user data
USER={
	"username":"admin",
	"password":"password123"
}

@app.route('/')
def index():
	return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
	#get the information from the form
	if request.method=='POST':
		username=request.form['username']
		password=request.form['password']

		#check if the information on the form is correct in order to login
		if username==USER['username'] and password== USER['password']:
			session['username']=username
			return redirect(url_for('home'))

		else:
			return "INVALID CREDENTIALS. Try Again!!"
	# 👇 Fix: return the login form for GET request
	return render_template('login.html')

@app.route('/home')
def home():
	if 'username' in session:
		return render_template('home.html', username=session['username'])

	else:
		return redirect(url_for('login'))


@app.route('/logout')
def logout():
	session.pop('username', None)
	return redirect(url_for('login'))

if __name__=='__main__':
	app.run(debug=True)
