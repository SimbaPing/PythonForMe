# Created with IntelliJ IDEA by Django on 2021/1/8 23:44

f = open("demofile2.txt", "w")
f.write("Fuck You!")
f = open("demofile2.txt", "r")
print(f.read())
f = open("demofile2.txt", "a")
f.write("Yes, Fuck You!")
f = open("demofile2.txt", "r")
print(f.read())
