from PyQt5 import QtCore, QtGui, QtWidgets
from Plant import Plant
import UI.mainWindow as mainWindow

class Ui_MainWindow(object):
    def __init__(self,MainWindow,loadedgreenhouses) -> None:
        self.MainWindow=MainWindow
        self.loadedgreenhouses=loadedgreenhouses

    def setupUi(self):
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(640, 440)
        self.MainWindow.setMinimumSize(QtCore.QSize(640, 440))
        self.MainWindow.setMaximumSize(QtCore.QSize(640, 440))
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 620, 401))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_kind = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_kind.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_kind.setFont(font)
        self.label_kind.setObjectName("label_kind")
        self.horizontalLayout.addWidget(self.label_kind)
        self.comboBox_kind = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_kind.setMinimumSize(QtCore.QSize(140, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_kind.setFont(font)
        self.comboBox_kind.setCurrentText("")
        self.comboBox_kind.setMaxVisibleItems(8)
        self.comboBox_kind.setObjectName("comboBox_kind")
        self.horizontalLayout.addWidget(self.comboBox_kind)

        self.comboBox_kind.addItems(Plant.kindsList)
        self.comboBox_kind.setCurrentIndex(0)
        self.comboBox_kind.currentIndexChanged.connect(lambda:self.plantSelected(self.comboBox_kind.currentText())) 

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_amount = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_amount.setMaximumSize(QtCore.QSize(77, 16777205))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_amount.setFont(font)
        self.label_amount.setObjectName("label_amount")
        self.horizontalLayout.addWidget(self.label_amount)
        self.spinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox.setMinimumSize(QtCore.QSize(65, 0))
        self.spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(5000)
        self.spinBox.setProperty("value", 1)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_growTime = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_growTime.setFont(font)
        self.label_growTime.setAlignment(QtCore.Qt.AlignCenter)
        self.label_growTime.setObjectName("label_growTime")
        self.horizontalLayout_2.addWidget(self.label_growTime)
        self.label_temp = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_temp.setFont(font)
        self.label_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.label_temp.setObjectName("label_temp")
        self.horizontalLayout_2.addWidget(self.label_temp)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_totalSpace = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_totalSpace.setFont(font)
        self.label_totalSpace.setAlignment(QtCore.Qt.AlignCenter)
        self.label_totalSpace.setObjectName("label_totalSpace")
        self.verticalLayout_4.addWidget(self.label_totalSpace)
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.verticalLayout_4.addWidget(self.tableWidget)

        self.plantSelected(self.comboBox_kind.currentText())

        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.pushButton_cancel = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_3.addWidget(self.pushButton_cancel)

        self.pushButton_cancel.clicked.connect(lambda: self.backBtn())

        self.pushButton_plant = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_plant.setFont(font)
        self.pushButton_plant.setObjectName("pushButton_plant")
        self.horizontalLayout_3.addWidget(self.pushButton_plant)

        self.pushButton_plant.clicked.connect(lambda: self.addPlants(self.comboBox_kind.currentText(),self.spinBox.value()))

        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi()
        
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_kind.setText(_translate("MainWindow", "kind:"))
        self.label_amount.setText(_translate("MainWindow", "amount:"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "greenhouse ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "avg temperature"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "avilable points"))
        self.pushButton_cancel.setText(_translate("MainWindow", "cancel"))
        self.pushButton_plant.setText(_translate("MainWindow", "plant!"))

    def startPlantToGreenhouseUI(self):
        self.setupUi()
        self.MainWindow.show()
    
    def backBtn(self):
        ui = mainWindow.Ui_MainWindow(self.MainWindow,self.loadedgreenhouses)
        ui.startUI()

    def plantSelected(self,kind):
        temp=Plant.tempScopeByKind(kind)
        growTime=Plant.growTimeByKind(kind)
        self.label_growTime.setText(f"grow time: {growTime}")
        self.label_temp.setText(f"temperature from {temp[0]} to {temp[1]}")

        self.clearTable()
        self.platableCnt=0
        i=0
        for gh in self.loadedgreenhouses:
            if gh.avgTemp>temp[0] and gh.avgTemp<temp[1]:
                fp=sum([1 for pp in gh.palntingPoints if not pp.isUsed])
                self.platableCnt+=fp
                
                self.addToTable(i,gh.greenhousID,gh.avgTemp,fp)
                i+=1

        self.label_totalSpace.setText(f"total avilable spaces: {self.platableCnt}")

    def clearTable(self):
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)

    def addToTable(self,i,id,temp,amount):
        self.tableWidget.insertRow(self.tableWidget.rowCount())
        self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(id)))
        self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(temp)))
        self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(amount)))

    def addPlants(self,kind,amount): 
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("planting")

        if amount>self.platableCnt:
            msg.setText(f"asked to plant {amount} but has only {self.platableCnt} avalable spaces")
            x = msg.exec_()
            return
        else:
            msg.setText(f"planted {amount} of {kind}")

        temp=Plant.tempScopeByKind(kind)
        for gh in self.loadedgreenhouses:
            if gh.avgTemp>temp[0] and gh.avgTemp<temp[1]:
                for pp in gh.palntingPoints:
                    if amount==0:
                        gh.updateJson()
                        x = msg.exec_()
                        if msg.standardButton(msg.clickedButton()) == QtWidgets.QMessageBox.Ok:
                            self.backBtn()
                            return

                    if pp.isUsed is False:
                        pp.enterPlant(kind)
                        amount-=1
        
        

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
