import re
import chardet

file_name = 'story.txt'

# Detect encoding
with open(file_name, 'rb') as file:
    raw_data = file.read()
    encoding = chardet.detect(raw_data)['encoding']
    print(f"encoding = {encoding}")

# with open(file_name, 'r', encoding=encoding) as file:
#     content = file.read()
    
# Ouvrir le fichier en mode lecture
with open('story.txt', 'r', encoding=encoding) as file:
    # Lire le contenu du fichier
    content = file.read()
    
# Remplacer les caractères accentués par leur équivalent sans accent

content = re.sub(r'[àâ]', 'a', content)
content = re.sub(r'[éèêë]', 'e', content)
content = re.sub(r'[îïì]', 'i', content)
content = re.sub(r'[ôöò]', 'o', content)
content = re.sub(r'[ùû]', 'u', content)
content = re.sub(r'[ç]', 'c', content)

# Afficher le contenu du fichier
print(content)