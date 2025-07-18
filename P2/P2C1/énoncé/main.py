nombre1 = input("Veuillez entrer un premier nombre : ")
if not nombre1.isnumeric() :
    print("Erreur : Ce n'est pas un nombre entier.")
    raise SystemExit("Fin du programme.")
else :
    nombre1 = int(nombre1)

nombre2 = input("Veuillez entree un second nombre : ")
if not nombre2.isnumeric() :
    print("Erreur : Ce n'est pas un nombre entier.")
    raise SystemExit("Fin du programme.")
else :
    nombre2 = int(nombre2)

operation = input("Veuillez saisir un symbole d'opération :")
if operation not in ["*", "+", "-", "/"] :
    print("Erreur : le symbole doit être '*' ou '+' ou '-' ou '/' .")
    raise SystemExit("Fin du programme")

if operation == "*" :
    resultat = nombre1*nombre2
elif operation == "+" :
    resultat = nombre1+nombre1
elif operation == "-" :
    resultat = nombre1-nombre2
else :
    if nombre2 == 0 :
        print("Erreur : Impossible de diviser par zéro.")
        raise SystemExit("Fin du programme.")
    resultat = round(nombre1/nombre2)

print(f"{str(nombre1)} {str(operation)} {str(nombre2)} = {str(resultat)}")

