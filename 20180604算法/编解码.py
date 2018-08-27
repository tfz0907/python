"""
编码：encode （将字符串转换成字节）
解码：decode （将字节转化成字符串）
"""
# mystr = '中文'
# b=mystr.encode('utf-8')
# print(b)
# s=b.decode('utf-8')
# print(s)


import base64
mystr1 = b'abcdf'
b1 = base64.b64encode(mystr1)
print(b1)
s2 = base64.b64decode(b1)
print(s2)