from PyQt5 import QtCore, QtGui, QtWidgets
import UI.greenhouses as greenhouses

class Ui_MainWindow(object):
    def __init__(self,MainWindow,loadedgreenhouses,ghID) -> None:
        self.MainWindow=MainWindow
        self.loadedgreenhouses=loadedgreenhouses
        self.ghID=ghID

    def setupUi(self):
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(640, 460)
        self.MainWindow.setMinimumSize(QtCore.QSize(640, 460))
        self.MainWindow.setMaximumSize(QtCore.QSize(640, 460))
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 621, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tabWidget = QtWidgets.QTabWidget(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.all = QtWidgets.QWidget()
        self.all.setObjectName("all")
        self.tabWidget.addTab(self.all, "")
        self.forHarvest = QtWidgets.QWidget()
        self.forHarvest.setObjectName("forHarvest")
        self.tabWidget.addTab(self.forHarvest, "")
        self.inUse = QtWidgets.QWidget()
        self.inUse.setObjectName("inUse")
        self.tabWidget.addTab(self.inUse, "")
        self.free = QtWidgets.QWidget()
        self.free.setObjectName("free")
        self.tabWidget.addTab(self.free, "")
        self.verticalLayout.addWidget(self.tabWidget)

        self.setTable()

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(510, 400, 113, 32))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(lambda:self.backBtn())
        
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi()
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "points data"))
        self.label.setText(_translate("MainWindow", f"greenhouse N.o: {self.ghID}"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.all), _translate("MainWindow", "all"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.forHarvest), _translate("MainWindow", "for harvest"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.inUse), _translate("MainWindow", "in use"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.free), _translate("MainWindow", "free"))
        self.pushButton.setText(_translate("MainWindow", "BACK"))

    def startPlantingPointsUI(self):
        self.setupUi()
        self.MainWindow.show()

    def backBtn(self):
        ui=greenhouses.Ui_MainWindow(self.MainWindow,self.loadedgreenhouses)
        ui.startGreenhouseUI()

    def setTable(self):
        tabs=[self.all,self.forHarvest,self.inUse,self.free]
        for i in range(4):
            self.tableWidget = QtWidgets.QTableWidget(tabs[i])
            self.tableWidget.setGeometry(QtCore.QRect(-5, 1, 621, 321))
            self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
            self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
            self.tableWidget.setObjectName(f"tableWidget{i}")
            self.tableWidget.setColumnCount(4)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(0, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(1, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(2, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(3, item)
            self.tableWidget.horizontalHeader().setVisible(True)
            self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
            self.tableWidget.horizontalHeader().setHighlightSections(True)
            self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
            self.tableWidget.horizontalHeader().setStretchLastSection(True)
            self.tableWidget.verticalHeader().setVisible(False)
            self.tableWidget.verticalHeader().setHighlightSections(False)
            item = self.tableWidget.horizontalHeaderItem(0)
            item.setText("point id")
            item = self.tableWidget.horizontalHeaderItem(1)
            item.setText("is used")
            item = self.tableWidget.horizontalHeaderItem(2)
            item.setText("plant kind")
            item = self.tableWidget.horizontalHeaderItem(3)
            item.setText("planting date")
            self.loadData(self.tableWidget,i)
        
    def loadData(self,tab,i):
        
        if i==0:#all
            tab.setRowCount(len(self.loadedgreenhouses[self.ghID-1].palntingPoints)) #len of number of plants 
            for i,pp in enumerate(self.loadedgreenhouses[self.ghID-1].palntingPoints): #add to the table
                self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(pp.pointId)))
                self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(pp.isUsed)))
                self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(pp.pantKind))
                self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(pp.pantingDate))
        elif i==1:#for harvest
            pointsToLoad=[p for p in self.loadedgreenhouses[self.ghID-1].palntingPoints if p.checkHarvesable()]
            tab.setRowCount(len(pointsToLoad)) #len of number of plants 
            for i,pp in enumerate(pointsToLoad): #add to the table
                self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(pp.pointId)))
                self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(pp.isUsed)))
                self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(pp.pantKind))
                self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(pp.pantingDate))
        elif i==2:#in use
            pointsToLoad=[p for p in self.loadedgreenhouses[self.ghID-1].palntingPoints if p.isUsed==True]
            tab.setRowCount(len(pointsToLoad)) #len of number of plants 
            for i,pp in enumerate(pointsToLoad): #add to the table
                self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(pp.pointId)))
                self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(pp.isUsed)))
                self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(pp.pantKind))
                self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(pp.pantingDate))
        else:#free
            pointsToLoad=[p for p in self.loadedgreenhouses[self.ghID-1].palntingPoints if p.isUsed==False]
            tab.setRowCount(len(pointsToLoad)) #len of number of plants 
            for i,pp in enumerate(pointsToLoad): #add to the table
                self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(pp.pointId)))
                self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(pp.isUsed)))
                self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(pp.pantKind))
                self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(pp.pantingDate))
        

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
