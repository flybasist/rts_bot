import time
import settings
import telebot
import db
import checkmessage

idbot = settings.id_bot()
bot = telebot.TeleBot(idbot)

def reaction(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner):
    if checkvip == 100 and contenttype == 'text':
        violation = checkmessage.checktext(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip,
                                           vacuumcleaner)
        db.basewrite(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)

    elif checkvip == 100 and contenttype == 'photo':
        violation = checkmessage.checkcaption(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message,
                                              checkvip, vacuumcleaner)
        db.basewrite(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)
        
    elif checkvip == 100:
        db.basewrite(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)

    elif checkvip <= 99 and contenttype == 'text':
        violation = checkmessage.checktext(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip,
                                           vacuumcleaner)
        db.basewrite(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)
        # if violation == 2:
        #     try:
        #         bot.delete_message(chatid, messageid, None)
        #     except:
        #         answer = "Возникли проблемы с удалением"
        #         bot.send_message(chatid, answer)
        if violation == 1:
            count = db.basecounttext(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip,
                                     vacuumcleaner)
            if count <= 3:
                answer = "Гав!"
                bot.send_message(chatid, answer)
            elif count == 4:
                answer = "@" + username + " Следующий мяу последний, а после я начинаю их есть. Сутки"
                bot.send_message(chatid, answer)
            elif count == 5:
                db.basewrite(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)
                db.basewrite(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)
                db.basewrite(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)
                db.basewrite(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)
                db.basewrite(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)
                answer = "Щелк зубами"
                bot.send_message(chatid, answer)
            elif count >= 6:
                try:
                    bot.delete_message(chatid, messageid, None)
                except:
                    answer = "Возникли проблемы с удалением"
                    bot.send_message(chatid, answer)                
        else:
            pass

    elif checkvip <= 99 and contenttype == 'photo':
        violation = checkmessage.checkcaption(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message,
                                              checkvip, vacuumcleaner)
        if vacuumcleaner == 1:
            checkvip = vacuumcleaner
            db.basewrite(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)
            count = db.basecountvacuumcleaner(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message,
                                              checkvip, vacuumcleaner)
            if count == 1:
                answer = "@" + username + " , опять ты что то спылесосил"
                bot.send_message(chatid, answer)
            else:
                pass
        else:
            db.basewrite(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)
        if violation == 1:
            count = db.basecounttext(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip,
                                     vacuumcleaner)
            if count <= 3:
                answer = "Гав!"
                bot.send_message(chatid, answer)
            elif count == 4:
                answer = "@" + username + " Следующий мяу последний, а после я начинаю их есть. Сутки"
                bot.send_message(chatid, answer)
            elif count == 5:
                db.basewrite(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)
                db.basewrite(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)
                db.basewrite(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)
                db.basewrite(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)
                db.basewrite(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)
                answer = "Щелк зубами"
                bot.send_message(chatid, answer)
            elif count >= 6:
                try:
                    bot.delete_message(chatid, messageid, None)
                except:
                    answer = "Возникли проблемы с удалением"
                    bot.send_message(chatid, answer)   
        else:
            pass

    elif checkvip <= 99 and contenttype == 'sticker':
        db.basewrite(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)
        count = db.basecount(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)
        if count == 4:
            answer = "@" + username + \
                " В этом чате приветствуется классное, интересное, живое общение, а не стикершторм." + \
                    " За сутки от тебя прилетело уже четыре стикера. Давай пятый будет финальный, а дальше сутки придется страдать без них." + \
                    " Ну или юзай гифки если их лимит не исчерпан. А лучше фотки своих железок кидай(кота оставь в покое!), или трави кулстори!"
            bot.send_message(chatid, answer)
        elif count == 5:
            db.basewrite(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)
            db.basewrite(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)
            db.basewrite(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)
            db.basewrite(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)
            db.basewrite(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)
        elif count >= 6:
            try:
                bot.delete_message(chatid, messageid, None)
            except:
                answer = "Возникли проблемы с удалением"
                bot.send_message(chatid, answer)

    elif checkvip <= 99 and contenttype == 'animation':
        db.basewrite(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)
        count = db.basecount(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)
        if count == 4:
            answer = "@" + username + \
                " В этом чате приветствуется классное, интересное, живое общение, а не гифшторм." + \
                    " За сутки от тебя прилетело уже четыре гифки. Давай пятая будет финальная, а дальше сутки придется страдать без них" + \
                    " Ну или юзай стикеры если их лимит не исчерпан. А лучше фотки своих железок кидай(кота оставь в покое!), или трави кулстори!"
            bot.send_message(chatid, answer)
        elif count == 5:
            db.basewrite(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)
            db.basewrite(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)
            db.basewrite(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)
            db.basewrite(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)
            db.basewrite(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)
        elif count >= 6:
            try:
                bot.delete_message(chatid, messageid, None)
            except:
                answer = "Возникли проблемы с удалением"
                bot.send_message(chatid, answer)

    elif checkvip <= 99 and contenttype == 'voice':
        db.basewrite(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)
        answer = "Всем привет, я вижу что тут @" + username + " кинул ГС, здесь это запрещено, тут надо об играх писать"
        bot.send_message(chatid, answer)
        time.sleep(5)
        try:
            bot.delete_message(chatid, messageid, None)
            answer = "Никаких ГС в мою смену"
            bot.send_message(chatid, answer)
        except:
            answer = "Видимо у меня нет прав на удаление"
            bot.send_message(chatid, answer)

    elif checkvip <= 99 and contenttype == 'video_note':
        db.basewrite(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)
        answer = "Всем привет, я вижу что тут @" + username + " кинул кружочек, здесь это запрещено, тут надо об играх писать"
        bot.send_message(chatid, answer)
        time.sleep(5)
        try:
            bot.delete_message(chatid, messageid, None)
            answer = "Никаких кружочков в мою смену"
            bot.send_message(chatid, answer)
        except:
            answer = "Видимо у меня нет прав на удаление"
            bot.send_message(chatid, answer)
    else:
        # print (checkvip, "I kill you")
        # answer = "I kill you!"
        # bot.send_message(chatid, answer)
        pass
    
def reactionstatistics(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner,
                       countsticker, countanimation, countvoice, countvideonote, countext):
    db.basewrite(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)
    answer = "Дорогой @" + username + " за сутки ты накопил - " + str(countsticker) + " стикеров, " + str(countanimation) + " GIFок, " + str(countvoice) + \
    " скинутых (и скорее всего уничтоженных мною!) голосовух, " + str(countvideonote) + " скинутых (и опять же скорее всего уничтоженных мною) кружочков. А так же " \
        + str(countext) + " текстовых нарушений."
        # + "\nВо избежании флуд шторма, индивидуальная статистика доступна не более одного раза в час"
    bot.send_message(chatid, answer)

def reactionversion(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner, version):
    db.basewrite(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)
    answer = "Текущая версия - " + version + "\nПо всем вопросам писать автору бота - @FlyBasist"
    # + "\nВо избежании флуд шторма, вызов номера версии доступно не более раза в час"
    bot.send_message(chatid, answer)