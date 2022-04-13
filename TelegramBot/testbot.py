#!/usr/bin/env python3
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'hello {update.effective_user.first_name}')

updater = Updater('5275467894:AAGauowka-sQu5X-GKCLlfwTrWKvTZlHFRg')
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.start_polling()
updater.idle()
