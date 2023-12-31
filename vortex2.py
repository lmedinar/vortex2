# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1203, 1055)
        MainWindow.setMaximumSize(QtCore.QSize(16018730, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Iconos/assets/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.layoutCenterAll = QtWidgets.QWidget(MainWindow)
        self.layoutCenterAll.setObjectName("layoutCenterAll")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutCenterAll)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.layoutMainVertical = QtWidgets.QVBoxLayout()
        self.layoutMainVertical.setObjectName("layoutMainVertical")
        self.labelSeccion1 = QtWidgets.QLabel(self.layoutCenterAll)
        self.labelSeccion1.setStyleSheet("font-weight: 900;\n"
"font-size: 15pt;")
        self.labelSeccion1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelSeccion1.setObjectName("labelSeccion1")
        self.layoutMainVertical.addWidget(self.labelSeccion1)
        self.layoutArduinoSection = QtWidgets.QHBoxLayout()
        self.layoutArduinoSection.setObjectName("layoutArduinoSection")
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutCenterAll)
        self.pushButton_3.setObjectName("pushButton_3")
        self.layoutArduinoSection.addWidget(self.pushButton_3)
        self.label_13 = QtWidgets.QLabel(self.layoutCenterAll)
        self.label_13.setObjectName("label_13")
        self.layoutArduinoSection.addWidget(self.label_13)
        self.comboBox = QtWidgets.QComboBox(self.layoutCenterAll)
        self.comboBox.setMinimumSize(QtCore.QSize(100, 0))
        self.comboBox.setObjectName("comboBox")
        self.layoutArduinoSection.addWidget(self.comboBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layoutArduinoSection.addItem(spacerItem)
        self.layoutMainVertical.addLayout(self.layoutArduinoSection)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutMainVertical.addItem(spacerItem1)
        self.lineLong1 = QtWidgets.QFrame(self.layoutCenterAll)
        self.lineLong1.setSizeIncrement(QtCore.QSize(0, 0))
        self.lineLong1.setLineWidth(3)
        self.lineLong1.setMidLineWidth(3)
        self.lineLong1.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineLong1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineLong1.setObjectName("lineLong1")
        self.layoutMainVertical.addWidget(self.lineLong1)
        self.labelSeccion2 = QtWidgets.QLabel(self.layoutCenterAll)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelSeccion2.sizePolicy().hasHeightForWidth())
        self.labelSeccion2.setSizePolicy(sizePolicy)
        self.labelSeccion2.setStyleSheet("font-weight: 900;\n"
"font-size: 15pt;")
        self.labelSeccion2.setObjectName("labelSeccion2")
        self.layoutMainVertical.addWidget(self.labelSeccion2)
        self.layoutMainVertical2 = QtWidgets.QVBoxLayout()
        self.layoutMainVertical2.setObjectName("layoutMainVertical2")
        self.layoutImageCenter = QtWidgets.QHBoxLayout()
        self.layoutImageCenter.setObjectName("layoutImageCenter")
        spacerItem2 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.layoutImageCenter.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 150, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.layoutImageCenter.addItem(spacerItem3)
        self.labelSignal = QtWidgets.QLabel(self.layoutCenterAll)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.labelSignal.sizePolicy().hasHeightForWidth())
        self.labelSignal.setSizePolicy(sizePolicy)
        self.labelSignal.setMinimumSize(QtCore.QSize(0, 100))
        self.labelSignal.setMaximumSize(QtCore.QSize(700, 1500))
        self.labelSignal.setBaseSize(QtCore.QSize(400, 200))
        self.labelSignal.setAutoFillBackground(False)
        self.labelSignal.setText("")
        self.labelSignal.setPixmap(QtGui.QPixmap(":/ImagenGraf/assets/graph.png"))
        self.labelSignal.setScaledContents(True)
        self.labelSignal.setWordWrap(False)
        self.labelSignal.setOpenExternalLinks(False)
        self.labelSignal.setObjectName("labelSignal")
        self.layoutImageCenter.addWidget(self.labelSignal)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.layoutImageCenter.addItem(spacerItem4)
        self.layoutMainVertical2.addLayout(self.layoutImageCenter)
        self.layoutMainVertical.addLayout(self.layoutMainVertical2)
        self.layoutParams = QtWidgets.QGridLayout()
        self.layoutParams.setObjectName("layoutParams")
        self.labelUnidades2 = QtWidgets.QLabel(self.layoutCenterAll)
        self.labelUnidades2.setObjectName("labelUnidades2")
        self.layoutParams.addWidget(self.labelUnidades2, 3, 2, 1, 1)
        self.inSegundos = QtWidgets.QSpinBox(self.layoutCenterAll)
        self.inSegundos.setMaximumSize(QtCore.QSize(160, 16777215))
        self.inSegundos.setMinimum(10)
        self.inSegundos.setMaximum(1200)
        self.inSegundos.setSingleStep(5)
        self.inSegundos.setProperty("value", 120)
        self.inSegundos.setObjectName("inSegundos")
        self.layoutParams.addWidget(self.inSegundos, 6, 1, 1, 1)
        self.inTsubida = QtWidgets.QSpinBox(self.layoutCenterAll)
        self.inTsubida.setMaximumSize(QtCore.QSize(160, 16777215))
        self.inTsubida.setMinimum(10)
        self.inTsubida.setMaximum(600)
        self.inTsubida.setSingleStep(5)
        self.inTsubida.setProperty("value", 30)
        self.inTsubida.setObjectName("inTsubida")
        self.layoutParams.addWidget(self.inTsubida, 1, 1, 1, 1)
        self.labelUnidades1 = QtWidgets.QLabel(self.layoutCenterAll)
        self.labelUnidades1.setObjectName("labelUnidades1")
        self.layoutParams.addWidget(self.labelUnidades1, 1, 2, 1, 1)
        self.miniline4 = QtWidgets.QFrame(self.layoutCenterAll)
        self.miniline4.setMidLineWidth(1)
        self.miniline4.setFrameShape(QtWidgets.QFrame.HLine)
        self.miniline4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.miniline4.setObjectName("miniline4")
        self.layoutParams.addWidget(self.miniline4, 8, 0, 1, 1)
        self.inRadioSegs = QtWidgets.QRadioButton(self.layoutCenterAll)
        self.inRadioSegs.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.inRadioSegs.setChecked(True)
        self.inRadioSegs.setObjectName("inRadioSegs")
        self.layoutParams.addWidget(self.inRadioSegs, 6, 0, 1, 1)
        self.labelTiempoEstable = QtWidgets.QLabel(self.layoutCenterAll)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTiempoEstable.sizePolicy().hasHeightForWidth())
        self.labelTiempoEstable.setSizePolicy(sizePolicy)
        self.labelTiempoEstable.setStyleSheet("font-weight:900;")
        self.labelTiempoEstable.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTiempoEstable.setObjectName("labelTiempoEstable")
        self.layoutParams.addWidget(self.labelTiempoEstable, 5, 0, 1, 1)
        self.miniline1 = QtWidgets.QFrame(self.layoutCenterAll)
        self.miniline1.setMinimumSize(QtCore.QSize(0, 0))
        self.miniline1.setMidLineWidth(1)
        self.miniline1.setFrameShape(QtWidgets.QFrame.HLine)
        self.miniline1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.miniline1.setObjectName("miniline1")
        self.layoutParams.addWidget(self.miniline1, 0, 0, 1, 1)
        self.miniline3 = QtWidgets.QFrame(self.layoutCenterAll)
        self.miniline3.setMidLineWidth(1)
        self.miniline3.setFrameShape(QtWidgets.QFrame.HLine)
        self.miniline3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.miniline3.setObjectName("miniline3")
        self.layoutParams.addWidget(self.miniline3, 4, 0, 1, 1)
        self.inRPM = QtWidgets.QSpinBox(self.layoutCenterAll)
        self.inRPM.setMaximumSize(QtCore.QSize(160, 16777215))
        self.inRPM.setMinimum(500)
        self.inRPM.setMaximum(10000)
        self.inRPM.setSingleStep(500)
        self.inRPM.setProperty("value", 5000)
        self.inRPM.setObjectName("inRPM")
        self.layoutParams.addWidget(self.inRPM, 3, 1, 1, 1)
        self.inTbajada = QtWidgets.QSpinBox(self.layoutCenterAll)
        self.inTbajada.setMaximumSize(QtCore.QSize(160, 16777215))
        self.inTbajada.setMinimum(10)
        self.inTbajada.setMaximum(600)
        self.inTbajada.setSingleStep(5)
        self.inTbajada.setObjectName("inTbajada")
        self.layoutParams.addWidget(self.inTbajada, 9, 1, 1, 1)
        self.miniline2 = QtWidgets.QFrame(self.layoutCenterAll)
        self.miniline2.setMinimumSize(QtCore.QSize(0, 0))
        self.miniline2.setMidLineWidth(1)
        self.miniline2.setFrameShape(QtWidgets.QFrame.HLine)
        self.miniline2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.miniline2.setObjectName("miniline2")
        self.layoutParams.addWidget(self.miniline2, 2, 0, 1, 1)
        self.labelVelocidadMax = QtWidgets.QLabel(self.layoutCenterAll)
        self.labelVelocidadMax.setStyleSheet("font-weight:900;")
        self.labelVelocidadMax.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelVelocidadMax.setObjectName("labelVelocidadMax")
        self.layoutParams.addWidget(self.labelVelocidadMax, 3, 0, 1, 1)
        self.inRadioMins = QtWidgets.QRadioButton(self.layoutCenterAll)
        self.inRadioMins.setAcceptDrops(False)
        self.inRadioMins.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.inRadioMins.setAutoFillBackground(False)
        self.inRadioMins.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Mexico))
        self.inRadioMins.setObjectName("inRadioMins")
        self.layoutParams.addWidget(self.inRadioMins, 7, 0, 1, 1)
        self.labelTiempoEstimadoTxt = QtWidgets.QLabel(self.layoutCenterAll)
        self.labelTiempoEstimadoTxt.setStyleSheet("font-weight:900;")
        self.labelTiempoEstimadoTxt.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTiempoEstimadoTxt.setObjectName("labelTiempoEstimadoTxt")
        self.layoutParams.addWidget(self.labelTiempoEstimadoTxt, 11, 0, 1, 1)
        self.inMinutos = QtWidgets.QSpinBox(self.layoutCenterAll)
        self.inMinutos.setEnabled(False)
        self.inMinutos.setMaximumSize(QtCore.QSize(160, 16777215))
        self.inMinutos.setMinimum(1)
        self.inMinutos.setMaximum(15)
        self.inMinutos.setProperty("value", 2)
        self.inMinutos.setObjectName("inMinutos")
        self.layoutParams.addWidget(self.inMinutos, 7, 1, 1, 1)
        self.layoutTiempoSalida = QtWidgets.QLabel(self.layoutCenterAll)
        self.layoutTiempoSalida.setStyleSheet("font-weight: 900;")
        self.layoutTiempoSalida.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.layoutTiempoSalida.setObjectName("layoutTiempoSalida")
        self.layoutParams.addWidget(self.layoutTiempoSalida, 1, 0, 1, 1)
        self.labelTiempoEstimado = QtWidgets.QLabel(self.layoutCenterAll)
        self.labelTiempoEstimado.setObjectName("labelTiempoEstimado")
        self.layoutParams.addWidget(self.labelTiempoEstimado, 11, 1, 1, 1)
        self.labelTiempoFrenado = QtWidgets.QLabel(self.layoutCenterAll)
        self.labelTiempoFrenado.setStyleSheet("font-weight:900;")
        self.labelTiempoFrenado.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTiempoFrenado.setObjectName("labelTiempoFrenado")
        self.layoutParams.addWidget(self.labelTiempoFrenado, 9, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.layoutCenterAll)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.layoutParams.addWidget(self.line, 10, 0, 1, 1)
        self.layoutMainVertical.addLayout(self.layoutParams)
        spacerItem5 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutMainVertical.addItem(spacerItem5)
        self.lineLong2 = QtWidgets.QFrame(self.layoutCenterAll)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineLong2.sizePolicy().hasHeightForWidth())
        self.lineLong2.setSizePolicy(sizePolicy)
        self.lineLong2.setMaximumSize(QtCore.QSize(16777215, 10))
        self.lineLong2.setLineWidth(3)
        self.lineLong2.setMidLineWidth(3)
        self.lineLong2.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineLong2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineLong2.setObjectName("lineLong2")
        self.layoutMainVertical.addWidget(self.lineLong2)
        self.labelSeccion3 = QtWidgets.QLabel(self.layoutCenterAll)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelSeccion3.sizePolicy().hasHeightForWidth())
        self.labelSeccion3.setSizePolicy(sizePolicy)
        self.labelSeccion3.setStyleSheet("font-weight: 900;\n"
"font-size: 15pt;")
        self.labelSeccion3.setObjectName("labelSeccion3")
        self.layoutMainVertical.addWidget(self.labelSeccion3)
        self.centerControl1 = QtWidgets.QHBoxLayout()
        self.centerControl1.setObjectName("centerControl1")
        self.centerControl2 = QtWidgets.QHBoxLayout()
        self.centerControl2.setObjectName("centerControl2")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.centerControl2.addItem(spacerItem6)
        self.buttonIniciar = QtWidgets.QPushButton(self.layoutCenterAll)
        self.buttonIniciar.setObjectName("buttonIniciar")
        self.centerControl2.addWidget(self.buttonIniciar)
        self.buttonDetener = QtWidgets.QPushButton(self.layoutCenterAll)
        self.buttonDetener.setEnabled(False)
        self.buttonDetener.setObjectName("buttonDetener")
        self.centerControl2.addWidget(self.buttonDetener)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.centerControl2.addItem(spacerItem7)
        self.centerControl1.addLayout(self.centerControl2)
        self.layoutMainVertical.addLayout(self.centerControl1)
        self.layoutBarras1 = QtWidgets.QHBoxLayout()
        self.layoutBarras1.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.layoutBarras1.setSpacing(6)
        self.layoutBarras1.setObjectName("layoutBarras1")
        self.layoutBarras2 = QtWidgets.QGridLayout()
        self.layoutBarras2.setObjectName("layoutBarras2")
        self.progressBar2 = QtWidgets.QProgressBar(self.layoutCenterAll)
        self.progressBar2.setProperty("value", 24)
        self.progressBar2.setObjectName("progressBar2")
        self.layoutBarras2.addWidget(self.progressBar2, 1, 1, 1, 1)
        self.labelBarra1 = QtWidgets.QLabel(self.layoutCenterAll)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelBarra1.sizePolicy().hasHeightForWidth())
        self.labelBarra1.setSizePolicy(sizePolicy)
        self.labelBarra1.setObjectName("labelBarra1")
        self.layoutBarras2.addWidget(self.labelBarra1, 0, 0, 1, 1)
        self.progressBar1 = QtWidgets.QProgressBar(self.layoutCenterAll)
        self.progressBar1.setProperty("value", 24)
        self.progressBar1.setObjectName("progressBar1")
        self.layoutBarras2.addWidget(self.progressBar1, 1, 0, 1, 1)
        self.labelBarra2 = QtWidgets.QLabel(self.layoutCenterAll)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelBarra2.sizePolicy().hasHeightForWidth())
        self.labelBarra2.setSizePolicy(sizePolicy)
        self.labelBarra2.setObjectName("labelBarra2")
        self.layoutBarras2.addWidget(self.labelBarra2, 0, 1, 1, 1)
        self.labelBarra3 = QtWidgets.QLabel(self.layoutCenterAll)
        self.labelBarra3.setObjectName("labelBarra3")
        self.layoutBarras2.addWidget(self.labelBarra3, 0, 2, 1, 1)
        self.progressBar3 = QtWidgets.QProgressBar(self.layoutCenterAll)
        self.progressBar3.setProperty("value", 24)
        self.progressBar3.setObjectName("progressBar3")
        self.layoutBarras2.addWidget(self.progressBar3, 1, 2, 1, 1)
        self.layoutBarras1.addLayout(self.layoutBarras2)
        self.layoutMainVertical.addLayout(self.layoutBarras1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.layoutMainVertical.addItem(spacerItem8)
        self.lineLong3 = QtWidgets.QFrame(self.layoutCenterAll)
        self.lineLong3.setLineWidth(3)
        self.lineLong3.setMidLineWidth(3)
        self.lineLong3.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineLong3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineLong3.setObjectName("lineLong3")
        self.layoutMainVertical.addWidget(self.lineLong3)
        self.labelSection4 = QtWidgets.QLabel(self.layoutCenterAll)
        self.labelSection4.setStyleSheet("font-weight: 900;\n"
"font-size: 15pt;")
        self.labelSection4.setObjectName("labelSection4")
        self.layoutMainVertical.addWidget(self.labelSection4)
        self.textEdit = QtWidgets.QTextEdit(self.layoutCenterAll)
        self.textEdit.setObjectName("textEdit")
        self.layoutMainVertical.addWidget(self.textEdit)
        self.layoutSubirBitacora = QtWidgets.QHBoxLayout()
        self.layoutSubirBitacora.setObjectName("layoutSubirBitacora")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layoutSubirBitacora.addItem(spacerItem9)
        self.buttonBitacora = QtWidgets.QPushButton(self.layoutCenterAll)
        self.buttonBitacora.setObjectName("buttonBitacora")
        self.layoutSubirBitacora.addWidget(self.buttonBitacora)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layoutSubirBitacora.addItem(spacerItem10)
        self.layoutMainVertical.addLayout(self.layoutSubirBitacora)
        self.horizontalLayout.addLayout(self.layoutMainVertical)
        MainWindow.setCentralWidget(self.layoutCenterAll)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1203, 32))
        self.menubar.setObjectName("menubar")
        self.menuA_cerca_de = QtWidgets.QMenu(self.menubar)
        self.menuA_cerca_de.setObjectName("menuA_cerca_de")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAcerca_de = QtWidgets.QAction(MainWindow)
        self.actionAcerca_de.setObjectName("actionAcerca_de")
        self.menuA_cerca_de.addAction(self.actionAcerca_de)
        self.menubar.addAction(self.menuA_cerca_de.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vortex2"))
        self.labelSeccion1.setText(_translate("MainWindow", "Detección de Arduino:"))
        self.pushButton_3.setText(_translate("MainWindow", "Actualizar lista"))
        self.label_13.setText(_translate("MainWindow", "Seleccione puerto:"))
        self.labelSeccion2.setText(_translate("MainWindow", "Parámetros de giro:"))
        self.labelUnidades2.setText(_translate("MainWindow", "RPM"))
        self.labelUnidades1.setText(_translate("MainWindow", "segundos"))
        self.inRadioSegs.setText(_translate("MainWindow", "Segundos:"))
        self.labelTiempoEstable.setText(_translate("MainWindow", "Tiempo estable:"))
        self.labelVelocidadMax.setText(_translate("MainWindow", "Velocidad máxima (estable):"))
        self.inRadioMins.setText(_translate("MainWindow", "Minutos:"))
        self.labelTiempoEstimadoTxt.setText(_translate("MainWindow", "Tiempo total estimado:"))
        self.layoutTiempoSalida.setText(_translate("MainWindow", "Tiempo de subida:"))
        self.labelTiempoEstimado.setText(_translate("MainWindow", "2 minutos con 40 segundos"))
        self.labelTiempoFrenado.setText(_translate("MainWindow", "Tiempo de bajada:"))
        self.labelSeccion3.setText(_translate("MainWindow", "Iniciar/Detener:"))
        self.buttonIniciar.setText(_translate("MainWindow", "Iniciar"))
        self.buttonDetener.setText(_translate("MainWindow", "Detener"))
        self.labelBarra1.setText(_translate("MainWindow", "Aceleración"))
        self.labelBarra2.setText(_translate("MainWindow", "Velocidad constante"))
        self.labelBarra3.setText(_translate("MainWindow", "Frenado"))
        self.labelSection4.setText(_translate("MainWindow", "Notas del experimento (bitácora digital):"))
        self.buttonBitacora.setText(_translate("MainWindow", "Subir a bitácora"))
        self.menuA_cerca_de.setTitle(_translate("MainWindow", "Ayuda"))
        self.actionAcerca_de.setText(_translate("MainWindow", "Acerca de"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
