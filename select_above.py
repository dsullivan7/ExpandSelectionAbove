import sublime, sublime_plugin

class SelectAboveCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		curr_1 = self.view.sel()[0].begin()
		curr_2 = self.view.sel()[-1].end()
		row_1, col_1 = self.view.rowcol(curr_1)
		row_2, col_2 = self.view.rowcol(curr_2)
		if (col_1 == 0 and col_1 != col_2 and row_1 != 0):
			 row = row_1 - 1
		else:
			row = row_1
		line = self.view.line(curr_1)
		end_row, end_col = self.view.rowcol(line.end())
		my_from = self.view.text_point(row , end_col)
		my_to = self.view.text_point(row, 0)
		line = self.view.line(self.view.text_point(5, 3))
		cur_region = self.view.sel()[0]
		self.view.sel().clear()
		self.view.sel().add(cur_region.cover(sublime.Region(my_from, my_to)))
