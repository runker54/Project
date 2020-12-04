#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date:2020-12-03
# Author:Runker54
# -----------------------
# !/usr/bin/env python3

import time
from subprocess import Popen, PIPE
import shlex
import os
import re
from glob import glob
import signal
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow,
                             QInputDialog, QFileDialog, QVBoxLayout, QHBoxLayout, QPushButton,
                             QTableWidget, QTableWidgetItem, QCheckBox, QLabel, QDialog, QLineEdit,
                             QDialogButtonBox, QSpinBox, QComboBox, QMessageBox, QFormLayout,
                             QRadioButton, QStatusBar, QProgressBar, QFrame, QColorDialog,
                             QDoubleSpinBox, QStyle, QPlainTextEdit, QGridLayout)
from PyQt5.QtCore import Qt
from threading import Thread
from PyQt5.QtGui import QPixmap, QIcon, QColor, QPalette


class ImageOptions:

    def __init__(self, info={}):
        """Optionally pass in an initial dictionary of items"""
        if type(info) != type({}):
            raise TypeError("ImageOptions requires a dictionary, but was given %s" % type(info))
        self.info = info
        return

    def add_info(self, info_dict):
        """Add information via a dictionary"""
        if type(info_dict) != type({}):
            raise TypeError("Add_info requires a dictionary, but was given %s"
                            % type(info_dict))

        for key in info_dict.keys():
            self.info[key] = info_dict[key]

    def has_info(self, key):
        """Check whether the required key is present or not"""
        try:
            value = self.info[key]
            return True
        except KeyError:
            return False

    def update_info(self, key, value):
        """ Update the dictionary as long as the key already exits."""
        if self.has_info(key):
            self.info[key] = value
            return True
        else:
            return False

    def print_info(self, key):
        """Return the info corresponding to key"""
        return self.info[key]

    def get_dict(self):
        return self.info


# https://gist.github.com/onlyjus/d7f99fb16e9e904e3ba0
class ProgressDialog(QDialog):
    def __init__(self):
        super(ProgressDialog, self).__init__()

        self.setWindowTitle('Sign PDF GUI')

        vbox = QVBoxLayout()
        self.setLayout(vbox)

        self.label = QLabel()
        vbox.addWidget(self.label)

        self.bar = QProgressBar()
        vbox.addWidget(self.bar)

        self.btns = QDialogButtonBox()
        self.btns.setStandardButtons(QDialogButtonBox.Cancel |
                                     QDialogButtonBox.Ok)
        vbox.addWidget(self.btns)

        # The Ok button is initially disabled
        self.btns.button(QDialogButtonBox.Ok).setEnabled(False)

        self.btns.accepted.connect(self.accept)
        self.btns.rejected.connect(self.reject)

    def setRange(self, min_, max_):
        self.bar.setRange(min_, max_)

    def setMinimum(self, value):
        self.bar.setMinimum(value)

    def setMaximum(self, value):
        self.bar.setMaximum(value)

    def setValue(self, value):
        self.bar.setValue(value)

    def setFormat(self, string):
        self.bar.setFormat(string)


# Thread to do the work
class Worker:

    def __init__(self, instance):
        self.keepRunning = True
        self.instance = instance

    def terminate(self):
        self.keepRunning = False
        try:
            os.kill(self.proc.pid, signal.SIGTERM)
        except ProcessLookupError:
            return

    def run(self):

        cmd = self.instance.cliApp
        if self.instance.showGrid.isChecked():
            cmd = cmd + ' -g '

        if self.instance.otherConfigs['multiple']:
            cmd = cmd + ' -m '

        cmd = cmd + ' -t ' + str(self.instance.otherConfigs['threshold'])
        cmd = cmd + ' -m ' + self.instance.otherConfigs['mask']

        # m = List of image
        m = len(self.instance.listImage)
        for j in range(0, m):
            imgDict = self.instance.listImage[j].get_dict()

            imageOptions = '"' + imgDict['image'] + '"' + ','

            if imgDict['type'] == 'template':
                imageOptions = imageOptions + imgDict['template'] + ','

            imageOptions = (imageOptions + imgDict['xvalue'] + ','
                            + imgDict['yvalue'] + ',' + str(imgDict['scale']) + ','
                            + str(imgDict['page']) + ',' + str(imgDict['rotation']))

            cmd = cmd + ' -i ' + imageOptions

        # n = List of pdf files
        n = len(self.instance.listPdf)

        self.instance.statusBar.showMessage("Starting...")
        i = 0
        while self.keepRunning and i < n:

            ifileBasename = os.path.basename(self.instance.listPdf[i])
            self.instance.pd.label.setText('Working on "'
                                           + ifileBasename + '"')

            cmdFinal = cmd + ' "' + self.instance.listPdf[i] + '"'

            if self.instance.printCmd.isChecked():
                print(cmdFinal)

            self.proc = Popen(shlex.split(cmdFinal), stdout=PIPE, stderr=PIPE,
                              shell=False)
            stdout, stderr = self.proc.communicate()
            rtn = self.proc.returncode

            if rtn != 0:
                self.instance.statusBar.showMessage(
                    "Problem in running code or canceled.")
                return rtn

            self.instance.pd.setValue(i + 1)

            # If reached the end of the bar, then enable the Ok button
            if i + 1 == n:
                self.instance.pd.btns.button(
                    QDialogButtonBox.Ok).setEnabled(True)

            i += 1

        self.instance.statusBar.showMessage("Done!")
        return


