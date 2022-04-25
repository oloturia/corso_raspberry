#!/usr/bin/env python3
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

import grovepi

def get_temp(update: Update, context: CallbackContext) -> None:
    [temp,hun] = grovepi.dht(4,0)
    update.message.reply_text(str(temp))

if __name__ == "__main__":
    with open("TOKEN") as token_file:
        token_lines = token_file.readlines()
    token = token_lines[0].strip()
    updater = Updater(token)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('temp', get_temp))

    updater.start_polling()
    updater.idle()
