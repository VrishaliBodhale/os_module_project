import os

# os module and frequently used methods

# Our project
# Select similar files from a folder. Cut and paste them to

print(os.name)
print(os.sep)
print(os.uname())

# make new folder
#os.makedirs("new folder")

#get current working directory
print(os.getcwd())
current_folder=os.getcwd()

print(os.walk(current_folder))
for root,dirs,files in os.walk(current_folder):
    print(files)

print("--------------------------------------------------------------------------------------------")

print(os.getcwd())

if not (os.path.exists("new_folder")):
    os.makedirs("new_folder")
    os.chdir("new_folder")
    print(os.getcwd())
else:
    print("new_folder exists already. so not created again")

file_name=os.path.join(os.getcwd(), "Fremont Societies.txt")
print(os.path.split(file_name))
print(os.path.splitext(file_name))

os.chdir("new_folder")

with open("Fremont Societies.txt", "w") as f:
    f.write("SOCIETIES IN FREMONT: ")
    f.write("1. The presidio\n2.Water stone")
f.close()

os.remove("Fremont Societies.txt")





