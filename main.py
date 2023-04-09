import os
from functions import *


cont = True

while cont:
    os.system("cls")
    print("""
    Register of Students:

    1- Add
    2- Modify
    3- Delete
    4- Students Lis
    5- Log Out
    """)
    opt = input("Select a option: ")
    if opt == "1":
        add()
    elif opt == "2":
        modify()
    elif opt == "3":
        delete()
    elif opt == "4":
        liststudent()
    elif opt == "5":
        cont = False
        input("See you later👋!!\nPress enter to logout!")
    else:
        input("Select a option between 1 to 5")
