nombres = input("Veuillez saisir une liste de nombre séparé par des virgules : ")

liste = nombres.split(',')
print("Liste des nombres : " , liste)

liste_entiers = []
for nombre in liste :
    nombre_entier = int(nombre)
    liste_entiers.append(nombre_entier)

somme = 0
for nombre in liste_entiers :
    somme += nombre
print("La somme des valeurs de la liste = " , somme)

moyenne = round(somme / len(liste_entiers))
print("La moyenne des valeurs de la listes = " , moyenne)

liste_nombres_superieur_moyenne = []
for nombre in liste :
    if int(nombre) > moyenne :
        liste_nombres_superieur_moyenne.append(nombre)

print("Liste des valeurs supérieurs à la moyenne de la liste d'origine : " ,liste_nombres_superieur_moyenne)