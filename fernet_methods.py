# PyQt5 requirements
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from cryptography.fernet import Fernet

# other libs
import hashlib
import sys
import cryptography.fernet
import pyperclip as pc


class fernet_methods:
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
            wa.setText("The key you entered is not a valid Fernet key.")
            wa.setInformativeText("You can generate a new valid key by pressing \"Generate\" button on the right.")
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
            print(ex)
            wa = QMessageBox()
            wa.setText("The key you entered is not a valid Fernet key.")
            wa.setInformativeText("You can generate a new valid key by pressing \"Generate\" button on the right.")
            wa.setStandardButtons(QMessageBox.Ok)
            wa.setIcon(QMessageBox.Warning)
            wa.exec_()
            return 0
        try:
            # print(self.result_fd.text())
            decrypted = f.decrypt(self.result_fd.text().encode())
        except cryptography.fernet.InvalidToken:
            wa = QMessageBox()
            wa.setText("Unable to decrypt data.")
            wa.setInformativeText("Either the encrypted data was corrupted, or this key cannot be used for this data.")
            wa.setStandardButtons(QMessageBox.Ok)
            wa.setIcon(QMessageBox.Critical)
            wa.exec_()
            return 0
        self.textEdit_fd.setText(decrypted.decode())

    def fgenerate_fe(self):
        wa = QMessageBox()
        wa.setText("You are about to generate a new Fernet key.")
        wa.setInformativeText("The new key is going to replace the old one. Are you sure you can safely proceed?")
        wa.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
        # wa.setDefaultButton(QMessageBox.No)
        wa.setIcon(QMessageBox.Question)
        if wa.exec() == QMessageBox.Yes:
            self.generate_fernet_key()

    def fgenerate_fd(self):
        wa = QMessageBox()
        wa.setText("You are about to generate a new Fernet key.")
        wa.setInformativeText("The new key is going to replace the old one. Are you sure you can safely proceed?")
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