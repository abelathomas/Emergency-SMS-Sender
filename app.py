import os

from dotenv import load_dotenv
from flask import (
    Flask,
    flash, 
    render_template, 
    redirect,
    request,
    url_for,
)
from twilio.rest import Client

load_dotenv()
app = Flask(__name__)
app.secret_key = "ssssh don't tell anyone"

TWILIO_NUMBER = os.getenv('TWILIO_NUMBER')

client = Client()

def get_sent_messages():
    messages = client.messages.list(from_=TWILIO_NUMBER)
    return messages

def send_message(to, body):
    client.messages.create(to=to,from_=TWILIO_NUMBER,body=body)

@app.route("/", methods=["GET"])
def index():
    messages = get_sent_messages()
    return render_template("index.html", messages=messages)

@app.route("/add-msg", methods=["POST"])
def add_msg():
    sender = request.values.get('sender')
    msg = request.values.get('msg')
    to = request.values.get('to')
    body = f'EMERGENY TEXT FROM {sender}: {msg}.'
    send_message(to, body)
    flash('Your message was successfully sent')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
