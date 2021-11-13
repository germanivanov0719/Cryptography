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
    def __init__(self):
        self.dict = []

    def auto_language(self):
        loc = locale.getdefaultlocale()
        # print(loc)
        if loc[0] in ('ru_RU', 'be_BE', 'kk_KK', 'uk-UK', 'uz-UZ', 'tk-TK'):
            self.to_russian()
        else:
            self.to_english()

    def to_english(self, state=True):
        self.dict = self.d.dict_en()
        self.menuEnglish.setChecked(True)
        self.menuRussian.setChecked(False)

        # hide and reopen help
        self.help_fe.click()
        self.help_fd.click()
        self.help_sha.click()
        self.help_md5.click()
        self.help_fe.click()
        self.help_fd.click()
        self.help_sha.click()
        self.help_md5.click()
        # menubar
        self.menuLanguage.setTitle("Language")
        self.menuDatabases.setTitle("Databases")
        self.show_keys_db.setText("Show all keys")
        self.clear_keys_db.setText("Delete saved keys")
        self.menuFernet_keys.setTitle("Fernet keys")
        self.export_db.setText("Export to CSV")
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
        self.save_fe.setText("Save")
        # Fernet decrypt
        self.label_fd.setText("Decrypted text:")
        self.label_2_fd.setText("Key:")
        self.label_3_fd.setText("Encrypted text:")
        self.decrypt_fd.setText("Decrypt")
        self.copy_fd.setText("Copy")
        self.paste_fd.setText("Paste")
        self.generate_fd.setText("Generate")
        self.save_fd.setText("Save")
        # sha hashing
        self.label_2_sha.setText("Result:")
        self.label_3_sha.setText("Algorithm:")
        self.label_sha.setText("Text to hash:")
        self.copy_sha.setText("Copy")
        self.paste_sha.setText("Paste")
        self.hash_sha.setText("Hash")
        self.file_sha.setText("Select a file to hash")
        # md5 hashing
        self.label_2_md5.setText("Result:")
        self.label_md5.setText("Text to hash:")
        self.copy_md5.setText("Copy")
        self.paste_md5.setText("Paste")
        self.hash_md5.setText("Hash")
        self.file_md5.setText("Select a file to hash")
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
        # reset help
        self.help_fe.click()
        self.help_fd.click()
        self.help_sha.click()
        self.help_md5.click()
        self.help_fe.click()
        self.help_fd.click()
        self.help_sha.click()
        self.help_md5.click()
        # menubar
        self.menuLanguage.setTitle("Язык")
        self.menuDatabases.setTitle("Базы данных")
        self.show_keys_db.setText("Показать все ключи")
        self.clear_keys_db.setText("Удалить сохранненые ключи")
        self.menuFernet_keys.setTitle("Ключи Fernet")
        self.export_db.setText("Экспорт в CSV")
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
        self.save_fe.setText("Сохранить")
        # Fernet decrypt
        self.label_fd.setText("Расшифрованный текст:")
        self.label_2_fd.setText("Ключ:")
        self.label_3_fd.setText("Зашифрованный текст:")
        self.decrypt_fd.setText("Расшифровать")
        self.copy_fd.setText("Копировать")
        self.paste_fd.setText("Вставить")
        self.generate_fd.setText("Генерировать")
        self.save_fe.setText("Сохранить")
        # sha hashing
        self.label_2_sha.setText("Результат:")
        self.label_3_sha.setText("Алгоритм:")
        self.label_sha.setText("Текст для хеширования:")
        self.copy_sha.setText("Копировать")
        self.paste_sha.setText("Вставить")
        self.hash_sha.setText("Хешировать")
        self.file_sha.setText("Выбрать файл для хеширования")
        # md5 hashing
        self.label_2_md5.setText("Результат:")
        self.label_md5.setText("Текст для хеширования:")
        self.copy_md5.setText("Копировать")
        self.paste_md5.setText("Вставить")
        self.hash_md5.setText("Хешировать")
        self.file_md5.setText("Выбрать файл для хеширования")
        # compare
        self.label_comp.setText("Первый текст:")
        self.label_2_comp.setText("Второй текст:")
        self.paste1_comp.setText("Вставить")
        self.paste2_comp.setText("Вставить")
        self.label_3_comp.setText("Результат:")
        self.compare()

    def dt_auto_format(self, time):
        return time.strftime("%x %X")

    def update_helps(self):
        # Fernet Encrypt
        self.help_visibility[0] = not self.help_visibility[0]
        if self.help_visibility[0]:
            self.helpText_fe.show()
            self.help_fe.setText(self.dict["Hide help"])
        else:
            self.helpText_fe.hide()
            self.help_fe.setText(self.dict["Show help"])
        self.help_visibility[1] = not self.help_visibility[1]
        # Fernet Decrypt
        if self.help_visibility[1]:
            self.helpText_fd.show()
            self.help_fd.setText(self.dict["Hide help"])
        else:
            self.helpText_fd.hide()
            self.help_fd.setText(self.dict["Show help"])
        # MD5
        self.help_visibility[3] = not self.help_visibility[3]
        if self.help_visibility[3]:
            self.helpText_md5.show()
            self.help_md5.setText(self.dict["Hide help"])
        else:
            self.helpText_md5.hide()
            self.help_md5.setText(self.dict["Show help"])
        # SHA
        self.help_visibility[2] = not self.help_visibility[2]
        if self.help_visibility[2]:
            self.helpText_sha.show()
            self.help_sha.setText(self.dict["Hide help"])
        else:
            self.helpText_sha.hide()
            self.help_sha.setText(self.dict["Show help"])

