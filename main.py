import os
import tkinter as tk
#import subprocess
#import sys

tk._test()

#console clear
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

#install modules(WIP)
#def install(package):
#    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

end = 1

#unit calculation
def unit():
    Hadanite = 0.0
    Aphorite = 0
    Dolovine = 0
    while(end == 1):
        print("What ore did you mine?")
        print("Hadanite = 0")
        print("Aphorite = 1")
        print("Dolovine = 2")
        ore = input()
        clear()
        if ore == "0":
            amount = 0
            amount = float(input("how much did you farm?"))
            Hadanite =  amount
        elif ore == "1":
            amount = 0
            amount = str(input("how much did you farm?"))
            Aphorite = amount
        elif ore == "2":
            amount = 0
            amount = int(input("how much did you farm?"))
            Dolovine = amount
        else:
            print("not applicable")

        Price_had = Hadanite * 275
        Price_aph = Aphorite * 150
        Price_dol = Dolovine * 130
        Price_full = Price_had + Price_aph + Price_dol
        print("price Hadernite")
        print(Price_had)
        print("price Aphorite")
        print(Price_aph)
        print("price olovine")
        print(Price_dol)
        print("total")
        print(Price_full)

#if percent calculation is wanted or units
percent_or_unit = 0

#user choice

choice = input("what would you like to calculate?")
clear()

if choice == "0":
    unit()
elif choice == "1":
    print("elif")
else:
    print("nope")
#test