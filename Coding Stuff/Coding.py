import time
import datetime as d
from twilio.rest import Client
import random
half_sid = "ACc6d5a5f2b1a4938d"
half_token = "b85247c7acdd2b67"
other_sid = open('othersid', 'r')
other_token = open('othertoken', 'r')

SID = half_sid + other_sid.read()
TKN = half_token + other_token.read()
client = Client(SID, TKN)

def frequent_texter():
        random_msgs = ["Consider drinking water :)",
                       "Do something productive dammit!",
                       "Duolingo Time!!!",
                       "Have you completed today's streak?",
                       "Beware of MK MK germs qwq",
                       "Wash your hands",
                       "Consider looking away for a while"
                       ]
        for i in range(1,8):
            message = client.messages.create(
                body=random.choice(random_msgs),
                from_='whatsapp:+14155238886',
                to='whatsapp:+919502760173'
            )
            time.sleep(60*20)
frequent_texter()
