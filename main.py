import os
from functions.utils import *

if __name__ == '__main__':
    # Folder to run the script
    target_path = "D:/test/" #"C:/Users/aakas/Downloads/"

    # Create folder tree if running for the first time
    if not os.path.exists(target_path + 'File Tree'):
        # Destination to move files in target
        os.makedirs(target_path + 'File Tree/Files')

        # Destination to move sub-folders in target
        os.mkdir(target_path + 'File Tree/Folders')

    # Get list of files and sub-folders in target folder
    for root, directories, files in os.walk(target_path):
        break
    directories.remove('File Tree')
    
    # Move folders
    handleFolders(target_path, directories)
    # Move Files
    handleFiles(target_path, files)