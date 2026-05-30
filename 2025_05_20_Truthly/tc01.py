# MISSION: Pythoneering 'Truthy' and 'Falsy'.
# STATUS: Research
# VERSION: 1.0.0
# NOTES: https://github.com/TotalPythoneering and https://www.youtube.com/@TotalPythoneering
# DATE: 2026-05-30 06:45:47
# FILE: tc_tstr01.py
# AUTHOR: Randall Nagy
#
from blank_str import BlankStr

# Omitting the bool()ean castings on any
# of 'yon tests shalt test __eq__():

if bool(BlankStr(0))     == True: print("Error 001")
if bool(BlankStr(0j))    == True: print("Error 002")
if bool(BlankStr(0.0))   == True: print("Error 003")
if bool(BlankStr(0x00))  == True: print("Error 004")
if bool(BlankStr(' '))   == True: print("Error 005")
if bool(BlankStr('\n'))  == True: print("Error 006")
if bool(BlankStr(' \t')) == True: print("Error 007")

if bool(BlankStr(1))     == False: print("Error 011")
if bool(BlankStr(1j))    == False: print("Error 012")
if bool(BlankStr(0.001)) == False: print("Error 013")
if bool(BlankStr(0x000001)) == False: print("Error 014")
if bool(BlankStr('?'))      == False: print("Error 015")
if bool(BlankStr(' '))      != False: print("Error 016")
if bool(BlankStr('\n'))     != False: print("Error 017")
if bool(BlankStr('\t'))     != False: print("Error 018")

print("Tested")

