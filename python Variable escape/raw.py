
#变量字符串转义替换函数

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