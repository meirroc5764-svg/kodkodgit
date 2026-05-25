import os
#1)
def load_tasks(filename):
    lst = []
    '''
:dicts קוראת את הקובץ ומחזירה רשימה של
[{'id': 1, 'status': 'PENDING', 'desc':
 'ללמוד Python'}, ...]

אם הקובץ לא קיים — מחזירה רשימה ריקה
'''
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()

            for line in lines:
                dict_task = {}

                if not line.strip():
                    continue

                num,status,name = line.strip().split("|")

                dict_task["id"] = num
                dict_task["status"] = status
                dict_task["desk"] = name

                lst.append(dict_task)

    except FileNotFoundError:
        print(f"{filename} not found")

    return lst

#2)
def save_tasks(filename, tasks):
    with open(filename, "a", encoding="utf-8") as f:
        for dict in tasks:
            f.write(f"\n{dict["id"]}|{dict["status"]}|{dict["desk"]}")
    return         


#3)
def add_task(filename, description):
    '''
    :מוסיפה משימה חדשה עם
    מספר המשימה הבאה = ID -
    - status = 'PENDING'
    הפרמטר שניתן = description -
    '''
    with open(filename,"r+", encoding="utf-8") as f:
        the_file = f.readlines()
        num_line = len(the_file)
        for i in the_file:
            if not i[0].isdigit():
                num_line -= 1
                continue
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"\n{num_line + 1}|{"PENDING"}|{description}")
    return    
#add_task("task.txt", "asdfghjkl;")

#4)
def complete_task(filename, task_id):
    '''
    DONE-ל PENDING-מ id_task של משימה status משנה את
    לא קיים — מדפיסה הודעת שגיאה ID-אם ה
    '''
    if os.path.exists(filename):
        with open(filename, "r+",encoding="utf-8") as f:
            the_lines = f.readlines()
            
            for index,line in enumerate(the_lines):
                the_line = line.strip().split("|")
                
                if  the_line[0] == str(task_id):
                    new_line = f"{the_line[0]}|DONE|{the_line[2]}\n"
                
                    the_lines[index] = new_line
                    f.seek(0)
                    f.writelines(the_lines)
                    f.truncate()
                return
        return "no have task"
    else:
        return "file not found"    

#5)
def list_tasks(filename):
    '''
    :מציגה את כל המשימות בפורמט מסודר
    ]✓[ 2 [ 2 |לכת תרתרג 1
    ] [ 3 | לסיים את הפרויקט
    '''
    done_simbol = ["✅"]
    pending = []
    list_of_dict_task =load_tasks(filename)
    for dict in list_of_dict_task:
        if dict["status"] == "done" or dict["status"] == "DONE":
            print(f"{dict["id"]}|{dict["desk"]}|{done_simbol}")
        else:
            print(f"{dict["id"]}|{dict["desk"]}|{pending}")
    return

def main():
    FILENAME = "tasks.txt"

    while True:
        print('\n=== To-Do List Manager ===')
        print('1. הצג משימות')
        print('2. הוסף משימה')
        print('3. סמן כהושלם')
        print('4. יציאה')

        choice = input('בחירה: ')

        if choice == '1':
            list_tasks(FILENAME)

        elif choice == '2':
            desc = input('תיאור המשימה: ')
            add_task(FILENAME, desc)
            print('המשימה נוספה!')

        elif choice == '3':
            task_id = int(input('משימה מספר: '))
            complete_task(FILENAME, task_id)

        elif choice == '4':
            print('להתראות!')
            break

        else:
            print('בחירה לא תקינה')


if __name__ == '__main__':
    main()