# lol
import telebot
import datetime
import time
import Scheduling

tmp = datetime.datetime.now().minute
hour = ((datetime.datetime.now().hour) - 12) if datetime.datetime.now().hour > 12 else datetime.datetime.now().hour

tmp = (str(hour) + " PM") if datetime.datetime.now().hour >= 12 else " AM"

current_time = str(hour) + ':' + str(datetime.datetime.now().minute) + tmp
bot = telebot.TeleBot("1367832954:AAFlfP275ECocvCs1arY2cT3SZdCzVY7dGc")
user = '1388226474'


def send_messages(message):
    bot.send_message(chat_id=user, text=message)
    print("Segmentation in progress..")


def main():
    while True:
        if current_time in Scheduling.dict:
            send_messages(Scheduling.dict[current_time])
            time.sleep(60)
        else:
            time.sleep(30)


print(current_time)
main()
