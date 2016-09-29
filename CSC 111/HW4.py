'''
Program:  HW4.py
Author:  Thomas M. Queenan
Class:   CSC 111
Instructor:  V Manes
Due:     27/9/16
Written  27/9/16

Program description: price claculator

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
Function description:  <brief description>

Parameters: none

Return: <describe return value,if any>
'''
def main( ):

    #variable declarations
    rate = 0
    
    #function body
    print('Hardrocker Insurance Calculator')
    gender = input('Gender? (m or f): ')
    relation = input('Marital status? (s or m): ')
    age = int(input('Age: '))
    base = float(input('Policy base rate: $'))
    
    if (relation == 'm'):
        if (gender == 'f'):
            rate = .25
        elif (gender == 'm'):
            rate = .2
    elif (relation == 's'):
        if (age > 25) & (gender == 'm'):
            rate = .15
        elif (age > 20) & (gender == 'f'):
            rate = .15
    else:
        rate = 0
    #end if
    
    print("You recived a discount of ${0:.2f}, making your total prenium ${1:.2f}".format(rate * base, base - (rate * base)))
#end main


#DO NOT DELETE THESE LINES, THEY MUST BE LAST LINES IN FILE           
if __name__ == '__main__':
   main()
