'''
Thomas Queenan
Graph software (ish)
started: 10/3/16
ended: ??/??/??
'''

#imports
import math

###
'''
Common functionsBaseException
'''
###

def inputStr(Display):
    #inital
    try:
        return input(Display)
    except BaseException:
        return "<<>>_Error_<<>>"
#end

def inputFloat(Display):
    #inital
    str = inputStr(Display)
    try:
        return float(str)
    except BaseException:
        return "<<>>_Error_<<>>"
#end

def inputInt(Display):
    #inital
    str = inputStr(Display)
    try:
        return int(str)
    except BaseException:
        return "<<>>_Error_<<>>"
#end

def toFloat(Str):
    #inital
    try:
        return float(Str)
    except BaseException:
        return "<<>>_Error_<<>>"
#end

def toInt(Str):
    #inital
    try:
        return int(Str)
    except BaseException:
        return "<<>>_Error_<<>>"
#end

def sum(list, start, end):
    #inital
    sum = 0
    for i in range(start, end):
        sum += list[i]
    #end For
    
    return sum
#end

###
'''
Sub Functions
'''
###

def parseString(Str):
    #inital
    
#end

def parseXString(Str):
    #inital
    
#end

def parseYString(Str):
    #inital
    
#end

def parseEmptyParams(Str):
    #inital
    
#end

def findParamGroups(Str):
    #inital
    length = len(Str)
    params[length] = []
    parts = []
    
    #change params to values for easy math
    for i in range(0,length):
        char = Str[i]
        if char == '(':
            params[i] = 1
        elif char == ')':
            params[i] = -1
        #end If
    #end For
    
    #find sets of params
    for i in range(0,length):
        charStart = Str[i]
        if charStart:
            for j in range(i+1,length):
                if not(sum(params,i,j)):
                    # seperate string into peices
                    
                    break #bad but needed
                #end If
            #end For
        #end If
    #end For
    
#end

###
'''
Main function
Thomas Queenan
'''
###

def main():
    #intial
    
#end


###
'''
Start Function
Thomas Queenan
'''
###

if __name__ == '__main__':
    main()