import json 
from model_note import Note
from datetime import *

def save(notes):
    try:
        with open("notes.json", "w") as save_file:
            json_string = json.dumps(notes, default=lambda o: o.__dict__, indent=4)
            save_file.write(json_string)
        return True
    except:
        return False

def load():
    notes = []
    try:
        with open("notes.json", "r") as file:
            json_string = json.load(file)
            for i in json_string:               
                #date = datetime.strptime(i['date'], '%d/%m/%y %H:%M:%S')
                note = Note.load(int(i['id']),i['header'],i['text'],i['date'])
                notes.append(note)
        return notes
    except:
        return None