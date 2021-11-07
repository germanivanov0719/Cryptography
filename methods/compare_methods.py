# PyQt5 requirements
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from cryptography.fernet import Fernet

# other libs
import hashlib
import sys
import cryptography.fernet
import pyperclip as pc
import locale


class compare_methods:
    def compare(self):
        if self.textEdit1_comp.toPlainText() == self.textEdit2_comp.toPlainText():
            self.result_comp.setText(self.dict['Same'])
            self.result_comp.setStyleSheet("border: 0; background-color: #00000000; color: green")
        else:
            self.result_comp.setText(self.dict['Different'])
            self.result_comp.setStyleSheet("border: 0; center; background-color: #00000000; color: red")

    def fpaste1_comp(self):
        self.textEdit1_comp.setText(pc.paste())

    def fpaste2_comp(self):
        self.textEdit2_comp.setText(pc.paste())