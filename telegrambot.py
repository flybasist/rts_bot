import traceback
import settings
import telebot
import logs
import time
import reaction
import db
import userstatistics
import scheduletask
import threading
import variables

def worksettings():
    global bot
    id_bot = settings.id_bot()
    bot = telebot.TeleBot(id_bot)
    botinfo = bot.get_me()
    db.startbase(botinfo, id_bot)
#    id_bot, userid_bot, username_bot = db.readsettingsbot()
#    bot = telebot.TeleBot(id_bot)

crash = 0
bot = None

worksettings()

@bot.message_handler(content_types=['new_chat_members'])
def handle_new_chat_members(message):
    logs.logging.info (message)
    variablesdict = variables.variables(message)
    db.clearbase(variablesdict)
    for new_member in message.new_chat_members:
        if new_member.id == bot.get_me().id:
            reaction.newchat(variablesdict)
        else:
            reaction.newmember(variablesdict)

@bot.message_handler(commands=['version'])
def start_message(message):
    logs.logging.info (message)
    variablesdict = variables.variables(message)
    db.clearbase(variablesdict)
    variablesdict = variables.variableslimits(variablesdict)
    reaction.reactionversion(variablesdict)
    
@bot.message_handler(commands=['statistics'])
def start_message(message):
    logs.logging.info (message)
    variablesdict = variables.variables(message)
    db.clearbase(variablesdict)
    variablesdict = variables.variableslimits(variablesdict)
    userstatistics.statistics(variablesdict)

@bot.message_handler(content_types=['audio', 'photo', 'voice', 'video', 'document', 'text', 'location', 'contact', 'sticker', 'animation', 'video_note'])
def send_text(message):
    logs.logging.info (message)
    variablesdict = variables.variables(message)
    db.clearbase(variablesdict)
    variablesdict = variables.variableslimits(variablesdict)
    reaction.newmessage(variablesdict)
    
@bot.edited_message_handler(func=lambda message: True)
def handle_edited_message(message):
    logs.logging.info (message)
    variablesdict = variables.variables(message)
    db.clearbase(variablesdict)
    reaction.newmessage(variablesdict)

def runpolling():
    global crash
    try:
        bot.polling()
    except:
        print(traceback.format_exc())
    finally:
        crash = 1

def schedules():
    global crash
    
    chatid = settings.chatforpostal()
    scheduletask.schedulesettins(chatid)
    
    while crash == 0:  
        try:        
            scheduletask.schedule.run_pending()
            time.sleep(1)
        except:
            print(traceback.format_exc())
            crash = 1

def runbot():
    thread1 = threading.Thread(target=runpolling, args=())
    thread2 = threading.Thread(target=schedules, args=())
    thread1.start()
    thread2.start()
