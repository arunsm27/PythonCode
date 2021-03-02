#Author: Arun
#Copy a file from one folder to another. Place this file in source folder.

import os
import shutil

dir_src = "D:\\source_folder\\"       #source directory. e.g  D:\\source_folder\\
dir_dst = "D:\\destination_folder\\"  #destination directory. D:\\destination_folder\\

for filename in os.listdir(dir_src)
       if filename.endswith('.qaz'):               #search for filename with extension .qaz to transfer files.
              shutil.copy(dir_src + filename, dir_dst)
                           

