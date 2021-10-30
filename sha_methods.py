# PyQt5 requirements
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from cryptography.fernet import Fernet

# other libs
import hashlib
import sys
import cryptography.fernet
import pyperclip as pc


class sha_methods:
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

    def fcopy_sha(self):
        pc.copy(self.result_sha.text())

    def fpaste_sha(self):
        self.textEdit_sha.setText(pc.paste())