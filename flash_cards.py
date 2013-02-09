#!python
import random

def load_wordlists(yupik, english):
    ylist = open(yupik)
    elist = open(english)

    ywords = ylist.readlines()
    ewords = elist.readlines()

    ywords = [x.strip() for x in ywords]
    ewords = [x.strip() for x in ewords]

    list = zip(ywords, ewords)

    #strip commented out lines
    for w in list:
        if w[0].startswith('#'):
            list.remove(w)

    return list

def print_list_files():
    print("Yup'ik word list file is:	" + ylist_file)
    print("English word list file is:	" + elist_file)
    print("")

# print the Yup'ik word list
def list_file_dump(list_file):
    with open(list_file) as list:
        for line in list:
            print(line)

def print_raw_list():
    print(wordlist)

def debug_dump():
    list_file_dump(ylist_file)
    list_file_dump(elist_file)
    print("")
    print_raw_list()
    print("")

def choose_word(list):
    index = random.randint(0, len(list) - 1)
    return list[index]

def prompt(wordlist):
    #0 = yup'ik
    #1 = english
    w = choose_word(wordlist)
    word_type = random.getrandbits(1)
    input = raw_input('%s: ' % w[word_type])
    if input == w[not word_type]:
        print('\tcorrect!')
        wordlist.remove(w)
    else:
        print('\tincorrect')
    print('')

# flash cards
def flashcards():
    print('Yup\'ik and English Flashcards')
    print('')
    print('Please type the correct translation in the line below.')
    while wordlist != []:
        prompt(wordlist)


ylist_file = "yupik.txt"
elist_file = "english.txt"

wordlist = load_wordlists(ylist_file, elist_file)

flashcards()
