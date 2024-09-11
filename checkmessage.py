import re
import settings
import db
import telebot
import reaction

idbot = settings.id_bot()
bot = telebot.TeleBot(idbot)

def botcheck(variablesdict, text, violation):
    variablesdictbot = variablesdict.copy()
    variablesdictbot["userid"] = variablesdict["useridbot"]
    variablesdictbot["username"] = variablesdict["usernamebot"]
    variablesdictbot["text"] = text
    variablesdictbot["messageid"] = None
    variablesdictbot["violation"] = violation
    variablesdict["violation"] = violation
    variablesdictbot["checkvip"] = 99
    return variablesdictbot

def modesend(variablesdict, x):
    if x[1] == "sticker":
        bot.send_sticker(variablesdict["chatid"], x[3])
    elif x[1] == "text":
        bot.send_message(variablesdict["chatid"], x[3])

def sendreaction(variablesdict, x, delta="deltahour_message"):
    variablesdictbot = botcheck(variablesdict, x[3], x[4])
    count = db.basecounttext(variablesdictbot, delta)
    if count:
        pass
    else:
        modesend(variablesdict, x)
        db.basewritebot(variablesdictbot)
   
def regextext(variablesdict, x):
    regex = None
    if variablesdict["caption"] != None:
        regex = variablesdict["caption"]
    elif variablesdict["text"] != None:
        regex = variablesdict["text"]
    if regex and x[2] != "disable":
        regexcheck = re.search(x[2], regex.lower())
    else:
        regexcheck = None
    if regexcheck and x[4] != 21:
        sendreaction(variablesdict, x)
        variablesdict["violation"] = x[4]
    elif regexcheck and x[4] == 21:
        countlimit = db.basecounttext(variablesdict, delta="deltaday_message", violation=x[4])
        if countlimit >= variablesdict["limitviolation"] and variablesdict["limitviolation"] != 0 and variablesdict["checkvip"] != 100:
            reaction.deletemessage(variablesdict)
            variablesdict["violation"] = -1
        elif countlimit + 2 == variablesdict["limitviolation"]:
            countlimit = countlimit + 1
            answer = "@" + variablesdict["username"] + " Ты набрал " + str(countlimit) + " из " + str(variablesdict["limitviolation"]) + " текстовых нарушений"
            bot.send_message(variablesdict["chatid"], answer)
        else:
            modesend(variablesdict, x)
        variablesdict["violation"] = x[4]
    elif x[2] == "disable":
        sendreaction(variablesdict, x, delta="deltaday_message")
        variablesdict["violation"] = x[4]
    return variablesdict 