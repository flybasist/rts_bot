import configparser

def id_bot():
    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read("settings.ini")  # читаем конфиг
    idbot = config["idbot"]["idbot"]
    return idbot

def useridbot():
    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read("settings.ini")  # читаем конфиг
    useridbot = config["useridbot"]["useridbot"]
    return useridbot

def usernamebot():
    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read("settings.ini")  # читаем конфиг
    usernamebot = config["usernamebot"]["usernamebot"]
    return usernamebot

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

def chatforpostal():
    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read("settings.ini")  # читаем конфиг
    chatforpostal = config["chatforpostal"]["chatforpostal"]
    try:
        chatforpostal = chatforpostal.split(',')
        chatforpostal = list(map(int,chatforpostal))
    except:
        pass
    return chatforpostal

def stickeramiga():
    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read("settings.ini")  # читаем конфиг
    stickeramiga = config["stickers"]["stickeramiga"]
    return stickeramiga

def stickerregidron():
    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read("settings.ini")  # читаем конфиг
    stickerregidron = config["stickers"]["stickersregidron"]
    return stickerregidron