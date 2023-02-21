import os
import shutil
import time

# step 1 : Check input validity
# step 2 : Create destination folder
# step 3 : Gather unique extensions and create directories
# step 4 : Copy files to extension directories

# # step 1 : Get input and check input validity


def createDestinationFolder(dest_folder):
    os.chdir(dest_folder)
    dest_folder = dest_folder + "/" + "File_Management"
    print(dest_folder)
    try:
        if os.path.exists(dest_folder):
            dest_folder_cp = dest_folder + "_" + str(time.time())
            os.rename(dest_folder, dest_folder_cp)
            print("*** Renamed existing " + dest_folder + " To " + dest_folder_cp)
            os.mkdir(dest_folder)
            print("Created: " + dest_folder)
        else:
            os.mkdir(dest_folder)
            print("Created: " + dest_folder)
    except Exception as e:
        print("Exception : " + e)
    return dest_folder


def getUniqExtensions(source_folder):
    os.chdir(source_folder)
    # print(os.listdir())
    extensions = []
    for file in os.listdir(source_folder):
        print(file)
        if not os.path.isdir(file):
            ext = os.path.splitext(file)[-1]
            ext = ext[1:]
            if ext:
                extensions.append(ext)
                print(extensions)

    uniq_extensions = set(extensions)
    print(uniq_extensions)
    return uniq_extensions


def getSourceAndDestinationDirectory():
    print("This program will sort your files from the source folder and copy them to the destination folder.")
    print("Find your files in a newly created folder - File_Management, inside a destinaiton folder")

    source_folder= input("Enter a source folder: ")
    #source_folder="/Users/Vrish/Downloads"
    print("Source folder=" + source_folder)
    if not os.path.exists(source_folder):
        print("ERROR: Invalid source path")
        exit(0)

    dest_folder=input("Enter a destination folder: ")
    #dest_folder="/Users/Vrish/Downloads"
    print("Destination folder=" + dest_folder)
    if not os.path.exists(dest_folder):
        print("ERROR: Invalid destination path")
        exit(0)
    return (source_folder,dest_folder)

source_folder,dest_folder = getSourceAndDestinationDirectory()

dest_folder=createDestinationFolder(dest_folder)

uniq_extensions=getUniqExtensions(source_folder)

for ext in uniq_extensions:
    os.mkdir(dest_folder+"/"+ext)
    print("Created new folder : " + dest_folder+"/"+ext)
    for file in os.listdir(source_folder):
        print("File : " + file)
        if ext in file:
            if not os.path.isdir(source_folder+"/"+file):
                shutil.copy(source_folder+"/"+file, dest_folder +"/"+ ext + "/" + file)
                print(".... File " + source_folder+"/"+file + " Copied to " + dest_folder +"/"+ ext + "/" + file )












