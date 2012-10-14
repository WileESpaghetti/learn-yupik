#!python

# Function naming conventions
# fps = first person singular
# fpd = first person dual
# fpp = first person plural
# sps = second person singular
# spd = second person dual
# spp = second person plural
# tps = third person singular
# tpd = third person dual
# tpp = third person plural

# rules for endings
# +	keeps final consonant of base
# -	drops final consonent
# ~	drops final 'e'
# ÷	keeps strong final consonents
# :	drops voiced velar consonents if between single vowels where first vowel is prime
# '	causes gemination of final consonent if base in the form of (C)VCe-
# @	???
# - -	base drops final conconant + vowel preceeding it. (only for shortened forms of consonent dropping postbases beginning with 'li'
# %	attaches irregularly (certain non-productive postbases only)


# TODO technically all of these begin with +(g/t)u, but we are not set up to do the kind of
# parsing necessary to work with postbases in the 'official manner' yet
fps_ending = ':nga'
fpd_ending = 'kuk'
fpp_ending = 'kut'
sps_ending = 'ten'
spd_ending = 'tek'
spp_ending = 'ci'
tps_ending = 'uq'
tpd_ending = 'uk'
tpp_ending = 'ut'

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
	elif type == '\'uq':
		word = word[:-3]
		word = word + 'e'
	elif type == 'Cuq':
		word = word[:-2]
		word = word + 'e'
	return word
		

def uq_forms():
	uqfile = open(uqwords)
	for w in [x.strip() for x in uqfile.readlines()]:
		print(uq_to_base(w))

uq_forms()
