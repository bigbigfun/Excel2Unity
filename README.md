# Excel2Unity
* 目标功能

    * 导出txt文本文件以及生成各个语言的解析版本(针对客户端和服务器)
    
* 目前功能 
    * 导出txt文本文件并生成相应的解析代码到unity(客户端)
    
* 代码修改

    打开`Config.py`文件, 修改几个配置属性
    
    ```python
    # Unity输出根目录
    UNITY_TABLE_ROOT_DIR = "./TestTable/Assets/"
    
    # Unity数据目录
    UNITY_TABLE_DATA_DIR = "GameData/TableData/"
    
    # Unity代码目录
    UNITY_TABLE_CODE_DIR = "Scripts/Table/"   
    ```
    
    有一个配置行暂时不需要修改, 目前配置文件都默认生成在Resources文件夹下
    ， 通过Resources.Load()加载，资源动态加载还没有完成
    ```python
    # Unity使用资源路径读取
    UINTY_TABLE_USE_RESOURCE_PATH_READ = True
    ```
    
*   Excel配置使用
    
    
    
    