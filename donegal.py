from flask import Flask, render_template, request

app = Flask("DonegalFlaskApp")

@app.route("/signup", methods=["POST"])
def sign_up():
	form_data = request.form

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox83ab942dbd1a4d8e9396b91b605ae76a.mailgun.org/messages",
        auth=("api", "key-fe7ddc05a0e87f60707a8b651f8a333b"),
        data={"from": "Donegal Newsletter <sureiwouldntknow@imfromdonegal.mailgun.org>",
              "to": form_data["email"],
              "subject": "Welcome to Donegal",
#need to make to "to" variable also need to make the dear "name" variable in the body text of the mailgun
              "text": "Dear User, Thank You for signing up for our Donegal Tourist Newsletter. We'll be in touch to let you know of any upcoming events! "})
