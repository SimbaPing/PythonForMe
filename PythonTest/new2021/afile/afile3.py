# Created with IntelliJ IDEA by Django on 2021/1/8 23:52

import os

if os.path.exists("demoDel.txt"):
    os.remove("demoDel.txt")
else:
    print("The file does not exist")

if os.path.exists("demoFolder"):
    os.rmdir("demoFolder")
else:
    print("The folder does not exist")
