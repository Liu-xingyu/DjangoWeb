import pymysql

# 在Django的web开发中，如果python使用的3.x版本（3.x版本中的mysql库是pymysql，2.x版本中是MySQLdb），
# 所以需要引用pymysql声明为Django能够识别的版本
pymysql.install_as_MySQLdb()
