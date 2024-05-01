import telebot
from telebot.types import Message
import utils
from repository import Repo
from entities import GroupSearch, GroupSend

repo = Repo()
bot = telebot.TeleBot(token=utils.from_config_get('BOT_SETTINGS', 'token'), parse_mode='HTML')


not_defined_groups = {}


@bot.message_handler(content_types=["text", "photo"])
def handle_message(message: Message):
	if message.from_user.is_bot:
		pass
	else:
		groups_search: list[GroupSearch] = repo.get_groups_search()
		groups_send: list[GroupSend] = repo.get_groups_send()
		keywords: list[str] = repo.get_keywords()
		minus_words: list[str] = repo.get_minus_words()
		if message.forward_from_chat.id in list(map(lambda g: g.group_id, groups_search)):
			text = message.text if message.text is not None else message.caption
			text = text.lower()
			for minus_word in minus_words:
				if minus_word in text:
					pass
			got_keyword = False
			howmany_keywords = 0
			
			for keyword in keywords:
				if keyword in text:
					how_many = text.count(keyword)
					got_keyword = True
					howmany_keywords += how_many
					text = text.replace(keyword, f"<b>{keyword.upper()}</b>")
			if got_keyword:
				if message.chat.username:
					new_text = utils.from_config_get("SEND_TEXT", "tt").format(message.from_user.username,
					                                                           message.from_user.full_name,
					                                                           message.chat.username,
					                                                           message.chat.title,
					                                                           howmany_keywords,
					                                                           text)
				else:
					new_text = utils.from_config_get("SEND_TEXT", "tn").format(message.from_user.username,
					                                                           message.from_user.full_name,
					                                                           message.chat.title,
					                                                           howmany_keywords,
					                                                           text)
				for group in groups_send:
					if message.content_type == "photo":
						photo1 = max(message.photo, key=lambda x: x.height)
						bot.send_photo(chat_id=group.group_id, caption=new_text, photo=photo1.file_id)
					else:
						bot.send_message(chat_id=group.group_id, text=new_text, disable_web_page_preview=True)



if __name__ == '__main__':
	bot.infinity_polling()