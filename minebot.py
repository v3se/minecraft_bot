import time
import logging
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
import os
from optparse import OptionParser

SLEEP_INTERVAL = 1.0
logging.basicConfig(format='%(asctime)s %(message)s',level="INFO", datefmt='%d/%m/%Y %H:%M:%S')
updater = Updater(token='<add-token>')
dispatcher = updater.dispatcher

mybots = {}

def start(bot, update):
    """Send a message when the command /start is issued."""
    mybots[update.message.chat_id] = bot
    update.message.reply_text("Bot started")

def send_later(msg):
    for id, bot in mybots.items():
        bot.send_message(id, text=msg)

def tail(fin):
    "Listen for new lines added to file."
    while True:
        where = fin.tell()
        line = fin.readline()
        if not line:
            time.sleep(SLEEP_INTERVAL)
            fin.seek(where)
        else:
            yield line
            
def main():
    logging.info("MineBot started!")
    p = OptionParser("usage: minebot.py logfile")
    (options, args) = p.parse_args()
    if len(args) < 1:
        p.error("must specify a file to watch")
    logging.info(f"Reading the log {args[0]}")

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    updater.start_polling()

    with open(args[0], 'r') as fin:
        for line in tail(fin):
            line = line.strip()
            if (line.find('Player connected') != -1):
                player = line.split("]")[1]
                logging.info(player)
                send_later(player)

            if (line.find('Player disconnected') != -1):
                player = line.split("]")[1]
                send_later(player)

if __name__ == '__main__':
    main()