# File Dialog with preview for images selected
# https://stackoverflow.com/questions/47599170/qfiledialog-preview
class QFileDialogPreview(QFileDialog):
    def __init__(self, *args, **kwargs):
        QFileDialog.__init__(self, *args, **kwargs)
        self.setOption(QFileDialog.DontUseNativeDialog, True)

        box = QVBoxLayout()

        self.setFixedSize(self.width() + 250, self.height())

        self.mpPreview = QLabel("Preview", self)
        self.mpPreview.setFixedSize(250, 250)
        self.mpPreview.setAlignment(Qt.AlignCenter)
        self.mpPreview.setObjectName("labelPreview")
        box.addWidget(self.mpPreview)

        box.addStretch()

        self.layout().addLayout(box, 1, 3, 1, 1)

        self.currentChanged.connect(self.onChange)
        self.fileSelected.connect(self.onFileSelected)
        self.filesSelected.connect(self.onFilesSelected)

        self._fileSelected = None
        self._filesSelected = None

    def onChange(self, path):
        pixmap = QPixmap(path)

        if (pixmap.isNull()):
            self.mpPreview.setText("Preview")
        else:
            self.mpPreview.setPixmap(pixmap.scaled(self.mpPreview.width(),
                                                   self.mpPreview.height(), Qt.KeepAspectRatio,
                                                   Qt.SmoothTransformation))

    def onFileSelected(self, file):
        self._fileSelected = file

    def onFilesSelected(self, files):
        self._filesSelected = files

    def getFileSelected(self):
        return self._fileSelected

    def getFilesSelected(self):
        return self._filesSelected


