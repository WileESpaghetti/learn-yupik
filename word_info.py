#!python
#encoding: utf-8
import grammar, string

""" used for printing out information about an inputted word """

def print_syllables(input):
	syl = ''
	for i in grammar.Word.getSyllables(input):
		syl = syl + '\t' + ''.join(i) + '\t/'
	# remove trailing '/'
	syl = syl[:-1]
	print(syl)

def print_rhythmicLength(input):
	length = ''

	rl = grammar.Word.getRhythmicVowelLengthPattern(input)
	for hasLength in rl:
		length = length + '\t'
		if hasLength:
			length = length + '^^\t/'
		else:
			length = length + '  \t/'

def print_voicing(input):
	print("Voicing:")
	exp = grammar.Base.explode(input)
	for i in range(len(exp)):
		if grammar.Alphabet.isNasal(exp[i]) or grammar.Alphabet.isFricative(exp[i]):
			voiced = grammar.Word.isVoiced(input, i)
		else:
			voiced = ''
		print(exp[i] + ": " + str(voiced))

def print_apos(input):
	if string.find(input, '\''):
		if grammar.Word.apostrophePurpose(input) == grammar.Word.APOS_GEMINATION_MARKER:
			print('\' = gemmination')
		elif grammar.Word.apostrophePurpose(input) == grammar.Word.APOS_NG_SEPARATOR:
			print('\' = separate n and g')
		elif grammar.Word.apostrophePurpose(input) == grammar.Word.APOS_PREVENT_DEVOICING:
			print('\' = stops and frics')
		elif grammar.Word.apostrophePurpose(input) == grammar.Word.APOS_PREVENT_GEMMINATION:
			print('\' = prevent gemmination')
		elif grammar.Word.apostrophePurpose(input) == grammar.Word.APOS_DISRUPT_STRESS:
			print('\' = stress pattern')
		elif grammar.Word.apostrophePurpose(input) == grammar.Word.APOS_SHORT_WORD:
			print('\' = end chopped')

def print_stress(input):
	print(grammar.Word.getStressPattern(input))


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
		print(grammar.Base.explode(input))
		print_rhythmicLength(input)
		print_syllables(input)
		print_apos(input)
		print_voicing(input)
		print_stress(input)

prompt_verbs()
print("")
print("")
