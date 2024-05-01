from utils import from_config_get
from entities import GroupSend, GroupSearch

class Repo:
	GROUPS_SEND_FILE = from_config_get("BOT_SETTINGS", "groups_send")
	GROUPS_SEARCH_FILE = from_config_get("BOT_SETTINGS", "groups_search")
	KEY_WORDS_FILE = from_config_get("BOT_SETTINGS", "key_words")
	MINUS_WORDS_FILE = from_config_get("BOT_SETTINGS", "minus_words")
	
	@classmethod
	def get_keywords(cls):
		keywords = []
		with open(cls.KEY_WORDS_FILE, "r", encoding="utf-8") as f:
			lines = f.readlines()
			for line in lines:
				keyword = line.replace("\n", "") if line != '\n' else None
				if keyword:
					keywords.append(keyword)
			
		return keywords
	
	
	@classmethod
	def get_minus_words(cls):
		minus_words = []
		with open(cls.MINUS_WORDS_FILE, "r", encoding="utf-8") as f:
			lines = f.readlines()
			for line in lines:
				minus_word = line.replace("\n", "") if line != '\n' else None
				if minus_word:
					minus_words.append(minus_word)
		
		return minus_words
	
	
	@classmethod
	def get_groups_send(cls) -> list[GroupSend]:
		groups_send = []
		with open(cls.GROUPS_SEND_FILE, "r", encoding="utf-8") as f:
			lines = f.readlines()
			for line in lines:
				group_id = line.replace("\n", "") if line != "\n" else None
				if group_id:
					groups_send.append(GroupSend(int(group_id)))
					
		return groups_send
	
	
	@classmethod
	def get_groups_search(cls) -> list[GroupSearch]:
		groups_search = []
		with open(cls.GROUPS_SEARCH_FILE, "r", encoding="utf-8") as f:
			lines = f.readlines()
			for line in lines:
				group_id = line.replace("\n", "") if line != "\n" else None
				if group_id:
					groups_search.append(GroupSearch(int(group_id)))
		
		return groups_search