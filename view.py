from app_controller import *

command_list = ['add','save','printall','read','edit','del','find','help','exit']
help_list = ['Создание заметки - "%s"' %command_list[0], 
               'Сохранение заметок - "%s"'%command_list[1], 
               'Список заметок - "%s"'%command_list[2],
               'Показать заметку (id) - "%s"'%command_list[3],
               'Редактировать заметку (id) - "%s"'%command_list[4], 
               'Удалить заметку (id) - "%s"'%command_list[5],
               'Найти заметку по дате - "%s"'%command_list[6],
               'Помощь - "%s"'%command_list[7],
               'Выход - "%s"'%command_list[8]] 

def start():
    print("Добро пожаловать в \033[93mМои Заметки\033[0m")
    add_log(['start', True])
    add_log(['load',load_note()])
    help()
    while(True):
        command = get_command()
        if command == command_list[0]:
            print("Запись добавленна.") if add_note(entry_row()) else print("Ошибка!")

        elif command == command_list[1]:
            print("Сохранено.") if save_notes() else print("Ошибка!")

        elif command == command_list[2]:
            notes = get_notes()
            flag = notes.pop()
            print_notes(notes)
            print("-------------") if flag else print("Записей нет.")

        elif command == command_list[3]:
            id = entry_id()
            if id != None:
                print("") if read_note(id) else print("Индекс не найден!")

        elif command == command_list[4]:
            id = entry_id()
            if id != None:
                data = entry_row()
                print("Перезаписанно.") if edit_notes((id,data[0],data[1])) else print("Индекс не найден!")

        elif command == command_list[5]:
            id = entry_id()
            if id != None:
                print("Запись удаленна.") if del_notes(id) else print("Ошибка!")

        elif command == command_list[6]:
            first = input("Введите первую дату интервала (DD/MM/YY): ")
            second = input("Введите вторую дату интервала (DD/MM/YY): ")
            result = find_note(first,second)
            if result == False:
                print("Некорректная дата!")
            elif len(result) == 0:
                print("Нет совпадений!")
            else:
                print_notes(result)

        elif command == command_list[7]:
            help()

        elif command == command_list[8]:
            add_log(['end', True])
            return

def help():
    print("\033[92mДоступные команды:\033[0m")
    for i in help_list:
        print(i)

def get_command():
    while True:
        act = input("\033[92mВведите команду: \033[0m")
        if not act in command_list:
            print("Неверный запрос!")
            help()
        else:
            return act

def print_notes(date):
    for i in date:
        print(i)

def entry_row():
    header = input("Введите заголовок: ")
    text = input("Введите текст: ")
    return (header,text)

def entry_id():
    id = input("Введите id заголовка: ")
    if not id.isdigit():
        print("Ошибка ввода!")
        return None
    else:
        return int(id)