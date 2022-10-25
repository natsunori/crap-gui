#rhys llewellyn holley 24/10/2022

import time


def clc():
        print("---------crapcalc---------")
        print("\n")
        num1 = float(input("input first number: "))
        num2 = float(input("input second number: "))
        opr = int(input("Input a operator \n \n 1.add \n 2.subtract \n 3.divide \n 4.multiply \n \n Input: "))
        
        if opr == 1:
            print("\n")
            print("output: ",num1+num2)
            print("\n")

        elif opr == 2:
            print("\n")
            print("output: ",num1-num2)
            print("\n")

        elif opr == 3:
            print("\n")
            print("output: ",num1/num2)
            print("\n")

        elif opr == 4:
            print("\n")
            print("output: ", num1*num2)
            print("\n")
        
        x = str(input("Return to crap gui? Y/N : "))
        if x == "y":
            print("\n")
            crapgui()
        elif x == "n":
            print("\n")
            clc()



def wallpaper():
#title
 print("\n---------- Wallpaper calculator ----------")
 print("Enter the wall height and lenght of all four walls. \n \n Wall Height Min. 2 Metres Max. 6 meters \n Wall lenght Min. 1 Metre Max. 25 Metres \n ")
 #height calculation
 height = float(input("Please enter the height of the wall: "))
 width = float(input("Please input Width of the wall: "))
 #invalid value checks 
 if height < 2:
    wlss102382 = int(input("Invalid height (too low) restart? 1. yes 2. no "))
 elif height > 6:
    wlss102382 = int(input("Invalid height (too high) restart? 1. yes 2.no  "))
 if width < 1:
    wlss102382 = int(input("Invalid height (too low) restart? 1. yes 2.no  "))
 elif width > 25:
     wlss102382 = int(input("Invalid width (too wide) restart? 1. yes 2.no  "))
 if wlss102382 == 1:
    wallpaper()
 elif wlss102382 == 2:
    print ("returning to app menu")
    counter = 10
    while counter != 0:
        print(counter)
        counter-=1
        time.sleep(1)
    print("returning.........")
    time.sleep(4)
    crapgui()











def crapgui():
        print ("--------------crap gui 1.1--------------")
        exe = int(input("Please execute a command file: \n 1.calc \n 2.wallpaper \n Input: "))
        if exe == 1:
            clc()
        elif exe == 2:
            wallpaper()

crapgui()
