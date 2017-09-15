
import os
import xlrd
from Config import EXCEL_DIR

class Excel2Unity :
	def __init__(self):
		self.mExcelFiles = []	# 所有的excel文件

	# 外部处理函数
	def process(self):
		self.recursiveSearchExcel(EXCEL_DIR)
		self.processClientExcel()
		self.processServerExcel()
		print(self.mExcelFiles)

	# 递归查找文件
	def recursiveSearchExcel(self, path):
		for dir in os.listdir(path):		# 遍历当前目录
			fullpath = os.path.join(path, dir)

			if (os.path.isdir(fullpath)):
				self.recursiveSearchExcel(fullpath)
			elif(os.path.isfile(fullpath)):
				if (os.path.splitext(fullpath)[1] == ".xlsx"):
					self.mExcelFiles.append(fullpath)

	# 处理客户端的excel文件
	def processClientExcel(self):
		i = 0

	# 处理服务器的excel文件
	def processServerExcel(self):
		i = 0