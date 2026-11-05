# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_transaction.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QDialog, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import res_new_window

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(363, 450)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"font-family: Noto Sans SC;")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setStyleSheet(u"background-color: rgba(255,255,255, 30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_new_transaction = QLabel(self.frame)
        self.lbl_new_transaction.setObjectName(u"lbl_new_transaction")
        self.lbl_new_transaction.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")
        self.lbl_new_transaction.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_new_transaction)

        self.cb_category = QComboBox(self.frame)
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.setObjectName(u"cb_category")
        self.cb_category.setMaximumSize(QSize(16777215, 16777215))
        self.cb_category.setStyleSheet(u"QComboBox {\n"
"font-size: 16pt;\n"
"color: black;\n"
"padding-left: 10px;\n"
"}\n"
"\n"
"QComboCox:item {\n"
"color: white; \n"
"padding-left: 10px;\n"
"}")

        self.verticalLayout.addWidget(self.cb_category)

        self.date = QDateEdit(self.frame)
        self.date.setObjectName(u"date")
        self.date.setStyleSheet(u"font-size: 16pt;\n"
"color: black;\n"
"padding-left: 10px;\n"
"")
        self.date.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.date.setDate(QDate(2026, 1, 1))

        self.verticalLayout.addWidget(self.date)

        self.le_description = QLineEdit(self.frame)
        self.le_description.setObjectName(u"le_description")
        self.le_description.setStyleSheet(u"font-size: 16pt;\n"
"color: black;\n"
"padding-left: 10px;")

        self.verticalLayout.addWidget(self.le_description)

        self.le_balance = QLineEdit(self.frame)
        self.le_balance.setObjectName(u"le_balance")
        self.le_balance.setStyleSheet(u"font-size: 16pt;\n"
"color: black;\n"
"padding-left: 10px;")

        self.verticalLayout.addWidget(self.le_balance)

        self.comboBox_2 = QComboBox(self.frame)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setStyleSheet(u"QComboBox {\n"
"font-size: 16pt;\n"
"color: black;\n"
"padding-left: 10px;\n"
"}\n"
"\n"
"QComboCox:item {\n"
"color: white; \n"
"padding-left: 10px;\n"
"}")

        self.verticalLayout.addWidget(self.comboBox_2)

        self.btn_new_transaction = QPushButton(self.frame)
        self.btn_new_transaction.setObjectName(u"btn_new_transaction")
        self.btn_new_transaction.setStyleSheet(u"QPushButton {\n"
"color: black;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255,255,255,70);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/icon black/post_add_24dp_000000_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_new_transaction.setIcon(icon)
        self.btn_new_transaction.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.btn_new_transaction)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        self.cb_category.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lbl_new_transaction.setText(QCoreApplication.translate("Dialog", u"\u041d\u043e\u0432\u0430\u044f \u0442\u0440\u0430\u0437\u0430\u043a\u0446\u0438\u044f", None))
        self.cb_category.setItemText(0, QCoreApplication.translate("Dialog", u"\u0411\u0430\u043a\u0430\u043b\u0435\u044f", None))
        self.cb_category.setItemText(1, QCoreApplication.translate("Dialog", u"\u0420\u0430\u0437\u0432\u043b\u0435\u0447\u0435\u043d\u0438\u044f", None))
        self.cb_category.setItemText(2, QCoreApplication.translate("Dialog", u"\u0410\u0432\u0442\u043e-\u0442\u043e\u0432\u0430\u0440\u044b", None))
        self.cb_category.setItemText(3, QCoreApplication.translate("Dialog", u"\u0414\u0440\u0443\u0433\u043e\u0435", None))
        self.cb_category.setItemText(4, QCoreApplication.translate("Dialog", u"\u0420\u0430\u0431\u043e\u0442\u0430", None))

        self.cb_category.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e", None))
        self.le_description.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.le_balance.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0411\u0430\u043b\u0430\u043d\u0441", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Dialog", u"\u0414\u043e\u0445\u043e\u0434", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Dialog", u"\u0420\u0430\u0441\u0445\u043e\u0434", None))

        self.btn_new_transaction.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043d\u043e\u0432\u0443\u044e \u0442\u0440\u0430\u0437\u0430\u043a\u0446\u0438\u044e", None))
    # retranslateUi

