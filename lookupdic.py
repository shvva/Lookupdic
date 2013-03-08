# lookupdic - Look up the words with Multiple Selections by means of alc EIJIRO on the web
#        a word on the cursor would be refered in case of no selection

import sublime, sublime_plugin, webbrowser, urllib

# URL to alc EIJIROweb
EIJIRO_URL = 'http://eow.alc.co.jp/search?q='

def lookupweb(str):
	webbrowser.open_new_tab(EIJIRO_URL + urllib.quote_plus(str.encode('utf-8', 'ignore')))

class lookupdicCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		str = ''
		regions = self.view.sel()
		if regions[0].empty():
			str = self.view.substr(self.view.word(regions[0]))
		else:
			for region in regions:
				str = str + self.view.substr(region) + ' '

		lookupweb(str)
