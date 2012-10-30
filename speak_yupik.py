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

def uq_forms():
	uqfile = open(uqwords)
	for w in [x.strip() for x in uqfile.readlines()]:
		print("Input word:\t\t%s" % w)
		grammar.Postbase.stripPostbase(w, "+\'(g/t)uq")

uq_forms()
print("")
print("")
grammar.Postbase.stripPostbase("ner'ukuk", "+\'(g/t)ukuk")
