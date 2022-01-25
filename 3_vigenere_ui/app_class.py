from main_window_ui import Ui_MainWindow
from vig_class import Vigener
import sys
from PyQt5 import QtWidgets


class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.vig = Vigener('')
        self.key = ''
        self.set_key.clicked.connect(self.make_vig)
        self.code_btn.clicked.connect(self.code)
        self.decode_btn.clicked.connect(self.decode)

    def code(self):
        if self.key != '':
            text = self.input_space.toPlainText()
            self.output_space.setPlainText(self.vig.code(text))
        else:
            pass

    def decode(self):
        if self.key != '':
            text = self.input_space.toPlainText()
            self.output_space.setPlainText(self.vig.decode(text))
        else:
            pass

    def make_vig(self):
        key = self.key_space.text()
        self.key = key
        self.vig = Vigener(key)


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение