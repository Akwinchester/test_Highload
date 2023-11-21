import telebot
from telebot import types
from settings import BOT_TOKEN, BUTTON_START_TEST, MESSAGE_TEXT
from google_sheets import send_google_sheet
from keyboard import *
import re
from keyboa import Keyboa



bot = telebot.TeleBot(BOT_TOKEN, parse_mode='HTML')


flag_final = 0

def write_responses(call):
    question_response = call.data.split('-')
    if call.message.chat.id in answer_users:
        answer_users[call.message.chat.id].append((question_response[0], question_response[1])) # в список по пользователю добавляем кортежи(номер вопроса, вариант ответа)


answer_users = {}
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, MESSAGE_TEXT['helloy'])
    bot.send_message(message.chat.id, MESSAGE_TEXT['privacy_policy'], reply_markup=make_keyboard_start())



@bot.message_handler(content_types=['text'], regexp=BUTTON_START_TEST)
def start_test(message):
    remove_keyboard = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, MESSAGE_TEXT['get_user_data'], reply_markup=remove_keyboard)
    bot.register_next_step_handler(message, get_user_data )


def get_user_data(message):
    answer_users[message.chat.id] = ['',]
    keyboard = Keyboa(items=['а','б'], items_in_row=2, front_marker='1-')

    if message.chat.id in answer_users:
        answer_users[message.chat.id][0] = message.text

    bot.send_message(message.chat.id, "Отлично, переходим к первому вопросу.")
    bot.send_message(message.chat.id, MESSAGE_TEXT['question_1'], reply_markup=keyboard())



@bot.callback_query_handler(func=lambda call: re.match(r"1-.", call.data))
def callback_inline(call):
    write_responses(call)
    question_2(call.message)


def question_2(message):
    keyboard = Keyboa(items=['а','б'], items_in_row=2, front_marker='2-')
    bot.send_message(message.chat.id, MESSAGE_TEXT['question_2'], reply_markup=keyboard())


@bot.callback_query_handler(func=lambda call: re.match(r"2-.", call.data))
def callback_inline(call):
    write_responses(call)
    question_3(call.message)


def question_3(message):
    keyboard = Keyboa(items=['а','б'], items_in_row=2, front_marker='3-')
    bot.send_message(message.chat.id, MESSAGE_TEXT['question_3'], reply_markup=keyboard())


@bot.callback_query_handler(func=lambda call: re.match(r"3-.", call.data))
def callback_inline(call):
    write_responses(call)
    question_4(call.message)


def question_4(message):
    keyboard = Keyboa(items=['а','б'], items_in_row=2, front_marker='4-')
    bot.send_message(message.chat.id, MESSAGE_TEXT['question_4'], reply_markup=keyboard())


@bot.callback_query_handler(func=lambda call: re.match(r"4-.", call.data))
def callback_inline(call):
    write_responses(call)
    question_5(call.message)


def question_5(message):
    keyboard = Keyboa(items=['а','б'], items_in_row=2, front_marker='5-')
    bot.send_message(message.chat.id, MESSAGE_TEXT['question_5'], reply_markup=keyboard())


@bot.callback_query_handler(func=lambda call: re.match(r"5-.", call.data))
def callback_inline(call):
    write_responses(call)
    question_6(call.message)


def question_6(message):
    keyboard = Keyboa(items=['а','б'], items_in_row=2, front_marker='6-')
    bot.send_message(message.chat.id, MESSAGE_TEXT['question_6'], reply_markup=keyboard())


@bot.callback_query_handler(func=lambda call: re.match(r"6-.", call.data))
def callback_inline(call):
    write_responses(call)
    question_7(call.message)


def question_7(message):
    keyboard = Keyboa(items=['а','б'], items_in_row=2, front_marker='7-')
    bot.send_message(message.chat.id, MESSAGE_TEXT['question_7'], reply_markup=keyboard())


@bot.callback_query_handler(func=lambda call: re.match(r"7-.", call.data))
def callback_inline(call):
    write_responses(call)
    question_8(call.message)


def question_8(message):
    keyboard = Keyboa(items=['а','б'], items_in_row=2, front_marker='8-')
    bot.send_message(message.chat.id, MESSAGE_TEXT['question_8'], reply_markup=keyboard())




@bot.callback_query_handler(func=lambda call: re.match(r"8-.", call.data))
def callback_inline(call):
    print(answer_users)
    write_responses(call)
    data = answer_users[call.message.chat.id]
    data_google = data[0].split('\n')
    # логика подсчета очков
    bot.send_message(call.message.chat.id, MESSAGE_TEXT['final'])

    #Чтобы что-то показать заказчику
    bot.send_message(call.message.chat.id, 'Данные, которые записываются в google-таблицу\n'+data[0])
    text_report = ''
    for i in range(1, len(data)):
        text_report +=data[i][0] + ' - ' + data[i][1] + '\n'
    bot.send_message(call.message.chat.id, text_report)

    send_google_sheet(data_google)




if __name__ == '__main__':
    bot.infinity_polling(none_stop=True)