class OtherDialog(QDialog):

    def __init__(self, inputDict):
        super(OtherDialog, self).__init__()

        self.setWindowTitle('Other configurations')

        mltpl = inputDict['multiple']
        thrshld = inputDict['threshold']
        msk = inputDict['mask']

        vbox = QVBoxLayout()
        self.setLayout(vbox)

        label = QLabel("(*) Only meant for image inserted by template")
        vbox.addWidget(label)

        hline = QFrame()
        hline.setFrameStyle(hline.HLine)
        hline.setLineWidth(1)
        vbox.addWidget(hline)

        formLayout = QFormLayout()
        vbox.addLayout(formLayout)

        self.multiple = QCheckBox()
        self.multiple.setChecked(mltpl)
        formLayout.addRow("Multiple Match (*):", self.multiple)

        self.threshold = QDoubleSpinBox()
        self.threshold.setDecimals(1)
        self.threshold.setRange(0, 1)
        self.threshold.setSingleStep(0.1)
        self.threshold.setValue(thrshld)
        formLayout.addRow("Threshold (*):", self.threshold)

        hbox = QHBoxLayout()

        colorBtn = QPushButton("Select")
        colorBtn.clicked.connect(self.colorBtn_clicked)
        hbox.addWidget(colorBtn)

        _, red, _, green, _, blue = msk.split(',')
        self.backgroundColor = ("background-color: rgb(" + red + ","
                                + green + "," + blue + ")")
        self.borderColor = "border: 1px solid black"

        self.frame = QFrame()
        self.frame.setStyleSheet(self.borderColor + ";"
                                 + self.backgroundColor)
        hbox.addWidget(self.frame)

        formLayout.addRow("Image background color:", hbox)

        self.btns = QDialogButtonBox()
        self.btns.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        vbox.addWidget(self.btns)

        self.btns.accepted.connect(self.accept)
        self.btns.rejected.connect(self.reject)

    def colorBtn_clicked(self):

        colorDialog = QColorDialog()
        colorDialog.setOption(QColorDialog.ShowAlphaChannel)
        color = colorDialog.getColor()

        if color.isValid():
            self.frame.setStyleSheet(self.borderColor + ";"
                                     + 'background-color: %s' % color.name())
        return

    def getMask(self):
        ''' Get the background color of the frame. '''

        # Get the background color of the frame
        frameColor = self.frame.palette().color(QPalette.Background)
        red, green, blue, alpha = (frameColor.red(), frameColor.green(),
                                   frameColor.blue(), frameColor.alpha())

        # Create a mask list
        maskList = []
        for c in red, green, blue:
            if int(c) == 0:
                maskList.append(str(c))
                maskList.append(str(int(c) + 2))
            elif int(c) == 255:
                maskList.append(str(int(c) - 2))
                maskList.append(str(c))
            else:
                maskList.append(str(int(c) - 1))
                maskList.append(str(int(c) + 1))
        # Join the list with comma
        mask = ','.join(maskList)

        return mask

    def accept(self):

        mask = self.getMask()

        # Create an empty dictionary
        self._output = {}

        # Fill the dictionary with values
        self._output['multiple'] = self.multiple.isChecked()
        self._output['threshold'] = self.threshold.value()
        self._output['mask'] = mask

        super(OtherDialog, self).accept()
        return

    def get_output(self):
        return self._output


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__()

        self.setWindowTitle('Sign PDF GUI')

        self.author = kwargs['author']
        self.version = kwargs['version']
        self.cliApp = kwargs['cliApp']

        self.title = 'Sign PDF GUI'

        cliAppBasename = os.path.splitext(self.cliApp)[0]

        scriptDir = os.path.dirname(os.path.realpath(__file__))
        iconPath = os.path.sep.join([scriptDir, 'icon', cliAppBasename])
        self.setWindowIcon(QIcon(iconPath))

        self.listPdf = []  # List of pdfs
        self.listImage = []  # List of images

        if 'pdflist' in kwargs.keys() and len(kwargs['pdflist']) > 0:
            n = len(kwargs['pdflist'])
            for i in range(0, n):
                self.listPdf.append(os.path.realpath(kwargs['pdflist'][i]))

        self.left = 10
        self.top = 10
        self.width = 700
        self.height = 480
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.btnWidth = 100
        self.btnHeight = 30
        self.selectAllWidth = 70

        widget = QWidget()
        self.setCentralWidget(widget)

        self.vbox = QVBoxLayout()
        widget.setLayout(self.vbox)

        multiple = False
        threshold = 0.9
        mask = "254,255,254,255,254,255"

        self.otherConfigs = {
            'multiple': multiple,
            'threshold': threshold,
            'mask': mask
        }

        self.createPdfBox()
        self.createPdfTable()
        self.createImageBox()
        self.createImageTable()
        self.createButtonBox()
        self.createStatusBar()

        self.updatePdfTable()

    def createPdfBox(self):

        hbox = QHBoxLayout()
        self.vbox.addLayout(hbox)
        self.vbox.setAlignment(Qt.AlignTop)

        addPdfBtn = QPushButton("Add PDF", self)
        addPdfBtn.setFixedSize(self.btnWidth, self.btnHeight)
        addPdfBtn.clicked.connect(self.addPdfFiles)
        hbox.addWidget(addPdfBtn)

        delPdfBtn = QPushButton("Remove PDF", self)
        delPdfBtn.setFixedSize(self.btnWidth, self.btnHeight)
        delPdfBtn.clicked.connect(self.delPdfFiles)
        hbox.addWidget(delPdfBtn)

        hbox.addStretch(1)

        self.showGrid = QCheckBox("Show grid")
        self.showGrid.stateChanged.connect(self.showGridState)
        hbox.addWidget(self.showGrid)

        self.printCmd = QCheckBox("Print cmd")
        self.printCmd.stateChanged.connect(self.printCmdState)
        hbox.addWidget(self.printCmd)

        otherBtn = QPushButton("Others")
        otherBtn.setFixedSize(self.btnWidth, self.btnHeight)
        otherBtn.clicked.connect(self.otherBtn_clicked)
        hbox.addWidget(otherBtn)

    def createPdfTable(self):

        npdf = len(self.listPdf)

        self.pdfTable = QTableWidget()
        self.pdfTable.setRowCount(npdf)
        self.pdfTable.setColumnCount(2)

        self.pdfTable.setHorizontalHeaderLabels(
            "Select All;PDF Filename".split(";"))

        header = self.pdfTable.horizontalHeader()
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.resizeSection(0, self.selectAllWidth)

        self.vbox.setAlignment(Qt.AlignTop)
        #         self.pdfTable.setMaximumHeight(self.tableMaxHeight)
        self.vbox.addWidget(self.pdfTable)

        # If header is clicked
        self.selectAllPdf = False
        header.sectionClicked.connect(self.onPdfTableHeaderClicked)

    def onPdfTableHeaderClicked(self, logicalIndex):
        n = len(self.listPdf)
        if logicalIndex == 0:  # If the first row is clicked

            if not self.selectAllPdf:  # If self.selectAllPdf is False
                self.selectAllPdf = True
                for r in range(0, n):
                    self.pdfTable.cellWidget(r, 0).findChild(
                        type(QCheckBox())).setChecked(True)

            else:
                self.selectAllPdf = False
                for r in range(0, n):
                    self.pdfTable.cellWidget(r, 0).findChild(
                        type(QCheckBox())).setChecked(False)

    def createImageBox(self):

        hbox = QHBoxLayout()
        self.vbox.addLayout(hbox)

        addImageBtn = QPushButton("Add Image")
        addImageBtn.setFixedSize(self.btnWidth, self.btnHeight)
        addImageBtn.clicked.connect(lambda x:
                                    self.addEditImage(False))
        hbox.addWidget(addImageBtn)

        delImageBtn = QPushButton("Remove Image")
        delImageBtn.setFixedSize(self.btnWidth, self.btnHeight)
        delImageBtn.clicked.connect(self.delImageFiles)
        hbox.addWidget(delImageBtn)

        hbox.addStretch(1)

    def delImageFiles(self):

        # Clear the status message
        self.statusBar.clearMessage()

        self.selectAllImage = False

        n = len(self.listImage)
        for r in range(0, n):
            if self.imageTable.cellWidget(r, 0).findChild(
                    type(QCheckBox())).isChecked():
                # Remove the element from the list
                del self.listImage[r]

                # Insert blank in the list so that the number of
                # elements remain the same.
                self.listImage.insert(r, "")

                # Remove the blanks that had been inserted
        while ("" in self.listImage):
            self.listImage.remove("")

        # Update the table
        self.updateImageTable()
        return

    def createImageTable(self):

        n = len(self.listImage)

        self.imageTable = QTableWidget()
        self.imageTable.setRowCount(n)
        self.imageTable.setColumnCount(9)

        self.imageTable.setHorizontalHeaderLabels(
            "Select All;Edit;Image;Template;XValue;YValue;Scale;Page;Rotation".split(";"))

        header = self.imageTable.horizontalHeader()
        #         header.setSectionResizeMode(1,QtWidgets.QHeaderView.Stretch)
        header.resizeSection(0, self.selectAllWidth)
        header.resizeSection(1, 46)

        self.vbox.setAlignment(Qt.AlignTop)
        #         self.imageTable.setMaximumHeight(self.tableMaxHeight)
        self.vbox.addWidget(self.imageTable)

        # If header is clicked
        self.selectAllImage = False
        header.sectionClicked.connect(self.onImageTableHeaderClicked)

        self.imageTable.itemChanged.connect(self.itemChangedText)

        return

    # If cell value have changed, then update them on the dictionary
    def itemChangedText(self, item):
        row = item.row()
        col = item.column()

        # Get the 'key' = column header
        key = self.imageTable.horizontalHeaderItem(col).text().lower()

        # Get the 'value' = cell value from the table
        value = str(self.imageTable.item(row, col).text())

        # Update the dictionary
        self.listImage[row].update_info(key, value)
        return

    # If image header has been clicked
    def onImageTableHeaderClicked(self, logicalIndex):
        n = len(self.listImage)
        if logicalIndex == 0:  # If the first row is clicked

            if not self.selectAllImage:  # If self.selectAllImage is False
                self.selectAllImage = True
                for r in range(0, n):
                    self.imageTable.cellWidget(r, 0).findChild(
                        type(QCheckBox())).setChecked(True)

            else:
                self.selectAllImage = False
                for r in range(0, n):
                    self.imageTable.cellWidget(r, 0).findChild(
                        type(QCheckBox())).setChecked(False)

    def updateImageTable(self):
        n = len(self.listImage)

        # Block the signals so that any editing doesn't call any signal
        self.imageTable.blockSignals(True)

        # Clears the table
        self.imageTable.setRowCount(0)

        # Create an empty list of 'Edit' buttons
        self.editImageBtn = []

        for row in range(0, n):

            # Insert a new row
            self.imageTable.insertRow(row)

            # Insert a checkbox in the first column (col = 0)
            qw = QWidget()
            self.checkbox = QCheckBox()
            self.checkbox.setCheckState(Qt.Unchecked)
            tabhlayout = QHBoxLayout(qw)
            tabhlayout.addWidget(self.checkbox)
            tabhlayout.setAlignment(Qt.AlignCenter)
            tabhlayout.setContentsMargins(0, 0, 0, 0)
            self.imageTable.setCellWidget(row, 0, qw)

            # Insert a checkbox in the second column (col = 1)
            # Append to the list of 'Edit' buttons
            self.editImageBtn.append(QPushButton('Edit'))
            self.editImageBtn[row].setStyleSheet('margin:3px')
            self.imageTable.setCellWidget(row, 1, self.editImageBtn[row])
            self.editImageBtn[row].clicked.connect(lambda x:
                                                   self.addEditImage(True))

            for col in range(2, 9):
                # Get the column header in lowercase
                colheader = self.imageTable.horizontalHeaderItem(
                    col).text().lower()

                if colheader == 'image' or colheader == 'template':

                    # If the column header is 'image' or 'template', then
                    # get the file basename and also make the cells read-only
                    itemString = os.path.basename(
                        str(self.listImage[row].info[colheader]))
                    item = QTableWidgetItem(itemString)
                    item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)

                else:

                    # Just get the value from the dictionary
                    itemString = str(self.listImage[row].info[colheader])
                    item = QTableWidgetItem(itemString)

                # Align and insert the value in the cell
                item.setTextAlignment(Qt.AlignCenter)
                self.imageTable.setItem(row, col, item)

        self.imageTable.blockSignals(False)

    # Add or edit the image info
    def addEditImage(self, editBool):

        # Clear the status message
        self.statusBar.clearMessage()

        dlg = ImageOptionsDialog(self)

        # If edit then
        if editBool:
            # Get the row number 'r'
            buttonClicked = self.sender()
            index = self.imageTable.indexAt(buttonClicked.pos())
            r = index.row()

            # Get the r-th row dictionary
            imageInfo = self.listImage[r].get_dict()

            # Insert the image info in the dialog
            dlg.editInfoDialog(imageInfo)

        if dlg.exec_() == ImageOptionsDialog.Accepted:

            data = dlg.get_output()

            if editBool:
                # If edit, the replace the original content with
                # the new content
                self.listImage[r] = data['image']
                self.listImage[r] = ImageOptions(data)

            else:
                # If not editing old info, then add it to the end
                self.listImage.append(data['image'])
                k = len(self.listImage)
                self.listImage[k - 1] = ImageOptions(data)

            # Update the image table
            self.updateImageTable()

        return

    def createButtonBox(self):

        hbox = QHBoxLayout()
        self.vbox.addLayout(hbox)

        aboutBtn = QPushButton("About")
        aboutBtn.setFixedSize(self.btnWidth, self.btnHeight)
        aboutBtn.clicked.connect(self.aboutBtn_clicked)
        hbox.addWidget(aboutBtn, alignment=Qt.AlignLeft)

        self.helpBtn = QPushButton("Help")
        self.helpBtn.setFixedSize(self.btnWidth, self.btnHeight)
        self.helpBtn.clicked.connect(self.helpBtn_clicked)
        hbox.addWidget(self.helpBtn)

        hbox.addStretch(1)

        self.applyBtn = QPushButton("Apply")
        self.applyBtn.setFixedSize(self.btnWidth, self.btnHeight)
        self.applyBtn.clicked.connect(self.applyBtn_clicked)
        hbox.addWidget(self.applyBtn)

        quitBtn = QPushButton("Quit")
        quitBtn.setFixedSize(self.btnWidth, self.btnHeight)
        quitBtn.clicked.connect(self.close)
        hbox.addWidget(quitBtn)

        return

    def aboutBtn_clicked(self):

        # Clear the status message
        self.statusBar.clearMessage()

        infoMsg = ('Version: ' + self.version + '\n' +
                   'Author: ' + self.author)

        dlg = MessageDialog(title=self.title + ': About',
                            text='Sign PDF GUI',
                            informativeText=infoMsg,
                            icon=QStyle.SP_MessageBoxInformation)
        dlg.setMinimumWidth(300)
        dlg.exec_()
        return

    def helpBtn_clicked(self):

        cmd = self.cliApp + ' --help'
        self.proc = Popen(shlex.split(cmd), stdout=PIPE, stderr=PIPE)
        stdout, stderr = self.proc.communicate()
        rtn = self.proc.returncode

        if rtn != 0:
            print("Problem getting help text.")
            return rtn

        msg = self.cliApp + ' --help'
        detailedMsg = stdout.decode("utf-8")

        dlg = MessageDialog(title=self.title + ': Help',
                            icon=QStyle.SP_MessageBoxInformation,
                            text=msg,
                            detailedText=detailedMsg,
                            )
        dlg.setMinimumSize(550, 400)
        dlg.exec_()

        return

    def applyBtn_clicked(self):

        n = len(self.listPdf)

        if n == 0:
            dlg = MessageDialog(title=self.title + ': Error',
                                text='Warning: No pdf file supplied.',
                                icon=QStyle.SP_MessageBoxCritical)
            dlg.exec_()
            return

        self.pd = ProgressDialog()
        self.pd.setMinimum(0)
        self.pd.setMaximum(n)
        self.pd.setFormat("%v/%m")

        self.work = Worker(self)
        self.thread = Thread(target=self.work.run)
        self.thread.start()

        if self.pd.exec_() == ProgressDialog.Rejected:
            self.work.terminate()

    def createStatusBar(self):
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        return

    def addPdfFiles(self):

        # Clear the status message
        self.statusBar.clearMessage()

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = (
            QFileDialog.getOpenFileNames(self,
                                         "QFileDialog.getOpenFileNames()", "", "PDF Files (*.pdf)",
                                         options=options))
        if files:
            self.listPdf.extend(files)
            self.updatePdfTable()

    def updatePdfTable(self):

        n = len(self.listPdf)
        self.pdfTable.setRowCount(0)  # Clear the table

        for r in range(0, n):
            self.pdfTable.insertRow(r)

            qw = QWidget()
            self.checkbox = QCheckBox()
            self.checkbox.setCheckState(Qt.Unchecked)
            tabhlayout = QHBoxLayout(qw)
            tabhlayout.addWidget(self.checkbox)
            tabhlayout.setAlignment(Qt.AlignCenter)
            tabhlayout.setContentsMargins(0, 0, 0, 0)
            self.pdfTable.setCellWidget(r, 0, qw)

            item = QTableWidgetItem(self.listPdf[r])
            item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            self.pdfTable.setItem(r, 1, item)

    def showGridState(self):
        self.statusBar.clearMessage()
        return

    def printCmdState(self):
        self.statusBar.clearMessage()
        return

    def delPdfFiles(self):

        # Clear the status message
        self.statusBar.clearMessage()

        self.selectAllPdf = False

        n = len(self.listPdf)
        for r in range(0, n):
            if self.pdfTable.cellWidget(r, 0).findChild(
                    type(QCheckBox())).isChecked():
                # Remove the element from the list
                del self.listPdf[r]

                # Insert blank in the list so that the number of
                # elements remain the same.
                self.listPdf.insert(r, "")

                # Remove the blanks that had been inserted
        while ("" in self.listPdf):
            self.listPdf.remove("")

        # Update the table
        self.updatePdfTable()

        return

    def otherBtn_clicked(self):
        dlg = OtherDialog(self.otherConfigs)
        if dlg.exec_() == OtherDialog.Accepted:
            self.otherConfigs = dlg.get_output()
        return


