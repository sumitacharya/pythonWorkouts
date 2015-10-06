#!/usr/bin/python

# Performs the First In First Out (FIFO) operation

# define class for fifo.

class Fifo:
	queueCount = 0               			# represents number of elements in a queue
	queueElements = []				# stores elements
	
	def __init__(self,value):
		self.value=value
		Fifo.queueCount += 1
		Fifo.queueElements.insert(0,value)

	def displayCountAndElements(self):
		print "Total number of elements in queue = ", Fifo.queueCount
		print "Elements : ", Fifo.queueElements

	def firstOut(self):
		if Fifo.queueCount == 0 :
			return None
		else:
			Fifo.queueCount -= 1
			return Fifo.queueElements.pop()

#In = Fifo(11)
#In.displayCountAndElements()
#In = Fifo(22)
#In.displayCountAndElements()

#print "\n\nOut 1 : ",In.firstOut()
#In.displayCountAndElements()
#print "\nOut 2 : ",In.firstOut()
#In.displayCountAndElements()
#print "\nOut 3 : ",In.firstOut()
#In.displayCountAndElements()

#print"\n\n"
#In = Fifo(66)
#In.displayCountAndElements()
#In = Fifo(77)
#In.displayCountAndElements()




		
		
		


