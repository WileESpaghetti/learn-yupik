# Red Dictionary has 4 sections:
# bases
#	nouns
#	demonstrative pronouns
#	demonstrative adverbs
#	positional bases
#	verbs
#	exclamations
#	adverbs
#	interogatives
#	roots
# postbases
# endings
# enclitics

# Red Dictionary Entry Sections
# citation form
# word annotations
# 	part of speech
# 	redirects
# 	dialect
# 	pluarlitry
# 	misc symbols
# 	immative
# 	loan word
#	synonyms
# definition
# subentries
# polarity (verbs only)
# analytic info
# unknown data
# break down

# Description of dictionary entry format
#FIXME need section for dialects, alternate spellings
# WORD: (PRONUNCIATION/SYLLABLES?)
# 1. (PART(s) OF SPEECH) DEFINITION
# 2. (PART(s) OF SPEECH) DEFINITION
# ...
#
# Examples:
# 1. EXAMPLE 1
# 2. EXAMPLE 2
# ...
#
#	SUB-ENTRIES

# Base Example
#

# classes
# Dictionary.Entry
import sqlite3
import json
import grammar



def getDefinitions(word):
	dbcon = sqlite3.connect('yupik_dictionary.db')
	dbcon.text_factory = str
	c = dbcon.cursor()

	sql = 'select "definition" from "definitions" as def where (select "word_id" from "words" as w where "citation_form" = "%s" and def.word = w.word_id)' % word
	definitions = c.execute(sql)
	defs = []
	for d in definitions:
		defs.append(d[0])

	return defs

def getEntry(word):
	e = {"word" : word}
	e['definitions'] = getDefinitions(word)
	e['syllables'] = grammar.Word.getSyllableText(word)
	e['gemmination'] = grammar.Word.getAutoGemminationPattern(word)
	e['stress'] = grammar.Word.getStressPattern(word)
	e['apostrophe'] = grammar.Word.apostrophePurpose(word)
	e['spelling'] = grammar.Base.explode(word)
	e['syllables2'] = grammar.Word.getSyllables(word)
	e['voicing'] = grammar.Word.getVoicingPattern(word)
	e['vowel_length'] = grammar.Word.getRhythmicVowelLengthPattern(word)
	return e

def getEntryJSON(word):
	return json.JSONEncoder().encode(getEntry(word))
