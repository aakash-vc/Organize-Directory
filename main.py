import os
from datetime import datetime

def createFolders(path):
    # Destinations to move files in target
    # List of common file types for folders
    file_dirs = ['PDF', 'PPT', 'Doc', 'Text', 'Executable', 'Compressed', 'Data', 'Miscellaneous', 'Images', 'Audio', 'Video']
    for name in file_dirs:
        os.makedirs(path + 'File Tree/Files/' + name)

    # Destination to move sub-folders in target
    os.mkdir(path + 'File Tree/Folders')

def handleFolders(target_path, directory_list):
    # Set destination path
    folder_path = target_path + 'File Tree/Folders/'

    for directory in directory_list:
        # Get last modified date of folder
        date = str(datetime.fromtimestamp(int(os.path.getmtime(target_path + directory))).date())
        
        # Create folder for date if not already present
        if not os.path.exists(folder_path + date):
            os.makedirs(folder_path + date)

        # Move folder to destination
        os.rename(target_path + directory, folder_path + date + '/' + directory)

def getFolder(filename):
    # Get file name and return appropriate destination folder based on file extension
    extension = filename.split('.')[-1]

    if extension == 'pdf':
        return 'PDF'

    elif extension in ['doc', 'docx']:
        return 'Doc'

    elif extension == 'txt':
        return 'Text'

    elif extension in ['exe', 'msi']:
        return 'Executable'

    elif extension in ['zip', 'tar', 'rar', '7z', 'gz']:
        return 'Compressed'

    elif extension in ['jpg', 'jpeg', 'png', 'JPG', 'JPEG', 'PNG']:
        return 'Images'

    elif extension in ['csv', 'xls', 'xlsx']:
        return 'Data'

    elif extension in ['pptx', 'ppt']:
        return 'PPT'

    elif extension in ['mp3', 'wav', 'aac']:
        return 'Audio'

    elif extension in ['mp4', 'mov', 'wmv', 'mkv', 'webm', 'flv', 'avi']:
        return 'Video'

    else:
        return 'Miscellaneous'

def handleFiles(target_path, file_list):
    # Set initial destination path
    file_path = target_path + 'File Tree/Files/'
    
    for file_ in file_list:
        # Get destination folder based on file name
        destination_folder = getFolder(file_)
        
        # New destination path based on file type
        new_file_path = file_path + destination_folder + '/'

        # Get last modified date of file
        date = str(datetime.fromtimestamp(int(os.path.getmtime(target_path + file_))).date())

        # Create folder for date if not already present
        if not os.path.exists(new_file_path + date):
            os.makedirs(new_file_path + date)

        # Move file to destination
        os.rename(target_path + file_, new_file_path + date + '/' + file_)


if __name__ == '__main__':
    # Folder to run the script
    target_path = "C:/Users/aakas/Downloads/"

    # Create folder tree if running for the first time
    if not os.path.exists(target_path + 'File Tree'):
        createFolders(target_path)

    # Get list of files and sub-folders in target folder
    for root, directories, files in os.walk(target_path):
        break
    directories.remove('File Tree')
    
    # Move folders
    handleFolders(target_path, directories)
    # Move Files
    handleFiles(target_path, files)