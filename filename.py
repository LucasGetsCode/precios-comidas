# Form implementation generated from reading ui file 'Interfaz.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(543, 377)
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 271, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.spinBox = QtWidgets.QSpinBox(parent=self.horizontalLayoutWidget)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 10, 171, 24))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 50, 91, 24))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(110, 50, 111, 24))
        self.pushButton_5.setObjectName("pushButton_5")
        self.scrollArea = QtWidgets.QScrollArea(parent=Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(360, 40, 171, 321))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 169, 319))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.groupBox = QtWidgets.QGroupBox(parent=Dialog)
        self.groupBox.setGeometry(QtCore.QRect(19, 140, 311, 80))
        self.groupBox.setObjectName("groupBox")
        self.graphicsView = QtWidgets.QGraphicsView(parent=self.groupBox)
        self.graphicsView.setGeometry(QtCore.QRect(10, 20, 41, 41))
        self.graphicsView.setObjectName("graphicsView")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 20, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(60, 50, 49, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(130, 50, 161, 16))
        self.label_2.setObjectName("label_2")
        self.spinBox_2 = QtWidgets.QSpinBox(parent=self.groupBox)
        self.spinBox_2.setGeometry(QtCore.QRect(180, 20, 42, 22))
        self.spinBox_2.setObjectName("spinBox_2")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(240, 20, 31, 24))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_7.setGeometry(QtCore.QRect(270, 20, 31, 24))
        self.pushButton_7.setObjectName("pushButton_7")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 220, 311, 80))
        self.groupBox_2.setObjectName("groupBox_2")
        self.graphicsView_2 = QtWidgets.QGraphicsView(parent=self.groupBox_2)
        self.graphicsView_2.setGeometry(QtCore.QRect(10, 20, 41, 41))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(60, 20, 113, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(60, 50, 49, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(130, 50, 161, 16))
        self.label_4.setObjectName("label_4")
        self.spinBox_3 = QtWidgets.QSpinBox(parent=self.groupBox_2)
        self.spinBox_3.setGeometry(QtCore.QRect(180, 20, 42, 22))
        self.spinBox_3.setObjectName("spinBox_3")
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButton_8.setGeometry(QtCore.QRect(240, 20, 31, 24))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButton_9.setGeometry(QtCore.QRect(270, 20, 31, 24))
        self.pushButton_9.setObjectName("pushButton_9")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "OK"))
        self.pushButton_2.setText(_translate("Dialog", "NO"))
        self.pushButton_3.setText(_translate("Dialog", "Actualizar Precios"))
        self.pushButton_4.setText(_translate("Dialog", "Agregar URL"))
        self.pushButton_5.setText(_translate("Dialog", "Agregar producto"))
        self.groupBox.setTitle(_translate("Dialog", "GroupBox"))
        self.label.setText(_translate("Dialog", "Precio:"))
        self.label_2.setText(_translate("Dialog", "Precio por KG/L/Unidad:"))
        self.pushButton_6.setText(_translate("Dialog", "OK"))
        self.pushButton_7.setText(_translate("Dialog", "NO"))
        self.groupBox_2.setTitle(_translate("Dialog", "GroupBox"))
        self.label_3.setText(_translate("Dialog", "Precio:"))
        self.label_4.setText(_translate("Dialog", "Precio por KG/L/Unidad:"))
        self.pushButton_8.setText(_translate("Dialog", "OK"))
        self.pushButton_9.setText(_translate("Dialog", "NO"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
