# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import CancelledTrain

app = Flask(__name__)

@app.route("/", methods=['POST'])
def sms_train_status():
    
	trainStatus = CancelledTrain.TrainStatus(True)
	
	message_body = request.form['Body'].split(' ')
	
	if len(message_body) >= 2:
		trainStatus.setStations(message_body[0], message_body[1])
	else:	
		trainStatus.setDefaultStations()
	trainStatus.buildUrl()
	text = trainStatus.scrapeRTT()
	
	resp = MessagingResponse()
	resp.message(text)

	return str(resp)	

@app.route("/", methods=['GET'])
def default_page():
	return 'Default home page :)'

if __name__ == "__main__":
	app.run(debug=True)