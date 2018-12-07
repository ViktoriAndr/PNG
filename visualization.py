import sys

from PyQt5.QtGui import QPalette, QColor, QIcon, QPainter, QImage
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication

from analysis import analysis


class visualization(QWidget):
    def __init__(self, image, chunk):
        super().__init__()
        self.analysis = analysis(image, chunk)
        self.width = self.analysis.width
        self.height = self.analysis.height
        self.setFixedSize(self.width, self.height)
        self.center()
        self.setWindowTitle("Analysis PNG")
        self.setWindowIcon(QIcon("icon.png"))
        pal = self.palette()
        pal.setColor(QPalette.Normal, QPalette.Background, QColor("white"))
        self.setPalette(pal)
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def paintEvent(self, e):
        painter = QPainter()
        painter.begin(self)
        self.image(painter)
        painter.end()

    def image(self, painter):
        image = QImage("images/facebook.png")
        painter.drawImage(0, 0, image)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # ex = visualization("images/facebook.png", "all")
    ex = visualization(sys.argv[1], sys.argv[2])
    sys.exit(app.exec_())
