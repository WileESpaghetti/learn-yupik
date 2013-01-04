#!python
#encoding: utf-8
import grammar, string

""" used for printing out information about an inputted word """

def print_syllables(input):
	syl = ''
	for i in grammar.Word.getSyllables(input):
		syl = syl + '\t' + ''.join(i) + '\t/'
	print(syl)

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
		print_syllables(input)
		print_apos(input)

prompt_verbs()
print("")
print("")
