# PyQt5 requirements
import datetime
import os
import sqlite3

from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QTableWidgetItem
from cryptography.fernet import Fernet

# other libs
import hashlib
import sys
import cryptography.fernet
import pyperclip as pc
import locale


# To create the correct table, use this:
# CREATE TABLE fernet_keys (
#     date  DATE,
#     [key] STRING
# );


class databases_methods:
    def fshow_keys_db(self):
        obj = self.show_keys_dialogue
        connection = sqlite3.connect("fernet_keys.sqlite")
        # print(connection)
        try:
            res = connection.cursor().execute("SELECT * FROM fernet_keys").fetchall()
        except Exception as ex:
            pass
            # print(ex)
        obj.tableWidget.setColumnCount(2)
        obj.tableWidget.setRowCount(0)
        for i, row in enumerate(res):
            obj.tableWidget.setRowCount(
                obj.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                item = QTableWidgetItem(str(elem))
                item.setFlags(item.flags() ^ Qt.ItemIsEditable)
                obj.tableWidget.setItem(
                    i, j, item)
        obj.show()
        connection.close()
        # obj.tableView

    def fclose_show(self):
        self.show_keys_dialogue.hide()

    def fclear_show(self):
        os.remove("fernet_keys.sqlite")
        self.init_db()

    def init_db(self):
        try:
            with open("fernet_keys.sqlite", 'r'):
                wa = QMessageBox()
                wa.setWindowTitle(self.dict['Confirm'])
                wa.setText("DB here")
                wa.setInformativeText("Remove? RISKS!!")
                wa.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                wa.setIcon(QMessageBox.Warning)
                r = wa.exec_()
                if r == QMessageBox.Yes:
                    os.remove("fernet_keys.sqlite")
                    with open("fernet_keys.sqlite", 'w'):
                        connection = sqlite3.connect("fernet_keys.sqlite")
                        connection.cursor().execute("""CREATE TABLE fernet_keys (
                                                            time  STRING,
                                                            value STRING);""")
        except FileNotFoundError:
            with open("fernet_keys.sqlite", 'w'):
                connection = sqlite3.connect("fernet_keys.sqlite")
                connection.cursor().execute("""CREATE TABLE fernet_keys (
                                                    time  STRING,
                                                    value STRING);""")

    def add_db(self, value):
        # print("adding", value)
        connection = sqlite3.connect("fernet_keys.sqlite")
        dt_now = self.dt_auto_format(datetime.datetime.now())
        connection.cursor().execute(f"""INSERT INTO fernet_keys (time, value)
                                    VALUES('{dt_now}', '{value}')""")
        connection.commit()
        connection.close()
        if self.show_keys_dialogue.isVisible():
            self.fshow_keys_db()
        else:
            self.fshow_keys_db()
            self.show_keys_dialogue.hide()

