#Create 30 directory with name tmr_0830_x inside a folder. x represents the
#number of the folder. Inside each directory add a .c file with the same
#name as directory. On executing this script the following directories
#would be visible in the main directory.
#tmr_0831_1
#tmr_0831_2
#tmr_0831_3
#tmr_0831_4
#tmr_0831_5
#............................

import os 
  
# Directory 
directory = "tmr_0831"
  
# Parent Directory path 
parent_dir = os.getcwd()
  
# Path 
path = os.path.join(parent_dir, directory) 
  
for x in range (1, 31):
    path = os.path.join(parent_dir, directory + "_" + "{}".format(x))
    os.mkdir(path)
print("% d Directory '% s' created" % (x, directory))





