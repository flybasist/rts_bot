import configparser

def id_bot():
    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read("settings.ini")  # читаем конфиг
    idbot = config["idbot"]["idbot"]
    return idbot

def vip_members():
    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read("settings.ini")  # читаем конфиг
    vipuser = config["vip"]["vip"]
    try:
        vipuser = vipuser.split(',')
        vipuser = list(map(int,vipuser))
    except:
        pass
    return vipuser

def vacuumcleaner():
    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read("settings.ini")  # читаем конфиг
    vacuumcleaner = config["vacuumcleaner"]["vacuumcleaner"]
    try:
        vacuumcleaner = vacuumcleaner.split(',')
        vacuumcleaner = list(map(int,vacuumcleaner))
    except:
        pass
    return vacuumcleaner

def namebase():
    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read("settings.ini")  # читаем конфиг
    namebase = config["namebase"]["namebase"]
    return namebase

def namelog():
    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read("settings.ini")  # читаем конфиг
    namelog = config["namelog"]["namelog"]
    return namelog