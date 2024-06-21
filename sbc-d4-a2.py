from random import randint #import random integer function from the random library module
#humpyang game
options = {0: "kulob", 1: "hayang"} #this line is the dictionary which contain 0 and 1 as key to choose an option if it's kulob or hayang

p1 = input("pick 0 kung kulob 1 kung hayang (kulob, hayang): "); p1 = options[int(p1)] #player will input the key to choose
c1 = options[randint(0, 1)] ; c2 = options[randint(0, 1)] #the randint function will choose randomly a number from 0-1 to pick from the dictionary

print(f"P1: {p1}"); print(f"c1: {c1}"); print(f"c2: {c2}") #the player inputted choice will be printed and also the random choice from c1 and c2

if p1 != c1 and p1 != c2: #compares if p1 choice is not the same with c1 and c2
    print("p1 ang daog!") #p1 wins if c1 and c2 chose the same
elif c1 != p1 and c1 != c2: #compares if c1 choice is not the same with p1 and c2
    print("c1 ang daog!") #c1 wins if p1 and c2 chose the same
elif c2 != p1 and c2 != c1: #compares if c2 choice is not the same with p1 and c1
    print("c2 ang daog!") #c2 wins if p1 and c1 chose the same
else:
    print("parehas tanan! utro!") #if p1, c1 and c2 are the same it'll be resulting as a draw