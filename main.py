import sys
from cryptography.fernet import Fernet

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('design.ui', self)
        self.generate_fe.clicked.connect(self.fgenerate_fe)

    def fgenerate_fe(self):
        wa = QMessageBox()
        wa.setText("You are about to generate a new Fernet key. ")
        wa.setInformativeText("The new key is going to replace the old one. Are you sure you can safely proceed?")
        wa.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
        # wa.setDefaultButton(QMessageBox.No)
        if wa.exec() == QMessageBox.Yes:
            self.key_fe.setText(Fernet.generate_key().decode())


    def generate_fernet_key(self):
        return Fernet.generate_key()



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())