# ~~ Hangman Game (without the graphic)~~

# The program provides a category for the user, the user has 10
# chances to guess the word/phrase, each time there is a correct
# guess a valid letter or word/phrase are populated and displayed.

def find_letter_in(word, guess):
    pos = []
    start = 0

    if word.find(guess, start) == -1:
        return None
    else:
        while start <= len(word):
            p = word.find(guess, start)
            if p == -1:
                break
            else:
                pos.append(p)
                start = p + 1
        return pos

def convert_c_to_cstr(current):
    current_str = ''
    for i in current:
        current_str = current_str + i
        return current_str


import random

word_list = {
            'Animal':['elephant', 'tarantula', 'eagle', 'humming bird'],
            'TV Show':['Mr Bean', 'Mr Robot', 'The Great Brittish Bake Off',
                        'Breaking Bad', 'Friends', 'A Man in the High Castle'],
            'Place we\'ve been on Holiday': ['France', 'Costa Rica', 'Maine', 'Las Vegas'],
            'Fruit' :['pineapple', 'mandarin', 'mango', 'star fruit', 'grapes']
            }
catagory = []
for c in word_list:
    catagory.append(c)

cat = random.choice(catagory)
word = random.choice(word_list[cat]).upper()
word2 = []
current = []

for w in word:
    for l in w:
        word2.append(l)

for l in word2:
    if l == ' ':
        current.append(' ')
    else:
        current.append('_ ')

print ('Let\'s play Hangman! Ok, here\'s the category: ' + cat)
guess = 'E' #input('Please guess a single letter or the word/phase:').upper()
counter = 0

u = find_letter_in(word,guess)
print (word)

if guess in [' ', '.', '-']:
    print('Sorry that\'s not a valid guess')
    #guess = input('Please guess a single letter or the word/phase:').upper()

else:
    counter = 0
    while guess:
        if counter > 10:
            print('Sorry, your 10 guesses are up. The man has been hung')
            break
        if len(guess) > 1 and guess == word:
            print('Yayy! you guessed it right! ' + word)
        else:
            if len(guess) == 1:
                pos = find_letter_in(word,guess)
                if pos is None:
                    print ('Nope!')
                    counter = counter + 1
                    guess = 'R'
                else:
                    for p in pos:
                        current[p] = guess
                    guess = 'I' #guess = input('Please guess a single letter or the word/phase:').upper()
                    print (current, counter)
