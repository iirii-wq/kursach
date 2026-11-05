# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1037, 746)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"font-family: Noto Sans SC;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.balance_frame = QFrame(self.centralwidget)
        self.balance_frame.setObjectName(u"balance_frame")
        self.balance_frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.verticalLayout = QVBoxLayout(self.balance_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(12, 12, 12, 12)
        self.le_current_balance = QLabel(self.balance_frame)
        self.le_current_balance.setObjectName(u"le_current_balance")
        self.le_current_balance.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.le_current_balance)

        self.le_balance = QLabel(self.balance_frame)
        self.le_balance.setObjectName(u"le_balance")
        self.le_balance.setStyleSheet(u"color: black;\n"
"font-size: 30pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.le_balance)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.icon_up_arrow = QLabel(self.balance_frame)
        self.icon_up_arrow.setObjectName(u"icon_up_arrow")
        self.icon_up_arrow.setMaximumSize(QSize(24, 16777215))
        self.icon_up_arrow.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.icon_up_arrow.setPixmap(QPixmap(u":/icon /icon black/north_west_24dp_000000_FILL0_wght400_GRAD0_opsz24.svg"))

        self.horizontalLayout.addWidget(self.icon_up_arrow)

        self.label_income = QLabel(self.balance_frame)
        self.label_income.setObjectName(u"label_income")
        self.label_income.setStyleSheet(u"color: black;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding-top: 10px;")

        self.horizontalLayout.addWidget(self.label_income)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.income_balance = QLabel(self.balance_frame)
        self.income_balance.setObjectName(u"income_balance")
        self.income_balance.setStyleSheet(u"color: black;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.income_balance)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ico_down_arrow = QLabel(self.balance_frame)
        self.ico_down_arrow.setObjectName(u"ico_down_arrow")
        self.ico_down_arrow.setMaximumSize(QSize(24, 16777215))
        self.ico_down_arrow.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.ico_down_arrow.setPixmap(QPixmap(u":/icon /icon black/call_received_24dp_000000_FILL0_wght400_GRAD0_opsz24.svg"))

        self.horizontalLayout_2.addWidget(self.ico_down_arrow)

        self.label_outcome = QLabel(self.balance_frame)
        self.label_outcome.setObjectName(u"label_outcome")
        self.label_outcome.setStyleSheet(u"color: black;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding-top: 10px;")

        self.horizontalLayout_2.addWidget(self.label_outcome)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.outcome_balance = QLabel(self.balance_frame)
        self.outcome_balance.setObjectName(u"outcome_balance")
        self.outcome_balance.setStyleSheet(u"color: black;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.outcome_balance)


        self.horizontalLayout_7.addWidget(self.balance_frame)

        self.categories_frame = QFrame(self.centralwidget)
        self.categories_frame.setObjectName(u"categories_frame")
        self.categories_frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.verticalLayout_2 = QVBoxLayout(self.categories_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(12, 12, 12, 12)
        self.label_9 = QLabel(self.categories_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout_2.addWidget(self.label_9)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.icon_groceries = QLabel(self.categories_frame)
        self.icon_groceries.setObjectName(u"icon_groceries")
        self.icon_groceries.setMaximumSize(QSize(24, 16777215))
        self.icon_groceries.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.icon_groceries.setPixmap(QPixmap(u":/icon /icon black/shopping_cart_24dp_000000_FILL0_wght400_GRAD0_opsz24.svg"))

        self.horizontalLayout_6.addWidget(self.icon_groceries)

        self.label_groceries = QLabel(self.categories_frame)
        self.label_groceries.setObjectName(u"label_groceries")
        self.label_groceries.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_6.addWidget(self.label_groceries)

        self.balance_groceries = QLabel(self.categories_frame)
        self.balance_groceries.setObjectName(u"balance_groceries")
        self.balance_groceries.setStyleSheet(u"colo: black;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_6.addWidget(self.balance_groceries)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.ico_entertainment = QLabel(self.categories_frame)
        self.ico_entertainment.setObjectName(u"ico_entertainment")
        self.ico_entertainment.setMaximumSize(QSize(24, 16777215))
        self.ico_entertainment.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.ico_entertainment.setPixmap(QPixmap(u":/icon /icon black/sports_esports_24dp_000000_FILL0_wght400_GRAD0_opsz24.svg"))

        self.horizontalLayout_5.addWidget(self.ico_entertainment)

        self.label_entertainment = QLabel(self.categories_frame)
        self.label_entertainment.setObjectName(u"label_entertainment")
        self.label_entertainment.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_5.addWidget(self.label_entertainment)

        self.balance_entertainment = QLabel(self.categories_frame)
        self.balance_entertainment.setObjectName(u"balance_entertainment")
        self.balance_entertainment.setStyleSheet(u"color: black;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_5.addWidget(self.balance_entertainment)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.ico_auto = QLabel(self.categories_frame)
        self.ico_auto.setObjectName(u"ico_auto")
        self.ico_auto.setMaximumSize(QSize(24, 16777215))
        self.ico_auto.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.ico_auto.setPixmap(QPixmap(u":/icon /icon black/directions_car_24dp_000000_FILL0_wght400_GRAD0_opsz24.svg"))

        self.horizontalLayout_4.addWidget(self.ico_auto)

        self.label_auto = QLabel(self.categories_frame)
        self.label_auto.setObjectName(u"label_auto")
        self.label_auto.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_4.addWidget(self.label_auto)

        self.balance_auto = QLabel(self.categories_frame)
        self.balance_auto.setObjectName(u"balance_auto")
        self.balance_auto.setStyleSheet(u"color: black;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_4.addWidget(self.balance_auto)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.icon_other = QLabel(self.categories_frame)
        self.icon_other.setObjectName(u"icon_other")
        self.icon_other.setMaximumSize(QSize(24, 16777215))
        self.icon_other.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.icon_other.setPixmap(QPixmap(u":/icon /icon black/list_24dp_000000_FILL0_wght400_GRAD0_opsz24.svg"))

        self.horizontalLayout_3.addWidget(self.icon_other)

        self.label_other = QLabel(self.categories_frame)
        self.label_other.setObjectName(u"label_other")
        self.label_other.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_3.addWidget(self.label_other)

        self.balance_other = QLabel(self.categories_frame)
        self.balance_other.setObjectName(u"balance_other")
        self.balance_other.setStyleSheet(u"color: black;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_3.addWidget(self.balance_other)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

#1
        # --- Добавляем 5-ю категорию с иконкой ---
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")

        # Метка для иконки здоровья
        self.icon_health = QLabel(self.categories_frame)
        self.icon_health.setObjectName(u"icon_health")
        self.icon_health.setMaximumSize(QSize(24, 16777215))
        self.icon_health.setStyleSheet(u"background-color: none;\nborder: none;")
        # Указываем путь к вашей иконке из файла ресурсов
        self.icon_health.setPixmap(
                QPixmap(u":/icon /icon black/heart_plus_24dp_000000_FILL0_wght400_GRAD0_opsz24.svg"))
        self.horizontalLayout_9.addWidget(self.icon_health)

        # Метка текста "Здоровье"
        self.label_health = QLabel(self.categories_frame)
        self.label_health.setObjectName(u"label_health")
        self.label_health.setStyleSheet(
                u"color: black;\nfont-weight: bold;\nfont-size: 14pt;\nbackground-color: none;\nborder: none;")
        self.horizontalLayout_9.addWidget(self.label_health)

        # Метка суммы для здоровья
        self.balance_health = QLabel(self.categories_frame)
        self.balance_health.setObjectName(u"balance_health")
        self.balance_health.setStyleSheet(u"color: black;\nfont-size: 16pt;\nbackground-color: none;\nborder: none;")
        self.horizontalLayout_9.addWidget(self.balance_health)

        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
#1

        self.horizontalLayout_7.addWidget(self.categories_frame)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btn_new_transaction = QPushButton(self.centralwidget)
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
        icon.addFile(u":/icon /icon black/post_add_24dp_000000_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_new_transaction.setIcon(icon)
        self.btn_new_transaction.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.btn_new_transaction)

        self.btn_edit_transaction = QPushButton(self.centralwidget)
        self.btn_edit_transaction.setObjectName(u"btn_edit_transaction")
        self.btn_edit_transaction.setStyleSheet(u"QPushButton {\n"
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
        icon1 = QIcon()
        icon1.addFile(u":/icon /icon black/edit_24dp_000000_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_edit_transaction.setIcon(icon1)
        self.btn_edit_transaction.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.btn_edit_transaction)

        self.btn_delete_transaction = QPushButton(self.centralwidget)
        self.btn_delete_transaction.setObjectName(u"btn_delete_transaction")
        self.btn_delete_transaction.setStyleSheet(u"QPushButton {\n"
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
        icon2 = QIcon()
        icon2.addFile(u":/icon /icon black/delete_24dp_000000_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_delete_transaction.setIcon(icon2)
        self.btn_delete_transaction.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.btn_delete_transaction)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"QTableView {\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-bottom-right-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"}\n"
"\n"
"QTableView::section {\n"
"background-color: rgba(53, 53, 53);\n"
"color: black;\n"
"border: none;\n"
"height: 50px;\n"
"font-size: 14pt;\n"
"}\n"
"\n"
"QTableView::item {\n"
"border-style: none; \n"
"border-bottom: rgba(255,255,255,50);\n"
"}\n"
"\n"
"QTableView:item:selected {\n"
"border: none;\n"
"color: rgba(255,255,255);\n"
"background-color: rgba(255, 255, 255, 50);\n"
"}")
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableView.setShowGrid(False)
        self.tableView.horizontalHeader().setDefaultSectionSize(135)

        self.verticalLayout_3.addWidget(self.tableView)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Expense tracker", None))
        self.le_current_balance.setText(QCoreApplication.translate("MainWindow",u"\u0412\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0439 \u0431\u0430\u043b\u0430\u043d\u0441",None))
        self.le_balance.setText(QCoreApplication.translate("MainWindow", u" $1450", None))
        self.icon_up_arrow.setText("")
        self.label_income.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0445\u043e\u0434", None))
        self.income_balance.setText(QCoreApplication.translate("MainWindow", u" $1450", None))
        self.ico_down_arrow.setText("")
        self.label_outcome.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0445\u043e\u0434", None))
        self.outcome_balance.setText(QCoreApplication.translate("MainWindow", u" $1450", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow",u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0440\u0430\u0441\u0445\u043e\u0434\u043e\u0432",None))

            # --- Вот здесь меняем названия категорий под наш новый список ---
        self.icon_groceries.setText("")
        self.label_groceries.setText(QCoreApplication.translate("MainWindow", u"Продукты", None))
        self.balance_groceries.setText(QCoreApplication.translate("MainWindow", u"$0", None))

        self.ico_entertainment.setText("")
        self.label_entertainment.setText(QCoreApplication.translate("MainWindow", u"Развлечения", None))
        self.balance_entertainment.setText(QCoreApplication.translate("MainWindow", u"$0", None))

        self.ico_auto.setText("")
        self.label_auto.setText(QCoreApplication.translate("MainWindow", u"Транспорт", None))
        self.balance_auto.setText(QCoreApplication.translate("MainWindow", u"$0", None))

        # Обратите внимание: у нас появилась 5-я категория (Здоровье).
        # Если в ui_main.py была только 4 категория "Другое", её тоже можно переименовать или добавить новую метку для здоровья.
        self.icon_health.setText("")
        self.label_health.setText(QCoreApplication.translate("MainWindow", u"Здоровье", None))
        self.balance_health.setText(QCoreApplication.translate("MainWindow", u"$0", None))

        self.icon_other.setText("")
        self.label_other.setText(QCoreApplication.translate("MainWindow", u"Другое", None))
        self.balance_other.setText(QCoreApplication.translate("MainWindow", u"$0", None))

        self.btn_new_transaction.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u044f", None))
        self.btn_edit_transaction.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u044e", None))
        self.btn_delete_transaction.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u044e", None))
    # retranslateUi

