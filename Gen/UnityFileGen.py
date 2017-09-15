
from Gen.FileGen import FileGen


class UnityFileGen(FileGen):

	# 文件生成函数
	def process(self, filename):
		print("UnityFileGen : " + filename)
