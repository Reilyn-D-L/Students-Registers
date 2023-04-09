import os
from peewee import *
from prettytable import PrettyTable

db = SqliteDatabase("Student.db")

class students(Model):
    idnumber = CharField(10)
    name = CharField(50)
    last_name = CharField(50)
    Q1 = IntegerField()
    Q2 = IntegerField()

    class Meta:
        database = db

db.connect()
db.create_tables([students])

def cls():
    os.system("cls")

def add():
    cls()
    print("Add Student")
    st = students()
    st.idnumber = input("Digit the Id Number: ")
    st.name = input("Digit the name student: ")
    st.last_name = input("Digit the Last Name student: ")
    st.Q1 = input("Digit the first Qualification: ")
    st.Q2 = input("Digit the second Qualification: ")
    st.save()
    idx = input("Student Save Succesfully✔!!\nPress Enter to continue!")
    if idx == "x" or "":
        return False

def confirmdata(camp, value):
    print("")
    print("The field "+camp+" have value: "+ value)
    tmp = input("Digit the new value or leave it blank for not change: ")
    if tmp == "":
        return value
    else:
        return tmp

def qual(note):
    eq = "F"
    if(note >= 90):
        eq = "A"
    elif(note >= 80):
        eq = "B"
    elif(note >= 70):
        eq = "C"
    return eq

def seestudentdisplay():
    tbl = PrettyTable()
    print("                                  Students List ")
    tbl.field_names = ["Id", "School Enrollment", "Name", "Last Name", "Q1", "Q2", "Average", "Final Score"]
    for st in students.select():
        AVER = (st.Q1+st.Q2)/2
        tbl.add_row([st.id, st.idnumber, st.name, st.last_name, st.Q1, st.Q2, AVER, qual(AVER)])
    return tbl
    
def modify():
    cls()
    print(seestudentdisplay())
    idx = input("Enter id student that you need modify, X for cancel: ")
    if idx == "x" or "":
        return False
    st = students.select().where(students.id ==idx).get()

    st.idnumber = confirmdata("Id Number", st.idnumber)
    st.name = confirmdata("Name", st.name)
    st.last_name = confirmdata("Last Name", st.last_name)
    st.Q1 = int(confirmdata("Rating 1", str(st.Q1)))
    st.Q2 = int(confirmdata("Rating 2", str(st.Q2)))
    st.save()

    input("Modified Record Succesfully✔!!\nPress Enter to continue")
    
def delete():
    cls()
    print("Enter id student thet want delete: ")
    print(seestudentdisplay())
    idx = input("Enter id student that you need modify, X for cancel: ")
    if idx == "x" or "":
        return False
    st = students.select().where(students.id ==idx).get()
    input(f"Student {st.idnumber} => {st.name} was deleted succesfully✔!!\nPress Enter to continue!")
    st.delete_instance()

def liststudent():
    cls()
    print(seestudentdisplay())
    idx = input("Enter X for exit of the list: ")
    if idx == "x" or "":
        return False