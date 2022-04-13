#!/usr/bin/env python3
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import random

def dice_throw(update: Update, context: CallbackContext) -> None:
    if len(context.args) == 0:
        max_num = 6
    else:
        max_num = int(context.args[0])
    dice = str(random.randint(1,max_num))
    update.message.reply_text(dice)

def help_online(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Send /throw [x] for a random number from 1 to x, if x is omitted, 6 is the default value")

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Welcome to DadoBot")

if __name__ == "__main__":
    with open("TOKEN") as token_file:
       token_lines = token_file.readlines()
    token = token_lines[0].strip()
    updater = Updater(token)
    
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('throw', dice_throw, pass_args=True))
    dp.add_handler(CommandHandler('help', help_online))
    updater.start_polling()
    updater.idle()
