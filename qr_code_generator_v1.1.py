import sys
from PyQt5.QtWidgets import *

import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

class Window(QWidget):
   
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("QRCode generator")

        self.text = QLineEdit()
        self.button = QPushButton("Generate")

        layout = QVBoxLayout()
        layout.addWidget(self.text)
        layout.addWidget(self.button)
        self.setLayout(layout)

        self.resize(500,250)

        self.button.clicked.connect(self.button_enable)
        
    
    # used to verifie that the user is typing something in the text box
    def button_enable(self):
        texte_a_copier = self.text.text()
        if self.text.text() == "" :
            message = QMessageBox()
            message.setText("Invalid, try again")
            message.exec_()
        else:
            #texte_a_copier = self.text.text()

            qr.add_data(texte_a_copier)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")

            img.save("qr_code.png")

            im = Image.open("qr_code.png")

            im.show()

            # la méthode "setText" de QLabel permet de changer
            # le texte de l'étiquette
            # self.label.setText(texte_a_copier)
    

def main():
    app = QApplication.instance() 
    if not app:
        app = QApplication(sys.argv)
        
    window = Window()
    window.show()

    app.exec_()


if __name__ == '__main__':
    main()

