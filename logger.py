from datetime import *

def write_log(data):
    dt = datetime.now().strftime("%d/%m/%y %H:%M:%S")
    data.insert(0,dt)
    data[-1] =f"{data[-1]}\n"
    result = ";".join(data)
    with open("log.txt","a",encoding="UTF8") as file:
        file.write(result)
    