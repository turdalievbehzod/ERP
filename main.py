class Student:
    def __init__ (self, name, phone, age, email):
        self.name = name
        self.phone = phone      
        self.age = age
        self.email = email

class Group:
    def __init__(self, title, profession):
        self.title = title
        self.profession = profession
        self.students = []
class OTM:
    def __init__(self, title):
        self.title = title
        self.groups = []
        
class ERP:
    def __init__(self):
        self.title = "ERP"
        self.otms = []
        
# erp = ERP(), otm qoshish, group qoshish, student qoshish, otm guruhlari korish, bitta guruhning studentlarini korish, universitet nomini tahrirlash | uyga vazifa studentni update qilish, guruhlarni update qilish. OTM ochirish/qoshish
erp = ERP()
otm1 = OTM("TATU")
erp.otms.append(otm1)
group1 = Group("N73", "Computer Science")
otm1.groups.append(group1)
student1 = Student("Ali", "+998901234567", 20, "qwerty@gmail.com")
group1.students.append(student1)

def add_student_to_particular_group(g:Group):
    name = input("Enter student name: ")
    phone = input("Enter student phone: ")
    age = int(input("Enter student age: "))
    email = input("Enter student email: ")
    new_student = Student(name, phone, age, email)
    choice = input("Which group do you want to add this student to? (enter group title): ")
    for group in g:
        if group.title == choice:
            group.students.append(new_student)
            print(f"Student {name} added successfully to group {choice}.")
            return

def add_group_to_particular_OTM(otm:OTM):
    title = input("Enter group title: ")
    profession = input("Enter group profession: ")
    new_group = Group(title, profession)
    choice = input("Which OTM do you want to add this group to? (enter OTM title): ")
    for o in otm:
        if o.title == choice:
            o.groups.append(new_group)
            print(f"Group {title} added successfully to OTM {choice}.")
            return

def add_otm_to_ERP(erp:ERP):
    title = input("Enter OTM title: ")
    new_otm = OTM(title)
    erp.otms.append(new_otm)
    print(f"OTM {title} added successfully to ERP.")
    
def show_otms(otms):
    for otm in otms:
        print(f"OTM: {otm.title}")
        for group in otm.groups:
            print(f"  Group: {group.title}, Profession: {group.profession}")

def show_students_in_group(g:Group):
    choice = input("which group students do you want to see? (enter group title): ")
    for group in g:
        if group.title == choice:
            print(f"Students in group {group.title}:")
            for student in group.students:
                print(f"  Name: {student.name}, Phone: {student.phone}, Age: {student.age}, Email: {student.email}")
            return
def update_particular_university(otm:OTM):
    choice = input("Which OTM do you want to update? (enter OTM title): ")
    for o in otm:
        if o.title == choice:
            new_title = input("Enter new OTM title: ")
            o.title = new_title
            print(f"OTM title updated successfully to {new_title}.")
            return
    
def ERP_manager():
    while True:
        print("ERP Management System \n 1. Add OTM \n 2. Add Group to OTM \n 3. Add Student to Group \n 4. Show all OTMs and their Groups \n 5. Show Students in a Group \n 6. Update OTM Title \n 7. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            add_otm_to_ERP(erp)
        elif choice == "2":
            add_group_to_particular_OTM(erp.otms[0])
        elif choice == "3":
            add_student_to_particular_group(erp.otms[0].groups[0])
        elif choice == "4":
            show_otms(erp.otms)
        elif choice == "5":
            show_students_in_group(erp.otms[0].groups)
        elif choice == "6":
            update_particular_university(erp.otms)
        else:
            print("Exiting ERP Management System.")
            break
        
        
ERP_manager()