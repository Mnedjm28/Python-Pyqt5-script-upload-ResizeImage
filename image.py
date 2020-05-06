import imghdr
import sys

from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

def browseimage():
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    # le = QPixmap(fname[0])
    # le.setPixmap(QPixmap(fname))
    # print('enter')
    # filname = QFileDialog.getOpenFileName("QFileDialog.getOpenFileNames()", "",
    #                                             "All Files (*);;Python Files (*.py);;Image files (*.jpg *.gif)", options=options)
    filname =QFileDialog.getOpenFileName()
    imagepath = filname[0]
    # print(imagepath)
    # pixmap = QPixmap(imagepath)
    # print(pixmap)

    with open(imagepath, 'rb') as f:
        file_data = f.read()
        print(file_data,'-------------------------\n')
        file_type = imghdr.what(f.name)
        file_name = f.name
        print(file_name)

app = QApplication(sys.argv)
w = QWidget()
w.resize(400,350)
w.move(100,120)

btn = QPushButton('Close', w)
btn.resize(80,80)
btn.move(50,90)
btn.setToolTip('exit')
btn.clicked.connect(browseimage)
w.setGeometry(100,120,400,350)
w.setWindowTitle('browsing image')

w.show()


app.exec_()


# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
# from PyQt5.QtGui import QIcon
#
#
# class App(QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.title = 'PyQt5 file dialogs - pythonspot.com'
#         self.left = 10
#         self.top = 10
#         self.width = 640
#         self.height = 480
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left, self.top, self.width, self.height)
#
#         self.openFileNameDialog()
#         self.openFileNamesDialog()
#         self.saveFileDialog()
#
#         self.show()
#
#     def openFileNameDialog(self):
#         options = QFileDialog.Options()
#         options |= QFileDialog.DontUseNativeDialog
#         fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()",'Image files (*.jpg *.gif)' ,options=options)
#         if fileName:
#             print(fileName)
#
#     def openFileNamesDialog(self):
#         options = QFileDialog.Options()
#         options |= QFileDialog.DontUseNativeDialog
#         files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
#                                                 "All Files (*);;Python Files (*.py);;Image files (*.jpg *.gif)", options=options)
#         if files:
#             print(files)
#
#     def saveFileDialog(self):
#         options = QFileDialog.Options()
#         options |= QFileDialog.DontUseNativeDialog
#         fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
#                                                   "All Files (*);;Text Files (*.txt)", options=options)
#         if fileName:
#             print(fileName)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = App()
#     sys.exit(app.exec_())

