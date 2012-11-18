#!python
#encoding: utf-8
import grammar.Base, grammar.Postbase, string

""" Practice for adding the intransitive endings for the indicative mood """

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

fps_ending = "+'(g/t)u:nga"
fpd_ending = "+'(g/t)ukuk"
fpp_ending = "+'(g/t)ukut"

sps_ending = "+'(g/t)uten"
spd_ending = "+'(g/t)utek"
spp_ending = "+'(g/t)uci"

tps_ending = "+'(g/t)uq"
tpd_ending = "+'(g/t)uk"
tpp_ending = "+'(g/t)ut"

endings = [fps_ending, fpd_ending, fpp_ending, sps_ending, spd_ending, spp_ending, tps_ending, tpd_ending, tpp_ending]

verbtests = "verbs/indicitive-intransitive/"

bases_list = verbtests + "bases.txt"

fps_list = verbtests + "fps.txt"
fpd_list = verbtests + "fpd.txt"
fpp_list = verbtests + "fpp.txt"

sps_list = verbtests + "sps.txt"
spd_list = verbtests + "spd.txt"
spp_list = verbtests + "spp.txt"

tps_list = verbtests + "tps.txt"
tpd_list = verbtests + "tpd.txt"
tpp_list = verbtests + "tpp.txt"

def verb_test(test, postbase):
	tfile = open(test)
	for w in [x.strip() for x in tfile.readlines()]:
		print("Input word:\t\t%s" % w)
		grammar.Postbase.stripPostbase(w, postbase)

def tps_test():
	# does not handle words separated by spaces correctly
	verb_test(tps_list, tps_ending)

def detect_verb_postbase(word):
	#FIXME: this might make more sense inside of Postbase.py instead of here
	word = string.strip(word)
	postbase = ''
	
	# FIXME fp endings needed to be to be tested first because matching
	# currently matches "ut" for any occurence of ut in a base
	# so for example ukut, ut, and uten would all be matched
	for e in endings:
			#strip everything that doesn't need calculated
			parenClose = string.find(e, ')') + 1
			postEnd = e[parenClose:]
			wordEnd = -1 * len(postEnd)

			colon = string.find(e, ":")
			hasColon = colon > -1
			if hasColon:
				# test for velar dropping
				for ve in grammar.Postbase.getVelarDropPostbases(e):
					parenClose = string.find(ve, ')') + 1
					postEnd = ve[parenClose:]
					wordEnd = -1 * len(postEnd)
					if word[wordEnd:] == postEnd:
						postbase = ve
						break	
			elif word[wordEnd:] == postEnd:
				postbase = e
				break
	return postbase

def print_verb_type(postbase):
	# skip fps for now because it contains velar dropping
	if postbase == fpd_ending:
		print("Verb Type:\t\tFirst Person Dual")
	elif postbase == fpp_ending:
		print("Verb Type:\t\tFirst Person Plural")
	elif postbase == sps_ending:
		print("Verb Type:\t\tSecond Person Singular")
	elif postbase == spd_ending:
		print("Verb Type:\t\tSecond Person Dual")
	elif postbase == spp_ending:
		print("Verb Type:\t\tSecond Person Plural")
	elif postbase == tps_ending:
		print("Verb Type:\t\tThird Person Singular")
	elif postbase == tpd_ending:
		print("Verb Type:\t\tThird Person Dual")
	elif postbase == tpp_ending:
		print("Verb Type:\t\tThird Person Plural")
	elif postbase == '':
		print("Verb Type:\t\tBase")
	else:
		for ve in grammar.Postbase.getVelarDropPostbases(fps_ending):
			if ve == postbase:
				print("Verb Type:\t\tFirst Person Singular")
				break

def apply_ending(word, postbase):
	grammar.Postbase.stripPostbase(word, postbase)
	
def prompt_verbs():
	input = ''
	print("")
	print("Type the word \"exit\" at any time to quit the program")
	print("\n\n")
	while not input == "exit":
		input = raw_input("Please input a word: ")
		if input == 'exit':
			break

		print("\n")
		print(input)

		ending = detect_verb_postbase(input)
		print_verb_type(ending)
		apply_ending(input, ending)

prompt_verbs()
print("")
print("")
