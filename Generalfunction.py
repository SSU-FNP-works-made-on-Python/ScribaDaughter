import telebot
import zabiraemraspesanie as zbiralka
import config
from telebot import types

departmentkees = {
'ФНП':'fnp',
'ФНБМТ':'nbmt',
'КНИИТ':'knt',
'ИН ЯЗ Ф-Т':'fi',
'СОЦ Ф-Т':'sf',
'МЕХМАТ':'mm',
'И-Т ХИМИИ':'ih',
'ИФИЖ':'ifg',
'И-Т ФИЗ КУЛ':'ifk',
'ИИИМО':'imo',
'И-Т ИСКУССТВ':'ii',
'ИДПО':'idpo',
'ГЕОЛОГ Ф-Т':'gl',
'ГЕОГРАФ Ф-Т':'gf',
'БИОЛОГ Ф-Т':'bf',
'ПСИХОЛОГ Ф-Т':'fps',
'ППИСО':'fppso',
'ФИЗФАК':'ff',
'ФИЛОСОФ Ф-Т':'fp',
'ЭКОНОМ Ф-Т':'ef',
'ЮРФАК':'uf',
'ГЕОЛОГ К-Ж':'kgl',
'К-Ж ЯБЛОЧКОВА':'cre',
'Главное меню':'chifmenu'
}

TOKEN = config.token


def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        chatid = m.chat.id
        if m.content_type == 'text':
            text = m.text
            tb.send_message(chatid, departmentkees[text] + ":::::придумай мне красивую аватарку")
            sendmessage = zbiralka.load_department(departmentkees[text])
            tb.send_message(chatid, ", ".join(sendmessage))
            markup = types.ReplyKeyboardMarkup(row_width=2)
            itembtn1 = types.KeyboardButton('ФНП')
            itembtn2 = types.KeyboardButton('ФНБМТ')
            itembtn3 = types.KeyboardButton('КНИИТ')
            itembtn4 = types.KeyboardButton('ИН ЯЗ Ф-Т')
            itembtn5 = types.KeyboardButton('СОЦ Ф-Т')
            itembtn6 = types.KeyboardButton('МЕХМАТ')
            itembtn7 = types.KeyboardButton('И-Т ХИМИИ')
            itembtn8 = types.KeyboardButton('ИФИЖ')
            itembtn9 = types.KeyboardButton('И-Т ФИЗ КУЛ')
            itembtn10 = types.KeyboardButton('ИИИМО')
            itembtn11 = types.KeyboardButton('И-Т ИСКУССТВ')
            itembtn12 = types.KeyboardButton('ИДПО')
            itembtn13 = types.KeyboardButton('ГЕОЛОГ Ф-Т')
            itembtn14 = types.KeyboardButton('ГЕОГРАФ Ф-Т')
            itembtn15 = types.KeyboardButton('БИОЛОГ Ф-Т')
            itembtn16 = types.KeyboardButton('ПСИХОЛОГ Ф-Т')
            itembtn17 = types.KeyboardButton('ППИСО')
            itembtn18 = types.KeyboardButton('ФИЗФАК')
            itembtn19 = types.KeyboardButton('ФИЛОСОФ Ф-Т')
            itembtn20 = types.KeyboardButton('ЭКОНОМ Ф-Т')
            itembtn21 = types.KeyboardButton('ЮРФАК')
            itembtn22 = types.KeyboardButton('ГЕОЛОГ К-Ж')
            itembtn23 = types.KeyboardButton('К-Ж ЯБЛОЧКОВА')
            itembtn24 = types.KeyboardButton('Главное меню')
            markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5,
                       itembtn6, itembtn7, itembtn8, itembtn9, itembtn10,
                       itembtn11, itembtn12, itembtn13, itembtn14, itembtn15,
                       itembtn16, itembtn17, itembtn18, itembtn19, itembtn20,
                       itembtn21, itembtn22, itembtn23, itembtn24)
            sendmessage = zbiralka.load_department(departmentkees[text])
            tb.send_message(chatid, "пролистайте ниже", reply_markup=markup)


tb = telebot.TeleBot(TOKEN)
tb.set_update_listener(listener) #register listener
tb.polling()
#Use none_stop flag let polling will not stop when get new message occur error.
tb.polling(none_stop=True)
# Interval setup. Sleep 3 secs between request new message.
tb.polling(interval=3)

while True: # Don't let the main Thread end.
    pass
