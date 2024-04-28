import json


def from_config_get(head, name):
	with open("config.json", "r", encoding="utf-8") as f:
		data = json.load(f)
		return data[head][name]
	
	

def save_group_send(group_name, group_id):
	with open("GROUPS_SEND.txt", "a+") as f:
		f.write(f"{group_name}, {group_id}\n")

def save_group_search(group_name, group_id):
	with open("GROUPS_SEARCH.txt", "a+") as f:
		f.write(f"{group_name}, {group_id}\n")

def save_key_word(keyword):
	with open("KEY_WORDS.txt", "a+") as f:
		f.write(f"{keyword}\n")