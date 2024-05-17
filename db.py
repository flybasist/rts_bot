import sqlite3
import settings

def checkbase():
    namebase = settings.namebase()
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
            
def clearbase(variablesdict):
    sqlite_connection = sqlite3.connect(variablesdict["namebase"])
    cursor = sqlite_connection.cursor()
    cursor.execute("DELETE FROM tg WHERE date_message < ? ;", (variablesdict["deltaday_message"], ))
    cursor.connection.commit()
    sqlite_connection.close()    

def basewrite(variablesdict):
    sqlite_connection = sqlite3.connect(variablesdict["namebase"])
    cursor = sqlite_connection.cursor()
    cursor.execute("INSERT INTO tg (chat_id, user_id, chatname, chattitle, username, message_id, contenttype, text, caption, vip, violation, date_message) \
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", (variablesdict["chatid"], variablesdict["userid"], variablesdict["chatname"], variablesdict["chattitle"],
                                                                variablesdict["username"],
                                                                variablesdict["messageid"], variablesdict["contenttype"], variablesdict["text"], variablesdict["caption"], 
                                                                variablesdict["checkvip"],
                                                                variablesdict["violation"], variablesdict["date_message"]))
    cursor.connection.commit()
    sqlite_connection.close()
    
def basewritebot(variablesdict):
    sqlite_connection = sqlite3.connect(variablesdict["namebase"])
    cursor = sqlite_connection.cursor()
    cursor.execute("INSERT INTO tg (chat_id, user_id, chatname, chattitle, username, message_id, contenttype, text, caption, vip, violation, date_message) \
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", (variablesdict["chatid"], variablesdict["userid"], variablesdict["chatname"], variablesdict["chattitle"],
                                                                variablesdict["username"],
                                                                variablesdict["messageid"], variablesdict["contenttype"], variablesdict["text"], variablesdict["caption"], 
                                                                variablesdict["checkvip"],
                                                                variablesdict["violation"], variablesdict["date_message"]))
    cursor.connection.commit()
    sqlite_connection.close()

def basecount(variablesdict):
    sqlite_connection = sqlite3.connect(variablesdict["namebase"])
    cursor = sqlite_connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM tg WHERE user_id=? AND chat_id=? AND contenttype=? AND date_message > ? ;", (variablesdict["userid"], variablesdict["chatid"],
                                                                                                                      variablesdict["contenttype"], 
                                                                                                                      variablesdict["deltaday_message"]))
    count = cursor.fetchall()
    count = count[0][0]
    sqlite_connection.close()
    return count

def basecounttext(variablesdict, delta="deltaday_message"):
    sqlite_connection = sqlite3.connect(variablesdict["namebase"])
    cursor = sqlite_connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM tg WHERE user_id=? AND chat_id=? AND violation=? AND date_message > ? ;", (variablesdict["userid"], variablesdict["chatid"],
                                                                                                                      variablesdict["violation"], variablesdict[delta]))
    countext = cursor.fetchall()
    countext = countext[0][0]
    sqlite_connection.close()
    return countext

def basecountvacuumcleaner(variablesdict, delta="deltaday_message"):
    sqlite_connection = sqlite3.connect(variablesdict["namebase"])
    cursor = sqlite_connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM tg WHERE user_id=? AND chat_id=? AND vip=? AND contenttype=? AND date_message > ? ;", (variablesdict["userid"], variablesdict["chatid"],
                                                                                                                                variablesdict["vacuumcleaner"], 
                                                                                                                                variablesdict["contenttype"], variablesdict[delta]))
    countvacuumcleaner = cursor.fetchall()
    countvacuumcleaner = countvacuumcleaner[0][0]
    sqlite_connection.close()
    return countvacuumcleaner
