def statistics(chatid, userid, username, messageid, contenttype, text, caption, checkvip, vacuumcleaner, violation, date_message, delta_message, bot, sql, checkmessages):
    contenttype = ("sticker")
    countsticker = sql.basecount(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message, delta_message)
    contenttype = ("animation")
    countanimation = sql.basecount(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message, delta_message)
    contenttype = ("voice")
    countvoice = sql.basecount(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message, delta_message)
    contenttype = ("video_note")
    countvideonote = sql.basecount(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message, delta_message)
    contenttype = ("text")
    violation = 1
    countext = sql.basecounttext(chatid, userid, username, messageid, contenttype, text, caption, checkvip, violation, date_message, delta_message)
    return (countsticker, countanimation, countvoice, countvideonote, countext)