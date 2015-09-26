#!/usr/bin/python

# Rolling Dice
# Simple game to generate a random number between 1 to 6

import random

def numberToName(number):
	if number==1:
		return "ONE"
	elif number==2:
		return "TWO"
	elif number==3:
		return "THREE"
	elif number==4:
		return "FOUR"
	elif number==5:
		return "FIVE"
	else :
		return "SIX"

def roll_dice():
	rolledValue = random.randint(min,max)
	print"The number IS : ",rolledValue
	print "Written as : ", numberToName(rolledValue)

# Define Variables
min = 1
max = 6
rolledValue = 0

n=raw_input("Press 'c' to roll the dice : ")
while(n=="c") :
	roll_dice()
	n=raw_input("Press 'c' to roll the dice : ")
#exit()


	
	
