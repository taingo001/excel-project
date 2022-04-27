from unicodedata import name
from flask import Flask, redirect, url_for, render_template, request, send_from_directory
import pandas as pd
import csv
import numpy as np
import statistics

from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'csv'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#Create a route to home page
@app.route("/", methods=['GET', 'POST'])
def index():
	return render_template("index.html")

#Create a route to application page
@app.route("/application", methods=['GET', 'POST'])
def application():
	return render_template("application.html")


@app.route("/data", methods=['GET', 'POST'])
def data():
	if request.method == 'POST':
		f = request.form['myfile']
	elif request.method == 'GET':
		f = f"./uploads/{request.args.get('file')}"

	data = []
	with open(f) as file:
		csvfile = csv.reader(file)
		for row in csvfile:
			data.append(row)
	data = pd.DataFrame(data)
	return render_template("data.html", data=data.to_html(header=False, index=False), file=request.args.get('file'))

#Create a route to about page
@app.route("/about")
def about():
	return render_template("about.html")

#Create a route to help page
@app.route("/help")
def help():
	return render_template("help.html")


@app.route('/upload', methods=['GET', 'POST'])
def upload():
	if request.method == 'POST':
		f = request.files['myfile']
		f.save(f'./uploads/{secure_filename(f.filename)}')
	return redirect(url_for('data', file=secure_filename(f.filename)))

#Create a route to download the template
@app.route("/download/<path:name>")
def download(name):
	return send_from_directory(
		app.config['UPLOAD_FOLDER'], name, as_attachment=True)

@app.route("/cost", methods=["POST", "GET"])
def cost():
	if request.method == 'POST':
		f = request.form['cost']
		df = pd.read_csv(r'test.csv')
		mean1 = round(df['Cost'].mean(),2)
		data = []
		with open("static/cost.csv") as file:
			csvfile = csv.reader(file)
			for row in csvfile:
				data.append(row)
		data = pd.DataFrame(data)
		
	return render_template("cost.html", data=data.to_html(header=False, index=False)+"Mean of Cost: "+ str(mean1))

@app.route("/paid", methods=["POST", "GET"])
def paid():
	if request.method == 'POST':
		f = request.form['paid']
		df = pd.read_csv(r'test.csv')
		mean2 = round(df['Payed'].mean(),2)
		data = []
		with open("static/payed.csv") as file:
			csvfile = csv.reader(file)
			for row in csvfile:
				data.append(row)
		data = pd.DataFrame(data)		
	return render_template("paid.html", data=data.to_html(header=False, index=False)+"Mean of Payed: "+ str(mean2))

@app.route("/owed", methods=["POST", "GET"])
def owed():
	if request.method == 'POST':
		f = request.form['owed']
		df = pd.read_csv(r'test.csv')
		mean3 = round(df['Owed'].mean(),2)
		data = []
		with open("static/owed.csv") as file:
			csvfile = csv.reader(file)
			for row in csvfile:
				data.append(row)
		data = pd.DataFrame(data)		

	return render_template("owed.html", data= data.to_html(header=False, index=False) +"Mean of Owed: "+ str(mean3))

if __name__ == "__main__":
	app.run(debug=True)
