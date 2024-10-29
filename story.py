# Ouvrir le fichier en mode lecture
with open('story.txt', 'r', encoding='utf-8') as file:
    # Lire le contenu du fichier
    content = file.read()

# Afficher le contenu du fichier
print(content)