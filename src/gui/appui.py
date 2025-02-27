# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'appui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

# Это автогенерируемый файл с помощью Qt Designer

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        """
        Метод, который создает объекты и задаёт их расположение
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(923, 431)
        MainWindow.setStyleSheet("#RamProgressBar {\n"
                                 "    text-align: center;\n"
                                 "}\n"
                                 "#RamProgressBar::chunk {\n"
                                 "    background-color: #3498db;\n"
                                 "}\n"
                                 "#CpuProgressBar {\n"
                                 "    text-align: center;\n"
                                 "}\n"
                                 "#CpuProgressBar::chunk {\n"
                                 "    background-color: #2ecc71;\n"
                                 "}\n"
                                 "#DiskProgressBar {\n"
                                 "    text-align: center;\n"
                                 "}\n"
                                 "#DiskProgressBar::chunk {\n"
                                 "   background-color: #9b59b6;\n"
                                 "}\n"
                                 "QProgressBar\n"
                                 "{\n"
                                 "border: solid grey;\n"
                                 "border-radius: 15px;\n"
                                 "color: black;\n"
                                 "}\n"
                                 "QProgressBar::chunk \n"
                                 "{\n"
                                 "border-radius :15px;\n"
                                 "}    \n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(10, 20))
        self.label_5.setMaximumSize(QtCore.QSize(65, 15))
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(60, 50))
        self.label.setMaximumSize(QtCore.QSize(60, 50))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.RamProgressBar = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RamProgressBar.sizePolicy().hasHeightForWidth())
        self.RamProgressBar.setSizePolicy(sizePolicy)
        self.RamProgressBar.setMinimumSize(QtCore.QSize(461, 31))
        self.RamProgressBar.setMaximumSize(QtCore.QSize(461, 31))
        self.RamProgressBar.setProperty("value", 0)
        self.RamProgressBar.setOrientation(QtCore.Qt.Horizontal)
        self.RamProgressBar.setObjectName("RamProgressBar")
        self.verticalLayout.addWidget(self.RamProgressBar)
        self.ram_info = QtWidgets.QLabel(self.centralwidget)
        self.ram_info.setText("")
        self.ram_info.setObjectName("ram_info")
        self.verticalLayout.addWidget(self.ram_info)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(60, 50))
        self.label_2.setMaximumSize(QtCore.QSize(60, 50))
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.CpuProgressBar = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CpuProgressBar.sizePolicy().hasHeightForWidth())
        self.CpuProgressBar.setSizePolicy(sizePolicy)
        self.CpuProgressBar.setMinimumSize(QtCore.QSize(461, 31))
        self.CpuProgressBar.setMaximumSize(QtCore.QSize(461, 31))
        self.CpuProgressBar.setProperty("value", 0)
        self.CpuProgressBar.setObjectName("CpuProgressBar")
        self.verticalLayout.addWidget(self.CpuProgressBar)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(60, 50))
        self.label_3.setMaximumSize(QtCore.QSize(60, 50))
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.DiskProgressBar = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DiskProgressBar.sizePolicy().hasHeightForWidth())
        self.DiskProgressBar.setSizePolicy(sizePolicy)
        self.DiskProgressBar.setMinimumSize(QtCore.QSize(461, 31))
        self.DiskProgressBar.setMaximumSize(QtCore.QSize(461, 31))
        self.DiskProgressBar.setProperty("value", 0)
        self.DiskProgressBar.setOrientation(QtCore.Qt.Horizontal)
        self.DiskProgressBar.setObjectName("DiskProgressBar")
        self.verticalLayout.addWidget(self.DiskProgressBar)
        self.diskinfo = QtWidgets.QLabel(self.centralwidget)
        self.diskinfo.setText("")
        self.diskinfo.setObjectName("diskinfo")
        self.verticalLayout.addWidget(self.diskinfo)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.host = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.host.sizePolicy().hasHeightForWidth())
        self.host.setSizePolicy(sizePolicy)
        self.host.setMinimumSize(QtCore.QSize(301, 40))
        self.host.setObjectName("host")
        self.verticalLayout_2.addWidget(self.host)
        self.pltf = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pltf.sizePolicy().hasHeightForWidth())
        self.pltf.setSizePolicy(sizePolicy)
        self.pltf.setMinimumSize(QtCore.QSize(301, 31))
        self.pltf.setObjectName("pltf")
        self.verticalLayout_2.addWidget(self.pltf)
        self.pltf_ver = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pltf_ver.sizePolicy().hasHeightForWidth())
        self.pltf_ver.setSizePolicy(sizePolicy)
        self.pltf_ver.setMinimumSize(QtCore.QSize(301, 31))
        self.pltf_ver.setObjectName("pltf_ver")
        self.verticalLayout_2.addWidget(self.pltf_ver)
        self.pltf_re = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pltf_re.sizePolicy().hasHeightForWidth())
        self.pltf_re.setSizePolicy(sizePolicy)
        self.pltf_re.setMinimumSize(QtCore.QSize(301, 31))
        self.pltf_re.setObjectName("pltf_re")
        self.verticalLayout_2.addWidget(self.pltf_re)
        self.ram = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ram.sizePolicy().hasHeightForWidth())
        self.ram.setSizePolicy(sizePolicy)
        self.ram.setMinimumSize(QtCore.QSize(301, 31))
        self.ram.setObjectName("ram")
        self.verticalLayout_2.addWidget(self.ram)
        self.cpu = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cpu.sizePolicy().hasHeightForWidth())
        self.cpu.setSizePolicy(sizePolicy)
        self.cpu.setMinimumSize(QtCore.QSize(301, 31))
        self.cpu.setObjectName("cpu")
        self.verticalLayout_2.addWidget(self.cpu)
        self.cpu_cores = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cpu_cores.sizePolicy().hasHeightForWidth())
        self.cpu_cores.setSizePolicy(sizePolicy)
        self.cpu_cores.setMinimumSize(QtCore.QSize(301, 31))
        self.cpu_cores.setObjectName("cpu_cores")
        self.verticalLayout_2.addWidget(self.cpu_cores)
        self.ip = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ip.sizePolicy().hasHeightForWidth())
        self.ip.setSizePolicy(sizePolicy)
        self.ip.setMinimumSize(QtCore.QSize(301, 31))
        self.ip.setObjectName("ip")
        self.verticalLayout_2.addWidget(self.ip)
        self.mac = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mac.sizePolicy().hasHeightForWidth())
        self.mac.setSizePolicy(sizePolicy)
        self.mac.setMinimumSize(QtCore.QSize(301, 31))
        self.mac.setObjectName("mac")
        self.verticalLayout_2.addWidget(self.mac)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 923, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuMenu.addAction(self.actionAbout)
        self.menuMenu.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """
        Метод, изменяющий текстовое отображение объектов
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PC Monitoring 1.0"))
        self.label_5.setText(_translate("MainWindow", "Resources"))
        self.label.setText(_translate("MainWindow", "Memory:"))
        self.label_2.setText(_translate("MainWindow", "Cpu:"))
        self.label_3.setText(_translate("MainWindow", "Disk:"))
        self.label_4.setText(_translate("MainWindow", "System Information"))
        self.host.setText(_translate("MainWindow", "Hostname:"))
        self.pltf.setText(_translate("MainWindow", "Platform:"))
        self.pltf_ver.setText(_translate("MainWindow", "Platform-version:"))
        self.pltf_re.setText(_translate("MainWindow", "Platform-release:"))
        self.ram.setText(_translate("MainWindow", "RAM in GB:"))
        self.cpu.setText(_translate("MainWindow", "Processor:"))
        self.cpu_cores.setText(_translate("MainWindow", "CPU-Cores:"))
        self.ip.setText(_translate("MainWindow", "Ip-address:"))
        self.mac.setText(_translate("MainWindow", "Mac-address:"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
