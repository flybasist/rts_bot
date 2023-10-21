import re

def checktext(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message, bot):
    if text == None:
        text = "empty"
    meowcheck = re.search(r'\bмяу\b', text.lower())
    amiga = re.search(r'\bамига\b', text.lower())

    if meowcheck != None:
        violation = 1

    if amiga != None:
        bot.send_sticker(chatid, 'CAACAgIAAxkBAANSY9ZRtd8zISOHv1Q1ji_mCaEzhhYAAgQAA7dBYg-r1QPjDQNzSC0E')
        
    return violation

def checkcaption(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message, bot):
    if caption == None:
        caption = "empty"
    meowcheck = re.search(r'\bмяу\b', caption.lower())
    amiga = re.search(r'\bамига\b', caption.lower())

    if meowcheck != None:
        violation = 1

    if amiga != None:
        bot.send_sticker(chatid, 'CAACAgIAAxkBAANSY9ZRtd8zISOHv1Q1ji_mCaEzhhYAAgQAA7dBYg-r1QPjDQNzSC0E')
        
    return violation