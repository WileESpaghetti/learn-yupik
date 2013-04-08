import grammar

# COMMAND LIST
#
# exit,	x	-	ends the session
# quit,	q	-	ends the session
# list,	l	-	list
# dump,	d	-	dumps all available info for a word
# help,	h,?	-	list help information for [command]
#  red,	r	-	output all information in Red Dictionary format

# TODO? webcmd - used to dump web services info?

# TODO add readline support

dict_prompt = 'dict> '

def dump(word):
	pass

def print_stress(word):
	print('\n')
	print(word)
	print('-' * len(word))
	print('\nSTRESS:')

def parse_cmd(line):
	cmd_parts = str.split(line)
	cmd = str.strip(cmd_parts[0].lower())
	args = cmd_parts[1:]

	if cmd == 'stress':
		print_stress(args[0])
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
		#print(grammar.Base.explode(usr_in))
		#print_rhythmicLength(input)
		#print_syllables(input)
		#print_apos(input)
		#print_voicing(input)
		#print_stress(input)
		#print_definition(input)

if __name__ == '__main__':
	start_shell()
