# CancelledTrain

### Requirements
This was written in Python 3.6 using:

Twilio 6.10.1  
Flask 0.12.2


### Set up
First of all you will need to [make a Twilio account](https://www.twilio.com/try-twilio)  
Second you need to [set up a phone number](https://www.twilio.com/docs/quickstart/python/sms#sign-up-for-twilio-and-get-a-phone-number), this will be the number that you will send and recieve texts from. If you're using the second method (detailed below) you will need to download and [set up ngrok as well](https://www.twilio.com/docs/quickstart/python/sms#allow-twilio-to-talk-to-your-flask-application).

In CancelledTrain.py there are functions setDefaultTrainStation and setDate, these are configured to use the stations and times I personally use to commute to work but you will probably want to change these too.

There are two ways to use this  
1) Run the script manually using CancelledTrain.py. If you do this in SendMessage.py you will need to populate the accountSID, authToken, fromPhoneNumber and toPhoneNumber fields.  
The toPhoneNumber is just your mobile number so that's simple. fromPhoneNumber is your new Twilio number. Remember to put the appropriate country code at the beginning (so +44 for UK numbers)  
accountSID and authToken are defined in your account profile under the same name.  

2) Run the flask app and text your Twilio number to recieve information on which trains are and are not cancelled. If you send a one word message you will recieve the same information as you would in the first method. Otherwise you can text the three letter abbreviations for two stations and it will list the status of all trains running from the first the second over the next hour. 



