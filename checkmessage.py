import re
import settings
import telebot

idbot = settings.id_bot()
bot = telebot.TeleBot(idbot)

def checktext(chatid, userid, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner):
    if text == None:
        text = "empty"
    meowcheck = re.search(r'\bмяу\b', text.lower())
    amiga = re.search(r'\bамига\b', text.lower())
    regidron = re.search(r'\bпохмелье\b', text.lower())

    if meowcheck != None:
        violation = 1

    if amiga != None:
        bot.send_sticker(chatid, 'CAACAgIAAxkBAANSY9ZRtd8zISOHv1Q1ji_mCaEzhhYAAgQAA7dBYg-r1QPjDQNzSC0E')
        
    if regidron !=None:
        bot.send_sticker(chatid, 'CAACAgIAAxkBAAIFQWYZxsE8tdgnQJheVs8fT8VyL9J6AAIIRAAC5efRSzB4d8SfqHljNAQ')
        
    return violation

def checkcaption(chatid, userid, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner):
    if caption == None:
        caption = "empty"
    meowcheck = re.search(r'\bмяу\b', caption.lower())
    amiga = re.search(r'\bамига\b', caption.lower())
    regidron = re.search(r'\bпохмелье\b', caption.lower())

    if meowcheck != None:
        violation = 1

    if amiga != None:
        bot.send_sticker(chatid, 'CAACAgIAAxkBAANSY9ZRtd8zISOHv1Q1ji_mCaEzhhYAAgQAA7dBYg-r1QPjDQNzSC0E')
        
    if regidron !=None:
        bot.send_sticker(chatid, 'CAACAgIAAxkBAAIFQWYZxsE8tdgnQJheVs8fT8VyL9J6AAIIRAAC5efRSzB4d8SfqHljNAQ')
        
    return violation
