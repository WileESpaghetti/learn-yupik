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
#	  ex	-	print the examples for [word]
#	 add	- 	starts the add word wizard

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
	print('PURPOSE OF FIRST APOSTROPHE')
	print '\t',

	if string.find(word, '\'') > -1:
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


def print_examples(word):
	print ('EXAMPLES')
	ex = ''
	wid = ydict.Dictionary.getWordID(word)
	if wid:
		examples = ydict.Dictionary.getExamplesByID(wid)
		for e in examples:
			ex += '\t%s\n' % e['example']
			ex += '\t\t%s\n\n' % e['translation']
		ex = ex[:-2]
	else:
		ex = '\tWARNING: word not found in dictionary'
	print ex

def print_definitions(word):
	print('DEFINITIONS')
	print '\t',
	defs = ''
	ddef = ydict.Dictionary.getDefinitions(word)

	if ddef:
		defs = '; '.join(ddef)
	else:
		defs = 'WARNING: word not found in dictionary'

	print(defs)

def print_voicing(word):
	print('VOICING')
	print '\t',
	print(grammar.Word.getVoicingText(word))


def print_rhythmic_length(word):
	print('RHYTHMIC VOWEL LENGTH')
	print '\t',
	print(grammar.Word.getRhythmicVowelLengthText(word))


def print_syllables(word):
	print('SYLLABLES')
	print '\t',
	print(grammar.Word.getSyllableText(word))


def print_spell(word):
	print('SPELLING')
	exp = grammar.Base.explode(word)
	print '\t',
	print(exp)

def print_stress(word):
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


def print_kitchen_sink(word):
	print_definitions(word)
	print_examples(word)
	print_spell(word)
	print_syllables(word)
	print_stress(word)
	print_rhythmic_length(word)
	print_voicing(word)
	print_apostrophe_purpose(word)

def add_definition():
	#FIXME ideally this would all get spell checked
	print('\n\tEnter definitions below')
	defs = []
	def_in = raw_input('\t\tdefinition> ')
	while def_in:
		defs.append(def_in)
		def_in = raw_input('\t\tdefinition> ')
	return defs


def add_examples():
	#FIXME ideallyt this would all get spell checked
	print('\n\tEnter an example usage of the word below')
	exam = []
	ex_in = raw_input('\t\texample> ')
	while ex_in:
		exam.append(ex_in)
		ex_in = raw_input('\t\texample> ')
	return exam


def add_section():
	#FIXME ideallyt this would all get spell checked
	# FIXME currently exoects input to be id number
	print('\n\tEnter the section the word should go in\n')
	exam = []
	seclist = ydict.Dictionary.getSections()
	#FIXME this might not always be in numerical order
	for i in seclist:
		print(str.format('\t\t{}. {}', i['id'], i['section']))

	# FIXME need to add validation
	# FIXME need to add the abillity to use the id or name
	sec = raw_input('\n\tSection> ')
	return exam


def add_word_wizard(word):
	print('CREATING DICTIONARY ENTRY FOR: %s' % word)

	# TODO for now we don't want to do anything if the word
	# is already in the database. Down the road we may want to
	# give the user the option to update the entry instead
	if not ydict.Dictionary.getWordID(word):
		sect = add_section()
		defs = add_definition()
		exam = add_examples()
	else:
		print('\tERROR: can not add %s. Entry already exists' % word)


def parse_cmd(line):
	cmd_parts = str.split(line)
	cmd = str.strip(cmd_parts[0].lower())
	args = cmd_parts[1:]

	print_header(args[0])
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
	elif cmd == 'ex' or cmd == 'examples':
		print_examples(args[0])
	elif cmd == 'kitchen_sink' or cmd == 'sink':
		print_kitchen_sink(args[0])
	elif cmd == 'add':
		add_word_wizard(args[0])
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
