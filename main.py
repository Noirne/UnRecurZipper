import zipfile
import os
import glob
import sys

# Actual directory that we could find somewhere
class Folder:
    def __init__(self, path):
        self.path = path
        print("Current working folder is: " + self.path)
        self.checkForZippedFile()
        self.checkForDirectories()
        
    def checkForZippedFile(self):
        self.filesToUnzip = list()
        self.filesToUnzip = glob.glob(os.path.join(self.path,'*.zip'), recursive=True)
        # If we find a .zip file in the current directory
        for fileToUnzip in self.filesToUnzip:
            print("new ZipFile found at: " + fileToUnzip)
            zip_ref = zipfile.ZipFile(fileToUnzip, 'r')         # We prepare to unzip
            zipFilePath = fileToUnzip.split('.zip')[0]          # Reformating the path to remove the .zip at the end
            print("Current zip is at: " + zipFilePath)
            zip_ref.extractall(zipFilePath)                     # Extracting .zip content
            zip_ref.close()                                     # Closing extraction flow
            os.remove(zipFilePath + '.zip')                     # Removing the zip files
            Folder(zipFilePath)                                 # Calling Folder again

    def checkForDirectories(self):
        with os.scandir(self.path) as listOfDirectories:
            for entry in listOfDirectories:
                # We check if the actual file is a directory and if it isn't the .git one
                if not entry.is_file() and entry.name != '.git':
                    entry = Folder(os.path.join(self.path, entry.name))

# Reading the first arg written in the console (program name not included)
fileTest = Folder(sys.argv[1])