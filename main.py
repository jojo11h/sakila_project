import time
import connect_db as cnx
from actor import show_actor

result = cnx.cursor

while True:
    print("_" * 50)
    print()
    print("Que veux tu faire :")
    print("-> 1. Voir le contenu (Film, Acteur)")
    print("-> 2. Modifier le contenu")
    print("-> 3. Supprimer du contenu")
    print(' -> "q pour quitter ')
    user_choice = input("=> ")

    if user_choice == "q":
        break

    if user_choice not in ["1", "2", "3"]:
        print("Veuillez choisir une donnée valide !")

    else:
        match user_choice:
            case "1":
                while True:
                    print("_" * 50)
                    print()
                    print("Que veux tu voir")
                    print("-> 1. Les acteurs")
                    print("-> 2. Les Films")
                    print("-> 3. Les vidéothèques")
                    print(' -> "q pour quitter ')
                    user_choice = input("=> ")

                    if user_choice == "q":
                        break

                    if user_choice not in ["1", "2", "3"]:
                        print("Veuillez choisir une donnée valide !")

                    else:
                        match user_choice:
                            case "1":
                                show_actor()
                                time.sleep(1.5)
                            case "2":
                                result.execute('select title from film;')
                                for table in result:
                                    print('-',' '.join(table))
                                time.sleep(1.5)
                                pass
                            case "3":
                                time.sleep(1.5)
                                pass
                            case _:
                                print("essais")
                time.sleep(1.5)
            case "2":
                pass
            case "3":
              pass
            case _:
                print("essais")




