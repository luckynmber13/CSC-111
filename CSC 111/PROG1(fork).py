'''
Program:  <progname>.py
Author:  Thomas M. Queenan
Class:   CSC 111
Instructor:  V Manes
Due:     <date>
Written  <date>

Program description: <what it does, how it does it. Briefly>

Program usage: <any special instructions>
'''

# Import statements go here
import math

# Constant declarations go here




#be sure to comment the code enough, but not too much
#there should be a comment for every group of lines that do a
#related task. The comment should be very brief


#YOU MUST HAVE A FUNCTION main( )
'''
Function:  Main
Author:  Thomas M. Queenan
Function description:  <brief description>

Parameters: none

Return: <describe return value,if any>
'''
def main( ):
    
    #variable declarations
    str = get_status()
    if str == "X":
        return
    int = get_income()
    
    #function body

    



#OTHER FUNCTIONS ARE OPTIONAL, BASED ON PROGRAM NEED
#(Delete this section if not used)
'''
Function:  isFloat
Author:  Thomas M. Queenan
Function description:  checks if value can be converted to a float

Parameters: value

Return: bool
'''

def isFloat(value):#Checks to se if it can be converted to a number
	try:
		float(value)
		return True #no error
	except ValueError:
		return False #error
#end

'''
Function:  <function name>
Author:  Thomas M. Queenan
Function description:  <brief description>

Parameters: <list inputs>

Return: <describe return value,if any>
'''

def get_income()
    input = inputFloat()


'''
Function: get_status 
Author:  Thomas M. Queenan
Function description:  gets the status and returns it

Parameters: none

Return: str
'''

def get_status():
    return inputStr("What is your marital status? (m or s): ", 3 , ['m','s'])
    

'''
Function:  inputStr
Author:  Thomas M. Queenan
Function description:  returns input that is valid bassed off of given info

Parameters: output, trys, options

Return: str
'''
    
def inputStr(output, trys, options):#returns input that is in options in x number of trys
    str = input(output).lower() #get input
    if (len(str) == 1): #is proper size
        if inOptions(str, options): #is in valid options
            str #str is good input
        else: #invalid input
            print("try agin") #retry
            trys = trys - 1
            str = inputStr(output, trys, options) #trys agin
    elif (trys <= 1): #tried max number of trys
        str = "X"
    elif (len(str) != 1): #too long
        print("try agin") #retry
        trys = trys - 1
        str = inputStr(output, trys, options) #ties agin
    return str #return str
#

'''
Function:  inOptions
Author:  Thomas M. Queenan
Function description:  Checks if input is in options array

Parameters: test, options

Return: true, false
'''

def inOptions(test, options): #checks if input is in options array
    for i in range(0, len(options)): #go through array of options
        if (test == options[i]):
            return True #returns true
    else:
        return False #returns false
#


    
#DO NOT DELETE THESE LINES, THEY MUST BE LAST LINES IN FILE           
if __name__ == '__main__':
    main()
