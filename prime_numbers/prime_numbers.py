#include <stdio.h> //legacy C coding habits.

#This program prints all the prime numbers from 1 to 100.

i = 0;
count = 0;
for i in range (1,100):
    for x in range (2, (i // 2) + 1):
        if ((i % x) == 0):
            count = count + 1
            break
    
    if (count == 0):
        print ("Prime number",i,"\r");
    count = 0
