# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_UI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 350)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 10, -1)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("斗鱼")
        self.comboBox.addItem("虎牙")
        self.comboBox.addItem("Bilibili")
        self.comboBox.addItem("触手")
        self.comboBox.addItem("抖音")
        self.comboBox.addItem("企鹅电竞")
        self.comboBox.addItem("花椒")
        self.comboBox.addItem("火猫")
        self.comboBox.addItem("爱奇艺")
        self.comboBox.addItem("快手")
        self.comboBox.addItem("酷狗")
        self.comboBox.addItem("龙珠")
        self.comboBox.addItem("NOW")
        self.comboBox.addItem("pps")
        self.comboBox.addItem("六间房")
        self.comboBox.addItem("网易CC")
        self.comboBox.addItem("西瓜")
        self.comboBox.addItem("映客")
        self.comboBox.addItem("一直播")
        self.comboBox.addItem("YY")
        self.comboBox.addItem("战旗")
        self.comboBox.addItem("17live")
        self.comboBox.addItem("来疯")
        self.horizontalLayout.addWidget(self.comboBox)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.roomID= QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.roomID.sizePolicy().hasHeightForWidth())
        self.roomID.setSizePolicy(sizePolicy)
        self.roomID.setInputMethodHints(QtCore.Qt.ImhNone)
        self.roomID.setObjectName("roomID")
        self.horizontalLayout_4.addWidget(self.roomID)
        self.getUrlButton = QtWidgets.QPushButton(self.centralwidget)
        self.getUrlButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.getUrlButton.sizePolicy().hasHeightForWidth())
        self.getUrlButton.setSizePolicy(sizePolicy)
        self.getUrlButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.getUrlButton.setObjectName("getUrlButton")
        self.horizontalLayout_4.addWidget(self.getUrlButton)
        self.horizontalLayout_4.setStretch(0, 6)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 5)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.exportButton = QtWidgets.QPushButton(self.centralwidget)
        self.exportButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exportButton.sizePolicy().hasHeightForWidth())
        self.exportButton.setSizePolicy(sizePolicy)
        self.exportButton.setMinimumSize(QtCore.QSize(82, 0))
        self.exportButton.setMaximumSize(QtCore.QSize(82, 16777215))
        self.exportButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.exportButton.setObjectName("exportButton")
        self.gridLayout.addWidget(self.exportButton, 1, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.selectedList = QtWidgets.QTableWidget(self.centralwidget)
        self.selectedList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.selectedList.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.selectedList.setObjectName("selectedList")
        self.selectedList.setColumnCount(3)
        self.selectedList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.selectedList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.selectedList.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.selectedList.setHorizontalHeaderItem(2, item)
        self.selectedList.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.selectedList, 0, 0, 1, 1)
        self.gridLayout.setColumnStretch(0, 7)
        self.verticalLayout_2.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "直播源提取"))
        self.getUrlButton.setText(_translate("MainWindow", "获取直链"))
        self.exportButton.setText(_translate("MainWindow", "导出"))
        item = self.selectedList.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "直播源"))
        item = self.selectedList.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "房间号"))
        item = self.selectedList.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "直链"))
        reg = QtCore.QRegExp('[0-9]*')
        self.roomID.setValidator(QtGui.QRegExpValidator(reg, self))
        self.selectedList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.selectedList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.setWindowIcon(QtGui.QIcon(':/realurlGUI.ico'))