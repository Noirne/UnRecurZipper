import zipfile
import os
import glob

# When an archive is found in a directory
class ZipFile(object):
    def __init__(self, path):
        self.path = path
        zip_ref = zipfile.ZipFile(self.path, 'r')
        self.path = self.path.split('.zip')[0]
        print("Current zip is at: " + self.path)
        self.UnzipFile(zip_ref)
    
    def UnzipFile(self, zip_ref):
        zip_ref.extractall(self.path)
        Folder(self.path)
        #os.remove(self.name + '.zip')

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
        for fileToUnzip in self.filesToUnzip:
            print("new ZipFile found at: " + fileToUnzip)
            fileToUnzip = ZipFile(fileToUnzip)

    def checkForDirectories(self):
        with os.scandir(self.path) as listOfDirectories:
            for entry in listOfDirectories:
                if not entry.is_file() and entry.name != '.git':
                    entry = Folder(os.path.join(self.path, entry.name))

fileTest = Folder('.')
#fileDirectories = fileTest.checkForDirectories()
#fileZip = fileTest.checkForZippedFile()
#print("Directories: ")
#print(fileDirectories)
#print("Files to unzip: ")
#print(fileZip)





