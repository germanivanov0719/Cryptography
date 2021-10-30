# PyQt5 requirements
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from cryptography.fernet import Fernet

# other libs
import hashlib
import sys
import cryptography.fernet
import pyperclip as pc


class md5_methods:
    def fhash_md5(self):
        text = self.textEdit_md5.toPlainText().encode()
        r = hashlib.md5(text)
        self.result_md5.setText(r.hexdigest())

    def fcopy_md5(self):
        pc.copy(self.result_md5.text())

    def fpaste_md5(self):
        self.textEdit_md5.setText(pc.paste())