# How to Rick Roll Your Friends:
### Writing a Program to Play Rick Astley Over the Phone
## Build a Tiny Web App
1. Create a small web app in Flask that can serve both XML and an .mp3 file of Rick Astley's "Never Gonna Give You Up"

My version of the web app is at ```tiny_web_app.py```. It responds with [TwiML](https://www.twilio.com/docs/api/twiml/your_response)
which allows use of Twilio's API.

2. Deploy the web app to the web.

I did this with ```Heroku```, which requires a ```Procfile``` for telling it what processes to run.
Here's the [website](https://afternoon-gorge-22076.herokuapp.com/)


## Use the Twilio API to Send Outgoing Calls
1. Implementation code can be found [here](https://github.com/mike-jolliffe/Projects/blob/master/Rick_Roll/twilio_api.py)
