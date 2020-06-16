 #!/usr/bin/env python
# coding: utf-8

#import os

TOKEN = '1189867677:AAGkceniFFRCJl-NJ_stQEI2PA4uHmyZhxU'

PORT = int(os.environ.get('PORT', '8443'))

#importation 
from telegram.ext import Updater, CommandHandler, MessageHandler,Filters
from telegram import Message
import logging

#import des foctions de retours de messages
from reponses import tuto, bienv, contenu, inter,member

#importation

#variables messages
lasttuto = tuto()
bienmsg = bienv()
contmsg = contenu()
intermsg = inter()
mbrmsg = member()
#variables messages

updater = Updater(TOKEN, use_context=True)

dispatcher = updater.dispatcher


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text = bienmsg.format(update.effective_user.first_name))

start_handler = CommandHandler('start', start)

dispatcher.add_handler(start_handler)
def link (update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = "Welearn : https://t.me/yeswecode")

link_handler = CommandHandler('link', link)
dispatcher.add_handler(link_handler)

def content(update,  context):
    context.bot.send_message(chat_id=update.effective_chat.id, text = contmsg)
    
content_handler = CommandHandler('content', content)
dispatcher.add_handler(content_handler)

def last(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text = lasttuto)

last_handler = CommandHandler('last', last)
dispatcher.add_handler(last_handler)

def quizz(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=intermsg)
    
quizz_handler = CommandHandler('quizz', quizz)
dispatcher.add_handler(quizz_handler)

def mentor(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="")

mentor_handler = CommandHandler('mentor', mentor)
dispatcher.add_handler(mentor_handler)

def nouvmbr(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=mbrmsg.format(update.effective_user.first_name))
    
nouvmbr_handler = MessageHandler(Filters.status_update.new_chat_members, nouvmbr)
dispatcher.add_handler(nouvmbr_handler)

updater.start_webhook(listen='0.0.0.0', port=PORT, url_path=TOKEN)
updater.bot.set_webhook("https://mayalearnbot.herokuapp.com/" + TOKEN)
updater.idle()


