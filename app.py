from unicodedata import name
from flask import Flask, redirect, url_for, render_template, request, send_from_directory
import pandas as pd
import csv
import statistics
import main.py
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
		data = []
		avgcost = []
		C_avg = []
		with open("C:\\Users\\Admin\\Downloads\\Going-Data-Way\\test.csv") as file:
			csvfile = csv.reader(file)
			for row in csvfile:
				data.append(row)
				data.pop(0)

			for i in range(len(data)):
				avgcost.append(float(data[i][2]))
				C_avg = np.mean(avgcost)
			C_avg=pd.DataFrame(C_avg)
	return render_template("cost.html")

@app.route("/paid", methods=["POST", "GET"])
def paid():
	if request.method == 'POST':
		f = request.form['paid']		
	return render_template("paid.html")

@app.route("/owned", methods=["POST", "GET"])
def owned():
	if request.method == 'POST':
		f = request.form['owned']		
	return render_template("owned.html")

@app.route("/test")
def dynamic_page():
	return main.column_average

if __name__ == "__main__":
	app.run(debug=True)