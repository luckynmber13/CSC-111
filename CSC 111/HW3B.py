'''
Program:  HW3B.py
Author:  Thomas M. Queenan
Class:   CSC 111
Instructor:  V Manes
Due:     9/19/16
Written  9/14/16

Program description: <what it does, how it does it. Briefly>

Program usage: <any special instructions>
'''

# Import statements go here

# Constant declarations go here

#be sure to comment the code enough, but not too much
#there should be a comment for every group of lines that do a
#related task. The comment should be very brief

#YOU MUST HAVE A FUNCTION main( )
'''
Function:  Main
Author:  Thomas M. Queenan
Function description: angle adder

Parameters: none

Return: <describe return value,if any>
'''
def main( ):

    #variable declarations

    #function body
    #sets angle 1
    angle1Deg = int(input("First Angle - degrees: "))
    angle1Min = int(input("First Angle - minutes: "))
    angle1Sec = int(input("First Angle - seconds: "))

    #sets angle 2
    angle2Deg = int(input("Second Angle - degrees: "))
    angle2Min = int(input("Second Angle - minutes: "))
    angle2Sec = int(input("Second Angle - seconds: "))

    #sets angle 3
    angle3Deg = angle1Deg + angle2Deg
    angle3Min = angle1Min + angle2Min
    angle3Sec = angle1Sec + angle2Sec

    #formats angle 3
    if (angle3Sec >= 60):
        angle3Min += angle3Sec // 60
        angle3Sec -= (angle3Sec // 60) * 60
    if (angle3Min >= 60):
        angle3Deg += angle3Min // 60
        angle3Min -= (angle3Min // 60) * 60

    #prints angle 3
    print( "%d" % angle3Deg + u"\u00b0" + "%d\"%d'" % ( angle3Min, angle3Sec ))    

#DO NOT DELETE THESE LINES, THEY MUST BE LAST LINES IN FILE           
if __name__ == '__main__':
   main()
