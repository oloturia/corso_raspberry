#!/usr/bin/env python3
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import random
import bargraph

history = [0]*6

def dice_throw(update: Update, context: CallbackContext) -> None:
    if len(context.args) == 0:
        max_num = 6
    else:
        max_num = int(context.args[0])
    dice = random.randint(1,max_num)
    if max_num == 6:
        history[dice-1] += 1
    update.message.reply_text(str(dice))

def stats(update: Update, context: CallbackContext) -> None:
    barGraph = bargraph.generate(history)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open("./stats.png","rb"))

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
    dp.add_handler(CommandHandler('stats', stats))
    updater.start_polling()
    updater.idle()
