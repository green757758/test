# 11111
import logging
import telepot


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def send_message():
    bot.sendMessage("Chat_id", "This file is about ... please check")
    bot.sendDocument("Chat_id", document=open("./test1.xlsx", "rb"))


def send_phone():
    bot.sendPhoto("Chat_id", photo=open("test1.jpg", "rb"))


if __name__ == '__main__':
    bot = telepot.Bot("TOKEN")
    # send_message()
    send_phone()
