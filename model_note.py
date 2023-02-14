from datetime import *

class Note:
    class_counter = 0

    def __init__(self,id,header,text,date):
        self.id = id
        self.header = header
        self.text = text
        self.date = date        

    def __str__(self) -> str:
        return f"id:{self.id} date:{str(self.date)} header:{self.header}"

    def create(header,text):
        Note.class_counter += 1
        date = datetime.now().strftime("%d/%m/%y %H:%M:%S")
        return Note(Note.class_counter,header,text,date)

    def load(id,header,text,date):
        if Note.class_counter < id:
            Note.class_counter = id
        return Note(id,header,text,date)
