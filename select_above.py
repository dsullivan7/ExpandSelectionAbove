import sublime, sublime_plugin

class SelectAboveCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		# get the current start and end of the selection
		curr_1 = self.view.sel()[0].begin()
		curr_2 = self.view.sel()[-1].end()

		#get the current row and column of the start and end of the selection
		row_1, col_1 = self.view.rowcol(curr_1)
		row_2, col_2 = self.view.rowcol(curr_2)

		# if we are at the beginning of the line with a selection and we are
		# not at the very beginning of the file, select the line above
		# otherwise we want to just highlight the first line
		if (col_1 == 0 and (col_1 != col_2 or row_1 != row_2) and row_1 != 0):
			row_to = row_1 - 1
		else:
			row_to = row_1

		my_from = self.view.text_point(row_1 + 1, 0)
		my_to = self.view.text_point(row_to, 0)
		cur_region = self.view.sel()[0]
		self.view.sel().clear()
		self.view.sel().add(cur_region.cover(sublime.Region(my_from, my_to)))
