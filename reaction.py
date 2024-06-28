import time
import settings
import telebot
import db
import checkmessage

idbot = settings.id_bot()
bot = telebot.TeleBot(idbot)

def wordcheck(variablesdict):
    if variablesdict["violation"] == 1:
        variablesdict["violation"] = 2
        count = db.basecounttext(variablesdict)
        if count:
            try:
                bot.delete_message(variablesdict["chatid"], variablesdict["messageid"], None)
                variablesdict["violation"] = 3
            except:
                answer = "Возникли проблемы с удалением"
                bot.send_message(variablesdict["chatid"], answer)
        else:
            variablesdict["violation"] = 1
            count = db.basecounttext(variablesdict)
            if count <= 3:
                answer = "@" + variablesdict["username"] + " Гав!"
                bot.send_message(variablesdict["chatid"], answer)
            elif count == 4:
                answer = "@" + variablesdict["username"] + " Следующий мяу последний, а после я начинаю их есть. Сутки"
                bot.send_message(variablesdict["chatid"], answer)
            elif count == 5:
                variablesdict["violation"] = 2
                answer = "@" + variablesdict["username"] + " Щелк зубами"
                bot.send_message(variablesdict["chatid"], answer)                
    elif variablesdict["violation"] == 4:
        variablesdict["violation"] = 5
        count = db.basecounttext(variablesdict)
        if count:
            try:
                bot.delete_message(variablesdict["chatid"], variablesdict["messageid"], None)
                variablesdict["violation"] = 6
            except:
                answer = "Возникли проблемы с удалением"
                bot.send_message(variablesdict["chatid"], answer)
        else:
            variablesdict["violation"] = 4
            count = db.basecounttext(variablesdict)
            if count <= 1:
                variablesdict["violation"] = 5
                answer = "@" + variablesdict["username"] + " Извини, но это моя фишка"
                bot.send_message(variablesdict["chatid"], answer)    
    else:
        pass
    return variablesdict

def vacuumcleanermessage(variablesdict):
    if variablesdict["vacuumcleaner"] == 1:
        variablesdict["checkvip"] = variablesdict["vacuumcleaner"]
        count = db.basecountvacuumcleaner(variablesdict)
        if count == 1:
            answer = "@" + variablesdict["username"] + " , опять ты что то спылесосил"
            bot.send_message(variablesdict["chatid"], answer)

