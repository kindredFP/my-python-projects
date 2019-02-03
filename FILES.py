import os

print("***")
print("A way to append folders " + os.path.join("mainFolder", "subFolder", "myfile.jpg") + "\n")

# get current working directory
print("Current  DIR " + os.getcwd() + "\n")

# change director
os.chdir("/Volumes/Storage/fpalattao/Documents/Dropbox/gitRepository/gitLabRepos/my-python-projects/resourceFiles")
print("Current  DIR after chdir function call " + os.getcwd() + "\n")

# convert relative path to an absolute one
print("Calling the abspath function " + os.path.abspath("myTestfile"))

# boolean to check if path exists
print("if path exist function = " + str(os.path.exists(
    "/Volumes/Storage/fpalattao/Documents/Dropbox/gitRepository/gitLabRepos/my-python-projects/NonExisting")))

# is file/dir exist
print("isFile() = " + str(os.path.isfile(
    "/Volumes/Storage/fpalattao/Documents/Dropbox/gitRepository/gitLabRepos/my-python-projects/FILES.py"))
      + " isDir() = " + str(
    os.path.isdir("/Volumes/Storage/fpalattao/Documents/Dropbox/gitRepository/gitLabRepos/my-python-projects")))

# list directory
os.chdir("/Volumes/Storage/fpalattao/Documents/Dropbox/gitRepository/gitLabRepos/my-python-projects/")
print(os.listdir(os.getcwd()))

# make a directory test on current working directory
# os.makedirs(os.getcwd() + "//test")
