# Thomas Queenan

# Prime generator

import math
import sys

# Is prime function (returns bool)
def isPrime( i, nums):
    root = math.sqrt(i) #Root of number
    for index in nums: #Repeat through primes list
        if (i % index == 0): #If evenly divisible by previous prime then...
            return False
    return True



# Main Function

primeMax = 100000 #Numbers up to...
Prime = False #is or is not prime
nums = [] #primes list
nums.insert(1,2) #pre-load 2
pIndex = 1

for i in range( 3, primeMax, 2): #Find primes under (primeMax)
    Prime = isPrime( i, nums) #isPrime Func
    if (Prime): #If true stick it in the index
        nums.append(i) #Prime added to prime list

print(nums) #display array
input("Press enter to continue")
