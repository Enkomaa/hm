def create_abbreviation(phrase):
    words = phrase.split()
    abbreviation = ""

    for word in words:
        if word and word[0].isalpha():
            abbreviation += word[0].upper()

    return abbreviation

my_phrase = "Высшее учебное заведение"
print(create_abbreviation(my_phrase))