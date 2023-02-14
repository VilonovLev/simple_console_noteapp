from model_note import *

notes_list = []

def get_all_notes():
    return notes_list

def set_notes(notes):
    for i in notes:
        notes_list.append(i)

def add(data):
    length = len(notes_list)
    header = data[0]
    text = data[1]
    notes_list.append(Note.create(header,text))
    if (len(notes_list) != length):
        return True
    return False

def read(id):
    note = search_node(id)
    if (note != None):
        print(f"id:{note.id}\nheader:{note.header}\ntext:{note.text}")
        return True
    return False

def edit(data):
    note = search_node(data[0])
    if (note != None):
        note.header = data[1]
        note.text = data[2]
        note.date = datetime.now().strftime("%d/%m/%y %H:%M:%S")
        return True
    return False

def delete(id):
    note = search_node(id)
    if (note != None):
        notes_list.remove(note)
        return True
    return False

def search_node(note_id):
    for note in notes_list:
        if note.id == note_id:
            return note
    return None

def find(first,second):
    search_date = []
    for note in notes_list:
        note_date = datetime.strptime(note.date,"%d/%m/%y %H:%M:%S").date()
        if (first<note_date) and (note_date<second):
            search_date.append(note)
    return search_date
    