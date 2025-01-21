def process_input(user_input):
    try:
        number = int(user_input)
        resultat=10/number
        print(f"le resultat: {resultat}.")
    except ValueError:
        print("nombre invalide")
    except ZeroDivisionError:
        print("division par zero")
process_input(input("entrer un nombre:"))