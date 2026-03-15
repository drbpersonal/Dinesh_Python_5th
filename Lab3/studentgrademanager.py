students = {}
try:
    file=open("students.txt", "r")
    for line in file:
        name,g1,g2,g3=line.split(",")
        students[name]=[int(g1), int(g2), int(g3)]
        file.close()
except FileNotFoundError:
    pass
while True:
    print("\n1. Add Student")
    print("2. Display all Students")
    print("3. Search Student")
    print("4. Exit")
    choice=input("Enter your choice: ")
    try:
        if choice=="1":
            name=input("Enter student name: ")
            g1=int(input("Enter grade 1: "))
            g2=int(input("Enter grade 2: "))
            g3=int(input("Enter grade 3: "))
            students[name]=[g1, g2, g3]
            file = open("students.txt", "w")
            for name, grades in students.items():
                file.write(f"{name},{grades[0]},{grades[1]},{grades[2]}\n")
            file.close()
        elif choice=="2":
            for name, grades in students.items():
                print(f"{name}: {grades}")
        elif choice=="3":
            name=input("Enter student name to search: ")
            if name in students:
                print(f"{name}: {students[name]}")
            else:
                print("Student not found.")
        elif choice=="4":
            break
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")
