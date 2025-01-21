def safe_division(a, b):
    try:
        S = a/b
        print(f"le resultat: {S}.")
    except ZeroDivisionError:
        print("erreur division par zero")
    else:
        print("la division a été effectuée avec succès")
    finally:
        print("fonction a ete terminer avec succe")
safe_division(1,1)