from random import randint #import random integer function from the random library module
#swertres game
taya1 = int(input("Enter first number (0-9):")); taya2 = int(input("Enter second number (0-9):")); taya3 = int(input("Enter third number (0-9):")) #player will input three numbers from 0-9 to play
result1 = randint(0,9); result2 = randint(0,9); result3 = randint(0,9) #generate three integer/number using randint function

print("Taya nimo:", taya1, taya2, taya3); print("Result:", result1, result2, result3) #the player input will be printed and also the generated result

if (taya1 == result1 and taya2 == result2 and taya3 == result3): #checking if the taya(player input number) matches with the generated result
    print("You Win!") #print if it matches
else:
    bet = [taya1, taya2, taya3]; result = [result1, result2, result3] #create bet/taya list and result list
    if sorted(bet) == sorted(result): #check if taya and result matches in any order using sorted function
        print("You Partially Win!") #the player partially win if the number matches in any order (e.g: bet: 1 2 3 result: 3 2 1)
    else:
        print("You Lose!") #else if players three numbers didn't match at all
