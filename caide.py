from flask import Flask, render_template

app = Flask("MyApp")

@app.route("/")
def hello():render_template("Donegal.html")

@app.route("/<Newsletter>")
def hello_someone(name):
	return render_template("DonegalNews.html", name=name.title())   

@app.route("/signup", methods=["POST"])
def sign_up():
	form_data = request.form
	print form_data["email"]
	return "All OK"	 

app.run(debug=True)