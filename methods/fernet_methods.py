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


class fernet_methods:
    def fsave_fe(self):
        self.add_db(self.key_fe.text())

    def fsave_fd(self):
        self.add_db(self.key_fd.text())

    def fhelp_fe(self):
        self.helpText_fe.setText(self.dict['fe help'])
        self.help_visibility[0] = not self.help_visibility[0]
        if self.help_visibility[0]:
            self.helpText_fe.show()
            self.help_fe.setText(self.dict["Hide help"])
        else:
            self.helpText_fe.hide()
            self.help_fe.setText(self.dict["Show help"])

    def fhelp_fd(self):
        self.helpText_fd.setText(self.dict['fd help'])
        self.help_visibility[1] = not self.help_visibility[1]
        if self.help_visibility[1]:
            self.helpText_fd.show()
            self.help_fd.setText(self.dict["Hide help"])
        else:
            self.helpText_fd.hide()
            self.help_fd.setText(self.dict["Show help"])

    def fcopy_fe(self):
        pc.copy(self.result_fe.text())

    def fcopy_fd(self):
        pc.copy(self.textEdit_fd.toPlainText())

    def fpaste_fe(self):
        self.textEdit_fe.setText(pc.paste())

    def fpaste_fd(self):
        self.result_fd.setText(pc.paste())

    def fencrypt_fe(self):
        try:
            f = Fernet(self.key_fe.text().encode())
            # print(self.key_fe.text())
        except ValueError:
            wa = QMessageBox()
            wa.setWindowTitle(self.dict['Warning'])
            wa.setText(self.dict['Invalid Fernet title'])
            wa.setInformativeText(self.dict['Invalid Fernet body'])
            wa.setStandardButtons(QMessageBox.Ok)
            wa.setIcon(QMessageBox.Warning)
            wa.exec_()
            return 0
        encrypted = f.encrypt(self.textEdit_fe.toPlainText().encode())
        self.result_fe.setText(encrypted.decode())

    def fdecrypt_fd(self):
        try:
            f = Fernet(self.key_fd.text().encode())
            # print(self.key_fd.text())
        except ValueError:
            wa = QMessageBox()
            wa.setWindowTitle(self.dict['Warning'])
            wa.setText(self.dict['Invalid Fernet title'])
            wa.setInformativeText(self.dict['Invalid Fernet body'])
            wa.setStandardButtons(QMessageBox.Ok)
            wa.setIcon(QMessageBox.Warning)
            wa.exec_()
            return 0
        try:
            # print(self.result_fd.text())
            decrypted = f.decrypt(self.result_fd.text().encode())
        except cryptography.fernet.InvalidToken:
            wa = QMessageBox()
            wa.setWindowTitle(self.dict['Error'])
            wa.setText(self.dict['Decryption error title'])
            wa.setInformativeText(self.dict['Decryption error body'])
            wa.setStandardButtons(QMessageBox.Ok)
            wa.setIcon(QMessageBox.Critical)
            wa.exec_()
            return 0
        self.textEdit_fd.setText(decrypted.decode())

    def fgenerate_fe(self):
        wa = QMessageBox()
        wa.setWindowTitle(self.dict['Confirm'])
        wa.setText(self.dict['New Fernet title'])
        wa.setInformativeText(self.dict['New Fernet body'])
        wa.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
        # wa.setDefaultButton(QMessageBox.No)
        wa.setIcon(QMessageBox.Question)
        if wa.exec() == QMessageBox.Yes:
            self.generate_fernet_key()

    def fgenerate_fd(self):
        wa = QMessageBox()
        wa.setWindowTitle(self.dict['Confirm'])
        wa.setText(self.dict['New Fernet title'])
        wa.setInformativeText(self.dict['New Fernet body'])
        wa.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
        wa.setIcon(QMessageBox.Question)
        # wa.setDefaultButton(QMessageBox.No)
        if wa.exec() == QMessageBox.Yes:
            self.generate_fernet_key()

    def generate_fernet_key(self):
        key = Fernet.generate_key().decode()
        self.key_fd.setText(key)
        self.key_fe.setText(key)
        return key
