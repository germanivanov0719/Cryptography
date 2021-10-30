import hashlib
import sys
from cryptography.fernet import Fernet
import hashlib
import pyperclip as pc

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox


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

        # Copy and Paste buttons
        # self.copy_fe.clicked.connect()

    def fencrypt_fe(self):
        f = 0
        try:
            f = Fernet(self.key_fe.text().encode())
        except ValueError:
            wa = QMessageBox()
            wa.setText("The key you entered is not a valid Fernet key")
            wa.setInformativeText("You can generate a new valid key by pressing \"Generate\"")
            wa.setStandardButtons(QMessageBox.Ok)
            wa.exec_()
            return 0
        encrypted = f.encrypt(self.textEdit_fe.toPlainText().encode())
        self.result_fe.setText(encrypted.decode())

    def fdecrypt_fd(self):
        f = 0
        try:
            f = Fernet(self.key_fd.text().encode())
        except ValueError:
            wa = QMessageBox()
            wa.setText("The key you entered is not a valid Fernet key")
            wa.setInformativeText("You can generate a new valid key by pressing \"Generate\"")
            wa.setStandardButtons(QMessageBox.Ok)
            wa.exec_()
            return 0
        decrypted = f.decrypt(self.result_fd.text().encode())
        self.textEdit_fd.setText(decrypted.decode())


    def fgenerate_fe(self):
        wa = QMessageBox()
        wa.setText("You are about to generate a new Fernet key. ")
        wa.setInformativeText("The new key is going to replace the old one. Are you sure you can safely proceed?")
        wa.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
        # wa.setDefaultButton(QMessageBox.No)
        if wa.exec() == QMessageBox.Yes:
            self.key_fe.setText(Fernet.generate_key().decode())

    def fgenerate_fd(self):
        wa = QMessageBox()
        wa.setText("You are about to generate a new Fernet key. ")
        wa.setInformativeText("The new key is going to replace the old one. Are you sure you can safely proceed?")
        wa.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
        # wa.setDefaultButton(QMessageBox.No)
        if wa.exec() == QMessageBox.Yes:
            self.key_fd.setText(Fernet.generate_key().decode())


    def generate_fernet_key(self):
        return Fernet.generate_key()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())