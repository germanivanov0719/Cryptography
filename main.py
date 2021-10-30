import hashlib
import sys

import cryptography.fernet
import pyperclip as pc
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from cryptography.fernet import Fernet


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('design.ui', self)

        # Connecting elements

        # Fernet Key Generators
        self.generate_fe.clicked.connect(self.fgenerate_fe)
        self.generate_fd.clicked.connect(self.fgenerate_fd)

        # Fernet Encrypt/Decrypt
        self.encrypt_fe.clicked.connect(self.fencrypt_fe)
        self.decrypt_fd.clicked.connect(self.fdecrypt_fd)

        # Copy
        self.copy_fe.clicked.connect(self.fcopy_fe)
        self.copy_fd.clicked.connect(self.fcopy_fd)

        # Paste
        self.paste_fe.clicked.connect(self.fpaste_fe)
        self.paste_fd.clicked.connect(self.fpaste_fd)

        # Sha hashing
        self.hash_sha.clicked.connect(self.fhash_sha)

    def fhash_sha(self):
        text = self.textEdit_sha.toPlainText().encode()
        alg = self.sha_btn_group.checkedButton().text().lower().replace('sha', '').replace('-', '')
        # print(alg)
        r = ''
        if alg == '1':
            r = hashlib.sha1(text)
        # SHA-2 family
        elif alg == '256':
            r = hashlib.sha256(text)
        elif alg == '224':
            r = hashlib.sha224(text)
        elif alg == '512':
            r = hashlib.sha512(text)
        elif alg == '384':
            r = hashlib.sha384(text)
        # SHA-3 family
        elif alg == '3256':
            r = hashlib.sha3_256(text)
        elif alg == '3224':
            r = hashlib.sha3_224(text)
        elif alg == '3512':
            r = hashlib.sha3_512(text)
        elif alg == '3384':
            r = hashlib.sha3_384(text)
        r = r.hexdigest()
        self.result_sha.setText(r)

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
