# Excel2Unity
* 目标功能

    * 导出txt文本文件以及生成各个语言的解析版本(针对客户端和服务器)
    
* 目前功能 
    * 导出txt文本文件并生成相应的解析代码到unity(客户端)
    
* 使用方法

    打开`Config.py`文件, 修改几个配置属性
    
    ```cs
    #Unity输出根目录
    UNITY_TABLE_ROOT_DIR = "./TestTable/Assets/"
    
    # Unity数据目录
    UNITY_TABLE_DATA_DIR = "GameData/TableData/"
    
    # Unity代码目录
    UNITY_TABLE_CODE_DIR = "Scripts/Table/"   
    ```
    