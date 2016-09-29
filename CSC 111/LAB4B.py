'''
Program:  LAB4.py
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

# Conversion ratios
ConvMToM = 1.6093 * 1000 #miles to kilometers conversion

# Constant declarations go here
GravConstant = 6.6726e-11 

#be sure to comment the code enough, but not too much
#there should be a comment for every group of lines that do a
#related task. The comment should be very brief


#YOU MUST HAVE A FUNCTION main( )
'''
Function:  Main
Author:  Thomas M. Queenan
Function description:  Main input and math

Parameters: none

Return: <describe return value,if any>
'''
def main( ):

    #variable declarations
    

    #function body
    #inputs
    print("Orbital calculator \nCalculates the period of a satalite around a planet.")
    altitude = float(input("Altitude of orbiting object in miles: ")) * ConvMToM
    MassPlanet = float(input("Planetary Mass (Kg): "))
    MassOrbital = float(input("Orbital's Mass (Kg): "))
    RadiusPlanet = (float(input("Planetary Radius (Miles): "))) * (ConvMToM)




    #math
    tAltitude = altitude + RadiusPlanet
    timeSec = math.sqrt( ( (4 * math.pi**2) / ( GravConstant * ( MassPlanet + MassOrbital ) ) ) * ( tAltitude ** 3 ) )

    #formating
    timeMin = timeSec / 60

    #display
    print("The orbital period will be about ", round(timeMin,1), " minutes.")

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
