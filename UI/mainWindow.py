from PyQt5 import QtCore, QtGui, QtWidgets
import UI.plantManagment as plantManagment
import UI.greenhouses as greenhouses
import UI.plantToGreenhouses as plantToGreenhouses

class Ui_MainWindow(object):
    def __init__(self,MainWindow,loadedgreenhouses) -> None:
        self.MainWindow=MainWindow
        self.loadedgreenhouses=loadedgreenhouses

    def setupUi(self):
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(480, 480)
        self.MainWindow.setMinimumSize(QtCore.QSize(480, 480))
        self.MainWindow.setMaximumSize(QtCore.QSize(480, 480))
        self.MainWindow.setTabletTracking(False)
        self.MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.MainWindow.setAnimated(True)
        self.MainWindow.setDocumentMode(False)
        self.MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 70, 321, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btn_managePlants = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_managePlants.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.btn_managePlants.setFont(font)
        self.btn_managePlants.setObjectName("btn_managePlants")
        self.verticalLayout.addWidget(self.btn_managePlants)

        self.btn_managePlants.clicked.connect(lambda:self.loadPalntsUI())

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.btn_manageGreenHouses = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_manageGreenHouses.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.btn_manageGreenHouses.setFont(font)
        self.btn_manageGreenHouses.setObjectName("btn_manageGreenHouses")
        self.verticalLayout.addWidget(self.btn_manageGreenHouses)

        self.btn_manageGreenHouses.clicked.connect(lambda:self.btnManageGreenhouses())

        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.btn_plant = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_plant.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.btn_plant.setFont(font)
        self.btn_plant.setCheckable(False)
        self.btn_plant.setChecked(False)
        self.btn_plant.setObjectName("btn_plant")
        self.verticalLayout.addWidget(self.btn_plant)

        self.btn_plant.clicked.connect(lambda: self.btnPlant())

        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.lable_harvestableNum = QtWidgets.QLabel(self.centralwidget)
        self.lable_harvestableNum.setGeometry(QtCore.QRect(70, 20, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.lable_harvestableNum.setFont(font)
        self.lable_harvestableNum.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lable_harvestableNum.setScaledContents(False)
        self.lable_harvestableNum.setAlignment(QtCore.Qt.AlignCenter)
        self.lable_harvestableNum.setWordWrap(False)
        self.lable_harvestableNum.setIndent(2)
        self.lable_harvestableNum.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.lable_harvestableNum.setObjectName("lable_harvestableNum")
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_managePlants.setText(_translate("MainWindow", "manage plants"))
        self.btn_manageGreenHouses.setText(_translate("MainWindow", "manage greenhouses"))
        self.btn_plant.setText(_translate("MainWindow", "plant"))
        self.lable_harvestableNum.setText(_translate("MainWindow", f"plant ready for harvest: {self.calcRadyToHarvest()}"))

    def calcRadyToHarvest(self):
        cnt=0
        for gh in self.loadedgreenhouses:
            for pp in gh.palntingPoints:
                if pp.checkHarvesable():
                    cnt+=1
        return cnt

    def btnManageGreenhouses(self):
        ui=greenhouses.Ui_MainWindow(self.MainWindow,self.loadedgreenhouses)
        ui.startGreenhouseUI()

    def startUI(self):
        self.setupUi()
        self.MainWindow.show()

    def loadPalntsUI(self):
        ui = plantManagment.Ui_MainWindow(self.MainWindow,self.loadedgreenhouses)
        ui.startPlantManagmentUI()
    
    def btnPlant(self):
        ui = plantToGreenhouses.Ui_MainWindow(self.MainWindow,self.loadedgreenhouses)
        ui.startPlantToGreenhouseUI()

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
