import string


def convert_word(word):
    cls = LeadingVowel if word[0] in 'aeiouAEIOU' else LeadingConsonant
    return cls(word).convert()


class Word:

    def __init__(self, english):
        self.english = english

    def maintain_case(self, latin):
        if self.english[-1] in string.uppercase:
            return latin.upper()
        elif self.english[0] in string.uppercase:
            return latin.capitalize()
        return latin

    def convert(self):
        return self.maintain_case(self.to_latin())


class LeadingVowel(Word):

    def to_latin(self):
        return self.english + 'way'


class LeadingConsonant(Word):

    def to_latin(self):
        return self.english[1:] + self.english[0] + 'ay'
