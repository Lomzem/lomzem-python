import os
import shutil


class MoveToCompleted:
    def __init__(self):
        self.folderPath = "D:/Other/Torrents/"
        self.completedFolderName = "completed"
        self.tempFolderName = "temp"

    def scanFolderPath(self):
        scannedItems = []
        excludedItemList = []
        excludedItemList.append(self.completedFolderName)
        excludedItemList.append(self.tempFolderName)
        for item in os.listdir():
            if item not in excludedItemList:
                scannedItems.append(item)
        return scannedItems

    def moveItems(self, scannedList):
        for item in scannedList:
            shutil.move(item, self.completedFolderName)

    def main(self):
        os.chdir(self.folderPath)
        scannedItems = self.scanFolderPath()
        self.moveItems(scannedItems)


if __name__ == "__main__":
    MoveToCompleted().main()
