import json
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

new_value = 2.0
file_location = "C:/Riot Games/League of Legends/Config/PersistedSettings.json"
# test file location:
# file_location = "C:/Riot Games/League of Legends/Config/PersistedSettings.json"


def find_value_line(lines):
  scale_value_line = 0
  for i in range(len(lines)):
    if '"CursorScale"' in lines[i]:
      scale_value_line = i+1
  return scale_value_line

def get_value(line):
  split_line = line.split('"')
  value_string = split_line[3]
  return float(value_string)

def make_substitute_line(split_line):
  new_line = ""
  for i in range(len(split_line)):
    if i == 3:
      new_line = new_line + str(split_line[i])
    else:
      new_line = new_line + split_line[i]
    if i < len(split_line) - 1:
      new_line = new_line + '"'
    else: 
      break
  return new_line

def update_scale():
  file = open(file_location, "r")
  lines = file.readlines()
  file.close()
  scale_value_line = find_value_line(lines)
  line = lines[scale_value_line]
  actual_value = get_value(line)
  if actual_value != new_value:
    split_line = line.split('"')
    split_line[3]=new_value
    new_line = make_substitute_line(split_line)
    lines[scale_value_line] = new_line
    new_file = ""
    for i in range(len(lines)):
      new_file += lines[i]
      file = open(file_location, "w")
      file.write(new_file)

def create_window():
  window = QtWidgets.QWidget()
  window.setWindowTitle("lolcursor")
  
  layout = QtWidgets.QVBoxLayout(window)
  
  label = QtWidgets.QLabel("Cursor Scale %")
  layout.addWidget(label)
  
  input = QtWidgets.QSpinBox()
  input.setRange(100, 400)
  input.setSingleStep(25)
  input.setValue(100)
  def update_new_value():
    global new_value
    new_value = input.value()/100
  input.valueChanged.connect(update_new_value)
  layout.addWidget(input)
  
  button = QtWidgets.QPushButton("Apply")
  button.clicked.connect(update_scale)
  layout.addWidget(button)

  window.setFixedSize(220, 100)
  window.show()
  return window

def main():
  app = QtWidgets.QApplication([])
  window = create_window()

  sys.exit(app.exec())

main()