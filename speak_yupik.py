#python
import random

ylist_file = "yupik.txt"
elist_file = "english.txt"
uqwords = "uq-test-words.txt"

yvowels = ['a', 'e', 'i', 'u'] #FIXME handle dbl letters and 'sometimes vowels'
yconsonants = ['c', 'g', 'gg', 'k', 'l', 'll', 'm', 'n', 'ng', 'p', 'q', 'r', 'rr', 's', 'ss', 't', 'v', 'vv', 'w', 'y']

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
		print(w)
		if w[0].startswith('#'):
			list.remove(w)

	return list

def print_list_files():
	print("Yup'ik word list is:	" + ylist_file) 
	print("English word list is:	" + elist_file) 
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
		print('correct!')
		wordlist.remove(w)
	else:
		print('incorrect')

wordlist = load_wordlists(ylist_file, elist_file)

# flash cards
def flashcards():
	while wordlist != []:
		prompt(wordlist)

def isVowel(c):
	vowel = False
	for v in yvowels:
		if c == v:
			vowel = True
			break
	return vowel

def citation_suffix_type(word):
	type = ''

	if isVowel(word[-3]):
		type = 'Vuq'
	elif isVowel(word[-4]) and isVowel(word[-5]):
		type = 'VVguq'
	elif word[-3] == '\'':
		type = '\'uq'
	elif word[-3] == 't':
		if word[-4] == 'g' and word[-5] != 'n':
			 type = 'gtuq'
		elif word[-4] == 'r':
			type = 'rtuq'
		else:
			type = 'Cuq'
	else:
		type = 'Cuq!' #does not account for invalid words $uq or xuq, etc.

	return type

def uq_to_base(word):
	type = citation_suffix_type(word)

	if type == 'gtuq' or type == 'rtuq' or type == 'VVguq':
		word = word[:-3]
		#print(word)
	elif type == '\'uq':
		word = word[:-3]
		word = word + 'e'
		#print(word)
	elif type == 'Cuq':
		word = word[:-2]
		word = word + 'e'
		#print(word)
	return word
		

def uq_forms():
	uqfile = open(uqwords)
	for w in [x.strip() for x in uqfile.readlines()]:
		uq_to_base(w)

uq_forms()
