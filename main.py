from GreenHouse import *
from Plant import *
from random import randint
from PyQt5 import QtWidgets
from UI.mainWindow import Ui_MainWindow
import os, sys

def main():
    
    if not os.path.isdir("greenhouses"): #if it's first load create dir and jsons 1-10
        os.mkdir("greenhouses")
        loadedgreenhouses=[]
        for i in range(1,11):
            with open(f"greenhouses/{i}.json","w") as f: #create the empty greenhoueses files
                gTMP=Greenhouse(randint(10,100),i)
                gTMP.createPoints()
                gTMP.updateJson()
                loadedgreenhouses.append(gTMP)
    else:
        loadedgreenhouses=Greenhouse.loadGreenhouses()

    Plant.loadPlants()

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow,loadedgreenhouses)
    ui.startUI()
    sys.exit(app.exec_())


if __name__=="__main__":
    main()

