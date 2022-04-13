#!/usr/bin/env python3
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'hello {update.effective_user.first_name}')

with open("TOKEN") as token_file:
    token_lines = token_file.readlines()
    token = token_lines[0].strip()
    
updater = Updater(token)
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.start_polling()
updater.idle()
