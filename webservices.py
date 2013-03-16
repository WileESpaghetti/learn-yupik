__author__ = 'Lehman'
import web
import grammar
import json
import dict
import sqlite3

urls = (
	"/syllables/(.*)", "syllables",
	"/word_info/(.*)", "word_info",
	"/entry/(.*)", "Entry"
)


class word_info:
	def GET(self, word):
		return dict.Dictionary.getEntryJSON(word)


class syllables:
	def GET(self, word):
		return json.JSONEncoder().encode(grammar.Word.getSyllables(word))


if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()