import random

def find_number():
    print("Mémorisez un nombre entier entre 1 et 100, le script va essayer de le retrouver, ne trichez pas :")
    
    nombreMin = 1
    nombreMax = 100    
    essais = 0
    
    while True:
        essais += 1
        try:
            proposition = random.randint(nombreMin, nombreMax)
        except ValueError:
            print(f"\nErreur : Vous avez ticher le chiffre doit être entre {nombreMax} et {nombreMin}.")
            print("Le jeu va s'arreter.")
            break

        print(f"Le script propose {proposition}")
        
        while True:
            try:
                reponse = input("Votre réponse (- ou + ou =) : ")
                if reponse not in ["-", "+", "="]:
                    raise ValueError("Réponse invalide")
                break
            except ValueError as e:
                print(f"Erreur : {e}. Veuillez répondre par '+', '-', ou '='.")
        
        if reponse == "-":
            nombreMax = proposition - 1
        elif reponse == "+":
            nombreMin = proposition + 1
        elif reponse == "=":
            print(f"\nLe script a trouvé le nombre {proposition} en {essais} essais !")
            break

if __name__ == "__main__":
    find_number()