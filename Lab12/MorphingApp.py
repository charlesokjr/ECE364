#######################################################
#   Author:     <Your Full Name>
#   email:      <Your Email>
#   ID:         <Your course ID, e.g. ee364j20>
#   Date:       <Start Date>
#######################################################

import sys
import os

from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QGraphicsScene
from MorphingGUI import *
import Morphing
from scipy.spatial import Delaunay
import numpy as np
import imageio
import matplotlib.pyplot as plt
import re


class Morphy(QMainWindow, Ui_Dialog):

    def __init__(self, parent=None):

        super(Morphy, self).__init__(parent)
        self.setupUi(self)
        self.figure = 0
        self.imgOne = False
        self.imgTwo = False
        self.leftPts = 0
        self.leftImg = 0
        self.rightPts = 0
        self.rightImg = 0
        self.morphed = 0
        self.figure = 0
        self.sizes = []
        self.lList = []
        self.rList = []
        self.lPoints = np.empty(0)
        self.rPoints = np.empty(0)
        self.lColors = []
        self.rColors = []
        self.btnBlend.setEnabled(False)
        self.btnBlend.clicked.connect(self.Morph)
        self.chkTri.stateChanged.connect(self.check)
        self.btnLoad1.clicked.connect(self.load1)
        self.btnLoad2.clicked.connect(self.load2)
        self.horizontalSlider.setEnabled(False)
        self.horizontalSlider.valueChanged.connect(self.textSlide)
        self.sliderText.setEnabled(False)

    def mousePressEvent(self, QMouseEvent):
        if len(self.rColors) == len(self.lColors) and self.imgOne and self.imgTwo:
            for index, val in enumerate(self.lColors):
                if val == 'og':
                    with open(self.leftPts, 'a') as f:
                        f.write(str(self.lPoints[index][0]) + ' ' + str(self.lPoints[index][1]) + '\n')
                    self.lColors[index] = 'ob'
            for index, val in enumerate(self.rColors):
                if val == 'og':
                    with open(self.rightPts, 'a') as f:
                        f.write(str(self.rPoints[index][0]) + ' ' + str(self.rPoints[index][1]) + '\n')
                    self.rColors[index] = 'ob'
            self.figure += 1
            plt.figure(self.figure)
            for index, val in enumerate(self.lColors):
                plt.plot(self.lPoints[index, 0], self.lPoints[index, 1], self.lColors[index])
            plt.imshow(plt.imread(self.leftImg), cmap="gray")
            plt.axis('off')
            plt.grid(b=None)
            plt.savefig('leftTri.png')
            scene = QGraphicsScene()
            scene.addPixmap(QPixmap('leftTri.png').scaled(216, 162))
            self.img1.setScene(scene)
            self.figure += 1
            plt.figure(self.figure)
            for index, val in enumerate(self.rColors):
                plt.plot(self.rPoints[index, 0], self.rPoints[index, 1], self.rColors[index])
            plt.imshow(plt.imread(self.rightImg), cmap="gray")
            plt.axis('off')
            plt.grid(b=None)
            plt.savefig('rightTri.png')
            scene = QGraphicsScene()
            scene.addPixmap(QPixmap('rightTri.png').scaled(216, 162))
            self.img2.setScene(scene)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Backspace:
            self.deletePoint()

    def load1(self):
        self.leftPts = 0
        self.loadData(1)

    def load2(self):
        self.rightPts = 0
        self.loadData(2)

    def textSlide(self):
        self.sliderText.setText(str(self.horizontalSlider.sliderPosition() / 20))

    def check(self):
        if self.chkTri.isChecked():
            rightD = np.array(Delaunay(self.lPoints).simplices)
            self.figure += 1
            plt.figure(self.figure)
            plt.imshow(plt.imread(self.rightImg), cmap="gray")
            plt.triplot(self.rPoints[:, 0], self.rPoints[:, 1], rightD, color='red')
            plt.axis('off')
            plt.grid(b=None)
            plt.savefig('rightTri.png')
            self.figure += 1
            plt.figure(self.figure)
            plt.axis('off')
            plt.grid(b=None)
            plt.imshow(plt.imread(self.leftImg), cmap="gray")
            plt.triplot(self.lPoints[:, 0], self.lPoints[:, 1], rightD, color='red')
            for index, val in enumerate(self.lColors):
                plt.plot(self.lPoints[index, 0], self.lPoints[index, 1], self.lColors[index])
            plt.savefig('leftTri.png')
            scene = QGraphicsScene()
            scene.addPixmap(QPixmap('rightTri.png').scaled(216, 162))
            self.img2.setScene(scene)
            scene = QGraphicsScene()
            scene.addPixmap(QPixmap('leftTri.png').scaled(216, 162))
            self.img1.setScene(scene)
        if not self.chkTri.isChecked():
            self.figure += 1
            plt.figure(self.figure)
            plt.imshow(plt.imread(self.rightImg), cmap="gray")
            for index, val in enumerate(self.rColors):
                plt.plot(self.rPoints[index, 0], self.rPoints[index, 1], self.rColors[index])
            plt.axis('off')
            plt.grid(b=None)
            plt.savefig('rightTri.png')
            self.figure += 1
            plt.figure(self.figure)
            plt.axis('off')
            plt.grid(b=None)
            plt.imshow(plt.imread(self.leftImg), cmap="gray")
            for index, val in enumerate(self.lColors):
                plt.plot(self.lPoints[index, 0], self.lPoints[index, 1], self.lColors[index])
            plt.savefig('leftTri.png')
            scene = QGraphicsScene()
            scene.addPixmap(QPixmap('rightTri.png').scaled(216, 162))
            self.img2.setScene(scene)
            scene = QGraphicsScene()
            scene.addPixmap(QPixmap('leftTri.png').scaled(216, 162))
            self.img1.setScene(scene)

    def deletePoint(self):
        if len(self.rColors) and self.rColors[0] == 'og':
            self.figure += 1
            plt.figure(self.figure)
            plt.imshow(plt.imread(self.rightImg), cmap="gray")
            self.rColors = []
            self.rList = []
            self.rPoints = np.empty(0)
            plt.axis('off')
            plt.grid(b=None)
            plt.savefig('rightTri.png')
            scene = QGraphicsScene()
            scene.addPixmap(QPixmap('rightTri.png').scaled(216, 162))
            self.img2.setScene(scene)
        elif self.lColors[0] == 'og':
            self.figure += 1
            plt.figure(self.figure)
            plt.imshow(plt.imread(self.leftImg), cmap="gray")
            self.lColors = []
            self.lList = []
            self.lPoints = np.empty(0)
            plt.axis('off')
            plt.grid(b=None)
            plt.savefig('leftTri.png')
            scene = QGraphicsScene()
            scene.addPixmap(QPixmap('leftTri.png').scaled(216, 162))
            self.img1.setScene(scene)
        elif self.rColors[-1] == 'og':
            self.figure += 1
            plt.figure(self.figure)
            plt.imshow(plt.imread(self.rightImg), cmap="gray")
            del self.rColors[-1]
            del self.rList[-1]
            self.rPoints = np.delete(self.rPoints, -1, 0)
            for index, val in enumerate(self.rColors):
                plt.plot(self.rPoints[index, 0], self.rPoints[index, 1], self.rColors[index])
            plt.axis('off')
            plt.grid(b=None)
            plt.savefig('rightTri.png')
            scene = QGraphicsScene()
            scene.addPixmap(QPixmap('rightTri.png').scaled(216, 162))
            self.img2.setScene(scene)
        elif self.lColors[-1] == 'og':
            self.figure += 1
            plt.figure(self.figure)
            plt.imshow(plt.imread(self.leftImg), cmap="gray")
            del self.lColors[-1]
            del self.lList[-1]
            np.delete(self.lPoints, -1)
            for index, val in enumerate(self.lColors):
                plt.plot(self.lPoints[index, 0], self.lPoints[index, 1], self.lColors[index])
            plt.axis('off')
            plt.grid(b=None)
            plt.savefig('leftTri.png')
            scene = QGraphicsScene()
            scene.addPixmap(QPixmap('leftTri.png').scaled(216, 162))
            self.img1.setScene(scene)

    def loadData(self, i):
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Select image', filter="jpg, png files (*.jpg, *.png)")
        if not filePath:
            return
        self.loadDataFromFile(filePath, i)

    def loadDataFromFile(self, filePath, i):
        status = 0
        if i == 1:
            self.figure += 1
            plt.figure(self.figure)
            self.lList = []
            self.lPoints = 0
            for file in os.listdir(os.curdir):
                if os.getcwd() + '/' + file == filePath + '.txt':
                    self.leftPts = filePath + ".txt"
                    status = 1
                    with open(self.leftPts, 'r') as fl:
                        l = fl.readlines()
                    if l[-1][-1] is not '\n':
                        with open(self.leftPts, 'a') as fa:
                            fa.write('\n')
                    for line in l:
                        self.lList.append([float(line.split()[0]), float(line.split()[1])])
                        self.lColors.append('or')
                    self.lPoints = np.array(self.lList)
                    for index, val in enumerate(self.lColors):
                        plt.plot(self.lPoints[index, 0], self.lPoints[index, 1], self.lColors[index])
            if not status:
                with open(filePath + '.txt', 'w') as f:
                    self.leftPts = filePath + '.txt'
                self.lList = []
                self.lPoints = np.array(self.lList)
                self.lColors = []
            self.imgOne = True
            plt.axis('off')
            plt.grid(b=None)
            self.leftImg = filePath
            self.sizes = [len(np.array(imageio.imread(self.leftImg))), len(np.array(imageio.imread(self.leftImg))[0])]
            plt.imshow(plt.imread(self.leftImg), cmap="gray")
            plt.savefig('leftTri.png')
            scene = QGraphicsScene()
            scene.addPixmap(QPixmap('leftTri.png').scaled(216, 162))
            self.img1.setScene(scene)
        elif i == 2:
            self.figure += 1
            plt.figure(self.figure)
            self.rList = []
            self.rPoints = 0
            for file in os.listdir(os.curdir):
                if os.getcwd() + '/' + file == filePath + '.txt':
                    self.rightPts = filePath + ".txt"
                    status = 1
                    with open(self.rightPts, 'r') as fr:
                        r = fr.readlines()
                    if r[-1][-1] is not '\n':
                        with open(self.rightPts, 'a') as fa:
                            fa.write('\n')
                    for line in r:
                        self.rList.append([float(line.split()[0]), float(line.split()[1])])
                        self.rColors.append('or')
                    self.rPoints = np.array(self.rList)
                    for index, val in enumerate(self.rColors):
                        plt.plot(self.rPoints[index, 0], self.rPoints[index, 1], self.rColors[index])
            if not status:
                with open(filePath + '.txt', 'w') as f:
                    self.rightPts = filePath + '.txt'
                self.rList = []
                self.rPoints = np.array(self.rList)
                self.rColors = []
            self.imgTwo = True
            self.rightImg = filePath
            plt.imshow(plt.imread(self.rightImg), cmap="gray")
            plt.axis('off')
            plt.grid(b=None)
            plt.savefig('rightTri.png')
            scene = QGraphicsScene()
            scene.addPixmap(QPixmap('rightTri.png').scaled(216, 162))
            self.img2.setScene(scene)
        if self.imgOne and self.imgTwo:
            self.btnBlend.setEnabled(True)
            self.horizontalSlider.setEnabled(True)
            self.horizontalSlider.setMaximum(20)
            self.horizontalSlider.setMinimum(0)
            for tick in range(0, 20):
                self.horizontalSlider.setTickPosition(tick)
            self.sliderText.setEnabled(True)
            self.sliderText.setText(str(0.0))
            self.img1.mousePressEvent = self.mouse1
            self.img2.mousePressEvent = self.mouse2
        pass

    def mouse1(self, event):
        if len(self.rColors) == len(self.lColors):
            for index, val in enumerate(self.lColors):
                if val == 'og':
                    with open(self.leftPts, 'a') as f:
                        f.write(str(self.lPoints[index][0]) + ' ' + str(self.lPoints[index][1]) + '\n')
                    self.lColors[index] = 'ob'
            for index, val in enumerate(self.rColors):
                if val == 'og':
                    with open(self.rightPts, 'a') as f:
                        f.write(str(self.rPoints[index][0]) + ' ' + str(self.rPoints[index][1]) + '\n')
                    self.rColors[index] = 'ob'
            self.figure += 1
            plt.figure(self.figure)
            plt.imshow(plt.imread(self.leftImg), cmap="gray")
            if (291 - 162) / 2 < event.pos().x() < (162 + (291 - 162) / 2) and (211 - 120) / 2 < event.pos().y() < (120 + (211 - 120) / 2):
                self.lList.append([(event.pos().x() - (291 - 162) / 2) * self.sizes[1] / 162, (event.pos().y() - (211 - 120) / 2) * self.sizes[0] / 120])
                self.lPoints = np.array(self.lList)
                self.lColors.append('og')
            if self.chkTri.isChecked():
                if self.lColors[-1] == 'og':
                    rightD = np.array(Delaunay(self.lPoints[:-1]).simplices)
                    plt.triplot(self.lPoints[:-1][:, 0], self.lPoints[:-1][:, 1], rightD, color='red')
                else:
                    rightD = np.array(Delaunay(self.lPoints).simplices)
                    plt.triplot(self.lPoints[:, 0], self.lPoints[:, 1], rightD, color='red')
            for index, val in enumerate(self.lColors):
                plt.plot(self.lPoints[index, 0], self.lPoints[index, 1], self.lColors[index])
            plt.axis('off')
            plt.grid(b=None)
            plt.savefig('leftTri.png')
            scene = QGraphicsScene()
            scene.addPixmap(QPixmap('leftTri.png').scaled(216, 162))
            self.img1.setScene(scene)
            self.figure += 1
            plt.figure(self.figure)
            for index, val in enumerate(self.rColors):
                plt.plot(self.rPoints[index, 0], self.rPoints[index, 1], self.rColors[index])
            plt.imshow(plt.imread(self.rightImg), cmap="gray")
            plt.axis('off')
            plt.grid(b=None)
            plt.savefig('rightTri.png')
            scene = QGraphicsScene()
            scene.addPixmap(QPixmap('rightTri.png').scaled(216, 162))
            self.img2.setScene(scene)

    def mouse2(self, event):
        if len(self.rColors) + 1 == len(self.lColors):
            for index, val in enumerate(self.rColors):
                if val == 'og':
                    with open(self.rightPts, 'a') as f:
                        f.write(str(self.rPoints[index][0]) + ' ' + str(self.rPoints[index][1]) + '\n')
                    self.rColors[index] = 'ob'
            self.figure += 1
            plt.figure(self.figure)
            plt.imshow(plt.imread(self.rightImg), cmap="gray")
            if (291 - 162) / 2 < event.pos().x() < (162 + (291 - 162) / 2) and (211 - 120) / 2 < event.pos().y() < (120 + (211 - 120) / 2):
                self.rList.append([(event.pos().x() - (291 - 162) / 2) * self.sizes[1] / 162, (event.pos().y() - (211 - 120) / 2) * self.sizes[0] / 120])
                self.rPoints = np.array(self.rList)
                self.rColors.append('og')
            for index, val in enumerate(self.rColors):
                plt.plot(self.rPoints[index, 0], self.rPoints[index, 1], self.rColors[index])
            if self.chkTri.isChecked():
                rightD = np.array(Delaunay(self.lPoints).simplices)
                plt.triplot(self.rPoints[:, 0], self.rPoints[:, 1], rightD, color='red')
            plt.axis('off')
            plt.grid(b=None)
            plt.savefig('rightTri.png')
            scene = QGraphicsScene()
            scene.addPixmap(QPixmap('rightTri.png').scaled(216, 162))
            self.img2.setScene(scene)

    def Morph(self):
        for index, val in enumerate(self.lColors):
            if val == 'og':
                with open(self.leftPts, 'a') as f:
                    f.write(str(self.lPoints[index][0]) + ' ' + str(self.lPoints[index][1]) + '\n')
                self.lColors[index] = 'ob'
        for index, val in enumerate(self.rColors):
            if val == 'og':
                with open(self.rightPts, 'a') as f:
                    f.write(str(self.rPoints[index][0]) + ' ' + str(self.rPoints[index][1]) + '\n')
                self.rColors[index] = 'ob'
        i1, i2 = np.array(imageio.imread(self.leftImg)), np.array(imageio.imread(self.rightImg))
        t1, t2 = Morphing.loadTriangles(self.leftPts, self.rightPts)
        if type(i1[0][0]) == np.dtype('uint8'):
            m = Morphing.Morpher(i1, t1, i2, t2)
        else:
            m = Morphing.ColorMorpher(i1, t1, i2, t2)
        imageio.imwrite('mix.png', m.getImageAtAlpha(float(self.sliderText.toPlainText())))
        self.morphed = 'mix.png'
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap(self.morphed).scaled(216, 162))
        self.imgMorph.setScene(scene)


if __name__ == "__main__":
    plt.close('all')
    currentApp = QApplication(sys.argv)
    currentForm = Morphy()

    currentForm.show()
    currentApp.exec_()
