import json


def from_config_get(head, name):
	with open("config.json", "r", encoding="utf-8") as f:
		data = json.load(f)
		return data[head][name]
