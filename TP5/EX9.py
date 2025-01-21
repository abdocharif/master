with open("journal.txt", "r") as file:
    lines = file.readlines()
    total_lines = len(lines)
    total_words = sum(len(line.split()) for line in lines)
    total_chars = sum(len(line.replace("\n","")) for line in lines)

print(f"Lignes : {total_lines}, Mots : {total_words}, Caractères : {total_chars}")
