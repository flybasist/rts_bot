import yaml

def id_bot():
    with open("settings.yaml", "r") as f:
        config = yaml.safe_load(f)
        idbot = config["idbot"]["idbot"]
    return idbot

def useridbot():
    with open("settings.yaml", "r") as f:
        config = yaml.safe_load(f)
        useridbot = config["useridbot"]["useridbot"]
    return useridbot

def usernamebot():
    with open("settings.yaml", "r") as f:
        config = yaml.safe_load(f)
        usernamebot = config["usernamebot"]["usernamebot"]
    return usernamebot

def vip_members():
    with open("settings.yaml", "r") as f:
        config = yaml.safe_load(f)
        vipuser = config["vip"]["vip"]
        try:
            vipuser = list(map(int, vipuser.split(',')))
        except:
            pass
    return vipuser

def vacuumcleaner():
    with open("settings.yaml", "r") as f:
        config = yaml.safe_load(f)
        vacuumcleaner = config["vacuumcleaner"]["vacuumcleaner"]
        try:
            vacuumcleaner = list(map(int, vacuumcleaner.split(',')))
        except:
            pass
    return vacuumcleaner

def namebase():
    with open("settings.yaml", "r") as f:
        config = yaml.safe_load(f)
        namebase = config["namebase"]["namebase"]
    return namebase

def namelog():
    with open("settings.yaml", "r") as f:
        config = yaml.safe_load(f)
        namelog = config["namelog"]["namelog"]
    return namelog

def chatforpostal():
    with open("settings.yaml", "r") as f:
        config = yaml.safe_load(f)
        chatforpostal = config["chatforpostal"]["chatforpostal"]
        try:
            chatforpostal = list(map(int, chatforpostal.split(',')))
        except:
            pass
    return chatforpostal

def stickeramiga():
    with open("settings.yaml", "r") as f:
        config = yaml.safe_load(f)
        stickeramiga = config["stickers"]["stickeramiga"]
    return stickeramiga

def stickerregidron():
    with open("settings.yaml", "r") as f:
        config = yaml.safe_load(f)
        stickerregidron = config["stickers"]["stickersregidron"]
    return stickerregidron
