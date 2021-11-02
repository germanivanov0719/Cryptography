# IMPORTS
# PyQt5 requirements
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from cryptography.fernet import Fernet

# this program parts
from fernet_methods import fernet_methods
from sha_methods import sha_methods
from md5_methods import md5_methods
from compare_methods import compare_methods
from translation import translation
from dynamic_translations import dictionary
from connections import connections


# other libs
import hashlib
import sys
import cryptography.fernet
import pyperclip as pc
import locale


class MainWindow(QMainWindow,
                 fernet_methods,
                 sha_methods, md5_methods,
                 compare_methods,
                 translation,
                 dictionary,
                 connections):
    def __init__(self):
        super().__init__()
        uic.loadUi('design.ui', self)
        self.d = dictionary()
        self.auto_language()
        self.setWindowTitle('Cryptography')
        self.connect()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    # Fix HiDPI
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
