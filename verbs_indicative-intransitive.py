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
					#print("velarpostbase: %s" % ve)
					#print(word[wordEnd:])
					#print(postEnd)
					if word[wordEnd:] == postEnd:
						postbase = ve
						print("Selecting postbase %s" % postbase)
						break	
			elif word[wordEnd:] == postEnd:
				postbase = e
				break
	return postbase

def detect_verb_type(word):
	postbase = detect_verb_postbase(word)
	vt = 'base'
	if postbase == fps_ending:
		vt = "fps"
	elif postbase == fpd_ending:
		vt = "fpd"
	elif postbase == fpp_ending:
		vt = "fpp"
	elif postbase == sps_ending:
		vt = "sps"
	elif postbase == spd_ending:
		vt = "spd"
	elif postbase == spp_ending:
		vt = "spp"
	elif postbase == tps_ending:
		vt = "tps"
	elif postbase == tpd_ending:
		vt = "tpd"
	elif postbase == tpp_ending:
		vt = "tpp"
	else:
		for ve in grammar.Postbase.getVelarDropPostbases(fps_ending):
			if ve == postbase:
				vt = ve
				break
	return vt

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

		type = detect_verb_type(input)

		print("\n")
		print(input)
		if type == "fps":
			ending = fps_ending
			print("Verb Tense:\t\tFirst Person Singular")
		elif type == "fpd":
			ending = fpd_ending
			print("Verb Tense:\t\tFirst Person Dual")
		elif type == "fpp":
			ending = fpp_ending
			print("Verb Tense:\t\tFirst Person Plural")
		elif type == "sps":
			ending = sps_ending
			print("Verb Tense:\t\tSecond Person Singular")
		elif type == "spd":
			ending = spd_ending
			print("Verb Tense:\t\tSecond Person Dual")
		elif type == "spp":
			ending = spp_ending
			print("Verb Tense:\t\tSecond Person Plural")
		elif type == "tps":
			ending = tps_ending
			print("Verb Tense:\t\tThird Person Singular")
		elif type == "tpd":
			ending = tpd_ending
			print("Verb Tense:\t\tThird Person Dual")
		elif type == "tpp":
			ending = tpp_ending
			print("Verb Tense:\t\tThird Person Plural")
		else:
			# word is a base or the result of velar dropping
			ending = ""
			for ve in grammar.Postbase.getVelarDropPostbases(fps_ending):
				print("ve = %s" % ve)
				print("type = %s" % ending)

				if ve == type:
					ending = ve
					print("ending = %s" % ending)
					break
			if not ending == "":
				print("Verb contains velar dropping")
			else:
				print("Verb Tense:\t\tBase")

		apply_ending(input, ending)

#tps_test()
prompt_verbs()
print("")
print("")
