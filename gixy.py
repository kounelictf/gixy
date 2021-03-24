import os
import sys
import re
from stringcolor import *
import time
from time import sleep
import platform 
import subprocess



#Main Start

def sclear():
    sysproc =  sys.platform
    if sysproc == ['linux2', 'linux']:
        os.system("clear")
    elif sysproc == ['win32', 'win64']:
        os.system("cls")


    
#Options Initialization
def clar():


    print(cs("0o0o0o0 - - - - - -0o0o0o0", "red"))
    print(cs("        Clone a Repo", "yellow"))
    print(cs("0o0o0o0 - - - - - -0o0o0o0", "red"))
    clarin = input(cs("Repository URL: ", "grey"))
    with open('clh.txt', 'w') as f:
        f.write(clarin)
    in_proc = os.system("git clone " + clarin)
    print(in_proc)

def clh():
    print(cs("0o0o0o0 - - - - - -0o0o0o0", "red"))
    print(cs("      Repository History", "blue"))
    print(cs("0o0o0o0 - - - - - -0o0o0o0", "red"))
    clh_push = open('clh.txt', 'r')
    print(clh_push.read())



def lfi():

    print(cs("""Install multiple Git repositories at once.\n Add all git repositories to the "reposit.txt" file   """, "green"))
    msg1 = print(cs("Coming soon......", "grey"))
    print(msg1)


#Main User Interface
sclear()

print(cs("""


   
   )\.-.   .'(       .'(  )\    /( 
 ,' ,-,_)  \  )  ,') \  ) \ (_.' / 
(  .   __  ) (  (  '/  /   )  _.'  
 ) '._\ _) \  )  )     )   / /     
(  ,   (    ) \ (  .'\ \  (  \     
 )/'._.'     )/  )/   )/   ).'     
                                   


       """, "blue"     ))
print(cs(""" Easily clone repositories from Github and Gitlab with this simple tool.\n Gixy allows you to access your clone history\n with additional features such as bulk cloning.!""", "orange"))
print(cs("   Created by Kouneli with <3", "red"))


print("""

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::                                                                ::
::   [1] ---->    CLONE A REPOSITORY                              ::
::                                                                ::
::                                                                ::
::                                                                ::
::                                                                ::
::                                                                ::
::   [2] ---->    CLONE HISTORY                                   ::
::                                                                ::
::                                                                ::
::                                                                ::
::                                                                ::
::   [3] ---->    LIST FILE INSTALLATION                          ::                       
::                                                                ::
::                                                                ::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::



""")
gixuin = input("Option: ")
sleep(15)

try:
    if gixuin == "1":
        sclear()
        clar()
    elif gixuin == "2":
        sclear()
        clh()
    elif gixuin == "3":
        sclear()
        lfi()
except ValueError:
        print(cs("Error, user didnt choose an optio\n now exiting", "red"))
        sys.exit()





    
