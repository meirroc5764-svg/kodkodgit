import os
#1)
def file_creation():
    with open("diary.txt","w",encoding="utf-8") as f:
        f.write("24-03-2024 to day i bay a car \n")
        f.write("30-07-2025 today is bad day \n")
        f.write("28-01-2026 im happy \n")
    return None  

def read_file():
    try:
        with open("diary.txt", "r", encoding="utf-8") as f:
            print(f.read())
        return None
    except:
        raise FileNotFoundError("no have a file")
#2)
def add_text(file):
    if os.path.pardir(file):
        with open(file, "a", encoding="utf-8") as f:
            f.write("end a first mission")
        return None
    else:
        raise FileNotFoundError("no have a file")
#3)
def is_in(file, keyword):
    try:
        with open(file, "r",encoding="utf-8") as f:
            text_file = f.readlines()
            for line in text_file:
                if keyword in line:
                    print(line)
        return None
    except:
        raise FileNotFoundError("no have a file")
