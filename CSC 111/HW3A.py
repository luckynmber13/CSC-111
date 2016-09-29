'''
Program:  HW3A.py
Author:  Thomas M. Queenan
Class:   CSC 111
Instructor:  V Manes
Due:     <date>
Written  9/14/16

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


    #function body
    print("Enter two numbers, they may be in floting point format.")
    
    a = float( input("Enter a number for (a): ") )
    b = float( input("Enter a number for (b): ") )

    print(a , " + ", b , " = " ,a + b, end="\n")
    print(a , " - ", b , " = " ,a - b, end="\n")
    print(b , " - ", a , " = " ,b - a, end="\n")
    print(a , " * ", b , " = " ,a * b, end="\n")
    print(a , " / ", b , " = " ,a / b, end="\n")
    print(b , " / ", a , " = " ,b / a, end="\n")
    print(a , " ^ ", b , " = " ,a ** b, end="\n")

    print("Integer division and modulus", end="\n")

    print( a , " / ", b , " = " , int(a // b), end="\n" )
    print( b , " / ", a , " = " , int(b // a), end="\n" )
    print( a , " % ", b , " = " , int(a % b), end="\n" )
    print( b , " % ", a , " = " , int(b % a), end="\n" )

    
#OTHER FUNCTIONS ARE OPTIONAL, BASED ON PROGRAM NEED
#(Delete this section if not used)
'''
Function:  <function name>
Author:  Thomas M. Queenan
Function description:  <brief description>

Parameters: <list inputs>

Return: <describe return value,if any>
'''
def some_funcion( ):
    #variable declarations


    #function body

    

    return  #if needed




    
#DO NOT DELETE THESE LINES, THEY MUST BE LAST LINES IN FILE           
if __name__ == '__main__':
   main()
