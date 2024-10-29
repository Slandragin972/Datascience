import re 

with open('/Users/camillekeisser/Documents/Datascience/story.txt', 'r') as file:
    text = file.read()

pattern = r'[^a-zA-Z0-9\s.,]'
cleaned_text = re.sub(pattern, '', text)

print(cleaned_text)