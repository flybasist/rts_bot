import re
import settings
import db
import telebot

idbot = settings.id_bot()
bot = telebot.TeleBot(idbot)

def botcheck(variablesdict, text, violation):
    variablesdict["userid"] = variablesdict["useridbot"]
    variablesdict["username"] = variablesdict["usernamebot"]
    variablesdict["text"] = text
    variablesdict["messageid"] = None
    variablesdict["violation"] = violation
    variablesdict["checkvip"] = 99
    return variablesdict

def basecheck(variablesdict, prefix):
    if prefix == "text":
        check = variablesdict["text"]
    elif prefix == "caption":
        check = variablesdict["caption"]

    if check == None:
        check = "empty"
        
    meowcheck = re.search(r'\b(?:[мmм]\s*([яyaɑа]|[aeiou])\s*([уuy]|[aeiou])|(?:meow|miau|мяу|мяў|мяв|miaw|mjaw|миау|μιου|مياو|먀우|ニャー))\b', check.lower())
    amiga = re.search(r'\bамига\b', check.lower())
    regidron = re.search(r'\bпохмелье\b', check.lower())

    if meowcheck != None:
        variablesdict["violation"] = 1
    else:
        variablesdict["violation"] = 0

    if amiga != None:
        variablesdictbot = botcheck(variablesdict, variablesdict["stickeramiga"], 51)
        count = db.basecounttext(variablesdictbot, delta="deltamin_message")
        if count:
            pass
        else:
            bot.send_sticker(variablesdict["chatid"], variablesdict["stickeramiga"])
            db.basewritebot(variablesdictbot)
            
    if regidron != None:
        variablesdictbot = botcheck(variablesdict, variablesdict["stickersregidron"], 52)
        count = db.basecounttext(variablesdictbot, delta="deltamin_message")
        if count:
            pass
        else:
            bot.send_sticker(variablesdict["chatid"], variablesdict["stickersregidron"])
            db.basewritebot(variablesdictbot)
        
    return variablesdict

def checktext(variablesdict):
    variablesdict = basecheck(variablesdict, prefix="text")      
    return variablesdict

def checkcaption(variablesdict):
    variablesdict = basecheck(variablesdict, prefix="caption")     
    return variablesdict