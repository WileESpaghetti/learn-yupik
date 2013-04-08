__author__ = 'Lehman'
#!/usr/bin/python
import os
import json
import web
import grammar
import ydict

#virtenv = os.environ['APPDIR'] + '/virtenv/'
#os.environ['PYTHON_EGG_CACHE'] = os.path.join(virtenv, 'lib/python2.6/site-packages')
#virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
#try:
#	execfile(virtualenv, dict(__file__=virtualenv))
#except IOError:
#	pass

urls = (
	"/syllables/(.*)", "syllables",
	"/word_info/(.*)", "word_info",
	"/entry/(.*)", "Entry",
	"/sections", "Sections"
)


class word_info:
	def GET(self, word):
		return ydict.Dictionary.getEntryJSON(word)


class syllables:
	def GET(self, word):
		return json.JSONEncoder().encode(grammar.Word.getSyllables(word))


class Sections:
	def GET(self):
		return json.JSONEncoder().encode(ydict.Dictionary.getSections())


# this variable needs to remain "application" in order to be run from openshift
application = web.application(urls, globals()).wsgifunc()

if __name__ == "__main__":
	web.runwsgi(application)