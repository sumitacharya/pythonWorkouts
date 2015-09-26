#!/usr/bin/python

# helper functions
import random

# Define range
min = 1
max  = 100

# Define variables
secret_num = 0
guess = 0
guesses_left = 6

# Game Info
print "Range is [",min,",",max,"]"
print "Number of guesses = ", guesses_left

# start game
secret_num = random.randint(min,max)

while (guesses_left > 0):
	print "\n"
	guess=input("Guess a Number : ")
	if guess>secret_num : 
		print "Secret number is LOWER!"
		guesses_left -= 1
		print "Guesses left = ",guesses_left
	elif guess<secret_num : 
		print "Secret number is LARGER!."		
		guesses_left -= 1
		print "Guesses left = ",guesses_left
	else : 
		print "CONGRATULATIONS ! Your guess is Correct."
		exit()	

print "\nGame Over"
print "The secret number is : ",secret_num

