import sys

LIST = []
MENU_RESTO =""" Bonjour Monsieur/Madamme,
Veillez faire votre choix parmi la liste ci-dessous .
1: Le plat du jour
2: Boire quelque chose
3: Emporter à manger
4: Acheter de la glace
5: Annuler un commande
6: Annuler tous vos commandes
7: afficher la liste de vos commandes
8: Quitter
  :) Vous désirez quoi?
  """

CHOIX_MENU = ["1", "2", "3", "4", "5", "6", "7", "8"]

while True:
    VOTRE_CHOIX = ""
    while VOTRE_CHOIX not in CHOIX_MENU:
        VOTRE_CHOIX = input(MENU_RESTO)
        if VOTRE_CHOIX not in CHOIX_MENU:
            print("OUPS !!! :]Veillez choisir parmis la liste proposée .")
    if VOTRE_CHOIX == "1":
        choix = input("Dites nous, vous choisissez quel plat ?")
        LIST.append(choix)
        if choix:  
            print(f"Merci d'avoir choisi le {choix}, nous allons vous en servir tout de suite.")
        else:
            print("Veillez nous indiquez le plat que vous désiriez manger.")

    elif VOTRE_CHOIX =="2":
        choix = input("Vous souhaitez boire quoi ?")
        LIST.append(choix)
        if choix:
            print(f"Voilà {choix} pour vous.")
        else:
            print("Nous vous offrons de l'eau alors")
            
    elif VOTRE_CHOIX == "3" :
        choix = input("On vous prépare quoi?") 
        LIST.append(choix)  
        if choix:
            print(f"Super! On vous amène votre {choix} tout de suite.")
        else:
            print(f"Votre commande {choix} a été annulé.")
        
    elif VOTRE_CHOIX == "4":
        choix = input("Vous voulez quel parfum")
        LIST.append(choix)
        if choix:
            print(f"D'accord, voilà votre {choix}")
        else:
            print("Vous avez pas fait de choix")
    
    elif VOTRE_CHOIX == "5": 
        choix = input("Que voulez-vous annuler ?")
        if choix in LIST: 
            LIST.remove(choix)  
            print(f"{choix} à bien été supprimer de la liste de vos commande.")  
        else:
            print(f"{choix} ne se trouve dans la liste de vos commande. ")
            
    elif VOTRE_CHOIX == "6":
        LIST.clear()
        print("La liste à été vidée")
    
    elif VOTRE_CHOIX == "7":
        if LIST:
            print("Voici le contenu de votre liste")
            for i, choix in enumerate(LIST, 1):
                print(f"{i}. {choix}")
        else:
            print("La liste est vide, vous avez pas encore fait de commande")
            
    elif VOTRE_CHOIX == "8":
        print("À bientôt")
        sys.exit()
    
    
    
    print("-" * 100)
    