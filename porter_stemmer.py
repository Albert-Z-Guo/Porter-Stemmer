class PorterStemmer:
    def vowel(self, letter):
            if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
                return True
            else:
                return False

    def consonant(self, word, letter_index):
        if not self.vowel(word[letter_index]) and word[letter_index] != 'y':
            return True
        elif not self.vowel(word[letter_index]) and word[letter_index] == 'y':
            if letter_index == 0:
                return True
            # y becomes a vowel if preceded by a consonant
        elif not self.vowel(word[letter_index - 1]):
                return False

    def measure(self, word, return_word_in_vc_representation=False):
        word_in_vc_representation = ''
        i = 0
        for letter in word:
            if self.vowel(letter):
                word_in_vc_representation += 'v'
            else:
                if self.consonant(word, i):
                    word_in_vc_representation += 'c'
                else:
                    word_in_vc_representation += 'v'
            i += 1
        if return_word_in_vc_representation: return word_in_vc_representation
        return word_in_vc_representation.count('vc')

    def contain_vowel(self, stem):
        for letter in stem:
            if self.vowel(letter):
                return True
        else:
            return False

    def end_with_double_consonant(self, stem):
        if stem[-1] == stem[-2] and self.consonant(stem, -1) and self.consonant(stem, -2):
            return True
        else:
            return False

    def end_with_cvc(self, stem):
        if self.measure(stem, True).endswith('cvc') and not (stem[-1] == 'w' or stem[-1] == 'x' or stem[-1] == 'y'):
            return True
        else:
            return False

    def step_1a(self, word):
        if word.endswith('sses'):
            word = word[:-4] + 'ss'
        elif word.endswith('ies'):
            word = word[:-3] + 'i'
        elif word.endswith('ss'):
            word = word[:-2] + 'ss'
        elif word.endswith('s'):
            word = word[:-1]
        return word

    def step_1b(self, word):
        trigger = False
        if self.measure(word[:-3]) > 0 and word.endswith('eed'):
            word = word[:-3] + 'ee'
        elif self.contain_vowel(word[:-2]) and word.endswith('ed'):
            word = word[:-2]
            trigger = True
        elif self.contain_vowel(word[:-3]) and word.endswith('ing'):
            word = word[:-3]
            trigger = True
        if trigger:
            if word.endswith('at') or word.endswith('bl') or word.endswith('iz'):
                word = word + 'e'
            elif self.end_with_double_consonant(word) and not (word.endswith('l') or word.endswith('s') or word.endswith('z')):
                word = word[:-1]
            elif self.measure(word) == 1 and self.end_with_cvc(word):
                word = word + 'e'
        return word

    def step_1c(self, word):
        if self.contain_vowel(word[:-1]) and word.endswith('y'):
            word = word[:-1] + 'i'
        return word

    def step_2(self, word):
        if self.measure(word[:-7]) > 0 and word.endswith('ational'):
            word = word[:-7] + 'ate'
        elif self.measure(word[:-6]) > 0 and word.endswith('tional'):
            word = word[:-6] + 'tion'
        elif self.measure(word[:-4]) > 0 and word.endswith('enci'):
            word = word[:-4] + 'ence'
        elif self.measure(word[:-4]) > 0 and word.endswith('anci'):
            word = word[:-4] + 'ance'
        elif self.measure(word[:-4]) > 0 and word.endswith('izer'):
            word = word[:-4] + 'ize'
        elif self.measure(word[:-4]) > 0 and word.endswith('abli'):
            word = word[:-4] + 'able'
        elif self.measure(word[:-4]) > 0 and word.endswith('alli'):
            word = word[:-4] + 'al'
        elif self.measure(word[:-5]) > 0 and word.endswith('entli'):
            word = word[:-5] + 'ent'
        elif self.measure(word[:-3]) > 0 and word.endswith('eli'):
            word = word[:-3] + 'e'
        elif self.measure(word[:-5]) > 0 and word.endswith('ousli'):
            word = word[:-5] + 'ous'
        elif self.measure(word[:-7]) > 0 and word.endswith('ization'):
            word = word[:-7] + 'ize'
        elif self.measure(word[:-5]) > 0 and word.endswith('ation'):
            word = word[:-5] + 'ate'
        elif self.measure(word[:-4]) > 0 and word.endswith('ator'):
            word = word[:-4] + 'ate'
        elif self.measure(word[:-5]) > 0 and word.endswith('alism'):
            word = word[:-5] + 'al'
        elif self.measure(word[:-7]) > 0 and word.endswith('iveness'):
            word = word[:-7] + 'ive'
        elif self.measure(word[:-7]) > 0 and word.endswith('fulness'):
            word = word[:-7] + 'ful'
        elif self.measure(word[:-7]) > 0 and word.endswith('ousness'):
            word = word[:-7] + 'ous'
        elif self.measure(word[:-5]) > 0 and word.endswith('aliti'):
            word = word[:-5] + 'al'
        elif self.measure(word[:-5]) > 0 and word.endswith('iviti'):
            word = word[:-5] + 'ive'
        elif self.measure(word[:-6]) > 0 and word.endswith('biliti'):
            word = word[:-6] + 'ble'
        return word

    def step_3(self, word):
        if self.measure(word[:-5]) > 0 and word.endswith('icate'):
            word = word[:-5] + 'ic'
        elif self.measure(word[:-6]) > 0 and word.endswith('active'):
            word = word[:-6]
        elif self.measure(word[:-5]) > 0 and word.endswith('alize'):
            word = word[:-5] + 'al'
        elif self.measure(word[:-5]) > 0 and word.endswith('iciti'):
            word = word[:-5] + 'ic'
        elif self.measure(word[:-3]) > 0 and word.endswith('ful'):
            word = word[:-3]
        elif self.measure(word[:-4]) > 0 and word.endswith('ness'):
            word = word[:-4]
        return word

    def step_4(self, word):
        if self.measure(word[:-2]) > 1 and word.endswith('al'):
            word = word[:-2]
        elif self.measure(word[:-4]) > 1 and word.endswith('ance'):
            word = word[:-4]
        elif self.measure(word[:-4]) > 1 and word.endswith('ence'):
            word = word[:-4]
        elif self.measure(word[:-2]) > 1 and word.endswith('er'):
            word = word[:-2]
        elif self.measure(word[:-2]) > 1 and word.endswith('ic'):
            word = word[:-2]
        elif self.measure(word[:-4]) > 1 and word.endswith('able'):
            word = word[:-4]
        elif self.measure(word[:-4]) > 1 and word.endswith('ible'):
            word = word[:-4]
        elif self.measure(word[:-3]) > 1 and word.endswith('ant'):
            word = word[:-3]
        elif self.measure(word[:-5]) > 1 and word.endswith('ement'):
            word = word[:-5]
        elif self.measure(word[:-4]) > 1 and word.endswith('ment'):
            word = word[:-4]
        elif self.measure(word[:-3]) > 1 and word.endswith('ent'):
            word = word[:-3]
        elif self.measure(word[:-4]) > 1 and word.endswith('ance'):
            word = word[:-4]
        elif self.measure(word[:-3]) > 1 and (word[-4] == 's' or word[-4] == 't') and word.endswith('ion'):
            word = word[:-3]
        elif self.measure(word[:-2]) > 1 and word.endswith('ou'):
            word = word[:-2]
        elif self.measure(word[:-3]) > 1 and word.endswith('ism'):
            word = word[:-3]
        elif self.measure(word[:-3]) > 1 and word.endswith('ate'):
            word = word[:-3]
        elif self.measure(word[:-3]) > 1 and word.endswith('iti'):
            word = word[:-3]
        elif self.measure(word[:-3]) > 1 and word.endswith('ous'):
            word = word[:-3]
        elif self.measure(word[:-3]) > 1 and word.endswith('ive'):
            word = word[:-3]
        elif self.measure(word[:-3]) > 1 and word.endswith('ize'):
            word = word[:-3]
        return word

    def step_5a(self, word):
        if self.measure(word[:-1]) > 1 and word.endswith('e'):
            word = word[:-1]
        elif self.measure(word[:-1]) == 1 and (not self.end_with_cvc(word[:-1])) and word.endswith('ize'):
            word = word[:-1]
        return word

    def step_5b(self, word):
        if self.measure(word) > 1 and self.end_with_double_consonant(word) and word.endswith('l'):
            word = word[:-1]
        return word

    def stem(self, word):
        word = self.step_1a(word)
        word = self.step_1b(word)
        word = self.step_1c(word)
        word = self.step_2(word)
        word = self.step_3(word)
        word = self.step_4(word)
        word = self.step_5a(word)
        word = self.step_5b(word)
        return word


# test
stemmer = PorterStemmer()
print(stemmer.step_1b('portrayed'))
