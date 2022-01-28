#include <stdio.h> //legacy C coding habits.

#Forming a hex number using dictionary.
#A dictionary hexValueDict is defined which holds the
#the bit values for a hex number.
#The dictionary values are accessed using key to form a value.

hexValueDict = {
                    'SEVENTH_BIT'   : 0,   #128
                    'SIXTH_BIT'     : 0,   #64
                    'FIFTH_BIT'     : 0,   #32
                    'FOURTH_BIT'    : 0,   #16
                    'THIRD_BIT'     : 0,   #8
                    'SECOND_BIT'    : 0,   #4
                    'FIRST_BIT'     : 0,   #2
                    'ZERO_BIT'      : 1    #1
               }

x = 1
print ("Value of x is %d" %x)

print ("Value of one left shift on x is %d" %(hexValueDict['ZERO_BIT'] << 1))
print ("Value of two left shift on x is %d" %(hexValueDict['ZERO_BIT'] << 3))
print ("Value of zero left shift on x is %d" %(hexValueDict['ZERO_BIT'] << 0))

a = ((hexValueDict['ZERO_BIT'] << 1) + (hexValueDict['ZERO_BIT'] << 3) + (hexValueDict['ZERO_BIT'] << 0))
y = ((hexValueDict['ZERO_BIT'] << 1) | (hexValueDict['ZERO_BIT'] << 3) | (hexValueDict['ZERO_BIT'] << 0)) 

print ("Plus operation: Value of a is %d" %a)
print ("Logical OR Operation: Value of y is %d" %y)

#-------------------------------------------------------------------------------------------------------------
#Output
#Value of x is 

# 1
#Value of one shift is 

# 2
#Value of two shift is 

# 8
#Value of two shift is 

# 1
#Value of a is 

# 11
#Value of y is 

# 11
#-------------------------------------------------------------------------------------------------------------
