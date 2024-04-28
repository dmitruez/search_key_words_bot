from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_add_group_keyboard(group_name, group_id):
	keyboard = InlineKeyboardMarkup()
	keyboard.add(InlineKeyboardButton(text=group_name, callback_data=str(group_id)))
	return keyboard
