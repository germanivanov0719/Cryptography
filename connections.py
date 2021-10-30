# PyQt5 requirements
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from cryptography.fernet import Fernet

# other libs
import hashlib
import sys
import cryptography.fernet
import pyperclip as pc


class connections:
    def connect(self):
        self.generate_fe.clicked.connect(self.fgenerate_fe)
        self.generate_fd.clicked.connect(self.fgenerate_fd)

        # Fernet Encrypt/Decrypt
        self.encrypt_fe.clicked.connect(self.fencrypt_fe)
        self.decrypt_fd.clicked.connect(self.fdecrypt_fd)

        # Copy
        self.copy_fe.clicked.connect(self.fcopy_fe)
        self.copy_fd.clicked.connect(self.fcopy_fd)
        self.copy_sha.clicked.connect(self.fcopy_sha)
        self.copy_md5.clicked.connect(self.fcopy_md5)

        # Paste
        self.paste_fe.clicked.connect(self.fpaste_fe)
        self.paste_fd.clicked.connect(self.fpaste_fd)
        self.paste_sha.clicked.connect(self.fpaste_sha)
        self.paste_md5.clicked.connect(self.fpaste_md5)

        # Sha hashing
        self.hash_sha.clicked.connect(self.fhash_sha)

        # Md5 hashing
        self.hash_md5.clicked.connect(self.fhash_md5)
