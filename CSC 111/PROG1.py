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
    
    #Gets status input
    str = get_status("What is your marital status? (M - Married or S - Single): ", 3 , ['m','s'])
    if str == "X":
        print("Too many attempts, Please consult your nearest IQ test")
        return 0
    #
    
    #gets income input
    int = get_income("What is your taxable income?: $", 3)
    if not(int):
        print("Too many attempts, Please consult your nearest IQ test")
        return 0
    #
    
    #checks if in parameters
    if (str == 's') and (int > 87850):
        print("Number is Too large, Please consult a specialist")
        return 0
    #
    if (str == 'm') and (int > 146400):
        print("Number is Too large, Please consult a specialist")
        return 0
    #
    
    #function body
    
    #Calculates tax ammount bassed off of income and marital status
    tax = compute_tax(str, int, [.1, .15, .25])
    
    #print
    if str == 'm':
        print("\nFiling status: Married")
    elif str == 's':
        print("\nFiling status: Single")
    else:
        print("\nYou are Magic!, No tax for you.")
        return 0
    #
    
    print("Taxable income: ${:.2f}".format(int))
    print("Tax due: ${:.2f}".format(tax))
    
    #exit
    return 0
    



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
	except BaseException:
		return False #error
#end

'''
Function:  get income
Author:  Thomas M. Queenan
Function description: gets income  

Parameters: output, trys

Return: int or 0
'''

def get_income(output,trys):
    str = input(output) #pulls input
    if (isFloat(str)):
        int = float(str) #convert to num
        if (int > 0): #Within bounds
            return int #returns the float
        elif (trys <= 1):
            print("{} is invalid input".format(str))
            return 0
        else:
            trys = trys - 1
            print("{} is too small, Please try values above zero".format(str))
            return get_income(output,trys) #recurse if out of bounds
    elif (trys <= 1):
        print("{} is invalid input".format(str))
        return 0
    else: #if number
        trys = trys - 1
        print('"{}" is not a number greater than zero'.format(str))
        return get_income(output,trys)#Recurse if not number    
#
'''
Function: get_status 
Author:  Thomas M. Queenan
Function description:  gets the status and returns it

Parameters: output, trys, options

Return: str
'''

def get_status(output, trys, options):
    try:
        str = input(output).lower() #get input
    except BaseException:
        print("Not a string")
        trys = trys - 1
        return get_status(output, trys, options) #trys agin
    if inOptions(str, options): #is in valid options
        return str #Return input
    elif (trys <= 1): #tried max number of trys
        print('"{}" is an invalid input, Please try M for Maried or S for Single'.format(str))
        return "X" #returns Failed
    else: #invalid input
        print('"{} is an invalid input, Please try M for Maried or S for Single'.format(str)) #retry
        trys = trys - 1
        return get_status(output, trys, options) #trys agin
    return "X" #return Failed
#


'''
Function:  compute tax
Author:  Thomas M. Queenan
Function description: computes tax

Parameters: str, int, taxRates

Return: str
'''
def compute_tax(str, int, taxRate):
    #declarations (used to doing this)
    limits = []
    change = []
    parts = []
    tax = 0
    
    #set up limits on brackets
    if str == 's': #single
        limits = [8925, 36250, 87850]
    elif str == 'm': #married
        limits = [17850, 72500, 146400]
    else: #???
        limits = [0, 0, 0]
    #
    
    #change limits into rate of change
    j = 0 #initial change needs manual set to 0
    for i in range(0, len(limits)): #calculates change in income brackets
        change.append(limits[i] - j)
        j = limits[i] 
    #
    
    #split money between brackets
    for i in range(0, len(change)): #larger
        if int > change[i]:
            parts.append(change[i]) #store full for that place value
            int -= change[i] #remove from total income
        #
        elif (int < change[i]) and (int >= 0):#within
            parts.append(int) #fill place value
            int -= change[i] #remove from total income
        elif (int < 0):#smaller
            parts.append(0) #fill place value with empty
    #
    
    #calculates tax bassed off of previos calculation
    for i in range(0, len(parts)):
        tax = tax + (parts[i] * taxRate[i]) #summs tax up for each bracket
    #
    
    #completed
    return tax
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
