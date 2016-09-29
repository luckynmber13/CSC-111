'''
Program:  LAB4.py
Author:  Thomas M. Queenan
Class:   CSC 111
Instructor:  V Manes
Due:     9/19/16
Written  9/19/16

Program description: Orbital Calcualtor

Program usage: <any special instructions>
'''

# Import statements go here
import math

# Conversion ratios
ConvMToM = 1.6093 * 1000 #miles to kilometers conversion

# Constant declarations go here
GravConstant = 6.6726e-11 #declare gravity (Nm^2/Kg^2)
MassPlanet = 5.972e24 #declare planitary mass (Kg)
MassOrbital = 0 #declare orbiting mass (Kg)
RadiusPlanet = (7917 / 2) * (ConvMToM)#declare radius of the planet (KM)

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

    #math
    tAltitude = altitude + RadiusPlanet
    timeSec = math.sqrt( ( (4 * math.pi**2) / ( GravConstant * ( MassPlanet + MassOrbital ) ) ) * ( tAltitude ** 3 ) )

    #formating
    timeMin = timeSec / 60

    #display
    print("The orbital period will be about ", round(timeMin,1), " minutes.")

#DO NOT DELETE THESE LINES, THEY MUST BE LAST LINES IN FILE           
if __name__ == '__main__':
   main()
