import string
import grammar
import ydict

# COMMAND LIST
#
# exit,	x	-	ends the session
# quit,	q	-	ends the session
# list,	l	-	list
# dump,	d	-	dumps all available info for a word
# help,	h,?	-	list help information for [command]
#  red,	r	-	output all information in Red Dictionary format
# stress	-	print the stress pattern for [word]
#  spell	-	print the spelling for [word]
#    syl	-	print syllables for [word]
#   rlen	-	print rhythmic vowel length for [word]
#   apos	-	print the purpose for the first apostrophe
#    voi	-	print the voicing for each letter in [word]
#    def	-	print the definitions for [word]

# TODO? webcmd - used to dump web services info?

# TODO add readline support

dict_prompt = 'dict> '

def dump(word):
	pass

def print_header(word):
	print
	print(word)
	print('-' * len(word))
	print

def print_apostrophe_purpose(word):
	print_header(word)
	print('PURPOSE OF FIRST APOSTROPHE')
	print '\t',

	if string.find(word, '\''):
		if grammar.Word.apostrophePurpose(word) == grammar.Word.APOS_GEMINATION_MARKER:
			print('gemination marker')
		elif grammar.Word.apostrophePurpose(word) == grammar.Word.APOS_NG_SEPARATOR:
			print('separates \'n\' and \'g\'')
		elif grammar.Word.apostrophePurpose(word) == grammar.Word.APOS_PREVENT_DEVOICING:
			print('prevents automatic devoicing')
		elif grammar.Word.apostrophePurpose(word) == grammar.Word.APOS_PREVENT_GEMMINATION:
			print('prevents automatic gemination')
		elif grammar.Word.apostrophePurpose(word) == grammar.Word.APOS_DISRUPT_STRESS:
			print('marks disruption of normal stress pattern')
		elif grammar.Word.apostrophePurpose(word) == grammar.Word.APOS_SHORT_WORD:
			print('indicates word has been shortened')
		else:
			print('ERROR: invalid use of apostrophe')
	else:
		print('no apostrophe found')


def print_definitions(word):
	print_header(word)
	print('DEFINITIONS')
	print '\t',
	defs = ''
	ddef = ydict.Dictionary.getDefinitions(word)

	if ddef:
		defs = '; '.join(ddef)
	else:
		defs = 'WARNING: word found in dictionary'

	print(defs)

def print_voicing(word):
	print_header(word)
	print('VOICING')
	print '\t',
	print(grammar.Word.getVoicingText(word))


def print_rhythmic_length(word):
	print_header(word)
	print('RHYTHMIC VOWEL LENGTH')
	print '\t',
	print(grammar.Word.getRhythmicVowelLengthText(word))


def print_syllables(word):
	print_header(word)
	print('SYLLABLES')
	print '\t',
	print(grammar.Word.getSyllableText(word))


def print_spell(word):
	print_header(word)
	print('SPELLING')
	exp = grammar.Base.explode(word)
	print '\t',
	print(exp)

def print_stress(word):
	print_header(word)
	print('STRESS:')
	#spat = grammar.Word.getStressPattern(word)
	#syls = grammar.Word.getSyllables(word)

	#stress = ''
	#stxt = ''
	#for i in range(len(syls)):
	#	sz = len(syls[i])
	#	if spat[i]:
	#		stxt = (' ' * (sz -1)) + '\''
	#	else:
	#		stxt = ' ' * (sz)
	#	stress = stress + '\t' + stxt + '\t/'
	#	stxt = ''
	#stress = stress[1:-2]
	#print '\t',
	#print(stress)
	#print '\t',
	#print(grammar.Word.getSyllableText(word))
	print '\t',
	print(grammar.Word.getStressText(word))

def parse_cmd(line):
	cmd_parts = str.split(line)
	cmd = str.strip(cmd_parts[0].lower())
	args = cmd_parts[1:]

	if cmd == 'spell':
		print_spell(args[0])
	elif cmd == 'stress':
		print_stress(args[0])
	elif cmd == 'syl' or cmd == 'syllables':
		print_syllables(args[0])
	elif cmd == 'rlen' or cmd == 'rhythmic_length':
		print_rhythmic_length(args[0])
	elif cmd == 'apos' or cmd == 'apostrophe':
		print_apostrophe_purpose(args[0])
	elif cmd == 'voi' or cmd == 'voicing':
		print_voicing(args[0])
	elif cmd == 'def' or cmd == 'definitions':
		print_definitions(args[0])
	elif cmd == 'q' or cmd == 'x' or cmd == 'quit' or cmd == 'exit':
		exit()

def start_shell():
	usr_in = ''
	print('Yup\'ik Dictionary Shell\n-----------------------\n\n')
	print("Type the word \"exit\" at any time to quit the program")
	print("\n\n")
	while not usr_in == "exit":
		usr_in = raw_input(dict_prompt)
		parse_cmd(usr_in)

		print("\n")

if __name__ == '__main__':
	start_shell()
