import sqlite3
import settings
import traceback
import checkmessage

def dbconnect():
    typedb = settings.typedb()
    
    if typedb == "sqlite":
        namebase = "rtsbot.db"
        sqlite_connection = sqlite3.connect(namebase)
        cursor = sqlite_connection.cursor()
            
        return cursor, sqlite_connection     
    elif typedb == "mysql":
        pass    
    elif typedb == "postgresql":
        pass

def limitdict(x, members=None):
    limitdict = {
        "limitaudio": x[0],
        "limitphoto": x[1],
        "limitvoice": x[2],
        "limitvideo": x[3],
        "limitdocument": x[4],
        "limittext": x[5],
        "limitlocation": x[6],
        "limitcontact": x[7],
        "limitsticker": x[8],
        "limitanimation": x[9],
        "limitvideo_note": x[10],
        "limitviolation": x[11],
        "checkvip": x[12]
    }
    if members:
        limitdict["members"] = members
    return limitdict

def startbase(botinfo, id_bot):
    table = "bot_settings"
    botinfoid = botinfo.id
    botinfousername = botinfo.username
    try:
        cursor, sqlite_connection = dbconnect()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        checktableusers = 1
        for x in cursor.fetchall():
            if x[0] == table:
                checktableusers = 0
        if checktableusers:
            cursor.execute (" CREATE TABLE '{}' ("
                    "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                    "id_bot TEXT,"
                    "userid_bot TEXT,"
                    "username_bot TEXT"
                    ");".format(table))
            cursor.execute("INSERT INTO bot_settings (id_bot, userid_bot, username_bot) VALUES (?, ?, ?);", (str(id_bot), botinfoid, botinfousername))
            cursor.connection.commit()
            cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
        traceback.print_exc()
    finally:
        if (sqlite_connection):
            sqlite_connection.close()

def readsettingsbot():
    cursor, sqlite_connection = dbconnect()
    cursor.execute("SELECT id_bot, userid_bot, username_bot FROM bot_settings WHERE id=1")
    for x in cursor.fetchall():
        id_bot = x[0]
        userid_bot = x[1]
        username_bot = x[2]
    sqlite_connection.close()
    return id_bot, userid_bot, username_bot

def checkchat(table):
    try:
        cursor, sqlite_connection = dbconnect()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        checktableusers = 1
        for x in cursor.fetchall():
            if x[0] == str(table):
                checktableusers = 0

        if checktableusers:
            cursor.execute (" CREATE TABLE '{}' ("
                    "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                    "chat_id TEXT,"
                    "user_id TEXT,"
                    "chatname TEXT,"
                    "chattitle TEXT,"
                    "username TEXT,"
                    "message_id TEXT,"
                    "contenttype TEXT,"
                    "text TEXT,"
                    "caption TEXT,"
                    "vip INTEGER DEFAULT (0),"
                    "violation INTEGER DEFAULT (0),"
                    "date_message TEXT"
                    ");".format(table))

            settingstable = str(table) + "_limits"
            cursor.execute (" CREATE TABLE '{}' ("
                    "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                    "user_id TEXT,"
                    "audio INTEGER DEFAULT (0),"
                    "photo INTEGER DEFAULT (0),"
                    "voice INTEGER DEFAULT (0),"
                    "video INTEGER DEFAULT (0),"
                    "document INTEGER DEFAULT (0),"
                    "text INTEGER DEFAULT (0),"
                    "location INTEGER DEFAULT (0),"
                    "contact INTEGER DEFAULT (0),"
                    "sticker INTEGER DEFAULT (0),"
                    "animation INTEGER DEFAULT (0),"
                    "video_note INTEGER DEFAULT (0),"
                    "violation INTEGER DEFAULT (0),"
                    "vip INTEGER DEFAULT (0)"
                    ");".format(settingstable))
            cursor.execute(f"INSERT INTO '{settingstable}' (user_id) VALUES (?);", ("allmembers",))
            settingstable = str(table) + "_reaction"
            cursor.execute (" CREATE TABLE '{}' ("
                    "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                    "user_id TEXT,"
                    "contenttype TEXT,"
                    "answertype TEXT,"
                    "regex TEXT,"
                    "answer TEXT,"
                    "violation INTEGER DEFAULT (0),"
                    "vip INTEGER DEFAULT (0)"
                    ");".format(settingstable))
            cursor.execute(f"INSERT INTO '{settingstable}' (user_id) VALUES (?);", ("allmembers",))
            cursor.connection.commit()
            cursor.close()
        else:
            cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
        traceback.print_exc()
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            
def clearbase(variablesdict):
    cursor, sqlite_connection = dbconnect()
    checkchat(variablesdict['chatid'])
    cursor.execute(f"DELETE FROM '{variablesdict['chatid']}' WHERE date_message < ? ;", (variablesdict["deltamonth_message"], ))
    cursor.connection.commit()
    sqlite_connection.close()    

