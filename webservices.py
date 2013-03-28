__author__ = 'Lehman'
import json
import web
import grammar
import dict


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


app = web.application(urls, globals()).wsgifunc()

if __name__ == "__main__":
	web.runwsgi(app)