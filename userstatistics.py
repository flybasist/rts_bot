import reaction
import db

def statistics(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner):

    contenttype = ("sticker")
    countsticker = db.basecount(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)
    contenttype = ("animation")
    countanimation = db.basecount(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)
    contenttype = ("voice")
    countvoice = db.basecount(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)
    contenttype = ("video_note")
    countvideonote = db.basecount(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)
    contenttype = ("text")
    countext = db.basecounttext(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner)

    reaction.reactionstatistics(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner,
                                countsticker, countanimation, countvoice, countvideonote, countext)