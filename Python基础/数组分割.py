#分割字符

## filter()会生成一个<filter  object at 0x00000208DAC98400>
str  = "aa bbb  cc d"
str_list = filter(None,str.split(" "))
print(str_list)

#这种方法会产生空的分割项 ['aa', 'bbb', '', 'cc', 'd']
str_list = str.split(" ")
print(str_list)

str_list = str.split()
print(str_list)