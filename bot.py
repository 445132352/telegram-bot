	#библиотеки, которые загружаем из вне
import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('static/welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("🔥 Мой репозиторий")
	item2 = types.KeyboardButton("🤝 Написать мне в личку")
	item3 = types.KeyboardButton("📧Написать на E-mail")

	markup.add(item1, item2, item3)

	bot.send_message(message.chat.id, "Приветствую тебя <b>{0.first_name}</b>, \nЯ - QA HotBot - бот способный дарить улыбку :)".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == '🔥 Мой репозиторий':
			bot.send_message(message.chat.id, 'https://github.com/445132352/cv')
		elif message.text == '🤝 Написать мне в личку':
			bot.send_message(message.chat.id, 'https://t.me/av_andrew')
		elif message.text == '📧Написать на E-mail':
			bot.send_message(message.chat.id, 'aav0289@gmail.com')
		else:
			bot.send_message(message.chat.id, 'Неожиданно!, дайте минуту на размышление :)')


bot.polling(none_stop=True)









#https://core.telegram.org/bots/api#available-methods