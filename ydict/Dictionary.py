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


# other sections
# word lists
# tags? - might be useful for creating word lists

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


# FIXME this needs to test for openshift_data_dir and set default
# value if not found
def openDictionary():
	dbcon = sqlite3.connect('yupik_dictionary.db')
	dbcon.text_factory = str
	c = dbcon.cursor()

	return c


def getSections():
	c = openDictionary()
	sql = "SELECT * FROM sections"

	sections = c.execute(sql)
	secList = []
	for s in sections:
		newSec = {'id': s[0], 'section': s[1]}
		secList.append(newSec)

	return secList

def getSectionNames():
	c = openDictionary()
	sql = "SELECT name FROM sections"

	sections = c.execute(sql)
	secList = []
	for s in sections:
		secList.append(s[0])

	return secList


## WORD CLASS

## id ##

def getID(word):
	pass

## type ##

def getType(wtype):
	pass


def getTypeID(id):
	pass


## section ##

def getSectionID(section):
	pass


def getSection(id):
	pass


## dialect
## parent

## citattion_form

def getWord(id):
	pass


## base_form



## definitions

def getDefinitions(word):
	c = openDictionary()

	sql = 'select "definition" from "definitions" as def where (select "id" from "words" as w where "citation_form" = "%s" and def.word = w.id)' % word
	definitions = c.execute(sql)
	defs = []
	for d in definitions:
		defs.append(d[0])

	return defs

def getDefinitionsByID(id):
	pass


def getDefinitionsByID(word):
	pass

## examples
def getExamplesByID(id):
	pass


def getExamples(word):
	pass


## spelling
## syllables
## gemination
## stress
## apostrophe purpose
## voicing
## vowel_length

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
