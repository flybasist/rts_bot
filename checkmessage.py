import re
import settings
import telebot

idbot = settings.id_bot()
bot = telebot.TeleBot(idbot)

def basecheck(chatid, check, violation):
    if check == None:
        check = "empty"
        
    meowcheck = re.search(r'\bмяу\b', check.lower())
    amiga = re.search(r'\bамига\b', check.lower())
    regidron = re.search(r'\bпохмелье\b', check.lower())

    if meowcheck != None:
        violation = 1

    if amiga != None:
        bot.send_sticker(chatid, 'CAACAgIAAxkBAANSY9ZRtd8zISOHv1Q1ji_mCaEzhhYAAgQAA7dBYg-r1QPjDQNzSC0E')
        
    if regidron !=None:
        bot.send_sticker(chatid, 'CAACAgIAAxkBAAIFQWYZxsE8tdgnQJheVs8fT8VyL9J6AAIIRAAC5efRSzB4d8SfqHljNAQ')
        
    return violation

def checktext(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner):
    violation = basecheck(chatid, text, violation)       
    return violation

def checkcaption(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner):
    violation = basecheck(chatid, caption, violation)       
    return violation