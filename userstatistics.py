import reaction
import db

def statistics(variablesdict):

    variablesdict["contenttype"] = "sticker"
    variablesdict["countsticker"] = db.basecount(variablesdict)
    variablesdict["contenttype"] = "animation"
    variablesdict["countanimation"] = db.basecount(variablesdict)
    variablesdict["contenttype"] = "voice"
    variablesdict["countvoice"] = db.basecount(variablesdict)
    variablesdict["contenttype"] = "video_note"
    variablesdict["countvideonote"] = db.basecount(variablesdict)
    variablesdict["contenttype"] = "text"
    variablesdict["violation"] = 1
    variablesdict["countext"] = db.basecounttext(variablesdict)
    variablesdict["violation"] = 0

    reaction.reactionstatistics(variablesdict)