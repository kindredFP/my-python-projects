import os

#change directory to resourcefiles and traverse there
os.chdir(os.getcwd() + "//resourceFiles")

for folderName, subfolders, filenames in os.walk(os.getcwd()):
                 print('The current folder is ' + folderName)
                 for subfolder in subfolders:
                     print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
                     print()


for filename in filenames:
                     print('FILE INSIDE ' + folderName + ': '+ filename)
print('')
