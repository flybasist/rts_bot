import yaml

def typedb():
    with open("settings.yaml", "r") as f:
        config = yaml.safe_load(f)
        typedb = config["typedb"]
    return typedb

def id_bot():
    with open("settings.yaml", "r") as f:
        config = yaml.safe_load(f)
        idbot = config["idbot"]
    return idbot

def chatforpostal():
    with open("settings.yaml", "r") as f:
        config = yaml.safe_load(f)
        chatforpostal = config["chatforpostal"]
        try:
            chatforpostal = list(map(int, chatforpostal.split(',')))
        except:
            pass
    return chatforpostal