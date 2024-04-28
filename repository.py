from utils import from_config_get

class Repo:
	GROUPS_SEND_FILE = from_config_get("BOT_SETTINGS", "groups_send")
	GROUPS_SEARCH_FILE = from_config_get("BOT_SETTINGS", "groups_search")
	KEY_WORDS_FILE = from_config_get("BOT_SETTINGS", "key_words")
	
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
	def get_groups_send(cls):
		groups_send = []
		with open(cls.GROUPS_SEND_FILE, "r", encoding="utf-8") as f:
			lines = f.readlines()
			for line in lines:
				group_id, group_name = line.replace("\n", "").split(", ") if line != "\n" else (None, None)
				if group_name:
					groups_send.append((group_id, group_name))
					
		return groups_send
	
	
	@classmethod
	def get_groups_search(cls):
		groups_search = []
		with open(cls.GROUPS_SEARCH_FILE, "r", encoding="utf-8") as f:
			lines = f.readlines()
			for line in lines:
				group_id, group_name = line.replace("\n", "").split(", ") if line != "\n" else (None, None)
				if group_name:
					groups_search.append((int(group_id), group_name))
		
		return groups_search


