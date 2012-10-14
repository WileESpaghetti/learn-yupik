#!python
uqwords = "uq-test-words.txt"

yvowels = ['a', 'e', 'i', 'u'] #FIXME handle dbl letters and 'sometimes vowels'
yconsonants = ['c', 'g', 'gg', 'k', 'l', 'll', 'm', 'n', 'ng', 'p', 'q', 'r', 'rr', 's', 'ss', 't', 'v', 'vv', 'w', 'y']

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
		type = 'Cuq' #does not account for invalid words $uq or xuq, etc.

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
		print(uq_to_base(w))

uq_forms()
