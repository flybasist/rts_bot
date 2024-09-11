import settings
import telebot
import db

idbot = settings.id_bot()
bot = telebot.TeleBot(idbot)

def deletemessage(variablesdict):
    try:
        bot.delete_message(variablesdict["chatid"], variablesdict["messageid"], None)
    except:
        answer = "Возникли проблемы с удалением"
        bot.send_message(variablesdict["chatid"], answer)
    
def newchat(variablesdict):
    answer = "Всем привет! Я ваш новый бот! Пока все индивидуальные настройки под чат задаются через @FlyBasist но потом меня можно будет настраивать владельцу чата самостоятельно"
    bot.send_message(variablesdict["chatid"], answer)

def newmember(variablesdict):
    answer = "Привет, @" + variablesdict["username"] + " ! Добро пожаловать в наш чат! Капча для новых пользователей в разработке, поэтому если ты спамер то удались сам пожалуйста"
    bot.send_message(variablesdict["chatid"], answer)

def newmessage(variablesdict):
    if variablesdict["checkvip"] != 100:
        limit = "limit" + str(variablesdict["contenttype"])
        checklimit = variablesdict[limit]
        if checklimit == -1:
            deletemessage(variablesdict)
            variablesdict["violation"] = -1
            answer = "@" + variablesdict["username"] + " В этом чате запрещен " + variablesdict["contenttype"] + " для " + variablesdict["members"]
            bot.send_message(variablesdict["chatid"], answer)
        elif checklimit >= 1:
            countlimit = db.basecount(variablesdict)
            if countlimit >= checklimit:
                deletemessage(variablesdict)
                variablesdict["violation"] = -1
            elif countlimit + 2 == checklimit:
                countlimit = countlimit + 1
                answer = "@" + variablesdict["username"] + " Ты набрал " + str(countlimit) + " из " + str(checklimit) + " " + variablesdict["contenttype"]
                bot.send_message(variablesdict["chatid"], answer)
        if variablesdict["violation"] != -1:
            variablesdict = db.checkuserreaction(variablesdict)
        db.basewrite(variablesdict)      
    else:
        variablesdict = db.checkuserreaction(variablesdict)
        db.basewrite(variablesdict)
    
def reactionversion(variablesdict):
    variablesdict["violation"] = 1 
    count = db.basecounttext(variablesdict, delta="deltahour_message")
    db.basewrite(variablesdict)
    if count and variablesdict["checkvip"] != 100:
        pass
    else:
        answer = "Текущая версия - " + variablesdict["version"] + "\nПо всем вопросам писать автору бота - @FlyBasist" + \
        "\nВо избежании флуд шторма, вызов номера версии доступно один раз в час" + \
        "\nИндивидуальная реакция стикером не чаще одного раза в десять минут" + \
        "\nРазработка бота требует ресурсов, поддержи разработку донатом!"
        bot.send_message(variablesdict["chatid"], answer)

def reactionstatistics(variablesdict):
    variablesdict["violation"] = 2
    count = db.basecounttext(variablesdict, delta="deltahour_message")
    db.basewrite(variablesdict)
    if count and variablesdict["checkvip"] != 100:
        pass
    else:
        answer = "@" + variablesdict["username"] + " статистика за сутки\n" + \
        str(variablesdict["countphoto"]) + " фото из " + str(variablesdict["limitphoto"]) + "\n" + \
        str(variablesdict["countaudio"]) + " аудио из " + str(variablesdict["limitaudio"]) + "\n" + \
        str(variablesdict["countvideo"]) + " видео из " + str(variablesdict["limitvideo"]) + "\n" + \
        str(variablesdict["countsticker"]) + " стикеров из " + str(variablesdict["limitsticker"]) + "\n" + \
        str(variablesdict["countanimation"]) + " GIFок, из " + str(variablesdict["limitanimation"]) + "\n" + \
        str(variablesdict["countvoice"]) + " голосовых сообщений из " + str(variablesdict["limitvoice"]) + "\n" + \
        str(variablesdict["countvideonote"]) + " кружочков из " + str(variablesdict["limitvideo_note"]) + "\n" + \
        str(variablesdict["countdocument"]) + " документов из " + str(variablesdict["limitdocument"]) + "\n" + \
        str(variablesdict["countlocation"]) + " локаций из " + str(variablesdict["limitlocation"]) + "\n" + \
        str(variablesdict["countcontact"]) + " контактов из " + str(variablesdict["limitcontact"]) + "\n" + \
        str(variablesdict["countext"]) + " текстовых нарушений из " + str(variablesdict["limitviolation"]) + "\n" + \
            "Где -1 запрещено полностью, 0 разрешено" + "\n" + \
            "Во избежании флуд шторма, индивидуальная статистика доступна один раз в час"
        bot.send_message(variablesdict["chatid"], answer)