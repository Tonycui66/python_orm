import os
from DAY.day1.test_web.main import *
dirname = os.path.dirname(__file__)
template = os.path.join(dirname, "templates")
class GenHtml():
	def __init__(self):
		"""

		"""
		self.main_html = "%s/index.html"%template
		self.view_html = "%s/view.html"%template
		self.save_html = "%s/save.html"%template
		self.edit_html = "%s/edit.html"%template
		self.gen_main_html
	## main html
	@property
	def gen_main_html(self):
		"""

		:return:
		"""
		with open(self.main_html,"w",encoding="gbk") as f:
			f.write(Message())

	## view html
	@property
	def gen_view_html(self):
		"""

		:return:
		"""
		with open(self.view_html,"w",encoding="gbk") as f:
			f.write(view())


	## save html
	@property
	def gen_save_html(self):
		"""

		:return:
		"""
		print(self.save_html)
		with open(self.save_html,"w",encoding="gbk") as f:
			f.write(save())

	## edit html
	@property
	def gen_edit_html(self):
		"""

		:return:
		"""
		with open(self.edit_html,"w",encoding="gbk") as f:
			f.write(edit())
