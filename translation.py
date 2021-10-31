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


class translation:
    def auto_language(self):
        loc = locale.getdefaultlocale()
        if loc in ('ru_RU', 'be_BE', 'kk_KK', 'uk-UK', 'uz-UZ', 'tk-TK'):
            self.to_russian()
        else:
            self.to_english()

    def to_english(self, state=True):
        self.dict = self.d.dict_en()
        self.menuEnglish.setChecked(True)
        self.menuRussian.setChecked(False)
        # menubar
        self.menuLanguage.setTitle("Language")
        # tabs
        self.tabWidget.setTabText(0, "Fernet Encryption")
        self.tabWidget.setTabText(1, "Fernet Decryption")
        self.tabWidget.setTabText(2, "SHA Hashing")
        self.tabWidget.setTabText(3, "MD5 Hashing")
        self.tabWidget.setTabText(4, "Compare")
        # Fernet encrypt
        self.label_fe.setText("Text to encrypt:")
        self.label_2_fe.setText("Key:")
        self.label_3_fe.setText("Result:")
        self.encrypt_fe.setText("Encrypt")
        self.copy_fe.setText("Copy")
        self.paste_fe.setText("Paste")
        self.generate_fe.setText("Generate")
        # Fernet decrypt
        self.label_fd.setText("Decrypted text:")
        self.label_2_fd.setText("Key:")
        self.label_3_fd.setText("Encrypted text:")
        self.decrypt_fd.setText("Decrypt")
        self.copy_fd.setText("Copy")
        self.paste_fd.setText("Paste")
        self.generate_fd.setText("Generate")
        # sha hashing
        self.label_2_sha.setText("Result:")
        self.label_3_sha.setText("Algorithm:")
        self.label_sha.setText("Text to hash:")
        self.copy_sha.setText("Copy")
        self.paste_sha.setText("Paste")
        self.hash_sha.setText("Hash")
        # md5 hashing
        self.label_2_md5.setText("Result:")
        self.label_md5.setText("Text to hash:")
        self.copy_md5.setText("Copy")
        self.paste_md5.setText("Paste")
        self.hash_md5.setText("Hash")
        # compare
        self.label_comp.setText("First text:")
        self.label_2_comp.setText("Second text:")
        self.paste1_comp.setText("Paste")
        self.paste2_comp.setText("Paste")
        self.label_3_comp.setText("Result:")
        self.compare()

    def to_russian(self, state=True):
        self.dict = self.d.dict_ru()
        self.menuEnglish.setChecked(False)
        self.menuRussian.setChecked(True)
        # menubar
        self.menuLanguage.setTitle("Язык")
        # tabs
        self.tabWidget.setTabText(0, "Шифрование Fernet")
        self.tabWidget.setTabText(1, "Расшифровка Fernet")
        self.tabWidget.setTabText(2, "Хеширование SHA")
        self.tabWidget.setTabText(3, "Хеширование MD5")
        self.tabWidget.setTabText(4, "Сравнить")
        # Fernet encrypt
        self.label_fe.setText("Текст для шифрования:")
        self.label_2_fe.setText("Ключ:")
        self.label_3_fe.setText("Результат:")
        self.encrypt_fe.setText("Шифровать")
        self.copy_fe.setText("Копировать")
        self.paste_fe.setText("Вставить")
        self.generate_fe.setText("Генерировать")
        # Fernet decrypt
        self.label_fd.setText("Расшифрованный текст:")
        self.label_2_fd.setText("Ключ:")
        self.label_3_fd.setText("Зашифрованный текст:")
        self.decrypt_fd.setText("Расшифровать")
        self.copy_fd.setText("Копировать")
        self.paste_fd.setText("Вставить")
        self.generate_fd.setText("Генерировать")
        # sha hashing
        self.label_2_sha.setText("Результат:")
        self.label_3_sha.setText("Алгоритм:")
        self.label_sha.setText("Текст для хеширования:")
        self.copy_sha.setText("Копировать")
        self.paste_sha.setText("Вставить")
        self.hash_sha.setText("Хешировать")
        # md5 hashing
        self.label_2_md5.setText("Результат:")
        self.label_md5.setText("Текст для хеширования:")
        self.copy_md5.setText("Копировать")
        self.paste_md5.setText("Вставить")
        self.hash_md5.setText("Хешировать")
        # compare
        self.label_comp.setText("Первый текст:")
        self.label_2_comp.setText("Второй текст:")
        self.paste1_comp.setText("Вставить")
        self.paste2_comp.setText("Вставить")
        self.label_3_comp.setText("Результат:")
        self.compare()

