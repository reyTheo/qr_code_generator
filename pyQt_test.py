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

class Fenetre(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # création du champ de texte
        self.champ = QLineEdit()
        
        # création du bouton
        self.bouton = QPushButton("GENERATE")
        # on connecte le signal "clicked" à la méthode "appui_bouton_copie"
        self.bouton.clicked.connect(self.appui_bouton_copie)
 
        # création de l'étiquette
        self.label = QLabel()
        
        # mise en place du gestionnaire de mise en forme
        layout = QVBoxLayout()
        layout.addWidget(self.champ)
        layout.addWidget(self.bouton)
        layout.addWidget(self.label)
        self.setLayout(layout)
        
        self.setWindowTitle("Link to QrCode")
        self.resize(500,250)
        # permet de fixer la fenetre position de la fenetre
        # sur l'ecran
        # self.move(300,50)

       

    # on définit une méthode à connecter au signal envoyé
    def appui_bouton_copie(self):
        # la méthode "text" de QLineEdit permet d'obtenir le texte à copier
        texte_a_copier = self.champ.text()

        qr.add_data(texte_a_copier)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        img.save("qr_code.png")

        im = Image.open("qr_code.png")

        im.show()

        # la méthode "setText" de QLabel permet de changer
        # le texte de l'étiquette
        # self.label.setText(texte_a_copier)

    def use_button(self):
        if self.champ.text() == "" :
            self.bouton.setEnabled(True) 


app = QApplication.instance() 
if not app:
    app = QApplication(sys.argv)
    
fen = Fenetre()
fen.show()

app.exec_()

