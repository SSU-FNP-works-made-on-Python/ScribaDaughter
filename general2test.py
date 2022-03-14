import telebot
import zabiraemraspesanie as zbiralka
import time
import config
from telebot import types

departmentkees = {
'ФНП':'fnp',
'ФНБМТ':'nbmt',
# 'knt_КНИИТ',
# 'fi_ИН ЯЗ Ф-Т',
# 'sf_СОЦ Ф-Т',
# 'mm_МЕХМАТ',
# 'ih_И-Т ХИМИИ',
# 'ifg_ИФИЖ',
# 'ifk_И-Т ФИЗ КУЛ',
# 'imo_ИИИМО',
# 'ii_И-Т ИСКУССТВ',
# 'idpo_ИДПО',
# 'gl_ГЕОЛОГ Ф-Т',
# 'gf_ГЕОГРАФ Ф-Т',
# 'bf_БИОЛОГ Ф-Т',
# 'fps_ПСИХОЛОГ Ф-Т',
# 'fppso_ППИСО',
# 'ff_ФИЗФАК',
# 'fp_ФИЛОСОФ Ф-Т',
# 'ef_ЭКОНОМ Ф-Т',
# 'uf_ЮРФАК',
# 'kgl_ГЕОЛОГ К-Ж',
# 'cre_К-Ж ЯБЛОЧКОВА',
# 'Главное меню'
}

TOKEN = config.token


def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        chatid = m.chat.id
        if m.content_type == 'text':
            print(m)
            text = m.text
            print(departmentkees)
            print(text)
            tb.send_message(chatid, departmentkees[text] + ":::::придумай мне красивую аватарку")
            markup = types.ReplyKeyboardMarkup(row_width=2)