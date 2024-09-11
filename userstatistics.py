import reaction
import db

def statistics(variablesdict):

    variablesdict["contenttype"] = "photo"
    variablesdict["countphoto"] = db.basecount(variablesdict)
    
    variablesdict["contenttype"] = "audio"
    variablesdict["countaudio"] = db.basecount(variablesdict)
    
    variablesdict["contenttype"] = "voice"
    variablesdict["countvoice"] = db.basecount(variablesdict)
    
    variablesdict["contenttype"] = "video"
    variablesdict["countvideo"] = db.basecount(variablesdict)
    
    variablesdict["contenttype"] = "document"
    variablesdict["countdocument"] = db.basecount(variablesdict)
    
    variablesdict["contenttype"] = "location"
    variablesdict["countlocation"] = db.basecount(variablesdict)
    
    variablesdict["contenttype"] = "contact"
    variablesdict["countcontact"] = db.basecount(variablesdict)
    
    variablesdict["contenttype"] = "sticker"
    variablesdict["countsticker"] = db.basecount(variablesdict)
    
    variablesdict["contenttype"] = "animation"
    variablesdict["countanimation"] = db.basecount(variablesdict)
    
    variablesdict["contenttype"] = "video_note"
    variablesdict["countvideonote"] = db.basecount(variablesdict)
    
    variablesdict["contenttype"] = "text"
    variablesdict["violation"] = 21
    variablesdict["countext"] = db.basecounttext(variablesdict)
    variablesdict["violation"] = 0

    reaction.reactionstatistics(variablesdict)