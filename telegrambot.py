import traceback
import settings
import telebot
import log
import time
import datetime
import reaction
import db
import userstatistics
import vip
import scheduletask
import threading

crash = 0

idbot = settings.id_bot()
bot = telebot.TeleBot(idbot)

def variables(message):
    variablesdict = {}
    variablesdict["version"] = ("0.4")
    variablesdict["namebase"] = settings.namebase()
    variablesdict["contenttype"] = message.content_type
    variablesdict["chatid"] = message.chat.id
    variablesdict["userid"] = message.from_user.id
    variablesdict["chatname"] = message.chat.username
    variablesdict["chattitle"] = message.chat.title
    variablesdict["username"] = message.from_user.username
    variablesdict["messageid"] = message.message_id
    variablesdict["text"] = message.text
    variablesdict["caption"] = message.caption
    variablesdict["violation"] = 0
    systemtime = datetime.datetime.today()  
    timedeltaday = systemtime - datetime.timedelta(days=1)
    timedeltahour = systemtime - datetime.timedelta(hours=1)
    timedeltamin = systemtime - datetime.timedelta(minutes=10)
    date_message = systemtime.strftime('%Y-%m-%d %H:%M:%S')
    deltaday_message = timedeltaday.strftime('%Y-%m-%d %H:%M:%S')
    deltahour_message = timedeltahour.strftime('%Y-%m-%d %H:%M:%S')
    deltamin_message = timedeltamin.strftime('%Y-%m-%d %H:%M:%S')
    variablesdict["date_message"] = date_message
    variablesdict["deltaday_message"] = deltaday_message
    variablesdict["deltahour_message"] = deltahour_message
    variablesdict["deltamin_message"] = deltamin_message
    checkvip = settings.vip_members()
    vacuumcleaner = settings.vacuumcleaner()
    checkvip = vip.checkuser(message.from_user.id, checkvip)
    variablesdict["checkvip"] = checkvip
    vacuumcleaner = vip.checkvacuumcleaner(message.from_user.id, vacuumcleaner)
    variablesdict["vacuumcleaner"] = vacuumcleaner
    variablesdict["stickeramiga"] = settings.stickeramiga()
    variablesdict["stickersregidron"] = settings.stickerregidron()
    variablesdict["useridbot"] = settings.useridbot()
    variablesdict["usernamebot"] = settings.usernamebot()
    return(variablesdict)

@bot.message_handler(commands=['version'])
def start_message(message):
    log.logging.info (message)
    variablesdict = variables(message)
    reaction.reactionversion(variablesdict)
    
@bot.message_handler(commands=['statistics'])
def start_message(message):
    log.logging.info (message)
    variablesdict = variables(message)
    userstatistics.statistics(variablesdict)

@bot.message_handler(content_types=['audio', 'photo', 'voice', 'video', 'document', 'text', 'location', 'contact', 'sticker', 'animation', 'video_note'])
def send_text(message):
    log.logging.info (message)
    variablesdict = variables(message)
    db.clearbase(variablesdict)
    reaction.reaction(variablesdict)
    
def runpolling():
    global crash
    try:
        db.checkbase()
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