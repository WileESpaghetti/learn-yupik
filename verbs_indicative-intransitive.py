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
	for e in endings:
			#strip everything that doesn't need calculated
			parenClose = string.find(e, ')') + 1
			postEnd = e[parenClose:]
			if string.rfind(word, postEnd) > -1:
				postbase = e
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

	return vt

def apply_ending(word, postbase):
	print("\n")
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

		if type == "tps":
			ending = tps_ending

		apply_ending(input, ending)
	print("")

#tps_test()
prompt_verbs()
print("")
print("")
