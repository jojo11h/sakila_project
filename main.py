import connect_db as cnx

result = cnx.cursor

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
                result.execute('select first_name , last_name from actor;')
                for table in result:
                    print('-',' '.join(table))
            case "2":
                result.execute('select title from film;')
                for table in result:
                    print('-',' '.join(table))
            case "3":
              pass
            case _:
                print("essais")




