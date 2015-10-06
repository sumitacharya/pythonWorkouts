#! /usr/bin/python

##################### Helper file ############################
from fifo import Fifo

###########Overriding Parent class FIFO ###########
####### Limits to given QUEUE DEPTH ## Rejects if QUEUE DEPTH is full ############

class fifoFull(Fifo):
	queueDepth = 2
	
	def __init__(self,value):
		self.value=value
		if Fifo.queueCount < fifoFull.queueDepth:
			Fifo.queueCount += 1
			Fifo.queueElements.insert(0,value)
		else :
			print "Packet Rejected !!! Queue is Full !!!"


############# Testing FIFO Operation with Queue Full ##################################

In = fifoFull(11)
In.displayCountAndElements()
print"\n"
In = fifoFull(22)
In.displayCountAndElements()
print"\n"
In = fifoFull(33)
In.displayCountAndElements()
print"\n"


print "\n\nOut 1 : ",In.firstOut()
In.displayCountAndElements()
print"\n"
print "\nOut 2 : ",In.firstOut()
In.displayCountAndElements()
print"\n"
print "\nOut 3 : ",In.firstOut()
In.displayCountAndElements()
print"\n"


In = Fifo(66)
In.displayCountAndElements()
print"\n"
In = Fifo(77)
In.displayCountAndElements()
#############################################################################################

