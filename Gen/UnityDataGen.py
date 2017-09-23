
from Config import EXCEL_DIR
from Config import UNITY_TABLE_ROOT_DIR
from Config import UNITY_TABLE_DATA_DIR
from Config import UNITY_TABLE_DATA_EXT
from Gen.DataGen import DataGen
import os;


class UnityDataGen(DataGen):

	# 文件生成函数
	def process(self, filename, fields, table):
		# 创建输出路径
		path = filename.replace(EXCEL_DIR, "")
		path = UNITY_TABLE_ROOT_DIR + UNITY_TABLE_DATA_DIR + path
		path = os.path.splitext(path)[0]
		path += UNITY_TABLE_DATA_EXT

		# 生成文件目录, 不重复创建目录
		filedir = os.path.dirname(path)
		if os.path.exists(filedir) == False:
			os.makedirs(filedir)

		# 生成数据
		fileContent = ""
		for row in range(5, table.nrows):
			for col in range(table.ncols):
				if col in fields:
					fileContent += ("{0}\t").format(table.cell(row, col).value)

			fileContent += "\n"

		# 保存
		file = open(path, "wb")
		file.write(fileContent.encode())
		file.close()
