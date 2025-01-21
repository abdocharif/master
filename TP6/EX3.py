def read_file(filename):
    try:
        fichier = open(filename,"r")
        lines = fichier.readlines()
        for line in lines:
            print(line)
    except FileNotFoundError:
        print("erreur: fichier non trouve")
    finally:
        if 'fichier' in locals():
             fichier.close()
filename = "error.log"
if __name__ == '__main__':
    read_file(filename)
