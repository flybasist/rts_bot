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
import schedule
import scheduletask
import threading

version = ("0.4 beta3")

crash = 0

idbot = settings.id_bot()
bot = telebot.TeleBot(idbot)

def variables(message):
    contenttype = message.content_type
    chatid = message.chat.id
    userid = message.from_user.id
    chatname = message.chat.username
    chattitle = message.chat.title
    username = message.from_user.username
    messageid = message.message_id
    text = message.text
    caption = message.caption
    violation = 0
    systemtime = datetime.datetime.today()
    timedelta = systemtime - datetime.timedelta(days=1)
    date_message = systemtime.strftime('%Y-%m-%d %H:%M:%S')
    delta_message = timedelta.strftime('%Y-%m-%d %H:%M:%S')
    checkvip = settings.vip_members()
    vacuumcleaner = settings.vacuumcleaner()
    checkvip = vip.checkuser(userid, checkvip)
    vacuumcleaner = vip.checkvacuumcleaner(userid, vacuumcleaner)
    return(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)

@bot.message_handler(commands=['version'])
def start_message(message):
    chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner = variables(message)
    log.logging.info (message)
    log.logging.info ("")
    reaction.reactionversion(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip,
                             vacuumcleaner, version)
    
@bot.message_handler(commands=['statistics'])
def start_message(message):
    chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner = variables(message)
    log.logging.info (message)
    log.logging.info ("")
    userstatistics.statistics(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)

@bot.message_handler(content_types=['audio', 'photo', 'voice', 'video', 'document', 'text', 'location', 'contact', 'sticker', 'animation', 'video_note'])
def send_text(message):
    log.logging.info (message)
    log.logging.info ("")
    chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner = variables(message)
    db.clearbase(delta_message)
    reaction.reaction(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)
    
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
    
    schedule.every().monday.at("09:00").do(scheduletask.postalmonday, chatid=chatid)
    schedule.every().tuesday.at("09:00").do(scheduletask.postaltuesday, chatid=chatid)
    schedule.every().wednesday.at("09:00").do(scheduletask.postalwednesday, chatid=chatid)
    schedule.every().thursday.at("09:00").do(scheduletask.postalthursday, chatid=chatid)
    schedule.every().friday.at("09:00").do(scheduletask.postalfriday, chatid=chatid)
    
    while crash == 0:  
        try:        
            schedule.run_pending()
            time.sleep(1)
        except:
            print(traceback.format_exc())
            crash = 1

def runbot():

    thread1 = threading.Thread(target=runpolling, args=())
    thread2 = threading.Thread(target=schedules, args=())

    thread1.start()
    thread2.start()