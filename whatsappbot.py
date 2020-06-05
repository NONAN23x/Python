from twilio.rest import Client

client = Client()

msg = str(input("Message : "))

message = client.messages.create(
                              body=msg,
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+919502760173'
                          )

print(message.sid)
