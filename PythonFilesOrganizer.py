#Organize files script
import os
import shutil

def organize_directory(directory):
    if not os.path.exists(directory):
        print("Directory does not exist.")
        return

    extensions = set()

    items = os.listdir(directory)

    for item in items:
        #gets item path directory + item ex Desktop\abcd.pdf
        item_path = os.path.join(directory, item)
        #check if is a file
        if os.path.isfile(item_path):
            base_name, extension = os.path.splitext(item)
            extension = extension[1:]

            extensions.add(extension)

            #Ex: My xlsx Files
            folder_name = "My {} Files".format(extension.upper())
            #ex: Desktop\My xlsx Files
            folder_path = os.path.join(directory, folder_name)
            #if !Desktop\My xlsx Files makes it
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)

            destination_path = os.path.join(folder_path, item)
            #Try move it if !move log the exception
            try:
                shutil.move(item_path, destination_path)
                print("Moved '{}' to '{}'".format(item_path, destination_path))
            except Exception as e:
                print("Error moving '{}': {}".format(item_path, str(e)))

    print("Organization completed.")


directory = input("Enter the name of the directory to organize (ex:Desktop, Documents) or Folder (ex:Documents/FolderName): ")
directory = os.path.abspath(os.path.expanduser(directory))
if not os.path.exists(directory):
    print(r"If Documents or Desktop doesn't exist please provide the full path ex: C:\Users\Name\Drive - drive\Documents")
else:
    print(directory)
    organize_directory(directory)


