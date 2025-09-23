z = str(input("Введіть речення: "))
words = z.split()
unique_words = list(set(words))
print("Різні слова у реченні:", unique_words)