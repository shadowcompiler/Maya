#!/usr/bin/env python
# coding: utf-8

import os

TOKEN = '1189867677:AAFC2awVNTR4diwp_xrwoiJEto39C8N3jeg'

PORT = int(os.environ.get('PORT', '8443'))

from telegram.ext import Updater, CommandHandler
from telegram import Message
import logging
from tuto import File

lasttuto = File()

updater = Updater(TOKEN, use_context=True)

dispatcher = updater.dispatcher


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text = "Ohayo {} sama ! Je suis le bot de WeLearn, vous pouvez m'appelez Maya je suis là pour vous servir. Dites moi ce que vous désirez, il vous suffit de choisir une commande dans la liste des commandes disponibles".format(update.effective_user.first_name))

start_handler = CommandHandler('start', start)

dispatcher.add_handler(start_handler)
def link (update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = "Welearn : https://t.me/yeswecode")

link_handler = CommandHandler('link', link)
dispatcher.add_handler(link_handler)

def content(update,  context):
    context.bot.send_message(chat_id=update.effective_chat.id, text = " Initiation à la programmation avec le C 1 : https://t.me/yeswecode/13 \n Initiation à la programmation avec le C 2 [Les ide]  : https://t.me/yeswecode/24 \n Du code ! : \nhttps://t.me/yeswecode/63")
    
content_handler = CommandHandler('content', content)
dispatcher.add_handler(content_handler)

def last(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text = lasttuto)

last_handler = CommandHandler('last', last)
dispatcher.add_handler(last_handler)

def quizz(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=" Les variables : http://t.me/QuizBot?start=0TukUH5k")
    
quizz_handler = CommandHandler('quizz', quizz)
dispatcher.add_handler(quizz_handler)

def mentor(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="")

mentor_handler = CommandHandler('mentor', mentor)
dispatcher.add_handler(mentor_handler)


updater.start_webhook(listen='0.0.0.0', port=PORT, url_path=TOKEN)
updater.bot.set_webhook("https://mayalearnbot.herokuapp.com/" + TOKEN)
updater.idle()


