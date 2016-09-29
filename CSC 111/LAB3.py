'''
Program:  LAB3.py
Author:  Thomas M. Queenan
Class:   CSC 111
Instructor:  V Manes
Due:     9/12/16
Written  9/12/16

Program description: Food calcuator
'''

# Import statements go here
import math

# Constant declarations go here
partPizza = 8 #slices
partBottle = 64 #oz.
servPizza = 3 #slices
servBottle = 12 #oz.

#be sure to comment the code enough, but not too much
#there should be a comment for every group of lines that do a
#related task. The comment should be very brief


#YOU MUST HAVE A FUNCTION main( )
'''
Function:  main()
Author:  Thomas M. Queenan
Function description:  food calcualator

Parameters: <list inputs>

Return: <describe return value,if any>
'''
def main( ):

    #variable declarations

    #neededBottle
    #neededPizza

    #pizza
    #bottle

    #function body
    print("Serving Ammount Calculator")
    pop = int(input("How many people? ")) # population of people

    neededPizza = pop * servPizza
    neededBottle = pop * servBottle

    pizza = math.ceil(neededPizza / partPizza) #calc pizzas
    bottle = math.ceil(neededBottle / partBottle) #calc bottles

    print("For ", pop, " you will need ", pizza, " pizzas and ",  bottle, " bottles of soda.")

    #Part B

    print('\n')
    print("Slices and Oz. Per person Calcualation")

    pop = int(input("How many people? "))
    pizza = int(input("How many pizzas? "))
    bottle = int(input("How many bottles? "))

    totalPizza = pizza * partPizza #calc total peices
    totalBottle = bottle * partBottle #calc total oz.

    partPizzaInt = totalPizza // pop
    partBottleInt = totalBottle // pop

    partPizzaFrac = totalPizza % pop
    partBottleFrac = totalBottle % pop

    print("Each person gets ", partPizzaInt, "slices and ", partBottleInt, "ounces of soda.")
    print("There will be ", partPizzaFrac, "slices and ", partBottleFrac, "ounces of soda extra.")
    
        
#DO NOT DELETE THESE LINES, THEY MUST BE LAST LINES IN FILE           
if __name__ == '__main__':
   main()
