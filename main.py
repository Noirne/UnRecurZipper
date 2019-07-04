import zipfile
import os
import glob

# When an archive is found in a directory
class ZipFile(object):
    def __init__(self, path, name):
        self.path = path
        self.name = name
        zip_ref = zipfile.ZipFile(self.path, 'r')
        self.UnzipFile(zip_ref)
    
    def UnzipFile(self, zip_ref):
        zip_ref.extractall(self.name)
        extractedFolder = File(os.path.join(self.path,self.name), list(), list())
        os.remove(self.name + '.zip')

# Actual directory that we could find somewhere
class Folder:
    def __init__(self, path, directoriesToCheck, filesToUnzip):
        self.path = path
        self.directoriesToCheck = directoriesToCheck
        self.filesToUnzip = filesToUnzip

    def checkForZippedFile(self):
        self.filesToUnzip = glob.glob('*.zip', recursive=True)
        for fileToUnzip in self.filesToUnzip:
            fileToUnzip = ZipFile(os.path.join(self.path, fileToUnzip), fileToUnzip.split('.',1)[0])
        return self.filesToUnzip

    def checkForDirectories(self):
        with os.scandir(self.path) as listOfDirectories:
            for entry in listOfDirectories:
                if not entry.is_file():
                    self.directoriesToCheck.append(entry)
        return self.directoriesToCheck






fileTest = Folder('.', list(), list())
fileDirectories = fileTest.checkForDirectories()
fileZip = fileTest.checkForZippedFile()
print("Directories: ")
print(fileDirectories)
print("Files to unzip: ")
print(fileZip)





