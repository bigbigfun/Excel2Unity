
from Gen.CodeGen import CodeGen


class UnityCodeGen(CodeGen):

	# 代码生成函数
	def process(self, filename, fields):
		print("UnityCodeGen : " + filename + str(fields))
