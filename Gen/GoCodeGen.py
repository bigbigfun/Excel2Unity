
from Gen.CodeGen import CodeGen
from Config import EXCEL_DIR
from Config import SERVER_TABLE_ROOT_DIR
from Config import SERVER_TABLE_CODE_DIR
from Config import SERVER_GO_CODE_TYPE
from Config import SERVER_CODE_TYPE
from Config import SERVER_GO_CODE_EXT
import os

class GoCodeGen(CodeGen):
	# 构造函数
	def __init__(self):
		self.mFileContent = ""

	# 代码生成函数
	def process(self, filename, fields, table):
		# 创建输出路径
		path = filename.replace(EXCEL_DIR, "")
		path = SERVER_TABLE_ROOT_DIR + SERVER_TABLE_CODE_DIR + path
		path = os.path.splitext(path)[0]
		path = path + self.getServerCodeExt()

		# 生成文件目录, 不重复创建目录
		filedir = os.path.dirname(path)
		if os.path.exists(filedir) == False:
			os.makedirs(filedir)

		# 保存
		file = open(path, "wb")
		file.write(self.mFileContent.encode())
		file.close()

	# 获取服务器后缀
	def getServerCodeExt(self):
		if SERVER_GO_CODE_TYPE == SERVER_CODE_TYPE:
			return SERVER_GO_CODE_EXT

		return SERVER_GO_CODE_EXT









