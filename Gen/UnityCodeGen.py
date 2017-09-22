
from Gen.CodeGen import CodeGen
from Config import KEY_MODIFIER_NAME
from Config import UNITY_TABLE_CODE_DIR
from Config import UNITY_TABLE_CODE_EXT
from Config import UNITY_CONFIGMANAGER_FILENAME
from Config import EXCEL_DIR
import os


class UnityCodeGen(CodeGen):
	def __init__(self):
		self.mFileContent = ""

	# 代码生成函数
	def process(self, filename, fields, table):
		# -----------------------table cfg class-----------------------

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
		self.mFileContent = ""
		self.mFileContent += "using System.Collections.Generic;\n"
		self.mFileContent += "using System.IO;\n"
		self.mFileContent += "using System.Text;\n"
		self.mFileContent += "using UnityEngine;\n"
		self.mFileContent += "\n"

		# table class
		tablebasename = os.path.basename(path)
		tablebasename = tablebasename.split(".")[0]
		tablename = tablebasename + "Cfg"
		self.mFileContent += "public class " + tablename + "\n"
		self.mFileContent += "{\n"

		for index in fields:
			fielddesc = table.cell(0, index).value
			fieldtype = table.cell(2, index).value
			fieldname = table.cell(3, index).value
			fieldtype = fieldtype.lower()
			self.mFileContent += "	public " + fieldtype + " " + fieldname + ";"
			self.mFileContent += "			//		" + fielddesc + "\n"

		self.mFileContent += "\n"
		self.mFileContent += "	public " + tablename + "(string line)\n"
		self.mFileContent += "	{\n"
		self.mFileContent += "		string []fields = line.Split('\t');\n"

		# 解析字段
		for index in fields:
			fieldtype = table.cell(2, index).value
			fieldname = table.cell(3, index).value
			fieldtype = fieldtype.lower()
			self.parse_fieldtype(fieldtype, fieldname, index)

		self.mFileContent += "	}\n"
		self.mFileContent += "}\n"
		self.mFileContent += "\n"

		# -----------------------table cfg manager class-----------------------

		# 获得keylist
		keylist = []
		for index in fields:
			value = table.cell(4, index).value
			if value == KEY_MODIFIER_NAME:
				keylist.append(index)

		tablemgrname = tablename + "Manager";
		format = "{0}.txt"
		self.mFileContent += "public class " + tablemgrname + "\n"
		self.mFileContent += "{\n"

		# 根据keylist判断
		uselist = (keylist.__len__() != 1)
		if uselist:
			self.mFileContent += "	private List<" + tablename + "> mList = new List<" + tablename + ">();\n"
		else:
			self.mFileContent += "	private Dictionary<int, " + tablename + "> mDict = new Dictionary<int, " + tablename + ">();\n"

		self.mFileContent += "\n"
		self.mFileContent += "	public void InitTable()\n"
		self.mFileContent += "	{\n"
		self.mFileContent += "		string tableDir = PathUtil.GetTableDataPath();\n"
		self.mFileContent += "		string tableName = \"" + tablename + "\";\n"
		self.mFileContent += "		string path = string.Format(\"{0}{1}.txt\", tableDir, tablename);\n "	#	引号里面有引号的用法
		self.mFileContent += "		StreamReader sr = new StreamReader(path, Encoding.UTF8);\n"
		self.mFileContent += "		string line;\n"
		self.mFileContent += "\n"
		self.mFileContent += "		while ((line = sr.ReadLine()) != null)\n"
		self.mFileContent += "		{\n"
		self.mFileContent += "			line = line.Trim();\n"
		self.mFileContent += "			if (line.Length > 0)\n"
		self.mFileContent += "			{\n"
		self.mFileContent += "				" + tablename + " rowdata = new " + tablename + "(line);\n"

		# 根据keylist判断
		if uselist:
			self.mFileContent += "				mList.Add(" "rowdata);\n"
		else:
			self.mFileContent += "				mDict.Add(rowdata." + table.cell(3, 0).value + ", rowdata);\n"

		self.mFileContent += "			}\n"
		self.mFileContent += "			else\n"
		self.mFileContent += "			{\n"
		self.mFileContent += "				continue;\n"
		self.mFileContent += "			}\n"
		self.mFileContent += "		}\n"
		self.mFileContent += "	}\n"

		# 生成生成数据函数
		self.gen_gendatafunc(table, tablename, keylist)

		self.mFileContent += "\n"
		self.mFileContent += "	private " + tablemgrname + "() { }\n"
		self.mFileContent += "\n"
		self.mFileContent += "	public static readonly " + tablemgrname + " Instance = new " + tablemgrname + "();\n"

		self.mFileContent += "}\n"

        # 保存
		file = open(path, "wb")
		file.write(self.mFileContent.encode())
		file.close()

	# 解析字段类型
	def parse_fieldtype(self, fieldtype, fieldname, index):
		if fieldtype == "int" or fieldtype == "float" or fieldtype == "string":
			self.mFileContent += "		" + fieldname + " = " + fieldtype + ".Parse(fields[" + str(index) + "])\n"

	# 生成生成数据函数
	def gen_gendatafunc(self, table, tablename, keylist):
		keylen = keylist.__len__()
		if keylen == 0:		# 没有key值没有生成函数
			return;
		elif keylen == 1:	# 有一个key值使用dict取值
			keytype = table.cell(2, keylist[0]).value
			keytype = keytype.lower()
			self.mFileContent += "\n"
			self.mFileContent += "	public " + tablename + " GetDataByID(" + keytype + " id)\n"
			self.mFileContent += "	{\n"
			self.mFileContent += "		" + tablename + " rowdata = null;\n"
			self.mFileContent += "		mDict.TryGetValue(id, out rowdata);\n"
			self.mFileContent += "		return rowdata;\n"
			self.mFileContent += "	}\n"
		else:
			self.mFileContent += "\n"

			self.mFileContent += "	public " + tablename + " GetDataByID("
			for keyindex in keylist:
				keytype = table.cell(2, keyindex).value
				keytype = keytype.lower()
				keyval = table.cell(3, keyindex).value
				self.mFileContent += keytype + " _" + keyval
				if keyindex != (keylen - 1):
					self.mFileContent += ", "
			self.mFileContent += ")\n"

			self.mFileContent += "	{\n"
			self.mFileContent += "		foreach (" + tablename + " data in mList)\n"
			self.mFileContent += "		{\n"

			self.mFileContent += "			if ("
			for keyindex in keylist:
				keyval = table.cell(3, keyindex).value
				self.mFileContent += "data." + keyval + " == _" + keyval
				if keyindex != (keylen - 1):
					self.mFileContent += " && "
			self.mFileContent += ")\n"

			self.mFileContent += "			{\n"
			self.mFileContent += "				return data;\n"
			self.mFileContent += "			}\n"
			self.mFileContent += "		}\n"
			self.mFileContent += "\n"
			self.mFileContent += "		return null;\n"
			self.mFileContent += "	}\n"

	# 生成配置管理类
	@staticmethod
	def gen_configmangercode(files):
		path = UNITY_TABLE_CODE_DIR + UNITY_CONFIGMANAGER_FILENAME + UNITY_TABLE_CODE_EXT

		filecontent = ""
		filecontent += "using System.Collections;\n"
		filecontent += "using System.Collections.Generic;\n"
		filecontent += "using UnityEngine;\n"
		filecontent += "\n"
		filecontent += "public class " +  UNITY_CONFIGMANAGER_FILENAME + "\n"
		filecontent += "{\n"
		filecontent += "	public static void Load()\n"
		filecontent += "	{\n"
		for file in files:
			tablename = os.path.basename(file)
			tablename = tablename.split(".")[0]
			tablename += "Cfg"
			filecontent += "		" +	tablename + "Manager.Instance.InitTable();\n"
		filecontent += "	}\n"
		filecontent += "}\n"

		# 保存
		file = open(path, "wb")
		file.write(filecontent.encode())
		file.close()


