import shutil, os

fileNameSource = "copyingFile.txt"
folderDestination = "targetLocation"
folderDestinationAndNewName = "targetLocation//newName.txt"
newFolderName = 'targetLocationBackup'
sourceMoveFile = 'movingFile.txt'
targetMovedFile = 'targetLocation//movingFile.txt'

# Change directory to resourceFiles subfolder
os.chdir(os.getcwd() + "//resourceFiles")

myFileObject = open(fileNameSource, "w")
myFileObject.write("We will copy this file")
myFileObject.close()

# copy to folderDestination folder
shutil.copy(fileNameSource, folderDestination)

# copy and rename
shutil.copy(fileNameSource, folderDestinationAndNewName)

# delete a full folder if it exists - this handles the case when I have already created the folder
shutil.rmtree(newFolderName)

# delete a file if it exists already
os.unlink(targetMovedFile)

# copy a full folder
shutil.copytree(folderDestination, newFolderName)

# create then move the file
myFileObject = open(sourceMoveFile, "w")
myFileObject.write("We will move this file")
myFileObject.close()

shutil.move(sourceMoveFile, targetMovedFile)
print(os.getcwd())
