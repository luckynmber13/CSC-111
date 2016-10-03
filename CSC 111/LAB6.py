'''
Program:  LAB6.py
Author:  Thomas M. Queenan
Class:   CSC 111
Instructor:  V Manes
Due:     10/3/16
Written  10/3/16

Program description: plays the game Arcturian darts

Program usage: <any special instructions>
'''

# Import statements go here
import math

#be sure to comment the code enough, but not too much
#there should be a comment for every group of lines that do a
#related task. The comment should be very brief


#YOU MUST HAVE A FUNCTION main( )
'''
Function:  Main
Author:  Thomas M. Queenan
Function description:  Gives scores for Arcturian darts

Parameters: none

Return: <describe return value,if any>
'''
def main( ):

    #variable declarations
    p1 = [0,0]
    p2 = [0,0]
    lSquare = [0,0]
    safeRect = [0,0]
    
    #Input
    print ("Player 1 up!")
    p1[0] = abs(inputInt("Player 1 x: "))
    p1[1] = abs(inputInt("player 1 y: "))
    
    print("\nPlayer 2 up")
    print("Shooting for ({0[0]},{0[1]})".format(p1))
    p2[0] = abs(inputInt("Player 2 x: "))
    p2[1] = abs(inputInt("player 2 y: "))

    #Collision calc 
    lSquare[0],lSquare[1] = p1[0]-p2[0],p1[1]-p2[1]
    
    #Claculates Largest posible safe rectangle
    if (p1[0] > p1[1]) or (p2[0] > p2[1]): #if x's are greater than y's
        if (p1[0] > p2[0]): #p1 x is larger
            safeRect[0] = p1[0] * (2/3)
            safeRect[1] = p1[1] * (3/2)
        else: #p2 x is larger
            safeRect[0] = p2[0] * (2/3)
            safeRect[1] = p2[1] * (3/2)
    else: # if y's are larger than x's
        if (p1[1] > p2[1]): #p1 x is larger
            safeRect[0] = p1[1] * (2/3)
            safeRect[1] = p1[0] * (3/2)
        else: #p2 x is larger
            safeRect[0] = p2[1] * (2/3)
            safeRect[1] = p2[0] * (3/2)
    #end
    
    #format values due to???
    safeRect[0], safeRect[1] = round(safeRect[0],0), round(safeRect[1],0)
    
    #debug
    #print(safeRect)
    
    if (p1 == p2): #same point
        print("Player 2 scores a direct hit! 50 points")
    elif (lSquare[0] == lSquare[1]): #perfect square
        print("Player 2 hit on square, 40 points, 1 gets 10")
    elif (p1[0] == p2[0]) or (p1[1] == p2[1]): #line
        print("Player 2 hit on line, 20 points, 1 gets 30")
    elif (abs(lSquare[0]) <= abs(safeRect[0])) and (abs(lSquare[1]) <= abs(safeRect[1])): #rect 3:2
        print("Player 2 hit in safe rectangle, 30 points, 1 gets 20")
    elif (abs(lSquare[0]) <= abs(safeRect[1])) and (abs(lSquare[1]) <= abs(safeRect[0])): #rect 2:3
        print("Player 2 hit in safe rectangle, 30 points, 1 gets 20")
    else: #miss
        print("Player 2 misses, 0 points, 1 gets 50")
    #end If
    
    
#OTHER FUNCTIONS ARE OPTIONAL, BASED ON PROGRAM NEED
#(Delete this section if not used)
'''
Function:  inputStr
Author:  Thomas M. Queenan
Function description:  Safe input

Parameters: Display

Return: String or "<<>>_Error_<<>>"
'''
def inputStr(Display):
    try:
        return  input(Display)
    except BaseException:
        return "<<>>_Error_<<>>"
#

'''
Function:  inputInt
Author:  Thomas M. Queenan
Function description:  Safe int input

Parameters: Display

Return: Int or "<<>>_Error_<<>>"
'''
def inputInt(Display):
    str = inputStr(Display)
    try:
        return  int(str)
    except BaseException:
        return "<<>>_Error_<<>>"
#
   
#DO NOT DELETE THESE LINES, THEY MUST BE LAST LINES IN FILE           
if __name__ == '__main__':
   main()
