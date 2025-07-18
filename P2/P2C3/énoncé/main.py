def salaire_mensuel(salaire_annuel) :
    return salaire_annuel / 12

def salaire_hebdomadaire(salaire_mensuel) :
    return salaire_mensuel / 4

def salaire_horaire(salaire_hebdomadaire, heures_travaillees) :
    return salaire_hebdomadaire / heures_travaillees

salaire_annuel = float(input("Veuillez entrer votre salaire annuel : "))
heures_travaillees = float(input("Veuillez entrer votre taux horaire hebdomadaire : "))

salaire_mensuel_utlisateur = salaire_mensuel(salaire_annuel)
salaire_hebdomadaire_utilisateur = salaire_hebdomadaire(salaire_mensuel_utlisateur)
salaire_horaire_utlisateur = salaire_horaire(salaire_hebdomadaire_utilisateur, heures_travaillees)

print(f"Votre salaire horaire est de {salaire_horaire_utlisateur} euros.")
