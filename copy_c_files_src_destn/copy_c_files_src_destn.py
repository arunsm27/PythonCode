#Author: Arun
#Given a folder containing different types of files.
#Group all files based on their extension (e.g *.pdf,*.c, *.docx)
#in their respective directories.

import os
import shutil
import glob

ProjectName = 'test'

TopView = os.getcwd()
print ("TopView %s",TopView)

# Path
directory = "c_source"
dest_folder = os.path.join(TopView, directory)
if not os.path.exists(dest_folder):
       os.mkdir(dest_folder) 
for filename in glob.glob(os.path.join(TopView, '*.c')):
    shutil.move(filename, dest_folder)

directory = "pdf_docs"
dest_folder = os.path.join(TopView, directory)
if not os.path.exists(dest_folder):
       os.mkdir(dest_folder)
for filename in glob.glob(os.path.join(TopView, '*.pdf')):
    shutil.move(filename, dest_folder)

directory = "wordx_docs"
dest_folder = os.path.join(TopView, directory)
if not os.path.exists(dest_folder):
       os.mkdir(dest_folder) 
for filename in glob.glob(os.path.join(TopView, '*.docx')):
    shutil.move(filename, dest_folder)

directory = "text_docs"
dest_folder = os.path.join(TopView, directory)
if not os.path.exists(dest_folder):
       os.mkdir(dest_folder) 
for filename in glob.glob(os.path.join(TopView, '*.txt')):
    shutil.move(filename, dest_folder)

directory = "odt_docs"
dest_folder = os.path.join(TopView, directory)
if not os.path.exists(dest_folder):
       os.mkdir(dest_folder) 
for filename in glob.glob(os.path.join(TopView, '*.odt')):
    shutil.move(filename, dest_folder)     

directory = "junk_docs"
dest_folder = os.path.join(TopView, directory)
if not os.path.exists(dest_folder):
       os.mkdir(dest_folder) 
for filename in glob.glob(os.path.join(TopView, '*.*')):
    shutil.move(filename, dest_folder)     

