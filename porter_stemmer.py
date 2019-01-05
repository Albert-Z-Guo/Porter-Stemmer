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
        elif self.measure(word[:-1]) == 1 and (not self.end_with_cvc(word[:-1])) and word.endswith('e'):
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
test = True
if test:
    stemmer = PorterStemmer()

    # tests for step 1a
    print('Step 1a:')
    print('caresses ->', stemmer.step_1a('caresses'))
    print('ponies   ->', stemmer.step_1a('ponies'))
    print('ties     ->', stemmer.step_1a('ties'))
    print('caress   ->', stemmer.step_1a('caress'))
    print('cats     ->', stemmer.step_1a('cats'))

    # tests for step 1b
    print('\nStep 1b:')
    print('feed      ->', stemmer.step_1b('feed'))
    print('agreed    ->', stemmer.step_1b('agreed'))
    print('plastered ->', stemmer.step_1b('plastered'))
    print('bled      ->', stemmer.step_1b('bled'))
    print('motoring  ->', stemmer.step_1b('motoring'))
    print('sing      ->', stemmer.step_1b('sing'))
    print('conflated ->', stemmer.step_1b('conflated'))
    print('troubled  ->', stemmer.step_1b('troubled'))
    print('sized     ->', stemmer.step_1b('sized'))
    print('hopping   ->', stemmer.step_1b('hopping'))
    print('tanned    ->', stemmer.step_1b('tanned'))
    print('falling   ->', stemmer.step_1b('falling'))
    print('hissing   ->', stemmer.step_1b('hissing'))
    print('failing   ->', stemmer.step_1b('failing'))
    print('filling   ->', stemmer.step_1b('filling'))

    # tests for step 1c
    print('\nStep 1c:')
    print('happy ->', stemmer.step_1c('happy'))
    print('sky   ->', stemmer.step_1c('sky'))

    # tests for step 2
    print('\nStep 2:')
    print('relational     ->', stemmer.step_2('relational'))
    print('conditional    ->', stemmer.step_2('conditional'))
    print('rational       ->', stemmer.step_2('rational'))
    print('valenci        ->', stemmer.step_2('valenci'))
    print('hesitanci      ->', stemmer.step_2('hesitanci'))
    print('digitizer      ->', stemmer.step_2('digitizer'))
    print('conformabli    ->', stemmer.step_2('conformabli'))
    print('radicalli      ->', stemmer.step_2('radicalli'))
    print('differentli    ->', stemmer.step_2('differentli'))
    print('vileli         ->', stemmer.step_2('vileli'))
    print('analogousli    ->', stemmer.step_2('analogousli'))
    print('vietnamization ->', stemmer.step_2('vietnamization'))
    print('predication     ->', stemmer.step_2('predication'))
    print('operator       ->', stemmer.step_2('operator'))
    print('feudalism      ->', stemmer.step_2('feudalism'))
    print('decisiveness   ->', stemmer.step_2('decisiveness'))
    print('hopefulness    ->', stemmer.step_2('hopefulness'))
    print('callousness    ->', stemmer.step_2('callousness'))
    print('formaliti      ->', stemmer.step_2('formaliti'))
    print('sensitiviti    ->', stemmer.step_2('sensitiviti'))
    print('sensibiliti    ->', stemmer.step_2('sensibiliti'))

    # tests for step 3
    print('\nStep 3:')
    print('triplicate  ->', stemmer.step_3('triplicate'))
    print('formative   ->', stemmer.step_3('formative'))
    print('formalize   ->', stemmer.step_3('formalize'))
    print('electriciti ->', stemmer.step_3('electriciti'))
    print('electrical  ->', stemmer.step_3('electrical'))
    print('hopeful     ->', stemmer.step_3('hopeful'))
    print('goodness    ->', stemmer.step_3('goodness'))

    # tests for step 4
    print('\nStep 4:')
    print('revival     ->', stemmer.step_4('revival'))
    print('allowance   ->', stemmer.step_4('allowance'))
    print('inference   ->', stemmer.step_4('inference'))
    print('airliner    ->', stemmer.step_4('airliner'))
    print('gyroscopic  ->', stemmer.step_4('gyroscopic'))
    print('adjustable  ->', stemmer.step_4('adjustable'))
    print('defensible  ->', stemmer.step_4('defensible'))
    print('irritant    ->', stemmer.step_4('irritant'))
    print('replacement ->', stemmer.step_4('replacement'))
    print('adjustment  ->', stemmer.step_4('adjustment'))
    print('dependent   ->', stemmer.step_4('dependent'))
    print('adoption    ->', stemmer.step_4('adoption'))
    print('homologou   ->', stemmer.step_4('homologou'))
    print('communism   ->', stemmer.step_4('communism'))
    print('activate    ->', stemmer.step_4('activate'))
    print('angulariti  ->', stemmer.step_4('angulariti'))
    print('homologous  ->', stemmer.step_4('homologous'))
    print('effective   ->', stemmer.step_4('effective'))
    print('bowdlerize  ->', stemmer.step_4('bowdlerize'))

    # tests for step 5a
    print('\nStep 5a:')
    print('probate ->', stemmer.step_5a('probate'))
    print('rate    ->', stemmer.step_5a('rate'))
    print('cease   ->', stemmer.step_5a('cease'))

    # tests for step 5b
    print('\nStep 5b:')
    print('controll ->', stemmer.step_5b('control'))
    print('roll     ->', stemmer.step_5b('roll'))


    # general tests
    print('\nGeneral tests:')
    print(stemmer.stem("Sally's"))
    print(stemmer.stem('hitting'))
    print(stemmer.stem('digging'))
    print(stemmer.stem("I'll"))
    print(stemmer.stem("We've"))
    print(stemmer.stem("don't"))
