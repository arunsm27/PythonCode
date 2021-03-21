#Author: ARUN S
#This program removes bin and obj files created after Xamarin compilation.
#This file (remove_bin_obj.py) will be in Tools folder which is available after cloning.
#Except Tools other folders (below) are created by Visual Studio.
#The directory structure for this tool to work is
#SolName
#SolName.Android
#SolName.iOS
#Tools
#SolName.sln
      
# importing os module   
import os
import shutil

#Go one level up from Tools Folder. This has a view on all folders containing
#bin and obj file.
TopView = os.path.dirname(os.getcwd())

for f_name in os.listdir(TopView):
    if f_name.endswith('.sln'):
      ProjectName = f_name
      break
          
print ("Solution Name is %s" % ProjectName)
root, ext = os.path.splitext(ProjectName) 
ProjectName = root

#########To delete the directory obj\bin in folder of project files.

path = os.path.join(TopView + "\\" + ProjectName, "obj")
shutil.rmtree(path, ignore_errors=True)

path = os.path.join(TopView + "\\" + ProjectName, "bin")
shutil.rmtree(path, ignore_errors=True)
print ("Removed bin and obj files in %s folder."% ProjectName)

########To delete the directory obj\bin in folder of Android project folder.

path = os.path.join(TopView + "\\" + ProjectName + ".Android", "obj")
shutil.rmtree(path, ignore_errors=True)

path = os.path.join(TopView + "\\" + ProjectName + ".Android", "bin")
shutil.rmtree(path, ignore_errors=True)
print ("Removed bin and obj files in %s Android folder" % ProjectName)

########To delete the directory obj\bin in folder of iOS project folder.

path = os.path.join(TopView + "\\" + ProjectName + ".iOS", "obj")
shutil.rmtree(path, ignore_errors=True)

path = os.path.join(TopView + "\\" + ProjectName + ".iOS", "bin")
shutil.rmtree(path, ignore_errors=True)
print ("Removed bin and obj files in %s iOS folder" % ProjectName)

########To delete the directory obj\bin in folder of iOS project folder.

path = os.path.join(TopView + "\\" + ProjectName + ".iOS", "obj")
shutil.rmtree(path, ignore_errors=True)

path = os.path.join(TopView + "\\" + ProjectName + ".iOS", "bin")
shutil.rmtree(path, ignore_errors=True)
print ("Removed bin and obj files in %s iOS folder" % ProjectName)