def basewrite(variablesdict):
    cursor, sqlite_connection = dbconnect()
    checkchat(variablesdict['chatid'])
    cursor.execute(f"INSERT INTO '{variablesdict['chatid']}' (chat_id, user_id, chatname, chattitle, username, message_id, contenttype, text, caption, vip, violation, date_message) \
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", (variablesdict["chatid"], variablesdict["userid"], variablesdict["chatname"], variablesdict["chattitle"],
                                                                variablesdict["username"],
                                                                variablesdict["messageid"], variablesdict["contenttype"], variablesdict["text"], variablesdict["caption"], 
                                                                variablesdict["checkvip"],
                                                                variablesdict["violation"], variablesdict["date_message"]))
    cursor.connection.commit()
    sqlite_connection.close()
    
def basewritebot(variablesdict):
    cursor, sqlite_connection = dbconnect()
    checkchat(variablesdict['chatid'])
    cursor.execute(f"INSERT INTO '{variablesdict['chatid']}' (chat_id, user_id, chatname, chattitle, username, message_id, contenttype, text, caption, vip, violation, date_message) \
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", (variablesdict["chatid"], variablesdict["userid"], variablesdict["chatname"], variablesdict["chattitle"],
                                                                variablesdict["username"],
                                                                variablesdict["messageid"], variablesdict["contenttype"], variablesdict["text"], variablesdict["caption"], 
                                                                variablesdict["checkvip"],
                                                                variablesdict["violation"], variablesdict["date_message"]))
    cursor.connection.commit()
    sqlite_connection.close()

def checkuserlimit(variablesdict):
    settingstable = str(variablesdict['chatid']) + "_limits"
    try:
        cursor, sqlite_connection = dbconnect()
        cursor.execute(f"SELECT audio, photo, voice, video, document, text, location, contact, sticker, animation, video_note, violation, vip \
                        FROM '{settingstable}' WHERE user_id=?;", (variablesdict["userid"],))
        checktableusers = 1
        for x in cursor.fetchall():
            if x:
                userlimit = limitdict(x, variablesdict["userid"])
                checktableusers = 0
        if checktableusers:
            cursor.execute(f"SELECT audio, photo, voice, video, document, text, location, contact, sticker, animation, video_note, violation, vip \
                       FROM '{settingstable}' WHERE user_id='allmembers';")
            for x in cursor.fetchall():
                if x:
                    userlimit = limitdict(x, "allmembers")
                    checktableusers = 0 
        cursor.connection.commit()
        cursor.close()
        return userlimit    
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
        traceback.print_exc()
    finally:
        if (sqlite_connection):
            sqlite_connection.close()

def checkuserreaction(variablesdict):
    settingstable = str(variablesdict['chatid']) + "_reaction"
    try:
        cursor, sqlite_connection = dbconnect()
        cursor.execute(f"SELECT contenttype, answertype, regex, answer, violation, vip \
                        FROM '{settingstable}' WHERE user_id=? AND contenttype=?;", (variablesdict["userid"], variablesdict["contenttype"]))
        checktableusers = 1
        for x in cursor.fetchall():
            if x:
                variablesdict = checkmessage.regextext(variablesdict, x)
                checktableusers = 0
        if checktableusers:
            cursor.execute(f"SELECT contenttype, answertype, regex, answer, violation, vip \
                       FROM '{settingstable}' WHERE user_id='allmembers' AND contenttype=?;", (variablesdict["contenttype"],))
            for x in cursor.fetchall():
                if x:
                    variablesdict = checkmessage.regextext(variablesdict, x)
                    checktableusers = 0 
        cursor.connection.commit()
        cursor.close()
        return variablesdict
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
        traceback.print_exc()
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
    

def basecount(variablesdict):
    cursor, sqlite_connection = dbconnect()
    checkchat(variablesdict['chatid'])
    cursor.execute(f"SELECT COUNT(*) FROM '{variablesdict['chatid']}' WHERE user_id=? AND chat_id=? AND contenttype=? AND date_message > ? ;", (variablesdict["userid"], variablesdict["chatid"],
                                                                                                                      variablesdict["contenttype"], 
                                                                                                                      variablesdict["deltaday_message"]))
    count = cursor.fetchall()
    count = count[0][0]
    sqlite_connection.close()
    return count

def basecounttext(variablesdict, delta="deltaday_message", violation=None):
    if violation:
        variablesdict["violation"] = violation
    cursor, sqlite_connection = dbconnect()
    checkchat(variablesdict['chatid'])
    cursor.execute(f"SELECT COUNT(*) FROM '{variablesdict['chatid']}' WHERE user_id=? AND chat_id=? AND violation=? AND date_message > ? ;", (variablesdict["userid"], variablesdict["chatid"],
                                                                                                                      variablesdict["violation"], variablesdict[delta]))
    countext = cursor.fetchall()
    countext = countext[0][0]
    sqlite_connection.close()
    return countext