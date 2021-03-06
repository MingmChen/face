# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import faceBackend as fb
from faceBackend.faceLib import facelib as fl
from faceBackend.faceLib import facedb as fdb
import numpy as np
import cv2
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os.path as path
import AppConfig

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		self.db=fdb.facedb()

		MainWindow.setObjectName("MainWindow")
		MainWindow.setEnabled(True)
		MainWindow.resize(1302, 901)

		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.frame_encode = QtWidgets.QFrame(self.centralwidget)
		self.frame_encode.setGeometry(QtCore.QRect(0, 59, 1300, 841))
		self.frame_encode.setStyleSheet("    #frame_encode { \n"
" \n"
"    background-color:rgb(49, 45, 61);\n"
"    }")
		self.frame_encode.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_encode.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_encode.setObjectName("frame_encode")
		self.label_encode_tag = QtWidgets.QLabel(self.frame_encode)
		self.label_encode_tag.setGeometry(QtCore.QRect(1175, 0, 131, 131))
		self.label_encode_tag.setStyleSheet("border-image: url(:/EnTag.png);")
		self.label_encode_tag.setText("")
		self.label_encode_tag.setObjectName("label_encode_tag")
		self.pushButton = QtWidgets.QPushButton(self.frame_encode)
		self.pushButton.setGeometry(QtCore.QRect(460, 340, 241, 111))
		self.pushButton.setStyleSheet("QPushButton{border-image: url(:/EncodeBtn.png)}\n"
"QPushButton:pressed{border-image: url(:/EncodeBtnDown.png)}")
		self.pushButton.setText("")
		self.pushButton.setObjectName("pushButton")
		self.emTagUs = QtWidgets.QPushButton(self.centralwidget)
		self.emTagUs.setGeometry(QtCore.QRect(880, 15, 120, 30))
		self.emTagUs.setStyleSheet("border-image: url(:/TabEmUs.png);")
		self.emTagUs.setText("")
		self.emTagUs.setObjectName("emTagUs")
		self.comTagUs = QtWidgets.QPushButton(self.centralwidget)
		self.comTagUs.setGeometry(QtCore.QRect(430, 15, 120, 30))
		self.comTagUs.setStyleSheet("border-image: url(:/TabComUs.png);")
		self.comTagUs.setText("")
		self.comTagUs.setObjectName("comTagUs")
		self.encodeTagS = QtWidgets.QPushButton(self.centralwidget)
		self.encodeTagS.setGeometry(QtCore.QRect(280, 15, 120, 45))
		self.encodeTagS.setStyleSheet("border-image: url(:/TabEncodeS.png);")
		self.encodeTagS.setText("")
		self.encodeTagS.setObjectName("encodeTagS")
		self.traTagUs = QtWidgets.QPushButton(self.centralwidget)
		self.traTagUs.setGeometry(QtCore.QRect(580, 15, 120, 30))
		self.traTagUs.setStyleSheet("border-image: url(:/TabTraUs.png);")
		self.traTagUs.setText("")
		self.traTagUs.setObjectName("traTagUs")
		self.menu = QtWidgets.QLabel(self.centralwidget)
		self.menu.setGeometry(QtCore.QRect(0, -5, 1300, 61))
		self.menu.setStyleSheet("background-color: rgb(255, 255, 255)\n"
"")
		self.menu.setText("")
		self.menu.setObjectName("menu")
		self.encodeTagUs = QtWidgets.QPushButton(self.centralwidget)
		self.encodeTagUs.setGeometry(QtCore.QRect(280, 15, 120, 30))
		self.encodeTagUs.setStyleSheet("border-image: url(:/TabEncodeUs.png);")
		self.encodeTagUs.setText("")
		self.encodeTagUs.setObjectName("encodeTagUs")
		self.encodeTagUs.setVisible(False)
		self.comTagS = QtWidgets.QPushButton(self.centralwidget)
		self.comTagS.setGeometry(QtCore.QRect(430, 15, 120, 45))
		self.comTagS.setStyleSheet("border-image: url(:/TabComS.png);")
		self.comTagS.setText("")
		self.comTagS.setObjectName("comTagS")
		self.comTagS.setVisible(False)
		self.traTagS = QtWidgets.QPushButton(self.centralwidget)
		self.traTagS.setGeometry(QtCore.QRect(580, 15, 120, 45))
		self.traTagS.setStyleSheet("border-image: url(:/TabTraS.png);")
		self.traTagS.setText("")
		self.traTagS.setObjectName("traTagS")
		self.traTagS.setVisible(False)
		self.emTagS = QtWidgets.QPushButton(self.centralwidget)
		self.emTagS.setGeometry(QtCore.QRect(880, 15, 120, 45))
		self.emTagS.setStyleSheet("border-image: url(:/TabEmS.png);")
		self.emTagS.setText("")
		self.emTagS.setObjectName("emTagS")
		self.emTagS.setVisible(False)
		self.frame_tracker = QtWidgets.QFrame(self.centralwidget)
		self.frame_tracker.setGeometry(QtCore.QRect(-1, 59, 1301, 841))
		self.frame_tracker.setStyleSheet("    #frame_tracker { \n"
"    background-color:rgb(49, 45, 61);\n"
"    }")
		self.frame_tracker.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_tracker.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_tracker.setObjectName("frame_tracker")
		self.frame_tracker.close()
		self.label_tracker_tag = QtWidgets.QLabel(self.frame_tracker)
		self.label_tracker_tag.setGeometry(QtCore.QRect(1175, 0, 131, 131))
		self.label_tracker_tag.setStyleSheet("border-image: url(:/TraTag.png);")
		self.label_tracker_tag.setText("")
		self.label_tracker_tag.setObjectName("label_tracker_tag")
		self.trackLabelShowCamera = QtWidgets.QLabel(self.frame_tracker)
		self.trackLabelShowCamera.setGeometry(QtCore.QRect(600, 110, 600, 500))
		self.trackLabelShowCamera.setStyleSheet("background-color: rgb(255, 255, 255);")
		self.trackLabelShowCamera.setText("")
		self.trackLabelShowCamera.setObjectName("trackLabelShowCamera")
		self.trackLabelShowCameraFrame = QtWidgets.QLabel(self.frame_tracker)
		self.trackLabelShowCameraFrame.setGeometry(QtCore.QRect(590, 100, 620, 520))
		self.trackLabelShowCameraFrame.setText("")
		self.trackLabelShowCameraFrame.setObjectName("trackLabelShowCameraFrame")
		self.trackLabelShowCameraFrame.setStyleSheet("border-image: url(:/frame.png);")
		self.idLineEdit = QtWidgets.QLineEdit(self.frame_tracker)
		self.idLineEdit.setGeometry(QtCore.QRect(50, 310, 481, 51))
		self.idLineEdit.setStyleSheet("font-size: 25px")
		self.idLineEdit.setText("")
		self.idLineEdit.setObjectName("idLineEdit")
		# self.idLineEdit.setStyleSheet("border-image: url(:/ResultBar.png);font-size:20px;")
		self.trackCameraSwitch = QtWidgets.QPushButton(self.frame_tracker)
		self.trackCameraSwitch.setGeometry(QtCore.QRect(820, 640, 161, 71))
		self.trackCameraSwitch.setStyleSheet("QPushButton{border-image: url(:/switchOff.png)}")
		self.trackCameraSwitch.setText("")
		self.trackCameraSwitch.setObjectName("trackCameraSwitch")
		self.trackerStartBtn = QtWidgets.QPushButton(self.frame_tracker)
		self.trackerStartBtn.setGeometry(QtCore.QRect(220, 460, 131, 51))
		self.trackerStartBtn.setStyleSheet("QPushButton{border-image: url(:/startBtn.png)}\n"
"QPushButton:hover{border-image: url(:/startBtnHover.png)}\n"
"QPushButton:pressed{border-image: url(:/startBtnActive.png)}")
		self.trackerStartBtn.setText("")
		self.trackerStartBtn.setObjectName("trackerStartBtn")
		self.label = QtWidgets.QLabel(self.frame_tracker)
		self.label.setGeometry(QtCore.QRect(53, 272, 241, 31))
		self.label.setStyleSheet("background-color: rgb(49, 45, 61);\n"
"color: rgb(0, 170, 255);")
		self.label.setObjectName("label")
		self.trackType1RB = QtWidgets.QRadioButton(self.frame_tracker)
		self.trackType1RB.setGeometry(QtCore.QRect(50, 160, 131, 41))
		self.trackType1RB.setStyleSheet("color: rgb(255, 0, 4);\n"
"font-size:20px")
		self.trackType1RB.setObjectName("trackType1RB")
		self.trackType1RB.setChecked(True)
		self.trackType2RB = QtWidgets.QRadioButton(self.frame_tracker)
		self.trackType2RB.setGeometry(QtCore.QRect(190, 160, 141, 41))
		self.trackType2RB.setStyleSheet("color: rgb(255, 0, 4);\n"
"font-size:20px")
		self.trackType2RB.setObjectName("trackType2RB")
		self.trackType2RB.setChecked(False)
		self.trackType3RB = QtWidgets.QRadioButton(self.frame_tracker)
		self.trackType3RB.setGeometry(QtCore.QRect(350, 160, 141, 41))
		self.trackType3RB.setStyleSheet("color: rgb(255, 0, 4);\n"
"font-size:20px")
		self.trackType3RB.setObjectName("trackType3RB")
		self.trackType3RB.setChecked(False)
		self.capTagUs = QtWidgets.QPushButton(self.centralwidget)
		self.capTagUs.setGeometry(QtCore.QRect(730, 15, 120, 30))
		self.capTagUs.setStyleSheet("border-image: url(:/TabCapUs.png);")
		self.capTagUs.setText("")
		self.capTagUs.setObjectName("capTagUs")
		#self.capTagUs.setVisible(False)
		self.capTagS = QtWidgets.QPushButton(self.centralwidget)
		self.capTagS.setGeometry(QtCore.QRect(730, 15, 120, 45))
		self.capTagS.setStyleSheet("border-image: url(:/TabCapS.png);")
		self.capTagS.setText("")
		self.capTagS.setObjectName("capTagS")
		self.capTagS.setVisible(False)
		self.frame_capture = QtWidgets.QFrame(self.centralwidget)
		self.frame_capture.setGeometry(QtCore.QRect(0, 59, 1300, 841))
		self.frame_capture.setStyleSheet("    #frame_capture { \n"
"    background-color:rgb(49, 45, 61);\n"
"    }")
		self.frame_capture.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_capture.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_capture.setObjectName("frame_capture")
		self.frame_capture.close()
		self.label_encode_tag_2 = QtWidgets.QLabel(self.frame_capture)
		self.label_encode_tag_2.setGeometry(QtCore.QRect(1175, 0, 131, 131))
		self.label_encode_tag_2.setStyleSheet("border-image: url(:/CapTag.png);")
		self.label_encode_tag_2.setText("")
		self.label_encode_tag_2.setObjectName("label_encode_tag_2")
		self.cap_photo0 = QtWidgets.QLabel(self.frame_capture)
		self.cap_photo0.setGeometry(QtCore.QRect(79, 129, 561, 481))
		self.cap_photo0.setText("")
		self.cap_photo0.setAlignment(QtCore.Qt.AlignCenter)
		self.cap_photo0.setObjectName("cap_photo0")
		self.cap_photoFrame0 = QtWidgets.QLabel(self.frame_capture)
		self.cap_photoFrame0.setGeometry(QtCore.QRect(60, 110, 601, 531))
		self.cap_photoFrame0.setStyleSheet("border-image: url(:/frame.png);")
		self.cap_photoFrame0.setText("")
		self.cap_photoFrame0.setObjectName("cap_photoFrame0")
		self.cap_selectPicBtn = QtWidgets.QPushButton(self.frame_capture)
		self.cap_selectPicBtn.setGeometry(QtCore.QRect(290, 690, 131, 51))
		self.cap_selectPicBtn.setStyleSheet("QPushButton{border-image: url(:/selectBtn.png)}\n"
"QPushButton:hover{border-image: url(:/selectBtnHover.png)}\n"
"QPushButton:pressed{border-image: url(:/selectBtnActive.png)}")
		self.cap_selectPicBtn.setText("")
		self.cap_selectPicBtn.setObjectName("cap_selectPicBtn")

		self.cap_photo0_2 = QtWidgets.QLabel(self.frame_capture)
		self.cap_photo0_2.setGeometry(QtCore.QRect(709, 129, 561, 491))
		self.cap_photo0_2.setText("")
		self.cap_photo0_2.setAlignment(QtCore.Qt.AlignCenter)
		self.cap_photo0_2.setObjectName("cap_photo0_2")
		self.cap_photoFrame0_2 = QtWidgets.QLabel(self.frame_capture)
		self.cap_photoFrame0_2.setGeometry(QtCore.QRect(690, 110, 601, 531))
		self.cap_photoFrame0_2.setStyleSheet("border-image: url(:/frame.png);")
		self.cap_photoFrame0_2.setText("")
		self.cap_photoFrame0_2.setObjectName("cap_photoFrame0_2")
		self.startCapBtn = QtWidgets.QPushButton(self.frame_capture)
		self.startCapBtn.setGeometry(QtCore.QRect(940, 670, 131, 51))
		self.startCapBtn.setStyleSheet("QPushButton{border-image: url(:/startBtn.png)}\n"
"QPushButton:hover{border-image: url(:/startBtnHover.png)}\n"
"QPushButton:pressed{border-image: url(:/startBtnActive.png)}")
		self.startCapBtn.setText("")
		self.startCapBtn.setObjectName("startCapBtn")
		self.frame_em = QtWidgets.QFrame(self.centralwidget)
		self.frame_em.setGeometry(QtCore.QRect(0, 59, 1300, 841))
		self.frame_em.setStyleSheet("    #frame_em { \n"
" \n"
"    background-color:rgb(49, 45, 61);\n"
"    }")
		self.frame_em.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_em.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_em.setObjectName("frame_em")
		self.frame_em.close()
		self.label_emotion_tag = QtWidgets.QLabel(self.frame_em)
		self.label_emotion_tag.setGeometry(QtCore.QRect(1175, 0, 131, 131))
		self.label_emotion_tag.setStyleSheet("border-image: url(:/EmTag.png);")
		self.label_emotion_tag.setText("")
		self.label_emotion_tag.setObjectName("label_emotion_tag")
		self.label_emotionResult = QtWidgets.QLabel(self.frame_em)
		self.label_emotionResult.setGeometry(QtCore.QRect(410, 740, 531, 51))
		self.label_emotionResult.setStyleSheet("border-image: url(:/ResultBar.png);\n"
"font-size:30px;\n"
"font-weight:bold;\n"
"font-family:Roman times;")
		self.label_emotionResult.setAlignment(QtCore.Qt.AlignCenter)
		self.label_emotionResult.setObjectName("label_emotionResult")
		self.emLabelShowCamera = QtWidgets.QLabel(self.frame_em)
		self.emLabelShowCamera.setGeometry(QtCore.QRect(380, 110, 600, 500))
		self.emLabelShowCamera.setStyleSheet("background-color: rgb(255, 255, 255);")
		self.emLabelShowCamera.setText("")
		self.emLabelShowCamera.setObjectName("emLabelShowCamera")
		self.emLabelShowCameraFrame = QtWidgets.QLabel(self.frame_em)
		self.emLabelShowCameraFrame.setGeometry(QtCore.QRect(370, 100, 620, 520))
		self.emLabelShowCameraFrame.setText("")
		self.emLabelShowCameraFrame.setObjectName("emLabelShowCameraFrame")
		self.emLabelShowCameraFrame.setStyleSheet("border-image: url(:/frame.png);")
		self.emCameraSwitch = QtWidgets.QPushButton(self.frame_em)
		self.emCameraSwitch.setGeometry(QtCore.QRect(580, 650, 161, 71))
		self.emCameraSwitch.setStyleSheet("QPushButton{border-image: url(:/switchOff.png)}")
		self.emCameraSwitch.setText("")
		self.emCameraSwitch.setObjectName("emCameraSwitch")
		self.emStartBtn = QtWidgets.QPushButton(self.frame_em)
		self.emStartBtn.setGeometry(QtCore.QRect(80, 320, 131, 51))
		self.emStartBtn.setStyleSheet("QPushButton{border-image: url(:/startBtn.png)}\n"
										   "QPushButton:hover{border-image: url(:/startBtnHover.png)}\n"
										   "QPushButton:pressed{border-image: url(:/startBtnActive.png)}")
		self.emStartBtn.setText("")
		self.emStartBtn.setObjectName("emStartBtn")

		self.label_emotionType = QtWidgets.QLabel(self.frame_em)
		self.label_emotionType.setGeometry(QtCore.QRect(420, 30, 531, 51))
		self.label_emotionType.setStyleSheet("border-image: url(:/ResultBar.png);\n"
"font-size:30px;\n"
"font-weight:bold;\n"
"font-family:Roman times;")
		self.label_emotionType.setAlignment(QtCore.Qt.AlignCenter)
		self.label_emotionType.setObjectName("label_emotionType")
		self.frame_compare = QtWidgets.QFrame(self.centralwidget)
		self.frame_compare.setGeometry(QtCore.QRect(0, 59, 1300, 841))
		self.frame_compare.setStyleSheet("    #frame_compare { \n"
" \n"
"    \n"
"    background-color:rgb(49, 45, 61);\n"
"    }")
		self.frame_compare.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_compare.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_compare.setObjectName("frame_compare")
		self.frame_compare.close()
		self.photoFrame0 = QtWidgets.QLabel(self.frame_compare)
		self.photoFrame0.setGeometry(QtCore.QRect(120, 230, 260, 370))
		self.photoFrame0.setStyleSheet("border-image: url(:/frame.png);")
		self.photoFrame0.setText("")
		self.photoFrame0.setObjectName("photoFrame0")
		self.photoFrame1 = QtWidgets.QLabel(self.frame_compare)
		self.photoFrame1.setGeometry(QtCore.QRect(700, 20, 200, 300))
		self.photoFrame1.setStyleSheet("border-image: url(:/frame.png);")
		self.photoFrame1.setText("")
		self.photoFrame1.setObjectName("photoFrame1")
		self.photoFrame2 = QtWidgets.QLabel(self.frame_compare)
		self.photoFrame2.setGeometry(QtCore.QRect(940, 20, 200, 300))
		self.photoFrame2.setStyleSheet("border-image: url(:/frame.png);")
		self.photoFrame2.setText("")
		self.photoFrame2.setObjectName("photoFrame2")
		self.photoFrame3 = QtWidgets.QLabel(self.frame_compare)
		self.photoFrame3.setGeometry(QtCore.QRect(820, 390, 200, 300))
		self.photoFrame3.setStyleSheet("border-image: url(:/frame.png);")
		self.photoFrame3.setText("")
		self.photoFrame3.setObjectName("photoFrame3")
		self.photoFrame4 = QtWidgets.QLabel(self.frame_compare)
		self.photoFrame4.setGeometry(QtCore.QRect(1050, 390, 200, 300))
		self.photoFrame4.setStyleSheet("border-image: url(:/frame.png);")
		self.photoFrame4.setText("")
		self.photoFrame4.setObjectName("photoFrame4")
		self.photoFrame5 = QtWidgets.QLabel(self.frame_compare)
		self.photoFrame5.setGeometry(QtCore.QRect(590, 390, 200, 300))
		self.photoFrame5.setStyleSheet("border-image: url(:/frame.png);")
		self.photoFrame5.setText("")
		self.photoFrame5.setObjectName("photoFrame5")
		self.photo0 = QtWidgets.QLabel(self.frame_compare)
		self.photo0.setGeometry(QtCore.QRect(125, 235, 250, 360))
		self.photo0.setText("")
		self.photo0.setAlignment(QtCore.Qt.AlignCenter)
		self.photo0.setObjectName("photo0")
		self.photo1 = QtWidgets.QLabel(self.frame_compare)
		self.photo1.setGeometry(QtCore.QRect(705, 25, 190, 290))
		self.photo1.setText("")
		self.photo1.setAlignment(QtCore.Qt.AlignCenter)
		self.photo1.setObjectName("photo1")
		self.photo2 = QtWidgets.QLabel(self.frame_compare)
		self.photo2.setGeometry(QtCore.QRect(945, 25, 190, 290))
		self.photo2.setText("")
		self.photo2.setAlignment(QtCore.Qt.AlignCenter)
		self.photo2.setObjectName("photo2")
		self.photo3 = QtWidgets.QLabel(self.frame_compare)
		self.photo3.setGeometry(QtCore.QRect(595, 395, 190, 290))
		self.photo3.setText("")
		self.photo3.setAlignment(QtCore.Qt.AlignCenter)
		self.photo3.setObjectName("photo3")
		self.photo4 = QtWidgets.QLabel(self.frame_compare)
		self.photo4.setGeometry(QtCore.QRect(825, 395, 190, 290))
		self.photo4.setText("")
		self.photo4.setAlignment(QtCore.Qt.AlignCenter)
		self.photo4.setObjectName("photo4")
		self.photo5 = QtWidgets.QLabel(self.frame_compare)
		self.photo5.setGeometry(QtCore.QRect(1055, 395, 190, 290))
		self.photo5.setText("")
		self.photo5.setAlignment(QtCore.Qt.AlignCenter)
		self.photo5.setObjectName("photo5")
		self.selectPicBtn = QtWidgets.QPushButton(self.frame_compare)
		self.selectPicBtn.setGeometry(QtCore.QRect(170, 620, 131, 51))
		self.selectPicBtn.setStyleSheet("QPushButton{border-image: url(:/selectBtn.png)}\n"
"QPushButton:hover{border-image: url(:/selectBtnHover.png)}\n"
"QPushButton:pressed{border-image: url(:/selectBtnActive.png)}")
		self.selectPicBtn.setText("")
		self.selectPicBtn.setObjectName("selectPicBtn")

		# Add extra (not in the .ui)
		self.com_startBtn = QtWidgets.QPushButton(self.frame_compare)
		self.com_startBtn.setGeometry(QtCore.QRect(170, 690, 131, 51))
		self.com_startBtn.setStyleSheet("QPushButton{border-image: url(:/startBtn.png)}\n"
"QPushButton:hover{border-image: url(:/startBtnHover.png)}\n"
"QPushButton:pressed{border-image: url(:/startBtnActive.png)}")
		self.com_startBtn.setText("")
		self.com_startBtn.setObjectName("com_startBtn")

		self.label_compare_tag = QtWidgets.QLabel(self.frame_compare)
		self.label_compare_tag.setGeometry(QtCore.QRect(1175, 0, 131, 131))
		self.label_compare_tag.setStyleSheet("border-image: url(:/ComTag.png);")
		self.label_compare_tag.setText("")
		self.label_compare_tag.setObjectName("label_compare_tag")
		self.label_compareResult = QtWidgets.QLabel(self.frame_compare)
		self.label_compareResult.setGeometry(QtCore.QRect(40, 760, 531, 51))
		self.label_compareResult.setStyleSheet("border-image: url(:/ResultBar.png);\n"
"font-size:20px;\n"
"font-weight:bold;\n"
"font-family:Roman times;")
		self.label_compareResult.setAlignment(QtCore.Qt.AlignCenter)
		self.label_compareResult.setObjectName("label_compareResult")
		self.clearPicBtn = QtWidgets.QPushButton(self.frame_compare)
		self.clearPicBtn.setGeometry(QtCore.QRect(870, 760, 131, 51))
		self.clearPicBtn.setStyleSheet("QPushButton{border-image: url(:/clearBtn.png)}\n"
"QPushButton:hover{border-image: url(:/clearBtnHover.png)}\n"
"QPushButton:pressed{border-image: url(:/clearBtnActive.png)}")
		self.clearPicBtn.setText("")
		self.clearPicBtn.setObjectName("clearPicBtn")
		self.searchTypeBtn = QtWidgets.QPushButton(self.frame_compare)
		self.searchTypeBtn.setGeometry(QtCore.QRect(0, 0, 160, 50))
		self.searchTypeBtn.setStyleSheet("border-image: url(:/SearchBtn.png);")
		self.searchTypeBtn.setText("")
		self.searchTypeBtn.setObjectName("searchTypeBtn")
		self.verifyTypeBtn = QtWidgets.QPushButton(self.frame_compare)
		self.verifyTypeBtn.setGeometry(QtCore.QRect(0, 50, 160, 50))
		self.verifyTypeBtn.setStyleSheet("border-image: url(:/VerifyBtn.png);")
		self.verifyTypeBtn.setText("")
		self.verifyTypeBtn.setObjectName("verifyTypeBtn")
		self.frame_compare_verify = QtWidgets.QFrame(self.centralwidget)
		self.frame_compare_verify.setGeometry(QtCore.QRect(0, 59, 1300, 841))
		self.frame_compare_verify.setStyleSheet("    #frame_compare_verify { \n"
" \n"
"    \n"
"    background-color:rgb(49, 45, 61);\n"
"    }")
		self.frame_compare_verify.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_compare_verify.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_compare_verify.setObjectName("frame_compare_verify")
		self.frame_compare_verify.close()
		self.label_compare_verify_tag = QtWidgets.QLabel(self.frame_compare_verify)
		self.label_compare_verify_tag.setGeometry(QtCore.QRect(1175, 0, 131, 131))
		self.label_compare_verify_tag.setStyleSheet("border-image: url(:/ComTag.png);")
		self.label_compare_verify_tag.setText("")
		self.label_compare_verify_tag.setObjectName("label_compare_verify_tag")
		self.listViewFileName = QtWidgets.QListView(self.frame_compare_verify)
		self.listViewFileName.setGeometry(QtCore.QRect(10, 130, 561, 511))
		self.listViewFileName.setStyleSheet("background-color:rgb(255,255,255);\n")
		self.listViewFileName.setObjectName("listViewFileName")
		# self.listViewFileName.setStyleSheet("border-image: url(:/frame.png);")
		self.selectPicBtn2 = QtWidgets.QPushButton(self.frame_compare_verify)
		self.selectPicBtn2.setGeometry(QtCore.QRect(70, 660, 131, 51))
		self.selectPicBtn2.setStyleSheet("QPushButton{border-image: url(:/selectBtn.png)}\n"
"QPushButton:hover{border-image: url(:/selectBtnHover.png)}\n"
"QPushButton:pressed{border-image: url(:/selectBtnActive.png)}")
		self.selectPicBtn2.setText("")
		self.selectPicBtn2.setObjectName("selectPicBtn2")
		self.label_verifyResult = QtWidgets.QLabel(self.frame_compare_verify)
		self.label_verifyResult.setGeometry(QtCore.QRect(430, 770, 531, 51))
		self.label_verifyResult.setStyleSheet("border-image: url(:/ResultBar.png);\n"
"font-size:30px;\n"
"font-weight:bold;\n"
"font-family:Roman times;")
		self.label_verifyResult.setAlignment(QtCore.Qt.AlignCenter)
		self.label_verifyResult.setObjectName("label_verifyResult")
		self.comVerifyStartBtn = QtWidgets.QPushButton(self.frame_compare_verify)
		self.comVerifyStartBtn.setGeometry(QtCore.QRect(400, 660, 131, 51))
		self.comVerifyStartBtn.setStyleSheet("QPushButton{border-image: url(:/startBtn.png)}\n"
"QPushButton:hover{border-image: url(:/startBtnHover.png)}\n"
"QPushButton:pressed{border-image: url(:/startBtnActive.png)}")
		self.comVerifyStartBtn.setText("")
		self.comVerifyStartBtn.setObjectName("comVerifyStartBtn")
		self.verifyTypeBtn_2 = QtWidgets.QPushButton(self.frame_compare_verify)
		self.verifyTypeBtn_2.setGeometry(QtCore.QRect(0, 50, 160, 50))
		self.verifyTypeBtn_2.setStyleSheet("border-image: url(:/VerifyBtn.png);")
		self.verifyTypeBtn_2.setText("")
		self.verifyTypeBtn_2.setObjectName("verifyTypeBtn_2")
		self.searchTypeBtn_2 = QtWidgets.QPushButton(self.frame_compare_verify)
		self.searchTypeBtn_2.setGeometry(QtCore.QRect(0, 0, 160, 50))
		self.searchTypeBtn_2.setStyleSheet("border-image: url(:/SearchBtn.png);")
		self.searchTypeBtn_2.setText("")
		self.searchTypeBtn_2.setObjectName("searchTypeBtn_2")
		self.labelInfo1 = QtWidgets.QLabel(self.frame_compare)
		self.labelInfo1.setGeometry(QtCore.QRect(710, 330, 181, 31))
		self.labelInfo1.setStyleSheet("background-color: rgb(49, 45, 61);\n"
"color: rgb(0, 170, 255);")
		self.labelInfo1.setObjectName("labelInfo1")
		self.labelInfo2 = QtWidgets.QLabel(self.frame_compare)
		self.labelInfo2.setGeometry(QtCore.QRect(950, 330, 181, 31))
		self.labelInfo2.setStyleSheet("background-color: rgb(49, 45, 61);\n"
"color: rgb(0, 170, 255);")
		self.labelInfo2.setObjectName("labelInfo2")
		self.labelInfo3 = QtWidgets.QLabel(self.frame_compare)
		self.labelInfo3.setGeometry(QtCore.QRect(600, 710, 181, 31))
		self.labelInfo3.setStyleSheet("background-color: rgb(49, 45, 61);\n"
"color: rgb(0, 170, 255);")
		self.labelInfo3.setObjectName("labelInfo3")
		self.labelInfo4 = QtWidgets.QLabel(self.frame_compare)
		self.labelInfo4.setGeometry(QtCore.QRect(830, 710, 181, 31))
		self.labelInfo4.setStyleSheet("background-color: rgb(49, 45, 61);\n"
"color: rgb(0, 170, 255);")
		self.labelInfo4.setObjectName("labelInfo4")
		self.labelInfo5 = QtWidgets.QLabel(self.frame_compare)
		self.labelInfo5.setGeometry(QtCore.QRect(1060, 710, 181, 31))
		self.labelInfo5.setStyleSheet("background-color: rgb(49, 45, 61);\n"
"color: rgb(0, 170, 255);")
		self.labelInfo5.setObjectName("labelInfo5")
		self.labelPS = QtWidgets.QLabel(self.frame_compare)
		self.labelPS.setGeometry(QtCore.QRect(190, 20, 281, 71))
		self.labelPS.setStyleSheet("background-color: rgb(49, 45, 61);\n"
"color: rgb(0, 170, 255);\n"
"font-size:15px")
		self.labelPS.setObjectName("labelPS")
		self.photoFrame0.raise_()
		self.photoFrame1.raise_()
		self.photoFrame2.raise_()
		self.photoFrame3.raise_()
		self.photoFrame4.raise_()
		self.photoFrame5.raise_()
		self.photo0.raise_()
		self.photo1.raise_()
		self.photo2.raise_()
		self.photo3.raise_()
		self.photo4.raise_()
		self.photo5.raise_()
		self.selectPicBtn.raise_()
		self.com_startBtn.raise_()
		self.label_compare_tag.raise_()
		self.label_compareResult.raise_()
		self.clearPicBtn.raise_()
		self.searchTypeBtn.raise_()
		self.verifyTypeBtn.raise_()
		self.labelInfo1.raise_()
		self.labelInfo2.raise_()
		self.labelInfo3.raise_()
		self.labelInfo4.raise_()
		self.labelInfo5.raise_()
		self.labelPS.raise_()
		self.frame_compare_verify.raise_()
		self.menu.raise_()
		self.comTagUs.raise_()
		self.encodeTagS.raise_()
		self.traTagUs.raise_()
		self.emTagUs.raise_()
		self.encodeTagUs.raise_()
		self.comTagS.raise_()
		self.traTagS.raise_()
		self.emTagS.raise_()
		self.capTagUs.raise_()
		self.capTagS.raise_()
		self.frame_capture.raise_()
		self.frame_compare.raise_()
		self.frame_em.raise_()
		self.frame_tracker.raise_()
		self.frame_encode.raise_()
		MainWindow.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
		self.currentFrame=self.frame_encode
		self.currentSTab=self.encodeTagS
		self.currentUsTab=self.encodeTagUs

		self.encodeTagUs.clicked.connect(self.EncodeTabEvent)
		self.comTagUs.clicked.connect(self.CompareTabEvent)
		self.capTagUs.clicked.connect(self.CaptureTabEvent)
		self.traTagUs.clicked.connect(self.TrackTabEvent)
		self.emTagUs.clicked.connect(self.EmotionTabEvent)


		self.pushButton.clicked.connect(self.EncodeAllChecker)

		self.searchTypeBtn.clicked.connect(self.SearchTypeBtnEvent)
		self.verifyTypeBtn.clicked.connect(self.VerifyTypeBtnEvent)
		self.searchTypeBtn_2.clicked.connect(self.SearchTypeBtnEvent)
		self.verifyTypeBtn_2.clicked.connect(self.VerifyTypeBtnEvent)
		self.selectPicBtn.clicked.connect(self.SelectPicBtnEvent)
		self.clearPicBtn.clicked.connect(self.clearPicBtnEvent)
		self.com_startBtn.clicked.connect(self.ComStartBtnEvent)
		self.selectPicBtn2.clicked.connect(self.SelectPicsBtnEvent)
		self.comVerifyStartBtn.clicked.connect(self.VerifyCompareBtnEvent)
		self.trackCameraSwitch.clicked.connect(self.TrackCameraSwitchEvent)
		self.cap_selectPicBtn.clicked.connect(self.CapSelectPicBtnEvent)
		self.startCapBtn.clicked.connect(self.StartCapBtnEvent)
		self.emCameraSwitch.clicked.connect(self.EmotionCameraSwitchEvent)
		self.trackerStartBtn.clicked.connect(self.TrackerStartBtnEvent)
		self.emStartBtn.clicked.connect(self.EmotionStartBtnEvent)

		self.photoFramePool=[self.photoFrame1,self.photoFrame2,self.photoFrame3,self.photoFrame4,self.photoFrame5]
		self.photoPool=[self.photo1,self.photo2,self.photo3,self.photo4,self.photo5]
		self.labelInfoPool = [self.labelInfo1, self.labelInfo2, self.labelInfo3, self.labelInfo4, self.labelInfo5]
		self.cameraIsOn = False
		self.video=AppConfig.AppConfig.videoAddr
		self.cap = cv2.VideoCapture(self.video)
		self.cameraTimer = QtCore.QTimer()
		self.isEmCam=True
		self.doingTrack=False
		self.faceTracker=fb.FaceTracker()
		self.siamFaceTracke=fb.SiamFaceTracker()
		self.siamBodyTracker=fb.SiamBodyTracker()

		self.doingEmotionRecg=False
		self.emotionRecognizer=fb.EmotionRecognizer()

		self.cameraTimer.timeout.connect(self.ShowCamera)

		self.EmotionRecgFrameInterval=self.emotionRecognizer.getRecgFrameInterval()

		#self.FrameSwitch(self.frame_capture)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.label.setText(_translate("MainWindow", "输入被追踪人员id（多个id用逗号隔开）"))
		self.trackType1RB.setText(_translate("MainWindow", "检测式追踪"))
		self.trackType2RB.setText(_translate("MainWindow", "高级面部追踪"))
		self.trackType3RB.setText(_translate("MainWindow", "高级身体追踪"))
		self.label_emotionResult.setText(_translate("MainWindow", ""))
		self.label_emotionType.setText(_translate("MainWindow", ""))
		self.label_compareResult.setText(_translate("MainWindow", ""))
		self.label_verifyResult.setText(_translate("MainWindow", ""))
		self.labelInfo1.setText(_translate("MainWindow", ""))
		self.labelInfo2.setText(_translate("MainWindow", ""))
		self.labelInfo3.setText(_translate("MainWindow", ""))
		self.labelInfo4.setText(_translate("MainWindow", ""))
		self.labelInfo5.setText(_translate("MainWindow", ""))
		self.labelPS.setText(_translate("MainWindow", "Dis越小越相似，质量检测值越小质量越高"))

	def FrameSwitch(self,frame):
		self.currentFrame.close()
		frame.show()
		self.currentFrame=frame

	def TabStateChange(self,tabSNext,tabUsNext):
		self.currentSTab.setVisible(False)
		self.currentUsTab.setVisible(True)
		tabSNext.setVisible(True)
		tabUsNext.setVisible(False)
		self.currentSTab=tabSNext
		self.currentUsTab=tabUsNext

	def EncodeTabEvent(self):
		self.TabStateChange(self.encodeTagS,self.encodeTagUs)
		self.FrameSwitch(self.frame_encode)
	def CompareTabEvent(self):
		self.TabStateChange(self.comTagS,self.comTagUs)
		self.FrameSwitch(self.frame_compare)
	def CaptureTabEvent(self):
		self.TabStateChange(self.capTagS,self.capTagUs)
		self.FrameSwitch(self.frame_capture)
	def TrackTabEvent(self):
		self.TabStateChange(self.traTagS,self.traTagUs)
		self.FrameSwitch(self.frame_tracker)
	def EmotionTabEvent(self):
		self.TabStateChange(self.emTagS,self.emTagUs)
		self.FrameSwitch(self.frame_em)

	def SearchTypeBtnEvent(self):
		if self.currentFrame==self.frame_compare_verify:
			# change parent to reuse widget
			for widget in self.photoFramePool+self.photoPool+self.labelInfoPool:
				widget.setParent(self.frame_compare)

			# clean widgets reused
			for widget in  self.photoPool+self.labelInfoPool:
				widget.clear()

			# switch frame
			self.FrameSwitch(self.frame_compare)
	def VerifyTypeBtnEvent(self):
		if self.currentFrame==self.frame_compare:
			for widget in self.photoFramePool+self.photoPool+self.labelInfoPool:
				widget.setParent(self.frame_compare_verify)

			for widget in  self.photoPool+self.labelInfoPool:
				widget.clear()

			self.FrameSwitch(self.frame_compare_verify)
	def SelectPicBtnEvent(self):
		Image,_=QFileDialog.getOpenFileName(self.centralwidget,"select file","C:/")
		if(len(Image)!=0):  # TODO这里可以完善：过滤器，判断文件是否存在
			img=cv2.imread(Image)
			self.ImagePath=Image
			self.showCV2imgInLabel(self.photo0,img)
			imageAss=fb.ImageQualityAssement()
			score = imageAss.assement(img)
			self.labelPS.setText("Dis越小越相似，质量检测值越小质量越高\n\n本次图片质量为%.4f"%(score))

	def SelectPicsBtnEvent(self):
		images,_=QFileDialog.getOpenFileNames(self.centralwidget,"select file","C:/")
		slm = QStringListModel()
		slm.setStringList(images)
		self.tempslm=slm
		#print(slm.stringList())
		self.listViewFileName.setModel(slm)

	def	VerifyCompareBtnEvent(self):
		self.label_verifyResult.clear()
		fileNameList=self.tempslm.stringList()
		imageList = []
		for imgName in fileNameList:
			imageList.append(cv2.imread(imgName))
		fileNameList=[path.basename(i) for i in fileNameList]

		# cut out n data to show, n=len(self.photoPool)
		showNumLimit=min(len(fileNameList),len(self.photoPool))
		imageListLimited=imageList[:showNumLimit]
		fileNameListLimited=fileNameList[:showNumLimit]
		photoPoolLimited=self.photoPool[:showNumLimit]
		labelInfoPoolLimited=self.labelInfoPool[:showNumLimit]


		# show result
		# clear widget
		for widget in self.photoPool + self.labelInfoPool:
			widget.clear()

		# show imgs
		for label,img in zip(photoPoolLimited,imageListLimited):
			self.showCV2imgInLabel(label,img)

		# show info
		for fileName,labelInfo in zip(fileNameListLimited,labelInfoPoolLimited):
			labelInfo.setText(fileName)

		# cal result
		Result=fb.faceCheckCompare(imageList)

		# show decision
		if Result==True:
			self.label_verifyResult.setText("Result:是同一个人")
		else:
			self.label_verifyResult.setText("Result:不是同一个人")

	def ComStartBtnEvent(self):
		imgOr=cv2.imread(self.ImagePath)
		info=fb.faceSearchCompare(imgOr)
		for personInfo,photo,labelInfo in zip(info,self.photoPool,self.labelInfoPool):
			ID,name,dis=personInfo
			labelInfo.setText("ID:%s Name:%s Dis:%.4f"%(ID,name,dis))
			imgBlob=self.db.getFaceByID(int(ID))
			img=fl.jpgBlob2img(imgBlob)
			self.showCV2imgInLabel(photo,img)
		self.label_compareResult.setText("Result：目标已找到！")

	def clearPicBtnEvent(self):
		self.photo0.clear()
		self.photo1.clear()
		self.photo2.clear()
		self.photo3.clear()
		self.photo4.clear()
		self.photo5.clear()



	def EncodeAllChecker(self):
		numEncoded=fb.genEncodings()
		msg=QMessageBox.information(self.centralwidget,"信息","建模已完成！共建模%d个人脸"%(numEncoded), QMessageBox.Ok)

	def TrackCameraSwitchEvent(self):
		if(self.cameraIsOn==False):
			self.trackCameraSwitch.setStyleSheet("QPushButton{border-image: url(:/switchOn.png)}")
			self.cameraIsOn=True
			self.isEmCam=False
			self.OpenCamera()
		else:
			self.trackCameraSwitch.setStyleSheet("QPushButton{border-image: url(:/switchOff.png)}")
			self.cameraIsOn=False
			self.CloseCamera()
			self.doingTrack=False
	def TrackerStartBtnEvent(self):
		OrString=self.idLineEdit.text()
		strList=OrString.split(",")
		wantIDs=[int(IDstr) for IDstr in strList]
		if self.cameraTimer.isActive()==True:
			self.doingTrack=True
			if self.trackType1RB.isChecked()==True:
				self.faceTracker.reset()
				self.faceTracker.setWantIDs(wantIDs)
			elif self.trackType2RB.isChecked()==True:
				self.siamFaceTracke.reset()
				self.siamFaceTracke.setWantIDs(wantIDs)
			else:
				self.siamBodyTracker.reset()
				self.siamBodyTracker.setWantIDs(wantIDs)
		else:
			msg = QMessageBox.information(self.centralwidget,"错误","摄像头未打开！", QMessageBox.Yes)


	def CapSelectPicBtnEvent(self):
		Image,_=QFileDialog.getOpenFileName(self.centralwidget,"select file","C:/")
		self.ImagePath=Image
		PImage=QPixmap(Image)
		SPImage=PImage.scaled(self.cap_photo0.width(),self.cap_photo0.height(),aspectRatioMode=Qt.KeepAspectRatio)
		self.cap_photo0.setPixmap(SPImage)
	def StartCapBtnEvent(self):
		imgOr=cv2.imread(self.ImagePath)
		caper=fb.faceCaper()
		img=caper.cap(imgOr)
		caper.save()
		msg = QMessageBox.information(self.centralwidget, "信息", "人脸图片已自动保存到%s！" % (path.abspath('.')), QMessageBox.Ok)
		show = cv2.resize(img, (self.cap_photo0_2.width(), self.cap_photo0_2.height()))
		show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
		showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], 3 * show.shape[1], QtGui.QImage.Format_RGB888)
		self.cap_photo0_2.setPixmap(QtGui.QPixmap.fromImage(showImage))

	def EmotionCameraSwitchEvent(self):
		if(self.cameraIsOn==False):
			self.emCameraSwitch.setStyleSheet("QPushButton{border-image: url(:/switchOn.png)}")
			self.cameraIsOn=True
			self.isEmCam=True
			self.OpenCamera()

		else:
			self.emCameraSwitch.setStyleSheet("QPushButton{border-image: url(:/switchOff.png)}")
			self.cameraIsOn=False
			self.CloseCamera()
			self.doingEmotionRecg=False

	def EmotionStartBtnEvent(self):
		if self.cameraTimer.isActive() == True:
			self.emotionRecognizer.reset()
			self.doingEmotionRecg = True
			self.doneEmotionCount=0
			self.needNextEmotion=True
			self.label_emotionResult.setText("")
		else:
			msg = QMessageBox.information(self.centralwidget, "错误", "摄像头未打开！", QMessageBox.Yes)

	def OpenCamera(self):
		self.emotionFrameNum=0
		if self.cameraTimer.isActive() == False:
			flag = self.cap.open(self.video)
			if flag == False:
				msg = QtWidgets.QMessageBox.warning(self, u"Warning", u"请检测相机与电脑是否连接正确",
													buttons=QtWidgets.QMessageBox.Ok,
													defaultButton=QtWidgets.QMessageBox.Ok)
			else:
				self.cameraTimer.start(30)

	def CloseCamera(self):
		if self.cameraTimer.isActive() == True:
			self.cameraTimer.stop()
			self.cap.release()
			if self.isEmCam:
				self.emLabelShowCamera.clear()
				self.label_emotionResult.setText('')
				self.label_emotionType.setText('')
			else:
				self.trackLabelShowCamera.clear()

	def ShowCamera(self):
		if self.doingTrack:
			ret, frameOr = self.cap.read()
			frameRes = None
			if self.trackType1RB.isChecked() == True:
				frameRes = self.faceTracker.track(frameOr)
			elif self.trackType2RB.isChecked() == True:
				frameRes = self.siamFaceTracke.track(frameOr)
			else:
				frameRes = self.siamBodyTracker.track(frameOr)
			show = cv2.resize(frameRes, (self.trackLabelShowCamera.width(), self.trackLabelShowCamera.height()))
			show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
			showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], show.shape[1] * 3,
									 QtGui.QImage.Format_RGB888)
			self.trackLabelShowCamera.setPixmap(QtGui.QPixmap.fromImage(showImage))
		elif self.doingEmotionRecg:
			self.emotionFrameNum+=1
			if self.needNextEmotion==True:
				self.expectEmotion=self.emotionRecognizer.genRandomRequireEmotion()
				self.label_emotionType.setText(self.expectEmotion)
				self.needNextEmotion=False
			_, self.image = self.cap.read()
			show = cv2.resize(self.image, (self.emLabelShowCamera.width(), self.emLabelShowCamera.height()))
			show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
			showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], show.shape[1] * 3,
									 QtGui.QImage.Format_RGB888)
			self.emLabelShowCamera.setPixmap(QtGui.QPixmap.fromImage(showImage))
			self.emotionFrameNum = (self.emotionFrameNum + 1) % self.EmotionRecgFrameInterval
			if not self.emotionFrameNum:   # time to check
				result=self.emotionRecognizer.checkEmotion(self.image, self.expectEmotion)
				if type(result)==str:   # time use out
					self.label_emotionResult.setText("Result：超时检测失败！")
					self.doingEmotionRecg = False
				elif result:
					self.doneEmotionCount+=1
					if self.doneEmotionCount == 3:
						self.label_emotionResult.setText("Result：是真人")
						self.label_emotionType.setText('')
						self.doingEmotionRecg = False
					else:
						self.needNextEmotion=True
		else:
			_, self.image = self.cap.read()
			if self.isEmCam == True:
				show = cv2.resize(self.image, (self.emLabelShowCamera.width(), self.emLabelShowCamera.height()))
			else:
				show = cv2.resize(self.image, (self.trackLabelShowCamera.width(), self.trackLabelShowCamera.height()))

			show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
			showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], show.shape[1] * 3,
									 QtGui.QImage.Format_RGB888)
			if self.isEmCam == True:
				self.emLabelShowCamera.setPixmap(QtGui.QPixmap.fromImage(showImage))
			else:
				self.trackLabelShowCamera.setPixmap(QtGui.QPixmap.fromImage(showImage))

	def showCV2imgInLabel(self,label,rawImage):
		_,_,w,h=label.geometry().getRect() # geometry() return QRect
		img = cv2.resize(rawImage, (w, h))
		img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		Qimg = QtGui.QImage(img.data, img.shape[1], img.shape[0], 3*w,QtGui.QImage.Format_RGB888)
		label.setPixmap(QtGui.QPixmap.fromImage(Qimg))

	def showPic(self,label,path):
		# deprecated
		# 使用QT的方法读取和显示图片在读取用手机拍摄的照片时会旋转90度
		PImage = QPixmap(path)
		SPImage = PImage.scaled(label.width(), label.height(), aspectRatioMode=Qt.KeepAspectRatio)
		label.setPixmap(SPImage)

import picture_rc

import sys

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	ex = Ui_MainWindow()
	w = QtWidgets.QMainWindow()
	ex.setupUi(w)
	w.show()
	sys.exit(app.exec_())