class MessageDialog(QDialog):

    def __init__(self, *args, **kwargs):
        super(MessageDialog, self).__init__()

        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)

        hbox = QHBoxLayout()
        self.vbox.addLayout(hbox)

        if 'title' in kwargs.keys():
            self.setWindowTitle(kwargs['title'])

        # https://stackoverflow.com/questions/25055552/how-do-i-add-standardpixmap-to-a-layout
        # https://doc.qt.io/qtforpython/PySide2/QtWidgets/QStyle.html#PySide2.QtWidgets.PySide2.QtWidgets.QStyle.standardIcon
        if 'icon' in kwargs.keys() and kwargs['icon'] != 'QStyle.SP_NoIcon':
            self.icon = QLabel()
            icon = self.style().standardIcon(kwargs['icon'])
            self.icon.setPixmap(icon.pixmap(48))
            hbox.addWidget(self.icon, alignment=Qt.AlignLeft)

        self.text = QLabel()
        hbox.addWidget(self.text, alignment=Qt.AlignLeft | Qt.AlignVCenter)
        if 'text' in kwargs.keys():
            self.text.setText(kwargs['text'])

        hbox.addStretch(1)

        self.grid = QGridLayout()
        self.vbox.addLayout(self.grid)

        self.informativeText = QLabel("")
        if 'informativeText' in kwargs.keys():
            self.informativeText.setText(kwargs['informativeText'])
            self.grid.addWidget(self.informativeText, 0, 0)

        self.detailedText = QPlainTextEdit()
        self.detailedText.setReadOnly(True)
        if 'detailedText' in kwargs.keys():
            self.detailedText.insertPlainText(kwargs['detailedText'])
            self.grid.addWidget(self.detailedText, 1, 0)

        self.btns = QDialogButtonBox()
        self.btns.setStandardButtons(QDialogButtonBox.Ok)
        self.vbox.addWidget(self.btns)

        self.btns.accepted.connect(self.close)

        return


