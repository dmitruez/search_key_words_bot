import telebot
from telebot.types import Message, CallbackQuery

from utils import from_config_get



bot = telebot.TeleBot(token=from_config_get('BOT_SETTINGS', 'token'), parse_mode='HTML')


@bot.message_handler(content_types=["text", "photo", "video", "document"])
def handle_message(message: Message):
	text = message.text if message.text is not None else message.caption
	bot.send_message(message.chat.id, text)




if __name__ == '__main__':
	bot.infinity_polling()