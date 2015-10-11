#!/usr/bin/python

import random
from caseConv import upper2Lower
from colors import txtcolors

# Just a small Banner
print txtcolors.RED +"				Hello"
print" 			WELCOME TO THE GAME"
print"				HANGMAN" + txtcolors.DEFAULT

# Welcome the user
name = raw_input("Enter your name : ")
print "\nWelcome... ",name," ! \nPlay well and don't get hanged"
print "\nAll the best."

# list of words
wordList=["private","man","caterpillar","matchstick","amend","doctor","travel","life","hungry","beautiful","hangman","code","lamp","rock","codeword","bed","successfull","laptop","stethescope","python","blanket"]

word = wordList[random.randint(1,len(wordList))]

# total number of turns to make mistakes
turns = 10
guesses = ''
dash = "_"

while turns > 0:
	# produce _ in place of letters
	failed = 0
	for char in word :	
		if char in guesses :
			print char,
		else:
			print dash,
			failed +=1
	if failed == 0 : 
		break
# Ask user to guess a character
	print ""
	guessChar=raw_input("Guess a new character : ")
	guessChar=upper2Lower(guessChar[0])
	guesses = guesses + guessChar
	
	if guessChar not in word : 
		turns = turns - 1
		print txtcolors.GREEN + "you have",turns,"turns left."+ txtcolors.DEFAULT 
	print"\nGuesses already made : ",guesses 

# Win Or Lose
if turns > 0 :
	print txtcolors.RED+"\nCongratulations..\nYou Won"+txtcolors.DEFAULT
else:
	print txtcolors.RED+"\nYou Lose ! \nThe correct word is : "+txtcolors.GREEN, word + txtcolors.DEFAULT		 	



