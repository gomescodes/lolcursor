import json

def find_value_location(data):
  obj_list = ["files", "sections", "settings"]
  val_list = ["Game.cfg", "General", "CursorScale"]
  temp = data
  location = []
  for i in range(len(obj_list)):
    for j in range(len(temp[obj_list[i]])):
      if temp[obj_list[i]][j]["name"] == val_list[i]:
        location.append(obj_list[i])
        location.append(j)
        temp = temp[obj_list[i]][j]
        break
  location.append("value")
  return location

def get_value(data, location):
  temp_data = data
  for i in range(len(location)):
    temp_data = temp_data[location[i]]
  return temp_data

# def set_value(data, location):

def updateFile():
  file = open("PersistedSettings.json", "r+")
  data = json.load(file)
  location = find_value_location(data)
  print(get_value(data, location))

updateFile()