import sublime
import sublime_plugin
import webbrowser
import os
import subprocess

class ExampleCommand(sublime_plugin.TextCommand):

	def run(self, edit, **args):
		window = sublime.active_window()
		folders = window.folders()
		file_path = self.view.file_name()
		path, file = os.path.split(file_path)
		folder_list = folders[0]
		settings = sublime.load_settings('bitlink.sublime-settings')
		remote = settings.get('remote')

		new_list = file_path[len(folder_list):]

		(row,col) = self.view.rowcol(self.view.sel()[0].begin())

		url = remote +'/src/default'+new_list + '?at=default&fileviewer=file-view-default#'+file+'-'+str(row+1)
		blame = remote +'/annotate/default'+new_list + '?at=default&fileviewer=file-view-default#'+file+'-'+str(row+1)

		if (args['open']) :
			webbrowser.open_new_tab(url)

		if (args['copy']) :
			sublime.set_clipboard(url);

		if (args['blame']) :
			webbrowser.open_new_tab(blame)