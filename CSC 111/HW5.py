'''
Program:  HW5.py
Author:  Thomas M. Queenan
Class:   CSC 111
Instructor:  V Manes
Due:     3/10/16
Written  28/9/16

Program description: Tests to see if a sphere can be fit in a cube

Program usage: <any special instructions>
'''

# Import statements go here
import math

# Constant declarations go here
PI = math.pi



#be sure to comment the code enough, but not too much
#there should be a comment for every group of lines that do a
#related task. The comment should be very brief


#YOU MUST HAVE A FUNCTION main( )
'''
Function:  Main
Author:  Thomas M. Queenan
Function description:  Calcs if a sphere can fit in a cube based off of user input

Parameters: none

Return: <describe return value,if any>
'''
def main( ):

    #variable declarations
    volume = float(input("What is the volume?: "))
    sideLength = float(input("What is the length of the side of your cube:? "))
    
    #Calcualtion
    radius = pow((3*((volume)/(4*PI))), (1/3))
    diameter = 2 * radius
    
    #formating
    fit = 1 - (diameter / sideLength)

    #Ifs    
    if (math.fabs(fit) <= .01):
        print("Perfect fit!")
    elif (fit <= .15) and (fit > 0):
        print("Loose fit.")
    elif (fit > .15):
        print("Bouncing.")
    elif (volume <= sideLength**3):
        print("Modified fit.")
    else:
        print("Cannot fit.")
    #
    

#DO NOT DELETE THESE LINES, THEY MUST BE LAST LINES IN FILE           
if __name__ == '__main__':
   main()
