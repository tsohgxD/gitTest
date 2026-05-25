#!/usr/bin/env python
#This Programm can search for a File, u have to type the whole path tho. This demonstrates that with the import os modul u can interact nicely with ur linux OS.
import os

file = input("Enter a filename: ")

if os.path.isfile(file):
    print("The file exists.")
else:
    print("The file does not exist")  