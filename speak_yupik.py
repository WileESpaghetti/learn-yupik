#!python
#encoding: utf-8

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
import grammar.Base, grammar.Postbase

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

yconsonants = ['c', 'g', 'gg', 'k', 'l', 'll', 'm', 'n', 'ng', 'p', 'q', 'r', 'rr', 's', 'ss', 't', 'v', 'vv', 'w', 'y']


def citation_suffix_type(word):
	type = ''

	if grammar.Vowel.isVowel(word[-3]):
		type = 'Vuq'
	elif grammar.Vowel.isVowel(word[-4]) and grammar.Vowel.isVowel(word[-5]):
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
	print("the type is:\t\t%s" % type)
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
	print("Old algorithm:\t\t%s" % word)
	grammar.Base.getClass(word)
	return word
		

def uq_forms():
	uqfile = open(uqwords)
	for w in [x.strip() for x in uqfile.readlines()]:
		print("Input word:\t\t%s" % w)
		uq_to_base(w)

		#new algorithm
		grammar.Postbase.stripPostbase(w, "+\'(g/t)uq")

def classTest():
	for w in ["cali", "nuna", "ui", "qercua", "neqe", "kuve", "piste", "inarte", "angute", "elite", "kiircete", "nerenrite", "angyar", "ingrir", "pengur", "nukalpiar", "ayag", "yurar", "ingrir", "pengur", "nukalpiar", "acag", "yug", "eqiur", "qanr", "acag", "yug", "atr", "yaquig", "ner"]:
		print(w)
		grammar.Base.debugClasses(w)

uq_forms()
#classTest()
