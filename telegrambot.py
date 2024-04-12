import settings
import telebot
import log
import datetime
import reaction
import db
import userstatistics
import vip

version = ("0.3.1")

idbot = settings.id_bot()
bot = telebot.TeleBot(idbot)

def variables(message):
    contenttype = message.content_type
    chatid = message.chat.id
    userid = message.from_user.id
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
    return(chatid, userid, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)

@bot.message_handler(commands=['version'])
def start_message(message):
    chatid, userid, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner = variables(message)
    log.logging.info (message)
    reaction.reactionversion(chatid, version)
    
@bot.message_handler(commands=['statistics'])
def start_message(message):
    chatid, userid, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner = variables(message)
    log.logging.info (message)
    userstatistics.statistics(chatid, userid, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)

@bot.message_handler(content_types=['audio', 'photo', 'voice', 'video', 'document', 'text', 'location', 'contact', 'sticker', 'animation', 'video_note'])
def send_text(message):
    log.logging.info (message)
    chatid, userid, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner = variables(message)
    db.clearbase(delta_message)
    reaction.reaction(chatid, userid, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)
    
def runbot():
    db.checkbase()
    bot.polling()