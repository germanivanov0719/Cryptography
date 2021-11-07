import sys

from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


class show_keys_dialogue(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('resources/show_keys_dialogue.ui', self)
        self.setWindowTitle('Fernet keys')

