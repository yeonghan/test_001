#-*- coding: utf-8 -*-
from flask import Flask, render_template, request, url_for

#Initialize
app = Flask(__name__)

#Define a route for url
@app.route('/')
def form():
	return render_template('form_submit.html')

#form action
@app.route('/hello', methods=['POST'] )
def action():
	firstname = request.form['firstname']
	lastname = request.form['lastname']
	email = request.form['email']
	return render_template('form_action.html', firstname=firstname, lastname=lastname, email=email)

#Run the app
if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)

