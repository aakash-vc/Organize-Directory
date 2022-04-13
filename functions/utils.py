import os
from functions.extensions import extension_paths

def createFolders(path):
    # Destination to move files in target
    os.makedirs(path + 'File Tree/Files')

    # Destination to move sub-folders in target
    os.mkdir(path + 'File Tree/Folders')

def handleFolders(target_path, directory_list):
    # Set destination path
    folder_path = target_path + 'File Tree/Folders/'

    for directory in directory_list:
        # Move folder to destination
        os.rename(target_path + directory, folder_path + directory)

def getFolder(filename):
    # Get file name and return appropriate destination folder based on file extension
    extension = filename.split('.')[-1].lower()
    try:
        return extension_paths[extension]
    except KeyError:
        return 'others'

def handleFiles(target_path, file_list):
    # Set initial destination path
    file_path = target_path + 'File Tree/Files/'
    
    for file_ in file_list:
        # Get destination folder based on file name
        destination_folder = getFolder(file_)
        
        # New destination path based on file type
        new_file_path = file_path + destination_folder + '/'

        # Create folder for date if not already present
        if not os.path.exists(new_file_path):
            os.makedirs(new_file_path)

        # If a file with the same name already exists in the destination folder
        new_file = file_
        dup = 1
        while os.path.exists(new_file_path + new_file):
            new_file = '.'.join([f'({dup})' + file_.split('.')[0]] + file_.split('.')[1:])
            dup += 1

        # Move file to destination
        os.rename(target_path + file_, new_file_path + new_file)