#Author: ARUN S
#This program searches for a pattern if( in a file and gives the line number.
#The file to be analysed needs to be along with the python script.

import os
import re
a = []
substring = "if("
line_no = 1                
with open('myfile.txt') as file1:
    for line in file1:
        line_no+=1
        out_number = ''
        for ele in line:
            if (ele == '.' and '.' not in out_number) or ele.isdigit():
                out_number += ele
                print(line_no)
            elif out_number:
                break
                
        
            

file1.close()








