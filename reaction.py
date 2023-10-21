import time

def reaction(chatid, userid, username, messageid, contenttype, text, caption, checkvip, vacuumcleaner, violation, date_message, delta_message, bot, sql, checkmessages):
    if checkvip == 100 and contenttype == 'text':
        violation = checkmessages.checktext(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message, bot)
        sql.basewrite(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message)

    elif checkvip == 100 and contenttype == 'photo':
        violation = checkmessages.checkcaption(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message, bot)
        sql.basewrite(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message)
        
    elif checkvip == 100:
        sql.basewrite(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message)

    elif checkvip <= 99 and contenttype == 'text':
        violation = checkmessages.checktext(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message, bot)
        sql.basewrite(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message)
        if violation == 1:
            count = sql.basecounttext(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message, delta_message)
            if count <= 3:
                answer = "Гав!"
                bot.send_message(chatid, answer)
            elif count == 4:
                answer = "@" + username + " Следующий мяу последний, а после я начинаю их есть. Сутки"
                bot.send_message(chatid, answer)
            elif count == 5:
                sql.basewrite(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message)
                sql.basewrite(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message)
                sql.basewrite(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message)
                sql.basewrite(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message)
                sql.basewrite(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message)
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
        if vacuumcleaner == 1:
            checkvip = vacuumcleaner
            violation = checkmessages.checkcaption(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message, bot)
            sql.basewrite(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message)
            count = sql.basecountvacuumcleaner(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message, delta_message)
            if count == 1:
                answer = "@" + username + " , опять ты что то спылесосил"
                bot.send_message(chatid, answer)
            else:
                pass
        if violation == 1:
            count = sql.basecounttext(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message, delta_message)
            if count <= 3:
                answer = "Гав!"
                bot.send_message(chatid, answer)
            elif count == 4:
                answer = "@" + username + " Следующий мяу последний, а после я начинаю их есть. Сутки"
                bot.send_message(chatid, answer)
            elif count == 5:
                sql.basewrite(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message)
                sql.basewrite(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message)
                sql.basewrite(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message)
                sql.basewrite(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message)
                sql.basewrite(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message)
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
        sql.basewrite(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message)
        count = sql.basecount(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message, delta_message)
        if count == 4:
            answer = "@" + username + \
                " В этом чате приветствуется классное, интересное, живое общение, а не стикершторм." + \
                    " За сутки от тебя прилетело уже четыре стикера. Давай пятый будет финальный, а дальше сутки придется страдать без них." + \
                    " Ну или юзай гифки если их лимит не исчерпан. А лучше фотки своих железок кидай(кота оставь в покое!), или трави кулстори!"
            bot.send_message(chatid, answer)
        elif count == 5:
            sql.basewrite(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message)
            sql.basewrite(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message)
            sql.basewrite(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message)
            sql.basewrite(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message)
            sql.basewrite(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message)
        elif count >= 6:
            try:
                bot.delete_message(chatid, messageid, None)
            except:
                answer = "Возникли проблемы с удалением"
                bot.send_message(chatid, answer)

    elif checkvip <= 99 and contenttype == 'animation':
        sql.basewrite(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message)
        count = sql.basecount(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message, delta_message)
        if count == 4:
            answer = "@" + username + \
                " В этом чате приветствуется классное, интересное, живое общение, а не гифшторм." + \
                    " За сутки от тебя прилетело уже четыре гифки. Давай пятая будет финальная, а дальше сутки придется страдать без них" + \
                    " Ну или юзай стикеры если их лимит не исчерпан. А лучше фотки своих железок кидай(кота оставь в покое!), или трави кулстори!"
            bot.send_message(chatid, answer)
        elif count == 5:
            sql.basewrite(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message)
            sql.basewrite(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message)
            sql.basewrite(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message)
            sql.basewrite(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message)
            sql.basewrite(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message)
        elif count >= 6:
            try:
                bot.delete_message(chatid, messageid, None)
            except:
                answer = "Возникли проблемы с удалением"
                bot.send_message(chatid, answer)

    elif checkvip <= 99 and contenttype == 'voice':
        sql.basewrite(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message)
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
        sql.basewrite(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message)
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