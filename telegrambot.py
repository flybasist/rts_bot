import settings
import telebot
import log
import vip
import datetime
import reaction
import db
import checkmessage
import statistics

version = ("0.3")

idbot = settings.id_bot()
bot = telebot.TeleBot(idbot)
sql = db
checkmessages = checkmessage

def variables(message):
    contenttype = message.content_type
    chatid = message.chat.id
    userid = message.from_user.id
    username = message.from_user.username
    messageid = message.message_id
    text = message.text
    caption = message.caption
    checkvip = settings.vip_members()
    vacuumcleaner = settings.vacuumcleaner()
    checkvip = vip.checkuser(userid, checkvip)
    vacuumcleaner = vip.checkvacuumcleaner(userid, vacuumcleaner)
    violation = 0
    systemtime = datetime.datetime.today()
    timedelta = systemtime - datetime.timedelta(days=1)
    date_message = systemtime.strftime('%Y-%m-%d %H:%M:%S')
    delta_message = timedelta.strftime('%Y-%m-%d %H:%M:%S')
    return(chatid, userid, username, messageid, contenttype, text, caption, checkvip, vacuumcleaner, violation, date_message, delta_message, bot, sql, checkmessages)

@bot.message_handler(commands=['version'])
def start_message(message):
    chatid, userid, username, messageid, contenttype, text, caption, checkvip, vacuumcleaner, violation, date_message, delta_message, bot, sql, checkmessages = variables(message)
    log.logging.info (message)
    reaction.reactionversion(chatid, userid, username, messageid, contenttype, text, caption, checkvip, vacuumcleaner, violation, date_message, delta_message, bot, sql, checkmessages, version)
    
@bot.message_handler(commands=['statistics'])
def start_message(message):
    chatid, userid, username, messageid, contenttype, text, caption, checkvip, vacuumcleaner, violation, date_message, delta_message, bot, sql, checkmessages = variables(message)
    log.logging.info (message)
    countsticker, countanimation, countvoice, countvideonote, countext = statistics.statistics(chatid, userid, username, messageid, contenttype, text, caption, checkvip, vacuumcleaner, violation, date_message, delta_message, bot, sql, checkmessages)
    reaction.reactionstatistics(chatid, userid, username, messageid, contenttype, text, caption, checkvip, vacuumcleaner, violation, date_message, delta_message, bot, sql, checkmessages, countsticker, countanimation, countvoice, countvideonote, countext)

@bot.message_handler(content_types=['audio', 'photo', 'voice', 'video', 'document', 'text', 'location', 'contact', 'sticker', 'animation', 'video_note'])
def send_text(message):
    log.logging.info (message)
    chatid, userid, username, messageid, contenttype, text, caption, checkvip, vacuumcleaner, violation, date_message, delta_message, bot, sql, checkmessages = variables(message)
    sql.clearbase(delta_message)
    reaction.reaction(chatid, userid, username, messageid, contenttype, text, caption, checkvip, vacuumcleaner, violation, date_message, delta_message, bot, sql, checkmessages)
    
def runbot():
    sql.checkbase()
    bot.polling()