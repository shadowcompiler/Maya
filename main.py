 #!/usr/bin/env python
# coding: utf-8

TOKEN = 'your bot token'

#import
from telegram.ext import Updater, CommandHandler, MessageHandler,Filters
from telegram import Message
import logging

#import func
from reponses import tuto, bienv, contenu, inter,member

#import

#var
lasttuto = tuto()
bienmsg = bienv()
contmsg = contenu()
intermsg = inter()
mbrmsg = member()
#var

updater = Updater(TOKEN, use_context=True)

dispatcher = updater.dispatcher


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text = bienmsg.format(update.effective_user.first_name))

start_handler = CommandHandler('start', start)

dispatcher.add_handler(start_handler)
def link (update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = "link")

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

updater.start_polling()
updater.idle()


