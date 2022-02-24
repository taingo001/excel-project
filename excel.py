from flask import Flask, redirect, url_for, render_template, request
import pandas as pd
import csv

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
	return render_template("home.html")

@app.route("/data", methods=['GET', 'POST'])
def data():
	if request.method == 'POST':
		f = request.form['csv file']
		data = []
		with open(f) as file:
			csvfile = csv.reader(file)
			for row in csvfile:
				data.append(row)
		data = pd.DataFrame(data)
		return render_template("data.html", data=data.to_html(header=False, index=False))

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/help")
def help():
	return render_template("help.html")

if __name__ == "__main__":
	app.run(debug=True)