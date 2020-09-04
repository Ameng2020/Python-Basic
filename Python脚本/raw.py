#变量字符串转义替换函数

'''
在我们日常使用中经常会遇到转义问题，一般字符串的转义直接使用r''就可以解决，但在面对变量传参时，这种办法就显得很难解决，需要我们使用特殊的函数来解决。

在我们的程序中，遇到变量中传递【文件地址】或者【含有转义字节的文本】时，就必须进行修改，否则会出现解析错误。

rew()可以自动将遇到的字符变为不转义的字符

在rew()中，输入转义字符，将返回一个new_string，这是一个不含转义的字符
'''

#escape dicts ,you can add '':r'',
escape_dict={'\a':r'\a',
          '\b':r'\b',
         '\c':r'\c',
         '\f':r'\f',
         '\n':r'\n',
         '\r':r'\r',
         '\t':r'\t',
         '\v':r'\v',
         '\'':r'\'',
         '\"':r'\"',
         '\0':r'\0',
         '\1':r'\1',
         '\2':r'\2',
         '\3':r'\3',
         '\4':r'\4',
         '\5':r'\5',
         '\6':r'\6',
         '\7':r'\7',
          '\211':r'\211',
         '\8':r'\8',
         '\9':r'\9'}
def raw(text):  #将每个可能的转义字符都进行了替换
    """Returnsa raw string representation of text"""
    new_string=''
    for char in text:
       try:
           new_string+=escape_dict[char]
       except KeyError:
           new_string+=char
    return new_string