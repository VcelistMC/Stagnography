from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import app_support
import os, random, string

class Ui_Bruh(object):
    def setupUi(self, Bruh):
        Bruh.setObjectName("Bruh")
        Bruh.resize(769, 333)
        Bruh.setMinimumSize(QtCore.QSize(769, 333))
        Bruh.setMaximumSize(QtCore.QSize(769, 333))
        self.centralwidget = QtWidgets.QWidget(Bruh)
        self.centralwidget.setObjectName("centralwidget")

        self.Preview_gbox = QtWidgets.QGroupBox(self.centralwidget)
        self.Preview_gbox.setGeometry(QtCore.QRect(10, 10, 391, 291))
        self.Preview_gbox.setObjectName("Preview_gbox")
        
        self.Preview_label = QtWidgets.QLabel(self.Preview_gbox)
        self.Preview_label.setGeometry(QtCore.QRect(10, 20, 371, 271))
        self.Preview_label.setText("")
        self.Preview_label.setScaledContents(True)
        self.Preview_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Preview_label.setObjectName("Preview_label")

        self.select_image = QtWidgets.QPushButton(self.centralwidget)
        self.select_image.setGeometry(QtCore.QRect(420, 15, 341, 61))
        self.select_image.setObjectName("select_image")
        self.select_image.clicked.connect(self.open_image)

        self.msg_box = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.msg_box.setGeometry(QtCore.QRect(420, 110, 231, 91))
        self.msg_box.setPlainText("")
        self.msg_box.setBackgroundVisible(False)
        self.msg_box.setObjectName("msg_box")

        self.embed_msg = QtWidgets.QPushButton(self.centralwidget)
        self.embed_msg.setGeometry(QtCore.QRect(660, 112, 101, 41))
        self.embed_msg.setObjectName("embed_msg")
        self.embed_msg.clicked.connect(self.embd_msg)

        self.rev_msg = QtWidgets.QPushButton(self.centralwidget)
        self.rev_msg.setGeometry(QtCore.QRect(660, 160, 101, 41))
        self.rev_msg.setObjectName("rev_msg")
        self.rev_msg.clicked.connect(self.rev)

        
        self.my_dir = ""
        

        self.key_lbl = QtWidgets.QLabel(self.centralwidget)
        self.key_lbl.setGeometry(QtCore.QRect(422, 246, 111, 16))
        self.key_lbl.setObjectName("key_lbl")

        self.key_box = QtWidgets.QLineEdit(self.centralwidget)
        self.key_box.setGeometry(QtCore.QRect(420, 262, 231, 20))
        self.key_box.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhLatinOnly)
        self.key_box.setInputMask("")
        self.key_box.setMaxLength(10)
        self.key_box.setObjectName("key_box")
        self.rand_key_but = QtWidgets.QPushButton(self.centralwidget)
        self.rand_key_but.setGeometry(QtCore.QRect(660, 260, 101, 23))
        self.rand_key_but.setWhatsThis("")
        self.rand_key_but.setObjectName("rand_key_but")
        self.rand_key_but.clicked.connect(self.randStr)

        self.name_lbl = QtWidgets.QLabel(self.centralwidget)
        self.name_lbl.setGeometry(QtCore.QRect(12, 310, 47, 13))
        self.name_lbl.setObjectName("name_lbl")

        self.name_box = QtWidgets.QLineEdit(self.centralwidget)
        self.name_box.setGeometry(QtCore.QRect(70, 308, 331, 20))
        self.name_box.setObjectName("name_box")
        Bruh.setCentralWidget(self.centralwidget)
        #Bruh.setStyleSheet(r"QWidget#centralwidget{background-color: rgb(54, 54, 54);} QWidget#select_image{background-color: rgb(187, 134, 252);} QWidget#embed_msg{background-color: rgb(187, 134, 252);color: rgb(255, 255, 255);} QWidget#rev_msg{background-color: rgb(187, 134, 252); color: rgb(255, 255, 255);} QWidget#msg_box{background-color: rgb(54, 54, 54);border: 1px solid white;color: rgb(255, 255, 255);}")

        self.retranslateUi(Bruh)
        QtCore.QMetaObject.connectSlotsByName(Bruh)

    def retranslateUi(self, Bruh):
        _translate = QtCore.QCoreApplication.translate
        Bruh.setWindowTitle(_translate("Bruh", "Stegonagrphy Tool"))
        self.Preview_gbox.setTitle(_translate("Bruh", "Preview"))
        self.select_image.setText(_translate("Bruh", "Select Image"))
        self.embed_msg.setText(_translate("Bruh", "Hide Message"))
        self.rev_msg.setText(_translate("Bruh", "Reveal Message"))
        self.key_lbl.setText(_translate("Bruh", "Key (OPTIONAL):"))
        self.key_box.setToolTip(_translate("Bruh", "<html><head/><body><p><span style=\" font-weight:600;\">OPTIONAL</span></p><p>Encode your message with a key, so that only people with the same key will be able to decode your message</p></body></html>"))
        self.key_box.setPlaceholderText(_translate("Bruh", "Only letters & numbers are allowed."))
        self.rand_key_but.setToolTip(_translate("Bruh", "Generate a random key"))
        self.rand_key_but.setText(_translate("Bruh", "Randomize"))
        self.name_lbl.setText(_translate("Bruh", "Save as:"))
        self.name_box.setPlaceholderText(_translate("Bruh", "File name"))
        

    def error(self, widget):
        widget.setStyleSheet("border: 1px solid red;")
    
    def open_image(self):
        self.fileName,_ = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","Image Files (*.png *.jpg *.jpeg)")
        print(self.fileName)
        img = QtGui.QPixmap(self.fileName).scaled(self.Preview_label.size(),QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.Preview_label.setPixmap(img)
        self.Preview_label.setScaledContents(False)
        self.my_dir = "/".join(self.fileName.split("/")[:-1])

    def embd_msg(self):
        msg = self.msg_box.toPlainText()
        key = "0000" if (self.key_box.text() == "") else self.key_box.text()
        output_s = "\output.png" if (self.name_box.text() == "") else str("\\" + self.name_box.text() + ".png")
        self.msg_box.clear()
        app_support.embed(self.fileName, msg, self.my_dir, key, output_s)
    
    def rev(self):
        key = "0000" if (self.key_box.text() == "") else self.key_box.text()
        msg = app_support.decode(self.fileName, key)
        self.msg_box.setPlainText(msg)
    
    def randStr(self):
        chars = list(string.ascii_uppercase + string.digits)
        key = [random.choice(chars) for _ in range(5)]
        key = ''.join(key)
        self.key_box.setText(key)

        
        
            

    
        



if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    Bruh = QtWidgets.QMainWindow()
    ui = Ui_Bruh()
    ui.setupUi(Bruh)
    Bruh.show()
    sys._excepthook = sys.excepthook 
    def exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback) 
        sys.exit(1) 
    sys.excepthook = exception_hook 
    sys.exit(app.exec_())
    
    
