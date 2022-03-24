from unicodedata import name
from flask import Flask, redirect, url_for, render_template, request, send_from_directory
import pandas as pd
import csv
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
		f = request.form['csv file']
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


@app.route("/download/<path:name>")
def download(name):
	return send_from_directory(
		app.config['UPLOAD_FOLDER'], name, as_attachment=True)

@app.route("/excel", methods=["POST", "GET"])
def excel(selected):
	if request.method == 'POST':
		result = request.form
		f = open("C:\\Users\\Admin\\Downloads\\Going-Data-Way\\test-file.csv")
		for element in f:
			total += int(element)
			average = total/len(data)
			print(average)
	return render_template("data.html", result = result)


if __name__ == "__main__":
	app.run(debug=True)