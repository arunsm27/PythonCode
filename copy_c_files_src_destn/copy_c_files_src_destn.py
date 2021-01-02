import os
import shutil
import glob

ProjectName = 'test'

TopView = os.getcwd()
print ("TopView %s",TopView)

# Directory 
directory = "c_source"
  
# Path 
path = os.path.join(TopView, directory)
os.mkdir(path) 

for filename in glob.glob(os.path.join(TopView, '*.c')):
    shutil.copy(filename, dest_folder)


