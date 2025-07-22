import requests
from bs4 import BeautifulSoup

from OPCRs_basicPython.P3.P3C2.correction.main import description

# extraction des infos avec BeautidulSoup
with open ("index.html", "r") as file :
    soup = BeautifulSoup(file.read(), 'html.parser')

# extraction du titre de la page
titre = soup.title.string
print(f"Titre : {titre}")

# extraction du texte de la balise h1
h1_text = soup.find("h1").string
print(f"Texte de la balise h1 : {h1_text}")

#initialisation du dictionnaire 'tous_les_produits' pour y stocker la listes des produits
tous_les_produits = {}

# extraction des noms et des prix des produits dans la liste
produits = soup.find_all("li")
for product in tous_les_produits :
    nom = soup.find("h2").string
    prix_str = soup.find("p", class_="price")
    prix_list = prix_str.split(" ")
    tous_les_produits[nom] = {"prix : ", prix_list[1]}

    # extraction de la descritpion des produits
    description = product.find_all("p")[-1].string
    tous_les_produits[nom]["descritption"] = description

# affichage des informations extraites
print("Produits : ", tous_les_produits)

# conversion des prix en dollars
for nom in tous_les_produits :
    prix_str = tous_les_produits[nom]["prix"]

    # supprimer le symbole '€'
    prix = prix_str.strip("€")

    # convertir en float puis en dollars
    prix = float(prix)
    prix_en_dollars = prix * 1.169
    tous_les_produits[nom]["prix en dollars"] = f"{prix_en_dollars}$"

# affichage avec les prix en dollars
print(f"Tous les produits : {tous_les_produits}")



