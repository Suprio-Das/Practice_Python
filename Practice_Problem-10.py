import re

def count_unique_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    unique_words = set(words)
    return len(unique_words)


text = "Hello, world! Hello Python."
print(count_unique_words(text))
