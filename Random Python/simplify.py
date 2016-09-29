#Thomas M. Queenan
#nth Root simplifier

#imports
import math

##
## Functions
##

# returns a bool on whether value is a number or not
def isFloat(value):
	try:
		float(value)
		return True #no error
	except ValueError:
		return False #error
#end

#calculates the nth root of a number in simplest terms and returns it as a string
def simpRoot(num, index):
	if not(isFloat(num) and isFloat(index)): #catch non numbers
		return "Not a number."
	else: #simplify
		num = float(num)
		index = float(index)
		if (num > 9999999999999999 or index > 9999999999999999 or num < 0 or index < 1): #catch inacuracy
			return "Too large or small to be precise."
		else: #simplify
			if (num == 0):
				return '{:.0f}'.format(num)
			for i in range(int(math.pow(num,(1/index))),1,-1):
				if(num % (i**index) == 0): #catch largest factor that can be removed
					if(num/i**index == 1):
						return '{:.0f}'.format(i)
					else:
						return '{:.0f} * ({:.0f}th \u221A( {:.0f}))'.format(i, index, num/(i**index)) #format string
			return '{:.0f}th \u221A( {})'.format(index, num) #can't factor
#end

##
## Main
##
def main():
	while 1: #loop!
		#input
		index = input("Nth root: ")
		num = input("input a radicand: ")
		
		#processing
		if not((num == "" or index == "") or (num == "exit" or index == "exit")): #if escape case
			print(simpRoot(num, index)) #calculate
		else: #exit
			return 0
#end
	
##
## Main launcher
##

if __name__ == '__main__':
   main() # runs main
#end