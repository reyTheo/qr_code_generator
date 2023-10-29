import tkinter as tk
import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Fonction appelée lorsque l'utilisateur clique sur le bouton "Valider"
def valider():
    contenu = entry.get()  # Obtenir la valeur saisie par l'utilisateur
    qr.add_data(contenu)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img.save("qr_code.png")

    im = Image.open("qr_code.png")

    im.show()

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.geometry("400x300")
fenetre.title("Saisie de l'URL de votre site")

# Créer un label pour afficher le message d'accueil
message = "Entrez l'URL de votre site :"
label = tk.Label(fenetre, text=message)
label.pack()

# Créer un champ de saisie (Entry) pour l'utilisateur
entry = tk.Entry(fenetre)
entry.pack()

# Créer un bouton "Valider" pour soumettre la valeur
bouton = tk.Button(fenetre, text="Valider", command=valider)
bouton.pack()

# Lancer la boucle principale de l'interface
fenetre.mainloop()
