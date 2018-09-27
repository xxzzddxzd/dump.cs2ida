# dump.cs2ida
恢复Unity可执行文件的Unity符号表
dump.cs由Il2CppDumper生成

# 使用
IDA中File->Script file载入py文件
下方python行中输入main('文件名')
如main('c:\dump.cs')

# 问题
两个相同name的class，后面的class命名时会出现重名然后无法命名的问题
