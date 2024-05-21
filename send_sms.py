# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()



# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='This is the meassage from python-django web app',
         from_='+16592229944',
         to='+16474737409',
         media_url=['https://c1.staticflickr.com/3/2899/14341091933_1e92e62d12_b.jpg'],
     )

print(message.sid)
print(message.status)
print(message.media._uri)
