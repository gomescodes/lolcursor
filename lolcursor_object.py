import json

json_file = open("PersistedSettings.json", "r")
json_data = json.load(json_file)
json_file.close()

game_cfg = next(filter(lambda obj : obj["name"] == "Game.cfg", json_data["files"]))
general_sec = next(filter(lambda obj : obj["name"] == "General", game_cfg["sections"]))
cursor_setting = next(filter(lambda obj : obj["name"] == "CursorScale", general_sec["settings"]))

print(json.dumps(cursor_setting))

cursor_setting["value"] = 10

game_cfg = next(filter(lambda obj : obj["name"] == "Game.cfg", json_data["files"]))
general_sec = next(filter(lambda obj : obj["name"] == "General", game_cfg["sections"]))
cursor_setting = next(filter(lambda obj : obj["name"] == "CursorScale", general_sec["settings"]))

print(json.dumps(cursor_setting))

json_file = open("PersistedSettings.json", "w")
json.dump(json_data, json_file)
json_file.close()