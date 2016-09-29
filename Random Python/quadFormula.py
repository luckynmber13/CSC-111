import math

def quadFormula(a,b,c):
	#(-b+-sqrt(b**2 - 4*a*c))/(2*a)
	topLeft = -b
	topRight = b**2 - (4*a*c)
	bottom = 2*a
	return "{} sqrt( {}) / {}".format(topLeft, topRight, bottom)

#main
#a = float(input("a: "))

chars = "0123456789ABCDEF"

#for x in range(0,16):
#    for y in range(0,16):
#        for z in range(0,16):
#            for w in range(0,16):
#                print(chr(chars[x] + chars[y] + chars[z] + chars[w]), '\\u{}{}{}{}'.format(chars[x], chars[y], chars[z], chars[w]))
#

for x in range(0,100000):
    try:
        print(chr(x), " charachter: {}".format(x))
    except:
        i=x









#^0 = 2070
#^1 = 00B9
#^2 = 00B2
#^3 = 00B3
#^4 = 2074
#^5 = 2075
#^6 = 2076
#^7 = 2077
#^8 = 2078
#^9 = 2079

# SUPER_SCRIPT = "\u2070" + "\u00B9" + "\u00B2" + "\u00B3" + "\u2074" + "\u2075" + "\u2076" + "\u2077" + "\u2078" + "\u2079"

def toSuperScript(string):
	output = ""
	for char in string:
		index = int(char)
		newChar = SUPER_SCRIPT[index]
		output = "{}{}".format(output, newChar)
	return output
	
# print(toSuperScript("12"))