def reaction(variablesdict):
    if variablesdict["checkvip"] == 100 and variablesdict["contenttype"] == 'text':
        variablesdict = checkmessage.checktext(variablesdict)
        db.basewrite(variablesdict)

    elif variablesdict["checkvip"]== 100 and variablesdict["contenttype"] == 'photo':
        variablesdict = checkmessage.checkcaption(variablesdict)
        db.basewrite(variablesdict)
        
    elif variablesdict["checkvip"]== 100:
        db.basewrite(variablesdict)

    elif variablesdict["checkvip"]<= 99 and variablesdict["contenttype"] == 'text':
        variablesdict = checkmessage.checktext(variablesdict)
        variablesdict = wordcheck(variablesdict)
        db.basewrite(variablesdict)

    elif variablesdict["checkvip"]<= 99 and variablesdict["contenttype"] == 'photo':
        vacuumcleanermessage(variablesdict)
        variablesdict = checkmessage.checkcaption(variablesdict)
        variablesdict = wordcheck(variablesdict)
        db.basewrite(variablesdict)

    elif variablesdict["checkvip"]<= 99 and variablesdict["contenttype"] == 'sticker':
        variablesdict["violation"] = 31
        count = db.basecounttext(variablesdict)
        if count:
            try:
                bot.delete_message(variablesdict["chatid"], variablesdict["messageid"], None)
            except:
                answer = "Возникли проблемы с удалением"
                bot.send_message(variablesdict["chatid"], answer)
        else:
            variablesdict["violation"] = 0
            count = db.basecount(variablesdict)
            if count == 3:
                answer = "@" + variablesdict["username"] + \
                " В этом чате приветствуется классное, интересное, живое общение, а не стикершторм." + \
                    " За сутки от тебя прилетело уже четыре стикера. Давай пятый будет финальный, а дальше сутки придется страдать без них." + \
                    " Ну или юзай гифки если их лимит не исчерпан. А лучше фотки своих железок кидай(кота оставь в покое!), или трави кулстори!"
                bot.send_message(variablesdict["chatid"], answer)
            elif count == 4:
                variablesdict["violation"] = 31
        db.basewrite(variablesdict)

    elif variablesdict["checkvip"]<= 99 and variablesdict["contenttype"]== 'animation':
        variablesdict["violation"] = 41
        count = db.basecounttext(variablesdict)
        if count:
            try:
                bot.delete_message(variablesdict["chatid"], variablesdict["messageid"], None)
            except:
                answer = "Возникли проблемы с удалением"
                bot.send_message(variablesdict["chatid"], answer)
        else:
            variablesdict["violation"] = 0
            count = db.basecount(variablesdict)
            if count == 3:
                answer = "@" + variablesdict["username"] + \
                " В этом чате приветствуется классное, интересное, живое общение, а не гифшторм." + \
                    " За сутки от тебя прилетело уже четыре гифки. Давай пятая будет финальная, а дальше сутки придется страдать без них" + \
                    " Ну или юзай стикеры если их лимит не исчерпан. А лучше фотки своих железок кидай(кота оставь в покое!), или трави кулстори!"
                bot.send_message(variablesdict["chatid"], answer)
            elif count == 4:
                variablesdict["violation"] = 41
        db.basewrite(variablesdict)

    elif variablesdict["checkvip"]<= 99 and variablesdict["contenttype"]== 'voice':
        db.basewrite(variablesdict)
        answer = "Всем привет, я вижу что тут @" + variablesdict["username"] + " кинул ГС, здесь это запрещено, тут надо об играх писать"
        bot.send_message(variablesdict["chatid"], answer)
        time.sleep(5)
        try:
            bot.delete_message(variablesdict["chatid"], variablesdict["messageid"], None)
            answer = "Никаких ГС в мою смену"
            bot.send_message(variablesdict["chatid"], answer)
        except:
            answer = "Видимо у меня нет прав на удаление"
            bot.send_message(variablesdict["chatid"], answer)

    elif variablesdict["checkvip"]<= 99 and variablesdict["contenttype"]== 'video_note':
        db.basewrite(variablesdict)
        answer = "Всем привет, я вижу что тут @" + variablesdict["username"] + " кинул кружочек, здесь это запрещено, тут надо об играх писать"
        bot.send_message(variablesdict["chatid"], answer)
        time.sleep(5)
        try:
            bot.delete_message(variablesdict["chatid"], variablesdict["messageid"], None)
            answer = "Никаких кружочков в мою смену"
            bot.send_message(variablesdict["chatid"], answer)
        except:
            answer = "Видимо у меня нет прав на удаление"
            bot.send_message(variablesdict["chatid"], answer)
    else:
        pass
    
def reactionversion(variablesdict):
    variablesdict["violation"] = 11 
    count = db.basecounttext(variablesdict, delta="deltahour_message")
    db.basewrite(variablesdict)
    if count and variablesdict["checkvip"] != 100:
        pass
    else:
        answer = "Текущая версия - " + variablesdict["version"] + "\nПо всем вопросам писать автору бота - @FlyBasist" + \
        "\nВо избежании флуд шторма, вызов номера версии доступно один раз в час. Индивидуальная реакция стикером не чаще одного раза в десять минут"
        bot.send_message(variablesdict["chatid"], answer)

def reactionstatistics(variablesdict):
    variablesdict["violation"] = 21 
    count = db.basecounttext(variablesdict, delta="deltahour_message")
    db.basewrite(variablesdict)
    if count and variablesdict["checkvip"] != 100:
        pass
    else:
        answer = "@" + variablesdict["username"] + " за сутки ты накопил - " + str(variablesdict["countsticker"]) + " стикеров, " + str(variablesdict["countanimation"]) + \
        " GIFок, " + str(variablesdict["countvoice"]) + " скинутых (и скорее всего уничтоженных мною!) голосовух, " + str(variablesdict["countvideonote"]) + \
            " скинутых (и опять же скорее всего уничтоженных мною) кружочков. А так же " + str(variablesdict["countext"]) + " текстовых нарушений." + \
            "\nВо избежании флуд шторма, индивидуальная статистика доступна один раз в час"
        bot.send_message(variablesdict["chatid"], answer)