from PyQt5 import QtCore, QtGui, QtWidgets
from Plant import Plant
import UI.mainWindow as mainWindow
import UI.addPlant as addPlant

class Ui_MainWindow(object):
    def __init__(self,MainWindow,loadedgreenhouses) -> None:
        self.MainWindow=MainWindow
        self.loadedgreenhouses=loadedgreenhouses

    def setupUi(self):
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.setWindowModality(QtCore.Qt.NonModal)
        self.MainWindow.setEnabled(True)
        self.MainWindow.resize(627, 409)
        self.MainWindow.setMinimumSize(QtCore.QSize(627, 409))
        self.MainWindow.setMaximumSize(QtCore.QSize(627, 409))
        self.MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 591, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_plants = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_plants.setFont(font)
        self.label_plants.setObjectName("label_plants")
        self.verticalLayout.addWidget(self.label_plants)
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.verticalLayout.addWidget(self.tableWidget)
        
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers) #forbid editing

        self.tableWidget.setRowCount(len(Plant.kindsList)) #len of number of plants
        for i,p in enumerate(Plant.plantsLst): #add to the table
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(p.kind))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(p.grow_time)))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(p.temp_min)))
            self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(p.temp_max)))
        
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_back = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_back.setFont(font)
        self.btn_back.setObjectName("btn_back")
        self.horizontalLayout.addWidget(self.btn_back)

        self.btn_back.clicked.connect(lambda:self.backBtn())
        
        self.btn_delete = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_delete.setFont(font)
        self.btn_delete.setObjectName("btn_delete")
        self.horizontalLayout.addWidget(self.btn_delete)

        self.btn_delete.clicked.connect(lambda: self.btnDelete())

        self.btn_addPlant = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_addPlant.setFont(font)
        self.btn_addPlant.setObjectName("btn_addPlant")

        if self.tableWidget.rowCount()>=8:
            self.btn_addPlant.setText("max plants of 8 has been reached")
            self.btn_addPlant.setEnabled(False)
        else:
            self.btn_addPlant.setText("add plant")
            self.btn_addPlant.clicked.connect(lambda: self.addBtn())
        
        self.horizontalLayout.addWidget(self.btn_addPlant)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "plant managment"))
        self.label_plants.setText(_translate("MainWindow", "plants:"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "kind"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "grow time"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "min temperature"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "max temperature"))
        self.btn_back.setText(_translate("MainWindow", "back"))
        self.btn_delete.setText(_translate("MainWindow", "delete"))
        # self.btn_addPlant.setText(_translate("MainWindow", "add plant"))
        self.tableWidget.show()
    
    def backBtn(self):
        ui = mainWindow.Ui_MainWindow(self.MainWindow,self.loadedgreenhouses)
        ui.startUI()

    def addBtn(self):
        ui = addPlant.Ui_MainWindow(self.MainWindow,self.loadedgreenhouses)
        ui.startAddPlantUI()
    
    def btnDelete(self):
        if self.tableWidget.currentRow()>=0:
            toDel=Plant.plantsLst[self.tableWidget.currentRow()].kind
            #going threw all the planting points if it's from the kind that's deleted then reset point
            for gh in self.loadedgreenhouses:
                gh.removePlant(toDel)

            Plant.plantsLst.remove(Plant.plantsLst[self.tableWidget.currentRow()])
            Plant.kindsList.remove(toDel)
            Plant.removePlant()

            self.startPlantManagmentUI() #refresh the page

    def startPlantManagmentUI(self):
        self.setupUi()
        self.MainWindow.show()

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow(MainWindow,None)
#     ui.setupUi()
#     MainWindow.show()
#     sys.exit(app.exec_())


