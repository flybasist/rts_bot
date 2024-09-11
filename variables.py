import db
import datetime

def variables(message):
    id_bot, userid_bot, username_bot = db.readsettingsbot()
    variablesdict = {
        "version": "0.5",
        "contenttype": message.content_type,
        "chatid": message.chat.id,
        "userid": message.from_user.id,
        "chatname": message.chat.username,
        "chattitle": message.chat.title,
        "username": message.from_user.username or "Empty",
        "messageid": message.message_id,
        "text": message.text,
        "caption": message.caption,
        "violation": 0,
        "useridbot": userid_bot,
        "usernamebot": username_bot
    }

    systemtime = datetime.datetime.today()
    time_deltas = {
        "deltamonth_message": datetime.timedelta(days=30),
        "deltaweek_message": datetime.timedelta(days=7),
        "deltaday_message": datetime.timedelta(days=1),
        "deltahour_message": datetime.timedelta(hours=1),
        "deltamin_message": datetime.timedelta(minutes=10)
    }

    variablesdict["date_message"] = systemtime.strftime('%Y-%m-%d %H:%M:%S')
    for key, delta in time_deltas.items():
        variablesdict[key] = (systemtime - delta).strftime('%Y-%m-%d %H:%M:%S')

    return variablesdict

def variableslimits(variablesdict):
    userlimit = db.checkuserlimit(variablesdict)
    variablesdict = {**variablesdict, **userlimit}
    
    return variablesdict