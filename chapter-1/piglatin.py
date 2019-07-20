import string


VOWELS = 'aeiouAEIOU'


def maintain_capitalisation(old, new):
    if old[-1] in string.uppercase:
        return new.upper()
    elif old[0] in string.uppercase:
        return new.capitalize()
    return new


def convert_word(word):
    first_character = word[0]
    if first_character in VOWELS:
        latin = word + 'way'
    else:
        latin = word[1:] + first_character + 'ay'
    return maintain_capitalisation(word, latin)
