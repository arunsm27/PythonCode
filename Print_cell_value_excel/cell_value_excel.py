#include <stdio.h> //legacy C coding habit.
#To open a python excel sheet, and navigate to sheet called TOTAL.
#Open cell in column D and row 18. Print the value existing in the cell.

import os

x1 = os.getcwd()
print (x1)

from openpyxl import load_workbook
wb = load_workbook(filename = 'x1.xlsx')
sheet_ranges = wb['TOTAL']
val = sheet_ranges['D18'].value
print (val)


