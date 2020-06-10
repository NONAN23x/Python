import time, random
from twilio.rest import Client
sid = "ACc6d5a5f2b1a4938dcee19c35bdcedf79"
token = "b85247c7acdd2b67f1deda560c5466d8"
client = Client(sid, token)
def frequent_texter():
        random_msgs = ["Consider drinking some water :)",
                       "Make sure you spend some time on Reddit :)",
                       "Duolingo Time!!!",
                       "Have you completed today's streak?",
                       "Beware of MK MK germs! qwq",
                       "Wash your hands!",
                       "Consider looking away for a while :)",
                       "Rub your eyes qwq",
                       "Hope everything's okay :)",
                       "Remember to practise your Python problems :)",
                       "I'm watching you!!! lol :)",
                       "Remember, there's a goal to achieve"
                       ]
        while True:
            message = client.messages.create(
                body=random.choice(random_msgs),
                from_='whatsapp:+14155238886',
                to='whatsapp:+919502760173'
            )
            time.sleep(1000)
frequent_texter()
