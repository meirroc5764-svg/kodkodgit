import os

def create_file():
    with open("grades.txt", "w", encoding="utf-8") as f:
        f.write(f"Dan,{[85,90,78]} \n")
        f.write( f"MOMO,{[92,88,95]} \n") 
        f.write (f"Yoni,{[70,65,80]}\n")
        f.write(f"Avi,{[100,95,98]}\n")
        f.write(f"Sara,{[60,72,68]}\n")
    return None

def calculate_averages(file):
    averages = {}
    
    with open(file, "r", encoding="utf-8") as f:
        the_file = f.readlines()
        
        for student in the_file:
            sum_greade = 0 
            
            name, grades_str = student.strip().split(",", 1)
            
            if len(grades_str) < 3:
                print("no hve all greade")

            if len(grades_str) < 1:
                print("this student no have greade")
                continue       
            
            grades_str = grades_str.strip("[]").split(",")
            
            for grade in grades_str:
                sum_greade += int(grade)
            
            averages[name] = sum_greade / len(grades_str)
    
    return averages

def save_results(averges, output_file_name):
    
    with open(output_file_name, "w", encoding="utf-8") as f:
        f.write(" === Student Results === \n")
        
        result = {k: v for k, v in sorted(averges.items(),
                key=lambda item:item[1] ,reverse= True)}
       
        for key,value in result.items():
            f.write(f"{key}:{round(value, 1)}\n")    
    
    return None

def all_statistics(file):
    num_studens = 0
    total = 0

    with open(file, "r+", encoding="utf-8") as f:
        all_lines = f.readlines()
        f.write(" === Statistics === \n")
    
        for student in all_lines:
            student = student.strip().split(":")

            if len(student) < 2:
                continue

            grade = float(student[1])

            total += grade
                
            if grade > 59:
                num_studens += 1

        avg = total / len(all_lines)
        f.write(f"Class average: {round(avg, 1)}\n")
        f.write(f"Highest: {all_lines[1]}")
        f.write(f"Lowest: {all_lines[-1]}")
        f.write(f"Passing (>=60): {num_studens}/{len(all_lines)}")
    return None




create_file()
results = calculate_averages("grades.txt")
for name, avg in results.items():
    print(f'{name}: {avg:.1f}')
save_results(results, "results.txt")
all_statistics("results.txt")
