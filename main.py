import imghdr
import sys
from random import randrange

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PIL import Image


class Main(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        super(Main, self).__init__()
        self.setWindowTitle('Test Image')
        self.resize(550,600)
        self.button = QPushButton('hello',self)
        self.button.resize(100,90)
        self.button.move(350,60)
        self.button.clicked.connect(self.get_image)
        self.label = QLabel(self)
        self.label.resize(300,300)

    def get_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog

        filename,_ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()","C:/Users/Nadjmo m/Desktop/Images Doctors","Image files(*.jpg *.gif *.png)",options=options)

        with open(filename[0],'rb') as f:
            format = imghdr.what(f.name)

        image = Image.open(str(filename[0]))
        newImage = image.resize((300, 300))
        new_image_name = f'{randrange(10000)}.{str(format)}'

        newImage.save(new_image_name)

        with open(new_image_name) as f:
            pixmap = QPixmap(f.name)
            self.label.setPixmap(pixmap)



def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()