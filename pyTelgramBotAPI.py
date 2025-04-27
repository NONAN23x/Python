# lol
import telebot
import datetime
import time
import Scheduling

bot = telebot.TeleBot("#Your Api Key here")
user = 'Your UserID'


def send_messages(message):
    bot.send_message(chat_id=user, text=message)


def main():
    send_messages("Segmentation initialised")
    while True:
        hour = datetime.datetime.now().hour - 12 if datetime.datetime.now().hour >= 13 else datetime.datetime.now().hour
        tmp = " PM" if datetime.datetime.now().hour >= 12 else " AM"
        current_time = str(hour) + ':' + str(datetime.datetime.now().minute) + tmp
        print(current_time)
        if current_time in Scheduling.dict:

            send_messages(Scheduling.dict[current_time])
            print("Message sent successfully")
            print(current_time)
            time.sleep(30)
        else:
            time.sleep(30)


if __name__ == '__main__':
   main()
