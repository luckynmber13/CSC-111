'''
Program:  LAB5.py
Author:  Thomas M. Queenan
Class:   CSC 111
Instructor:  V Manes
Due:     9/26/16
Written  9/26/16

Program description: Earth defense program almost...

Program usage: <any special instructions>
'''

# Import statements go here
import math
import random

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
    random.seed(0)
    vectorPosAix = random.randint(-20, 20)
    random.seed(0)
    vectorPosAiy = random.randint(1, 20)
    
    #function body
    print('Space Defender')
    print('Invading ship is at ({0}, {1})'.format(vectorPosAix, vectorPosAiy))
    
    angle = float(input('Shot angle (180 - 0): '))
    if angle > 180: # too large
        print('You are shooting the ground to the left')
        return # end
    elif angle < 0: # too small
        print('You are shooting the ground to the right')
        return # end
    
    range = float(input('Shot range ( 1 to 30 ): '))
    if ((range > 30) or (range < 1)): # out of range
        print('Your cannon explodes!')
        return # end
    
    #calc: Shot position
    radians = math.radians(angle)
    vectorShotx = range * math.cos( radians )
    vectorShoty = range * math.sin( radians )
    
    #print: Shot position
    print('Shot at ({0:.1f}, {1:.1f})'.format(vectorShotx, vectorShoty))
    
    #hit detect
    if (math.fabs(vectorShotx - vectorPosAix) <= 1): #x dimention
        if (math.fabs(vectorShoty - vectorPosAiy) <= 1): #y dimention
            print('You destoyed the enimy ship')
        elif (vectorShoty - vectorPosAiy >= -2) and (vectorShoty - vectorPosAiy <= -1): #y 2 before
            print('You dammaged the enemy ship!')
        else: #y miss
            print('You just missed!')
    else: #x miss
        print('You missed!')
    return #close
    
#DO NOT DELETE THESE LINES, THEY MUST BE LAST LINES IN FILE           
if __name__ == '__main__':
   main()
