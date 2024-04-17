import settings
import telebot

idbot = settings.id_bot()

bot = telebot.TeleBot(idbot)
    
def postalmonday(chatid):
    for x in chatid:
        bot.send_sticker(x, 'CAACAgIAAxkBAAIFoGYcFlsFwf7fWNihMnlWZ0vgdAvXAAKhAAOuzWgKuGAO1aQWu3o0BA')
    
def postaltuesday(chatid):
    for x in chatid:
        bot.send_sticker(x, 'CAACAgIAAxkBAAIFoWYcFl3Crc5ZAR6UwcFfnBr9R3sbAAKiAAOuzWgK0jyMnXeEx3w0BA')
    
def postalwednesday(chatid):
    for x in chatid:
        bot.send_sticker(x, 'CAACAgIAAxkBAAIFomYcFl8XBed2NGm-r3tzOVs3tlhVAAKjAAOuzWgKfTwrlcT0RQ80BA')
    
def postalthursday(chatid):
    for x in chatid:
        bot.send_sticker(x, 'CAACAgIAAxkBAAIFo2YcFmAn2wGcgfLaV0lu9UXx5fwWAAKkAAOuzWgKFb_Ydb0WSMo0BA')
    
def postalfriday(chatid):
    for x in chatid:
        bot.send_sticker(x, 'CAACAgIAAxkBAAIFpGYcFmGkRRv1DdW9YwFnPcoiwbIqAAKlAAOuzWgK9wUq3Hjbq6c0BA')