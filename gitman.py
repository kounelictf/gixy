#!/usr/bin/python
import os
import sys
import time
from time import sleep


print("oO0o-----------o0Oo")
print("      GITMAN ")
print("oO0o-----------o0Oo")
print("Gitlab / Github repo Installer <3")
print("by kouneli")

print("[1] Clone a Repo")
print("[2] Repo History")
print("[3] Clone from File")
uo = input("option:  ")

if uo == "1":
    try:
        opt_1 = input("Repo to clone: ")
        with open('repun.txt', 'w') as f:
            f.write(opt_1)
            glt = os.system("git clone " + opt_1)
            
    except:
        print(glt)

if uo == "2":
    f = open("repun.txt", "r")
    print("oO0o-----------o0Oo")
    print("      GITMAN ")
    print("oO0o-----------o0Oo")
    print("Repository History\n")
    print(f.read())
    sleep(5)
    exit()
    
if uo == "3":
    print(""" Make sure to put desired\n repositories in repos.txt""" )
    gr = open('repos.txt', 'r')
for x in gr:
    glt = os.system("git clone " + gr.read())
    with open('repun.txt', 'w') as f:
            f.write(glt)
    print(glt)

    

