from twilio.rest import Client

account_sid = "ACc6d5a5f2b1a4938dcee19c35bdcedf79"
auth_token = "41af7bdf7d98db72afa9c3ce5cb6cc0d"
client = Client(account_sid, auth_token)

msg = str(input("Message: "))
person = str(input("To : "))


message = client.messages.create(
                              body=msg,
                              from_='whatsapp:+14155238886',
                              to='whatsapp:' + person
                          )

print(message.sid)
