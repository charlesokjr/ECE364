# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MorphingGUI.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1046, 588)
        self.btnBlend = QtWidgets.QPushButton(Dialog)
        self.btnBlend.setGeometry(QtCore.QRect(430, 550, 92, 27))
        self.btnBlend.setObjectName("btnBlend")
        self.btnLoad1 = QtWidgets.QPushButton(Dialog)
        self.btnLoad1.setGeometry(QtCore.QRect(30, 10, 151, 27))
        self.btnLoad1.setObjectName("btnLoad1")
        self.btnLoad2 = QtWidgets.QPushButton(Dialog)
        self.btnLoad2.setGeometry(QtCore.QRect(540, 10, 151, 27))
        self.btnLoad2.setObjectName("btnLoad2")
        self.chkTri = QtWidgets.QCheckBox(Dialog)
        self.chkTri.setGeometry(QtCore.QRect(380, 250, 131, 22))
        self.chkTri.setObjectName("chkTri")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 250, 101, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(640, 250, 101, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(430, 530, 111, 17))
        self.label_3.setObjectName("label_3")
        self.horizontalSlider = QtWidgets.QSlider(Dialog)
        self.horizontalSlider.setGeometry(QtCore.QRect(80, 280, 691, 19))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(80, 300, 62, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(750, 300, 62, 17))
        self.label_5.setObjectName("label_5")
        self.sliderText = QtWidgets.QTextBrowser(Dialog)
        self.sliderText.setGeometry(QtCore.QRect(780, 280, 61, 31))
        self.sliderText.setObjectName("sliderText")
        self.img1 = QtWidgets.QGraphicsView(Dialog)
        self.img1.setGeometry(QtCore.QRect(30, 40, 291, 211))
        self.img1.setObjectName("img1")
        self.img2 = QtWidgets.QGraphicsView(Dialog)
        self.img2.setGeometry(QtCore.QRect(540, 40, 291, 211))
        self.img2.setObjectName("img2")
        self.imgMorph = QtWidgets.QGraphicsView(Dialog)
        self.imgMorph.setGeometry(QtCore.QRect(330, 320, 291, 211))
        self.imgMorph.setObjectName("imgMorph")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnBlend.setText(_translate("Dialog", "Blend"))
        self.btnLoad1.setText(_translate("Dialog", "Load Starting Image ..."))
        self.btnLoad2.setText(_translate("Dialog", "Load Ending Image ..."))
        self.chkTri.setText(_translate("Dialog", "Show Triangles"))
        self.label.setText(_translate("Dialog", "Starting Image"))
        self.label_2.setText(_translate("Dialog", "Ending Image"))
        self.label_3.setText(_translate("Dialog", "Blending Result"))
        self.label_4.setText(_translate("Dialog", "0.0"))
        self.label_5.setText(_translate("Dialog", "1.0"))

