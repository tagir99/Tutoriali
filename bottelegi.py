import telebot

bot = telebot.TeleBot("vstavit token")

@bot.message_handler(content_types=['text'])
def send_welcome(message):
    a = ( message.text )
    if a == "command":
       answer = "a" + "22"


    bot.send_message(message.chat.id, answer)



bot.polling( none_stop= True )