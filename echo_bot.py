import telebot
import config
from telebot import types
from city_information import moscow, st_petersburg, vladivostok, kazan, ekaterinburg, nizhny_novgorad, kaliningrad, \
    sochi, volgograd, arkhangelsk

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='Москва', callback_data=1))
    markup.add(types.InlineKeyboardButton(text='Санкт - Петербург', callback_data=2))
    markup.add(types.InlineKeyboardButton(text='Владивосток', callback_data=3))
    markup.add(types.InlineKeyboardButton(text='Казань', callback_data=4))
    markup.add(types.InlineKeyboardButton(text='Екатеренбург', callback_data=5))
    markup.add(types.InlineKeyboardButton(text='Нижний Новгород', callback_data=6))
    markup.add(types.InlineKeyboardButton(text='Калининград', callback_data=7))
    markup.add(types.InlineKeyboardButton(text='Сочи', callback_data=8))
    markup.add(types.InlineKeyboardButton(text='Волгоград', callback_data=9))
    markup.add(types.InlineKeyboardButton(text='Архангельск', callback_data=10))
    send_mess_start = f"<b>Привет {message.from_user.first_name}</b>!\nКакой город тебе интересен?"
    bot.send_message(message.chat.id, send_mess_start, parse_mode='html', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Краткая информация')
    answer = ''
    sity_img = ''
    if call.data == '1':
        answer = moscow
        sity_img = 'img_city/moscow.jpg'
    elif call.data == '2':
        answer = st_petersburg
        sity_img = 'img_city/spb.jpg'
    elif call.data == '3':
        answer = vladivostok
        sity_img = 'img_city/vlad.jpg'
    elif call.data == '4':
        answer = kazan
        sity_img = 'img_city/kazan.jpg'
    elif call.data == '5':
        answer = ekaterinburg
        sity_img = 'img_city/ekat.jpg'
    elif call.data == '6':
        answer = nizhny_novgorad
        sity_img = 'img_city/Kremlin_in_Nizhny_Novgorod.jpg'
    elif call.data == '7':
        answer = kaliningrad
        sity_img = 'img_city/kalini.jpg'
    elif call.data == '8':
        answer = sochi
        sity_img = 'img_city/sochi.jpg'
    elif call.data == '9':
        answer = volgograd
        sity_img = 'img_city/volgograd.jpg'
    elif call.data == '10':
        answer = arkhangelsk
        sity_img = 'img_city/arh.jpg'

    if sity_img:
        img = open(sity_img, 'rb')
        bot.send_photo(call.message.chat.id, img, answer)
    else:
        bot.send_message(call.message.chat.id, answer)


@bot.message_handler(commands=['info'])
def info(message):
    send_mess_info = 'Я могу помочь вам с краткой информацией о достопримечательностях 10 городов Росии.' \
                     '\nВы можете управлять мной, отправив эти команды:\n\n/start - запуск бота и отображение списка городов' \
                     '\n/help - расскажет как запустить бота'
    bot.send_message(message.chat.id, send_mess_info, parse_mode='html')


@bot.message_handler(commands=['help'])
def help_com(message):
    send_mess_help = f"<b>Привет {message.from_user.first_name}</b>!\nНапиши команду start"
    bot.send_message(message.chat.id, send_mess_help, parse_mode='html')


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        send_mess = f"<b>Привет {message.from_user.first_name}</b>!\nЯ бот который рассказывает краткую информацию об достопремичательностях 10 городов Росии. Введи start"
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBZ164Uw1RI8fWjPaOnMgkvdxKMumDAAJtAgACgGsjBlbkueq8RGAiGQQ')
        bot.send_message(message.chat.id, send_mess, parse_mode='html')
    elif message.text.lower() == 'пока':
        send_mess_b = f'<b>Прощайте {message.from_user.first_name}</b>!'
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBZ164Uw1RI8fWjPaOnMgkvdxKMumDAAJtAgACgGsjBlbkueq8RGAiGQQ')
        bot.send_message(message.chat.id, send_mess_b, parse_mode='html')
    else:
        send_mess_err = f"<b>Привет {message.from_user.first_name}</b>!\nЯ тебя не понимаю. Напиши команду info"
        bot.send_message(message.chat.id, send_mess_err, parse_mode='html')


bot.polling(none_stop=True)
