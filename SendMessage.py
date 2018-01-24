from twilio.rest import Client

def sendMessage(text):
	accountSID = '************'
	authToken = '************'
	
	fromPhoneNumber = '************'
	toPhoneNumber = '************'
	
	client = Client(accountSID,authToken)
	
	messages = client.messages.create(body=text,from_=fromPhoneNumber,to=toPhoneNumber)