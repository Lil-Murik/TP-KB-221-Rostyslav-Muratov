class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

students = [
    Student("Rostyslav", 21),
    Student("Bob", 20),
    Student("Liza", 19),
    Student("Zak", 20),
    Student("Dave", 21),
    Student("Chris", 20),
]

while True:
    whichSort = input("Sort by descending or ascending: ")
    if whichSort == "ascending":
        sortType = True
        break
    elif whichSort == "descending":
        sortType = False
        break
    else: 
        print("Invalid option. Try againg...")

sortStudents = sorted(students, key=lambda student: student.age, reverse=sortType)
for student in sortStudents:
    print(f"Name: {student.name}, Age: {student.age}")
    