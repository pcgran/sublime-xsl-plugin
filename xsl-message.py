import sublime, sublime_plugin

class XslMessageCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, self.view.sel()[0].begin(), '<xsl:message>variable<xsl:value-of select="$variable"/></xsl:message>')