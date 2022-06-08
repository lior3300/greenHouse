from PyQt5 import QtCore, QtGui, QtWidgets
import UI.mainWindow as mainWindow
import UI.pointsList as pointsList

class Ui_MainWindow(object):
    def __init__(self,MainWindow,loadedgreenhouses) -> None:
        self.MainWindow=MainWindow
        self.loadedgreenhouses=loadedgreenhouses

    def setupUi(self):
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(640, 460)
        self.MainWindow.setMinimumSize(QtCore.QSize(640, 460))
        self.MainWindow.setMaximumSize(QtCore.QSize(640, 460))
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 591, 391))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label_alart = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_alart.setFont(font)
        self.label_alart.setObjectName("label_alart")
        self.label_alart.setText("please choose a greenhouse")
        self.verticalLayout.addWidget(self.label_alart)

        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setAutoScrollMargin(22)
        self.tableWidget.setTabKeyNavigation(True)
        self.tableWidget.setProperty("showDropIndicator", True)
        self.tableWidget.setDragDropOverwriteMode(True)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers) #forbid editing

        self.tableWidget.setRowCount(len(self.loadedgreenhouses)) #len of number of plants
        for i,gh in enumerate(self.loadedgreenhouses): #add to the table
            harvestable=sum([pp.checkHarvesable() for pp in gh.palntingPoints])
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(gh.greenhousID)))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(gh.avgTemp)))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(harvestable)))

        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setKerning(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(19)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn_back = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btn_back.setFont(font)
        self.btn_back.setObjectName("btn_back")
        self.gridLayout.addWidget(self.btn_back, 3, 0, 1, 1)

        self.btn_back.clicked.connect(lambda: self.backBtn())

        self.btn_harvest = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btn_harvest.setFont(font)
        self.btn_harvest.setObjectName("btn_harvest")
        self.gridLayout.addWidget(self.btn_harvest, 2, 0, 1, 1)

        self.btn_harvest.clicked.connect(lambda: self.btnHarvest())

        self.btn_checkPoints = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btn_checkPoints.setFont(font)
        self.btn_checkPoints.setObjectName("btn_checkPoints")
        self.gridLayout.addWidget(self.btn_checkPoints, 2, 1, 1, 1)

        self.btn_checkPoints.clicked.connect(lambda:self.btnPoints())

        self.btn_clear = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btn_clear.setFont(font)
        self.btn_clear.setObjectName("btn_clear")
        self.gridLayout.addWidget(self.btn_clear, 3, 1, 1, 1)

        self.btn_clear.clicked.connect(lambda: self.btnClear())

        self.verticalLayout.addLayout(self.gridLayout)
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "greenhouses"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "greenhouse N.o"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "avg temperature"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "harvestable"))
        self.btn_back.setText(_translate("MainWindow", "back"))
        self.btn_harvest.setText(_translate("MainWindow", "harvest"))
        self.btn_checkPoints.setText(_translate("MainWindow", "check points"))
        self.btn_clear.setText(_translate("MainWindow", "clear greenhouse"))

    def startGreenhouseUI(self):
        self.setupUi()
        self.MainWindow.show()

    def backBtn(self):
        ui = mainWindow.Ui_MainWindow(self.MainWindow,self.loadedgreenhouses)
        ui.startUI()
    
    def btnHarvest(self):
        if self.tableWidget.currentRow()>=0:
            harvested = self.loadedgreenhouses[self.tableWidget.currentRow()].harvestPlants()
            cnt=0
            st="harvested:\n"
            for k,v in harvested.items():
                st+=f"{k}:{v}\n"
                cnt+=v
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("harvested")
            msg.setText(st)
            x = msg.exec_()
            
            cnt-=int(self.tableWidget.item(self.tableWidget.currentRow(),2).text())
            self.tableWidget.setItem(self.tableWidget.currentRow(), 2, QtWidgets.QTableWidgetItem(str(cnt)))    

        else:
            self.label_alart.setText("please choose a greenhouse!!")

    def btnClear(self):
        if self.tableWidget.currentRow()>=0:
            msg = QtWidgets.QMessageBox()
            msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel)
            msg.setWindowTitle("harvested")
            msg.setText("this will remove all plants in the greenhouse.\nwould you like to confirm?")
            x = msg.exec_()
            if msg.standardButton(msg.clickedButton()) == QtWidgets.QMessageBox.Yes:
                self.loadedgreenhouses[self.tableWidget.currentRow()].clearGreenhouse()
                self.tableWidget.setItem(self.tableWidget.currentRow(), 2, QtWidgets.QTableWidgetItem("0")) 
        else:
            self.label_alart.setText("please choose a greenhouse!!")
        
    def btnPoints(self):
        if self.tableWidget.currentRow()>=0:
            ui=pointsList.Ui_MainWindow(self.MainWindow,self.loadedgreenhouses,self.loadedgreenhouses[self.tableWidget.currentRow()].greenhousID)
            ui.startPlantingPointsUI()
        else:
            self.label_alart.setText("please choose a greenhouse!!")
        
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