class ImageOptionsDialog(QDialog):

    def __init__(self, *args, **kwargs):
        super(ImageOptionsDialog, self).__init__(*args, **kwargs)

        self.setWindowTitle('Select Image')
        self.setFixedWidth(350)

        vbox = QVBoxLayout()
        self.setLayout(vbox)

        insertImageLabel = QLabel("Insert image by:")
        vbox.addWidget(insertImageLabel)

        radioHbox = QHBoxLayout()
        vbox.addLayout(radioHbox)

        self.radioBtnCord = QRadioButton("Coordinate")
        self.radioBtnCord.setChecked(True)
        self.radioBtnCord.toggled.connect(self.onRadioBtnClicked)
        radioHbox.addWidget(self.radioBtnCord)
        self.insertImageBy = 'coordinate'

        self.radioBtnTemp = QRadioButton("Template")
        self.radioBtnTemp.setChecked(False)
        self.radioBtnTemp.toggled.connect(self.onRadioBtnClicked)
        radioHbox.addWidget(self.radioBtnTemp)

        formLayout = QFormLayout()
        vbox.addLayout(formLayout)

        hbox = QHBoxLayout()
        formLayout.addRow('Image:', hbox)
        openImageBtn = QPushButton("Open")
        hbox.addWidget(openImageBtn)
        openImageBtn.setFixedSize(60, 30)
        openImageBtn.clicked.connect(lambda:
                                     self.openImageBtn_clicked("coordinate"))
        self.imgFileName = ''
        self.imgFileLabel = QLabel(os.path.basename(self.imgFileName))
        hbox.addWidget(self.imgFileLabel)

        hbox = QHBoxLayout()
        formLayout.addRow('Template:', hbox)
        self.openTempBtn = QPushButton("Open")
        hbox.addWidget(self.openTempBtn)
        self.openTempBtn.setFixedSize(60, 30)
        self.openTempBtn.setEnabled(False)
        self.openTempBtn.clicked.connect(lambda:
                                         self.openImageBtn_clicked("template"))
        self.tempFileName = 'Not applicable'
        self.tempFileLabel = QLabel(os.path.basename(self.tempFileName))
        hbox.addWidget(self.tempFileLabel)

        self.xValue = QLineEdit()
        self.xValue.setText("0")
        formLayout.addRow('X-Cord/XOffset:', self.xValue)

        self.yValue = QLineEdit()
        self.yValue.setText("0")
        formLayout.addRow('Y-Cord/YOffset:', self.yValue)

        self.scale = QSpinBox()
        self.scale.setRange(0, 100)
        self.scale.setSingleStep(1)
        self.scale.setValue(15)
        self.scale.setSuffix(" %")
        formLayout.addRow('Scale:', self.scale)

        self.page = QSpinBox()
        self.page.setRange(1, 100)
        self.page.setSingleStep(1)
        self.page.setValue(1)
        formLayout.addRow('Page:', self.page)

        self.rotation = QSpinBox()
        self.rotation.setRange(-360, 360)
        self.rotation.setSingleStep(1)
        self.rotation.setValue(0)
        self.rotation.setSuffix(" deg")
        formLayout.addRow('Rotation:', self.rotation)

        self.btns = QDialogButtonBox()
        self.btns.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        vbox.addWidget(self.btns)

        self.btns.accepted.connect(self.accept)
        self.btns.rejected.connect(self.reject)

    def editInfoDialog(self, data):

        # Insert image by 'coordinate' or 'template'
        self.insertImageBy = data['type']

        # Click the correct radiobutton
        if self.insertImageBy == 'coordinate':
            self.radioBtnCord.setChecked(True)
        elif self.insertImageBy == 'template':
            self.radioBtnTemp.setChecked(True)

        # Set the image properties
        self.imgFileName = data['image']
        self.tempFileName = data['template']
        self.xValue.setText(data['xvalue'])
        self.yValue.setText(data['yvalue'])
        self.scale.setValue(float(data['scale']))
        self.page.setValue(int(data['page']))
        self.rotation.setValue(float(data['rotation']))

        # Set the label
        self.imgFileLabel.setText(os.path.basename(data['image']))
        self.tempFileLabel.setText(os.path.basename(data['template']))

        return

    def onRadioBtnClicked(self):
        radioButton = self.sender()

        if radioButton.isChecked():
            self.insertImageBy = radioButton.text().lower()

            if radioButton.text().lower() == 'coordinate':
                self.openTempBtn.setEnabled(False)
                self.tempFileName = 'Not applicable'
                self.tempFileLabel.setText(os.path.basename(self.tempFileName))

            elif radioButton.text().lower() == 'template':
                self.openTempBtn.setEnabled(True)
                self.tempFileLabel.setText('')

        return

    def openImageBtn_clicked(self, itype):

        filedialog = QFileDialogPreview(self, "Open File",
                                        "", "Image Files (*.png *.jpg *.jpeg)")
        filedialog.setFileMode(QFileDialog.ExistingFile)
        if filedialog.exec_() == QFileDialogPreview.Accepted:
            ifile = filedialog.getFileSelected()

            ifileBasename = os.path.basename(ifile)

            if itype == 'coordinate':
                self.imgFileName = ifile
                self.imgFileLabel.setText(ifileBasename)
            elif itype == 'template':
                self.tempFileName = ifile
                self.tempFileLabel.setText(ifileBasename)

        return

    def accept(self):

        if not self.checkValues():
            return

        self._output = {'type': self.insertImageBy,
                        'image': self.imgFileName,
                        'template': self.tempFileName,
                        'xvalue': self.xValue.text(),
                        'yvalue': self.yValue.text(),
                        'scale': self.scale.value(),
                        'page': self.page.value(),
                        'rotation': self.rotation.value()
                        }
        super(ImageOptionsDialog, self).accept()
        return

    def checkValues(self):

        errMsg = ''
        noError = True

        if not os.path.isfile(self.imgFileName):
            errMsg = "Image file not defined."
            noError = False

        if (self.insertImageBy == 'template' and
                not os.path.isfile(self.tempFileName)):
            errMsg = errMsg + "\n" + "Template image file not defined."
            noError = False

        if not self.xValue.text().lstrip('-').isdigit():
            errMsg = errMsg + "\n" + "X coordinate is not numeric."
            noError = False

        if not self.yValue.text().lstrip('-').isdigit():
            errMsg = errMsg + "\n" + "Y coordinate is not numeric."
            noError = False

        if not noError:
            dlg = MessageDialog(title='Insert Image: Error',
                                text=errMsg.strip(),
                                icon=QStyle.SP_MessageBoxWarning)
            dlg.exec_()

        return noError

    def get_output(self):
        return self._output


