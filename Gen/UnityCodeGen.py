
from Gen.CodeGen import CodeGen
from Config import UNITY_TABLE_CODE_DIR
from Config import UNITY_TABLE_CODE_EXT
from Config import EXCEL_DIR
from Config import EXCEL_EXT
import os


class UnityCodeGen(CodeGen):
	# 代码生成函数
	def process(self, filename, fields, table):
		# 创建输出路径
		path = filename.replace(EXCEL_DIR, "")
		path = UNITY_TABLE_CODE_DIR + path
		path = os.path.splitext(path)[0]
		path = path + UNITY_TABLE_CODE_EXT

		# 生成文件目录, 不重复创建目录
		filedir = os.path.dirname(path)
		if os.path.exists(filedir) == False:
			os.makedirs(filedir)

		# 填充内容
		filecontent = ""
		filecontent += "using System.Collections.Generic;\n"
		filecontent += "using System.IO;\n"
		filecontent += "using System.Text;\n"
		filecontent += "using UnityEngine;\n"
		filecontent += "\n"

		tablename = os.path.basename(path)
		tablename = tablename.split(".")[0] + "Config"
		filecontent += "public class " + tablename + "\n"
		filecontent += "{\n"

		for index in fields:
			fieldtype = table.cell(2, index).value
			fieldname = table.cell(3, index).value
			filecontent += "	public " + fieldtype + " " + fieldname + ";\n"

		filecontent += "	public " + tablename + "(string line)\n"
		filecontent += "	{\n"
		
		filecontent += "	}\n"

		filecontent += "}\n"
		filecontent += "\n"

		# 保存
		file = open(path, "wb")
		file.write(filecontent.encode())
		file.close()
