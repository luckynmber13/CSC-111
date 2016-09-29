#Program: HW2.py
#Author: Thomas M. Queenan
#Class: CSC 111
#Instructor: V Manes
#Due: 9/12/16
#Written: 9/7/16

#Solves the number of rice grains found on a chessbord if the amount doubles each tile

#calc grains
#calc tons based off grains
#calc cars based off tons
#calc miles based off cars
#disp information

#Function: Main, calculates rice grains
#Author: Thomas M. Queenan

def main():
    #Calculate values

    grains = 2**64 - 1 #grains in a 8*8 square
    tons = grains // 32000000 #grains to tons
    cars = tons // 100 #tons to cars
    miles = (cars * 65)// 5280 #cars to miles


    #Print output

    print("The number of grains is: " + '%.4e' % grains)
    print("The number of tons is: " + '%.4e' % tons)
    print("The number of traincars will be: " + '%.4e' % cars)
    print("The length of the train will be: " + '%.4e' % miles)

if __name__ == '__main__':
    main()
