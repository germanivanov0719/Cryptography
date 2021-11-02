# PyQt5 requirements
import os

from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from cryptography.fernet import Fernet

# other libs
import hashlib
import sys
import cryptography.fernet
import pyperclip as pc
import locale


class md5_methods:
    def hashing_core_md5(self):
        return hashlib.md5()

    def fhash_md5(self):
        text = self.textEdit_md5.toPlainText().encode()
        r = self.hashing_core_md5()
        r.update(text)
        self.result_md5.setText(r.hexdigest())

    def ffile_md5(self):
        path = QFileDialog.getOpenFileName(self, self.dict['Select File'], '')[0]
        if path == '':
            return 0
        r = self.hashing_core_md5()
        try:
            f = open(path, 'r')
            f.close()
            if os.stat(path).st_size // 1024 > 1e6:
                wa = QMessageBox()
                wa.setWindowTitle(self.dict['Confirm'])
                wa.setText(self.dict['Big file title'])
                wa.setInformativeText(self.dict['Big file body'])
                wa.setStandardButtons(QMessageBox.Yes | QMessageBox.Abort)
                wa.setIcon(QMessageBox.Question)
                if wa.exec_() != QMessageBox.Yes:
                    return 0
        except FileNotFoundError:
            wa = QMessageBox()
            wa.setWindowTitle(self.dict['Error'])
            wa.setText(self.dict['File not found title'])
            wa.setInformativeText(self.dict['File not found body'])
            wa.setStandardButtons(QMessageBox.Ok)
            wa.setIcon(QMessageBox.Critical)
            wa.exec_()
            return 0
        with open(path, 'rb') as f:
            chunk = 0
            while chunk != b'':
                chunk = f.read(1024)
                r.update(chunk)
            self.result_md5.setText(r.hexdigest())

    def fcopy_md5(self):
        pc.copy(self.result_md5.text())

    def fpaste_md5(self):
        self.textEdit_md5.setText(pc.paste())