import shutil

# Copier un fichier
shutil.copy("journal.txt", "journal_copie.txt")

# Déplacer un fichier
shutil.move("journal_copie.txt", "archives/")