def main():
    scriptname = os.path.basename(sys.argv[0])
    author = 'Anjishnu Sarkar'
    version = '0.24'
    cliApp = 'sign-pdf.py'

    listPdf = []  # List of pdfs

    # Number of arguments supplied via cli
    numargv = len(sys.argv) - 1
    # Argument count
    iargv = 1

    # Parse cli options
    while iargv <= numargv:

        if sys.argv[iargv] == "-h" or sys.argv[iargv] == "--help":
            helptext(scriptname, author, version, cliApp)
            sys.exit(0)

        elif re.search(".pdf$", sys.argv[iargv]):
            listPdf.extend(glob(sys.argv[iargv]))

        else:
            print("%s: Unspecified option: '%s'. Aborting."
                  % (scriptname, sys.argv[iargv]))
            sys.exit(1)

        iargv += 1

    app = QApplication(sys.argv)
    window = MainWindow(cliApp=cliApp, author=author, version=version,
                        pdflist=listPdf)
    window.show()
    sys.exit(app.exec_())


def helptext(sname, athr, vrsn, cli_app):
    print(sname, ": Sign PDF files with signature (image file)", sep='')
    print("Author: ", athr, sep='')
    print("Version: ", vrsn, sep='')
    print("")
    print("Usage: ", sname, " [options] [file1.pdf] [file2.pdf]", sep='')
    print("")
    print("Options:")
    print("-h|--help        Show the help and exit.")
    print("")
    print("For command line usage check '", cli_app, " --help'", sep='')
    print("The graphical interface is self-explanatory.")
    return


if __name__ == '__main__':
    main()