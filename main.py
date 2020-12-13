import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QInputDialog
from PyQt5.QtGui import QPainter, QColor
from random import randint


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Жёлтые круги')
        self.pushButton.clicked.connect(self.press)
        self.do_paint = False

    def press(self):
        name, ok_pressed = QInputDialog.getInt(self, "Введите количество",
                                               "Сколько кругов?")
        if ok_pressed:
            self.do_paint = True
            self.name = name

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def draw_circle(self, qp):
        for i in range(self.name):
            qp.setBrush(QColor(255, 255, 0))
            x, y = randint(0, 400), randint(0, 300)
            d = randint(1, 50)
            qp.drawEllipse(x, y, d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())