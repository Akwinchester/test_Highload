import telebot
from telebot import types
from settings import  BUTTON_START_TEST


def make_keyboard_start():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(BUTTON_START_TEST)
    markup.add(button1)
    return markup