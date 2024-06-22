# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1055, 783)
        self.actionConnect_to_server = QAction(MainWindow)
        self.actionConnect_to_server.setObjectName(u"actionConnect_to_server")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.player_label_art = QLabel(self.centralwidget)
        self.player_label_art.setObjectName(u"player_label_art")

        self.horizontalLayout.addWidget(self.player_label_art)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.player_label_title = QLabel(self.centralwidget)
        self.player_label_title.setObjectName(u"player_label_title")

        self.verticalLayout.addWidget(self.player_label_title)

        self.player_label_artist = QLabel(self.centralwidget)
        self.player_label_artist.setObjectName(u"player_label_artist")

        self.verticalLayout.addWidget(self.player_label_artist)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.player_button_prev = QPushButton(self.centralwidget)
        self.player_button_prev.setObjectName(u"player_button_prev")

        self.horizontalLayout_2.addWidget(self.player_button_prev)

        self.player_button_pause = QPushButton(self.centralwidget)
        self.player_button_pause.setObjectName(u"player_button_pause")

        self.horizontalLayout_2.addWidget(self.player_button_pause)

        self.player_button_next = QPushButton(self.centralwidget)
        self.player_button_next.setObjectName(u"player_button_next")

        self.horizontalLayout_2.addWidget(self.player_button_next)


        self.horizontalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.horizontalLayout.addLayout(self.horizontalLayout_3)

        self.player_button_shuffle = QPushButton(self.centralwidget)
        self.player_button_shuffle.setObjectName(u"player_button_shuffle")

        self.horizontalLayout.addWidget(self.player_button_shuffle)

        self.player_button_repeat = QPushButton(self.centralwidget)
        self.player_button_repeat.setObjectName(u"player_button_repeat")

        self.horizontalLayout.addWidget(self.player_button_repeat)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 11, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, 0, 0, -1)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 0, 1, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 0, 2, 1, 1)

        self.filters_genre = QListWidget(self.centralwidget)
        self.filters_genre.setObjectName(u"filters_genre")

        self.gridLayout_3.addWidget(self.filters_genre, 1, 0, 1, 1)

        self.filters_artists = QListWidget(self.centralwidget)
        self.filters_artists.setObjectName(u"filters_artists")

        self.gridLayout_3.addWidget(self.filters_artists, 1, 1, 1, 1)

        self.filters_albums = QListWidget(self.centralwidget)
        self.filters_albums.setObjectName(u"filters_albums")

        self.gridLayout_3.addWidget(self.filters_albums, 1, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.mpv_container = QWidget(self.centralwidget)
        self.mpv_container.setObjectName(u"mpv_container")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mpv_container.sizePolicy().hasHeightForWidth())
        self.mpv_container.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.mpv_container, 10, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1055, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionConnect_to_server)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionConnect_to_server.setText(QCoreApplication.translate("MainWindow", u"Connect to server", None))
        self.player_label_art.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.player_label_title.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.player_label_artist.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.player_button_prev.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.player_button_pause.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.player_button_next.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.player_button_shuffle.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.player_button_repeat.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Genres", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Artists", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Albums", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

