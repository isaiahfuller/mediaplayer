# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'subsonic_login.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFormLayout, QLabel, QLineEdit,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

class Ui_SubsonicLogin(object):
    def setupUi(self, SubsonicLogin):
        if not SubsonicLogin.objectName():
            SubsonicLogin.setObjectName(u"SubsonicLogin")
        SubsonicLogin.resize(391, 184)
        self.verticalLayout = QVBoxLayout(SubsonicLogin)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.subsonic_url = QLineEdit(SubsonicLogin)
        self.subsonic_url.setObjectName(u"subsonic_url")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.subsonic_url)

        self.subsonic_user = QLineEdit(SubsonicLogin)
        self.subsonic_user.setObjectName(u"subsonic_user")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.subsonic_user)

        self.subsonic_port = QSpinBox(SubsonicLogin)
        self.subsonic_port.setObjectName(u"subsonic_port")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subsonic_port.sizePolicy().hasHeightForWidth())
        self.subsonic_port.setSizePolicy(sizePolicy)
        self.subsonic_port.setMaximum(9999999)
        self.subsonic_port.setValue(4533)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.subsonic_port)

        self.label = QLabel(SubsonicLogin)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(SubsonicLogin)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(SubsonicLogin)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(SubsonicLogin)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.subsonic_password = QLineEdit(SubsonicLogin)
        self.subsonic_password.setObjectName(u"subsonic_password")
        self.subsonic_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.subsonic_password)

        self.label_5 = QLabel(SubsonicLogin)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.subsonic_servers = QComboBox(SubsonicLogin)
        self.subsonic_servers.setObjectName(u"subsonic_servers")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.subsonic_servers)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonBox = QDialogButtonBox(SubsonicLogin)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        QWidget.setTabOrder(self.subsonic_servers, self.subsonic_url)
        QWidget.setTabOrder(self.subsonic_url, self.subsonic_port)
        QWidget.setTabOrder(self.subsonic_port, self.subsonic_user)
        QWidget.setTabOrder(self.subsonic_user, self.subsonic_password)

        self.retranslateUi(SubsonicLogin)
        self.buttonBox.accepted.connect(SubsonicLogin.accept)
        self.buttonBox.rejected.connect(SubsonicLogin.reject)

        QMetaObject.connectSlotsByName(SubsonicLogin)
    # setupUi

    def retranslateUi(self, SubsonicLogin):
        SubsonicLogin.setWindowTitle(QCoreApplication.translate("SubsonicLogin", u"Dialog", None))
        self.subsonic_url.setText(QCoreApplication.translate("SubsonicLogin", u"http://127.0.0.1", None))
        self.subsonic_user.setText(QCoreApplication.translate("SubsonicLogin", u"user", None))
        self.label.setText(QCoreApplication.translate("SubsonicLogin", u"Port", None))
        self.label_2.setText(QCoreApplication.translate("SubsonicLogin", u"Username", None))
        self.label_3.setText(QCoreApplication.translate("SubsonicLogin", u"Password", None))
        self.label_4.setText(QCoreApplication.translate("SubsonicLogin", u"Server URL", None))
        self.label_5.setText(QCoreApplication.translate("SubsonicLogin", u"Servers", None))
    # retranslateUi

