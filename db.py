import sqlite3
import settings

namebase = settings.namebase()

def checkbase():
    try:
        sqlite_connection = sqlite3.connect(namebase)
        cursor = sqlite_connection.cursor()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        checktableusers = 0
        for x in cursor.fetchall():
            if x[0] == "tg":
                checktableusers = 1

        if checktableusers == 0:
            nametable = "tg"
            cursor.execute (" CREATE TABLE {} ("
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
                    ");".format(nametable))

            cursor.close()
        else:
            cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            
def clearbase(delta_message):
    sqlite_connection = sqlite3.connect(namebase)
    cursor = sqlite_connection.cursor()
    cursor.execute("DELETE FROM tg WHERE date_message < ? ;", (delta_message, ))
    cursor.connection.commit()
    sqlite_connection.close()    

def basewrite(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner):
    sqlite_connection = sqlite3.connect(namebase)
    cursor = sqlite_connection.cursor()
    cursor.execute("INSERT INTO tg (chat_id, user_id, chatname, chattitle, username, message_id, contenttype, text, caption, vip, violation, date_message) \
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", (chatid, userid, chatname, chattitle, username, messageid,
                                                                   contenttype, text, caption, checkvip, violation, date_message))
    cursor.connection.commit()
    sqlite_connection.close()

def basecount(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner):
    sqlite_connection = sqlite3.connect(namebase)
    cursor = sqlite_connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM tg WHERE user_id=? AND chat_id=? AND contenttype=? AND date_message > ? ;", (userid, chatid, contenttype, delta_message))
    count = cursor.fetchall()
    count = count[0][0]
    sqlite_connection.close()
    return count

def basecounttext(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner):
    violation = 1
    sqlite_connection = sqlite3.connect(namebase)
    cursor = sqlite_connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM tg WHERE user_id=? AND chat_id=? AND violation=? AND date_message > ? ;", (userid, chatid, violation, delta_message))
    countext = cursor.fetchall()
    countext = countext[0][0]
    sqlite_connection.close()
    return countext

def basecountvacuumcleaner(chatid, userid, chatname, chattitle, username, messageid, contenttype, text, caption, violation, date_message, delta_message, checkvip, vacuumcleaner):
    sqlite_connection = sqlite3.connect(namebase)
    cursor = sqlite_connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM tg WHERE user_id=? AND chat_id=? AND vip=? AND contenttype=? AND date_message > ? ;", (userid, chatid, vacuumcleaner, contenttype,
                                                                                                                                delta_message))
    countvacuumcleaner = cursor.fetchall()
    countvacuumcleaner = countvacuumcleaner[0][0]
    sqlite_connection.close()
    return countvacuumcleaner
