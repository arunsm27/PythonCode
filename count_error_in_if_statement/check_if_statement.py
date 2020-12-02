#Author: ARUN S
#This program searches for a pattern if( in a file and gives the line number.
#The file to be analysed needs to be along with the python script.

import os
import re

substring = "if("
line_no = 1                
with open('myfile.txt') as file1:
    for line in file1:
        line_no+=1
        if substring in line:
           print (line,line_no)
        
            

file1.close()








