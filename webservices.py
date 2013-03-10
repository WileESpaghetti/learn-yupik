__author__ = 'Lehman'
import web
import grammar
import json
import sqlite3

urls = (
	"/syllables/(.*)", "syllables",
   "/words/(.*)", "words"
)

class syllables:
	def GET(self, word):
		return json.JSONEncoder().encode(grammar.Word.getSyllables(word))


class words:
	def GET(self, word):
		dbcon = sqlite3.connect('yupik_dictionary.db')
		dbcon.text_factory = str
		c = dbcon.cursor()

		pb = '['
		index = 0
		for row in c.execute('select "definition" from "definitions" as def where (select "word_id" from "words" as w where "citation_form" = "%s" and def.word = w.word_id)' % word):
			if index == 0:
				pb += '"%s"' % row
			else:
				pb += ',"%s"' % row
			index += 1
		else:
			pb += ']'
		print pb
		return '<html><head><title></title><script src="http://code.jquery.com/jquery-1.9.1.min.js"></script><script>console.log($.parseJSON(\'[{"word":"%s", "definitions":%s}]\'));</script></head><body></body></html>' % (word, pb)


if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()