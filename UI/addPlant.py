from PyQt5 import QtCore, QtGui, QtWidgets
import UI.plantManagment as plantManagment
from Plant import Plant

class Ui_MainWindow(object):
    def __init__(self,MainWindow,loadedgreenhouses) -> None:
        self.MainWindow=MainWindow
        self.loadedgreenhouses=loadedgreenhouses

    def setupUi(self):
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(254, 365)
        self.MainWindow.setMinimumSize(QtCore.QSize(254, 365))
        self.MainWindow.setMaximumSize(QtCore.QSize(254, 365))
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 231, 351))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label_error = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_error.setFont(font)
        self.label_error.setObjectName("label_label_error")
        self.label_error.setGeometry(QtCore.QRect(10, 10, 250, 30))

        self.label_kind = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_kind.setFont(font)
        self.label_kind.setObjectName("label_kind")
        self.horizontalLayout.addWidget(self.label_kind)
        self.lineEdit_kind = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_kind.setObjectName("lineEdit_kind")
        self.horizontalLayout.addWidget(self.lineEdit_kind)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_growTime = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_growTime.setFont(font)
        self.label_growTime.setObjectName("label_growTime")
        self.horizontalLayout_6.addWidget(self.label_growTime)
        self.spinBox_growTime = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_growTime.setSuffix("")
        self.spinBox_growTime.setMaximum(10000)
        self.spinBox_growTime.setProperty("value", 1)
        self.spinBox_growTime.setMinimum(1)
        self.spinBox_growTime.setObjectName("spinBox_growTime")
        self.horizontalLayout_6.addWidget(self.spinBox_growTime)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_minTemp = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_minTemp.setFont(font)
        self.label_minTemp.setObjectName("label_minTemp")
        self.horizontalLayout_5.addWidget(self.label_minTemp)
        self.spinBox_minTemp = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_minTemp.setSuffix("")
        self.spinBox_minTemp.setProperty("value", 0)
        self.spinBox_minTemp.setObjectName("spinBox_minTemp")
        self.horizontalLayout_5.addWidget(self.spinBox_minTemp)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_maxTemp = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_maxTemp.setMinimumSize(QtCore.QSize(40, 0))
        self.label_maxTemp.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_maxTemp.setFont(font)
        self.label_maxTemp.setObjectName("label_maxTemp")
        self.horizontalLayout_4.addWidget(self.label_maxTemp)
        self.spinBox_maxTemp = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_maxTemp.setSuffix("")
        self.spinBox_maxTemp.setProperty("value", 0)
        self.spinBox_maxTemp.setObjectName("spinBox_maxTemp")
        self.horizontalLayout_4.addWidget(self.spinBox_maxTemp)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btn_add = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btn_add.setFont(font)
        self.btn_add.setObjectName("btn_add")
        self.horizontalLayout_7.addWidget(self.btn_add)

        self.btn_add.clicked.connect(lambda:self.btnAdd())

        self.btn_cancel = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btn_cancel.setFont(font)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout_7.addWidget(self.btn_cancel)

        self.btn_cancel.clicked.connect(lambda: self.btnCancel())

        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "add plant"))
        self.label_kind.setText(_translate("MainWindow", "kind:"))
        self.label_growTime.setText(_translate("MainWindow", "growing time:"))
        self.label_minTemp.setText(_translate("MainWindow", "min temperature:"))
        self.label_maxTemp.setText(_translate("MainWindow", "max temperature:"))
        self.btn_add.setText(_translate("MainWindow", "add"))
        self.btn_cancel.setText(_translate("MainWindow", "cancel"))

    def startAddPlantUI(self):
        self.setupUi()
        self.MainWindow.show()

    def btnCancel(self):
        ui = plantManagment.Ui_MainWindow(self.MainWindow,self.loadedgreenhouses)
        ui.startPlantManagmentUI()
    
    def btnAdd(self):
        # print(self.lineEdit_kind.text(),self.spinBox_growTime.value(),self.spinBox_minTemp.value(),self.spinBox_maxTemp.value())
        if self.lineEdit_kind.text()=="":
            self.label_error.setText("make sure to give kind!")
        else:
            if self.spinBox_minTemp.value()>self.spinBox_maxTemp.value():
                p=Plant(self.lineEdit_kind.text(),self.spinBox_growTime.value(),self.spinBox_maxTemp.value(),self.spinBox_minTemp.value())
            else:
                p=Plant(self.lineEdit_kind.text(),self.spinBox_growTime.value(),self.spinBox_minTemp.value(),self.spinBox_maxTemp.value())
            
            if not Plant.addPlant(p):
                self.label_error.setText("kind already exist")
                
            self.btnCancel()

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
