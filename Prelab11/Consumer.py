
#######################################################
#   Author:     <Your Full Name>
#   email:      <Your Email>
#   ID:         <Your course ID, e.g. ee364j20>
#   Date:       <Start Date>
#######################################################

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from BasicUI import *
import re


class Consumer(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(Consumer, self).__init__(parent)
        self.setupUi(self)

        self.btnSave.setEnabled(False)
        self.texts = [self.txtComponentName_1, self.txtComponentName_2, self.txtComponentName_3,
                 self.txtComponentName_4, self.txtComponentName_5, self.txtComponentName_6,
                 self.txtComponentName_7, self.txtComponentName_8, self.txtComponentName_9,
                 self.txtComponentName_10, self.txtComponentName_11, self.txtComponentName_12,
                 self.txtComponentName_13, self.txtComponentName_14, self.txtComponentName_15,
                 self.txtComponentName_16, self.txtComponentName_17, self.txtComponentName_18,
                 self.txtComponentName_19, self.txtComponentName_20, self.txtComponentCount_1,
                 self.txtComponentCount_2, self.txtComponentCount_3,
                 self.txtComponentCount_4, self.txtComponentCount_5, self.txtComponentCount_6,
                 self.txtComponentCount_7, self.txtComponentCount_8, self.txtComponentCount_9,
                 self.txtComponentCount_10, self.txtComponentCount_11, self.txtComponentCount_12,
                 self.txtComponentCount_13, self.txtComponentCount_14, self.txtComponentCount_15,
                 self.txtComponentCount_16, self.txtComponentCount_17, self.txtComponentCount_18,
                 self.txtComponentCount_19, self.txtComponentCount_20, self.txtStudentID,
                 self.txtStudentName]
        for t in self.texts:
            t.textEdited.connect(self.check)
        self.cboCollege.currentIndexChanged.connect(self.check)
        self.chkGraduate.stateChanged.connect(self.check)
        self.btnLoad.clicked.connect(self.loadData)
        self.btnSave.clicked.connect(self.saveData)
        self.btnClear.clicked.connect(self.displayName)

    def check(self):

        for t in self.texts:
            if t.text() != '':
                self.btnSave.setEnabled(True)
                self.btnLoad.setEnabled(False)
                return
        if self.chkGraduate.isChecked():
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
            return
        if self.cboCollege.currentText() != '-----':
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
            return

        self.btnSave.setEnabled(False)
        self.btnLoad.setEnabled(True)

    def displayName(self):
        self.btnSave.setEnabled(False)
        self.btnLoad.setEnabled(True)
        for t in self.texts:
            t.setText('')
        self.cboCollege.setCurrentText('-----')
        self.chkGraduate.setChecked(False)


    def saveData(self):
        with open('target.xml', 'w') as f:
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n<Content>\n')
            f.write('    <StudentName graduate="' + str.lower(str(self.chkGraduate.isChecked())) + '">' + self.txtStudentName.text() + '</StudentName>\n')
            f.write('    <StudentID>' + self.txtStudentID.text() + '</StudentID>\n')
            f.write('    <College>' + self.cboCollege.currentText() + '</College>\n    <Components>\n')
            names = [self.txtComponentName_1.text(), self.txtComponentName_2.text(), self.txtComponentName_3.text(), self.txtComponentName_4.text(), self.txtComponentName_5.text(), self.txtComponentName_6.text(), self.txtComponentName_7.text(), self.txtComponentName_8.text(), self.txtComponentName_9.text(), self.txtComponentName_10.text(), self.txtComponentName_11.text(), self.txtComponentName_12.text(), self.txtComponentName_13.text(), self.txtComponentName_14.text(), self.txtComponentName_15.text(), self.txtComponentName_16.text(), self.txtComponentName_17.text(), self.txtComponentName_18.text(), self.txtComponentName_19.text(), self.txtComponentName_20.text()]
            counts = [self.txtComponentCount_1.text(), self.txtComponentCount_2.text(), self.txtComponentCount_3.text(), self.txtComponentCount_4.text(), self.txtComponentCount_5.text(), self.txtComponentCount_6.text(), self.txtComponentCount_7.text(), self.txtComponentCount_8.text(), self.txtComponentCount_9.text(), self.txtComponentCount_10.text(), self.txtComponentCount_11.text(), self.txtComponentCount_12.text(), self.txtComponentCount_13.text(), self.txtComponentCount_14.text(), self.txtComponentCount_15.text(), self.txtComponentCount_16.text(), self.txtComponentCount_17.text(), self.txtComponentCount_18.text(), self.txtComponentCount_19.text(), self.txtComponentCount_20.text()]
            for index, name in enumerate(names):
                if name != '':
                    f.write('        <Component name="' + name + '" count="' +  counts[index] + '" />\n')
            f.write('    </Components>\n</Content>')


    def loadData(self):
        """
        *** DO NOT MODIFY THIS METHOD! ***
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        You must modify the method below.
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return

        self.loadDataFromFile(filePath)

    def loadDataFromFile(self, filePath):
        with open(filePath, 'r') as f:
            text = f.read()
        id = re.findall(r"<StudentID>(.+?)</StudentID>", text)
        name = re.findall(r">(.+?)</StudentName>", text)
        college = re.findall(r"<College>(.+?)</College>", text)

        if len(id):
            self.txtStudentID.setText(id[0])
        if len(name):
            self.txtStudentName.setText(name[0])
        if re.findall(r"<StudentName graduate=\"(.+?)\">", text)[0] == 'true':
            self.chkGraduate.setChecked(True)
        else:
            self.chkGraduate.setChecked(False)
        for index, nameCount in enumerate(re.findall(r"<Component name=\"(.+?)\" count=\"(.+?)\" />", text)):
            exec("self.txtComponentName_" + str(int(index)+1) + ".setText(nameCount[0])")
            exec("self.txtComponentCount_" + str(int(index)+1) + ".setText(nameCount[1])")
        if len(college):
            self.cboCollege.setCurrentText(college[0])

        """
        Handles the loading of the data from the given file name. This method will be invoked by the 'loadData' method.
        
        *** YOU MUST USE THIS METHOD TO LOAD DATA FILES. ***
        *** This method is required for unit tests! ***
        """

        pass



if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()
