import os
print(os.system("ls -l")) # to run a system command through python
print(os.getcwd()) # used to get the current working directory
print(os.listdir()) # to list the items in the current directory
print(os.chdir())  # to change the directory
print(os.listdir("/dev")) # to list the content of a direcorty
os.mkdir("testingforthemakingdir") # to create a directory
os.makedirs("/dev/testingforthemaking") # to make create a recurrisive directory
os.rmdir("testingforthemakingdir") # to remove a directory
print(os.getuid()) # to get user id
print(os.getgid()) # to get group id
os.removedirs("/dev/testingforthemakingdir") # to remove the direcorties
os.rename("last name","new name") # to rename a directory
print(os.path.exists("/os-module.py")) # to check the exsitence od a file ina folder
print(os.path.isdir("/python-for-devops")) # to check whether it is directory or not
print(os.path.isfile("/os-module")) # to check whether it is file or not
print(os.path.getsize("os-module.py")) # to get the size of the file
print(os.path.basename("/OS-Module/os-module")) # to get the base name
print(os.path.dirname("/OS-Module/os-module")) # to get dir name
os.path.join("path1","path2") # to join two paths
#print(list(os.walk("/dev"))) to get all the dir and files in a directory (the whole tree)