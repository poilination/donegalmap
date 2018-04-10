from flask import Flask, render_template, request
import requests 

app = Flask(__name__)

@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    #print form_data["email"]
    #requests.post 
    send_simple_message()

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox83ab942dbd1a4d8e9396b91b605ae76a.mailgun.org/messages",
        auth=("api", "key-fe7ddc05a0e87f60707a8b651f8a333b"),
        data={"from": "Donegal Newsletter <postmaster@sandbox83ab942dbd1a4d8e9396b91b605ae76a.mailgun.org>",
              "to": "Caitlin Roarty <caitlinroarty@gmail.com>",
              "subject": "Welcome to Donegal",
#need to make to "to" variable also need to make the dear "name" variable in the body text of the mailgun
              "text": "Dear Caitlin, Thank You for signing up for our Donegal Tourist Newsletter. We'll be in touch to let you know of any upcoming events! "})

@app.route("/news") 
def hello():
    return render_template("DonegalNews.html")


@app.route("/info") 
def info():
    return render_template("DonegalInfo.html")

@app.route("/") 
def home():
    return render_template("Donegal.html")





if __name__ == "__main__":
    app.run()