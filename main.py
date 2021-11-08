# IMPORTS
# PyQt5 requirements
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

# this program parts
from methods.fernet_methods import fernet_methods
from methods.sha_methods import sha_methods
from methods.md5_methods import md5_methods
from methods.compare_methods import compare_methods
from resources.translation import translation
from resources.dynamic_translations import dictionary
from connections import connections
from methods.databases_methods import databases_methods
from resources.show_keys_dialogue import show_keys_dialogue



# other libs
import sys
import os


class MainWindow(QMainWindow,
                 fernet_methods,
                 sha_methods, md5_methods,
                 compare_methods,
                 databases_methods,
                 translation,
                 dictionary,
                 connections):
    def __init__(self):
        super().__init__()
        uic.loadUi('./resources/design.ui', self)
        # self.show_keys_dialogue.exec()
        # self.show_keys_dialogue.hide()
        self.help_visibility = [False] * 4
        self.d = dictionary()
        self.auto_language()
        self.show_keys_dialogue = show_keys_dialogue()
        self.init_db()
        self.setWindowTitle('Cryptography')
        self.connect()

    def closeEvent(self, event):
        self.show_keys_dialogue.hide()
        wa = QMessageBox()
        wa.setWindowTitle(self.dict['Confirm'])
        wa.setText(self.dict['exit title'])
        wa.setInformativeText(self.dict['exit body'])
        wa.setStandardButtons(QMessageBox.Cancel | QMessageBox.No | QMessageBox.Yes)
        wa.setIcon(QMessageBox.Question)
        r = wa.exec_()
        if r == QMessageBox.Yes:
            os.remove("fernet_keys.sqlite")
            event.accept()
        elif r == QMessageBox.No:
            event.accept()
        else:
            event.ignore()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    # Fix HiDPI
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
