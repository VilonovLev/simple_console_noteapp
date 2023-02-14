from logger import write_log
from util_json import *
from service_notes import *

def load_note():
    notes = load() 
    if notes == None: 
        return False   
    set_notes(notes)
    return True

def add_log(data):
    write_log(data)

def add_note(date):
    flag = add(date)
    add_log(['add note', flag])
    return flag

def save_notes():
    flag = save(get_all_notes())
    add_log(['save note', flag])
    return flag

def get_notes():
    notes = get_all_notes()
    flag = False
    if len(notes) != 0: 
        flag = True
    add_log(['print notes', flag])
    notes.append(flag)
    return notes

def read_note(id):
    flag = read(id)
    add_log(['read note', flag])
    return flag

def edit_notes(date):
    flag = edit(date)
    add_log(['edit note', flag])
    return flag

def del_notes(id):
    flag = delete(id)
    add_log(['delete note', flag])
    return flag

def find_note(first,second):
    try:
        first = datetime.strptime(first,"%d/%m/%y").date()
        second = datetime.strptime(second,"%d/%m/%y").date()
    except:
        add_log(['find note', False])
        return False
    add_log(['find note', True])
    notes = find(first,second)
    return notes



