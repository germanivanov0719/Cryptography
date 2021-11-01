# PyQt5 requirements
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from cryptography.fernet import Fernet

# other libs
import hashlib
import sys
import cryptography.fernet
import pyperclip as pc
import locale


class sha_methods:
    def hashing_core_sha(self):
        alg = self.sha_btn_group.checkedButton().text().lower().replace('sha', '').replace('-', '')
        if alg == '1':
            return hashlib.sha1()
        # SHA-2 family
        elif alg == '256':
            return hashlib.sha256()
        elif alg == '224':
            return hashlib.sha224()
        elif alg == '512':
            return hashlib.sha512()
        elif alg == '384':
            return hashlib.sha384()
        # SHA-3 family
        elif alg == '3256':
            return hashlib.sha3_256()
        elif alg == '3224':
            return hashlib.sha3_224()
        elif alg == '3512':
            return hashlib.sha3_512()
        elif alg == '3384':
            return hashlib.sha3_384()

    def fhash_sha(self):
        text = self.textEdit_sha.toPlainText().encode()
        r = self.hashing_core_sha()
        r.update(text)
        self.result_sha.setText(r.hexdigest())

    def ffile_sha(self):
        path = QFileDialog.getOpenFileName(self, self.dict['Select File'], '')[0]
        if path == '':
            return 0
        r = self.hashing_core_sha()
        with open(path, 'rb') as f:
            chunk = 0
            while chunk != b'':
                chunk = f.read(1024)
                r.update(chunk)
            self.result_sha.setText(r.hexdigest())

    def fcopy_sha(self):
        pc.copy(self.result_sha.text())

    def fpaste_sha(self):
        self.textEdit_sha.setText(pc.paste())