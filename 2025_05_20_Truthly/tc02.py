# MISSION: Pythoneering 'Truthy' and 'Falsy'.
# STATUS: Research
# VERSION: 1.0.0
# NOTES: https://github.com/TotalPythoneering and https://www.youtube.com/@TotalPythoneering
# DATE: 2026-05-30 06:45:58
# FILE: tc_tstr02.py
# AUTHOR: Randall Nagy
#
from blank_str import BlankStr

# How omitting the bool()ean castings on any
# of 'yon tests shalt test __eq__():

if BlankStr(0)     == True: print("Error 001")
if BlankStr(0j)    == True: print("Error 002")
if BlankStr(0.0)   == True: print("Error 003")
if BlankStr(0x00)  == True: print("Error 004")
if BlankStr(' ')   == True: print("Error 005")
if BlankStr('\n')  == True: print("Error 006")
if BlankStr(' \t') == True: print("Error 007")

if BlankStr(1)     == False: print("Error 011")
if BlankStr(1j)    == False: print("Error 012")
if BlankStr(0.001) == False: print("Error 013")
if BlankStr(0x000001) == False: print("Error 014")
if BlankStr('?')      == False: print("Error 015")
if BlankStr(' ')      != False: print("Error 016") # Casting required!
if BlankStr('\n')     != False: print("Error 017") # Casting required!
if BlankStr('\t')     != False: print("Error 018") # Casting required!

print("Tested")

