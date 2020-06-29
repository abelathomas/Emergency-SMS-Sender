# Emergency SMS Sender


## Inspiration for the project
One day I lost my phone in my univeristy and I was supposed to meet my friend. I wanted to text my friend to let them know I would be late but since they didn't have
a data plan, I couldn't use messaging apps like whatsapp. Then I stuck me if I had a web app that would let me send text messages to my friends, it would have been 
very useful in such situations!


## Built Using
  - Python / Flask (Web app)
  - Postman (API Testing)
  - Twilio API (Programmable SMS API)


## Project Description
This is a Flask App that allows all the people whose phone numbers I have authenticated in my Twilio account, to send messages to each other.


## Local Installation
Update the `.env` and with your [Twilio](https://twilio.com) credentials.


### Running the application
* `python -m venv .venv`
* `.\.venv\Scripts\activate`
* `pip install -r requirements.txt`
* `flask run`
<br/>Open the link that flask generates


This application was inspired by an 'Intro to API course' by Dennis Craig 