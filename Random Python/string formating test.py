nums = [0,1,2,3,4,5,6,7,8,9]

#basic formating...
print('{} {}'.format('one','two')) # out>> one two

#more...
print('{} {}'.format(1,2)) #out>> 1 2

#Ordering
print('{1} {0}'.format('one','two')) #out>> two one

#formating
'{0!s} {0!r}'.format(Data()) #out>> str repr

#padding
'{:[char][operator][ammount]}'.format(var)
    #operators
        #> align left
        #  align right
        #^ align center

#truncating
'{:.5}'.format(var)

#padding + truncating
'{:[char][operator][ammount].[trunc]}'.format(var)

#Numbers
'{:d}'.format(var)
'{:f}'.format(var)

#padding numbers
'{:[amount]d}'.format(var)
'{:[amount]f}'.format(var)

#precision
'{:[padding].[percision]f}'.format(var)

#signs
'{:[sign]d}'.format(var)
    #signs
        #+
        #-

#spacing
'{: d}'.format(var) #out>> -num or _num
'{: f}'.format(var)

#padding sign
'{:=[ammount]d}.format(var)
'{:=[ammount]f}.format(var)

#named placeholders
data = {'first': 'hodor', 'last': 'hodor!'}
'{first} {last}'.format(**data)
'{first} {last}'.format(first = 'hodor', last = 'hodor!')

#getitem and getattr
data = {'first': 'hodor', 'last': 'hodor!'}
'{p[first]} {p[last]}'.format(p=data)

#lists
nums = [0,1,2,3,4,5,6,7,8,9]
'{d[4]} {d[5]}'format(d=nums)

#properties
plant = {}
plant.type = 'tree'
'{p.type}'.format(p=plant)
...

#date time
'{:%Y-%m-%d %H:%M}'.format(datetime(2001,2,3,4,5))

#parameters in formating
'{:{align}{width}}'.format('test', align='^', width='10')
etc...