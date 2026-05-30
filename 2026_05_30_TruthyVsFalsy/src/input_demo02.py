#!/usr/bin/env python3
# MISSION: Pythoneering 'Truthy' and 'Falsy'.
# STATUS: Research
# VERSION: 1.0.0
# NOTES: https://github.com/TotalPythoneering and https://www.youtube.com/@TotalPythoneering
# DATE: 2026-05-30 06:46:08
# FILE: input_demo02.py
# AUTHOR: Randall Nagy
#
from blank_str import BlankStr

print("Press 'control + c' to stop...")
while True:
    if bool(BlankStr(input("Which: "))):
        print("Truly")
    else:
        print("Flasy")

