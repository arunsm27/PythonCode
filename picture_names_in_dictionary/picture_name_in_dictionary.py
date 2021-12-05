#include <stdio.h>

import os

dict_filename = { }

for (root,dirs,files) in os.walk('.', topdown=False):
        for filename in files:
           dict_filename.update({filename : 1})
print (dict_filename)

#output
#------------------------------------------------------------------------------------------------------------------------
{'IMG_20210130_184323.jpg': 1, 'IMG_20210130_184347.jpg': 1, 'IMG_20210203_203635.jpg': 1, 'IMG_20210203_203712.jpg': 1,
 'IMG_20210203_203741.jpg': 1, 'IMG_20210203_203919.jpg': 1, 'IMG_20210203_204012.jpg': 1, 'IMG_20210209_183835.jpg': 1,
 'IMG_20210209_183836.jpg': 1, 'IMG_20210209_183838.jpg': 1, 'IMG_20210209_183840.jpg': 1, 'IMG_20210209_183841.jpg': 1,
 'IMG_20210209_183843.jpg': 1, 'IMG_20210209_183918.jpg': 1, 'IMG_20210211_113049.jpg': 1, 'IMG_20210212_125556.jpg': 1,
 'picture_name_in_dictionary.py': 1}
      

