# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

import sys
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("スタイル＆武器シャッフル")
        Dialog.resize(653, 220)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(280, 160, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.style1 = QtWidgets.QTextBrowser(Dialog)
        self.style1.setGeometry(QtCore.QRect(110, 110, 121, 31))
        self.style1.setObjectName("style1")
        self.arms1 = QtWidgets.QTextBrowser(Dialog)
        self.arms1.setGeometry(QtCore.QRect(110, 70, 121, 31))
        self.arms1.setObjectName("arms1")
        self.style2 = QtWidgets.QTextBrowser(Dialog)
        self.style2.setGeometry(QtCore.QRect(240, 110, 121, 31))
        self.style2.setObjectName("style2")
        self.arms2 = QtWidgets.QTextBrowser(Dialog)
        self.arms2.setGeometry(QtCore.QRect(240, 70, 121, 31))
        self.arms2.setObjectName("arms2")
        self.style3 = QtWidgets.QTextBrowser(Dialog)
        self.style3.setGeometry(QtCore.QRect(370, 110, 121, 31))
        self.style3.setObjectName("style3")
        self.style4 = QtWidgets.QTextBrowser(Dialog)
        self.style4.setGeometry(QtCore.QRect(500, 110, 121, 31))
        self.style4.setObjectName("style4")
        self.arms3 = QtWidgets.QTextBrowser(Dialog)
        self.arms3.setGeometry(QtCore.QRect(370, 70, 121, 31))
        self.arms3.setObjectName("arms3")
        self.arms4 = QtWidgets.QTextBrowser(Dialog)
        self.arms4.setGeometry(QtCore.QRect(500, 70, 121, 31))
        self.arms4.setObjectName("arms4")
        self.player1 = QtWidgets.QTextEdit(Dialog)
        self.player1.setGeometry(QtCore.QRect(110, 30, 121, 31))
        self.player1.setObjectName("player1")
        self.player2 = QtWidgets.QTextEdit(Dialog)
        self.player2.setGeometry(QtCore.QRect(240, 30, 121, 31))
        self.player2.setObjectName("player2")
        self.player3 = QtWidgets.QTextEdit(Dialog)
        self.player3.setGeometry(QtCore.QRect(370, 30, 121, 31))
        self.player3.setObjectName("player3")
        self.player4 = QtWidgets.QTextEdit(Dialog)
        self.player4.setGeometry(QtCore.QRect(500, 30, 121, 31))
        self.player4.setObjectName("player4")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 91, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 110, 41, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 70, 31, 31))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        self.buttonBox.clicked.connect(self.shuffle)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.buttonBox.clicked.connect(self.shuffle)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "PLAYER NAME"))
        self.label_2.setText(_translate("Dialog", "スタイル"))
        self.label_3.setText(_translate("Dialog", "武器"))

    def shuffle(self):
        style = shuffle_style()
        arms = shuffle_arms()
        self.arms1.setText(arms[0])
        self.arms2.setText(arms[1])
        self.arms3.setText(arms[2])
        self.arms4.setText(arms[3])
        self.style1.setText(style[0])
        self.style2.setText(style[1])
        self.style3.setText(style[2])
        self.style4.setText(style[3])

class View(QDialog):
    def __init__(self,parent=None):
        super(View, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

def shuffle_style():
    style = ['ギルド','ストライカー','エリアル','ブシドー','ブレイヴ','レンキン']
    select = np.random.choice(style,4,replace=False)
    return select

def shuffle_arms():
    arms = ['片手剣','太刀','大剣','ハンマー','双剣','狩猟笛','ランス','ガンランス','スラッシュアックス','チャージアックス','操虫棍','弓','ライトボウガン','ヘビィボウガン','猫']
    select = np.random.choice(arms,4,replace=False)
    return select

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = View()
    window.show()
    sys.exit(app.exec_())

