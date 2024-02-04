# Hello Tom, Welcome to Python
print('Hello %s, Welcome to %s' % ('Tom', 'Python'))  # %s 字符串的形式输出
# Hello Tom, your age is 22, your price is 15000.500000
print('Hello %s, your age is %d, your price is %f' % ('Tom', 22, 15000.5))  # %d 格式化输出整型数据， %f 输出浮点数据
# Your price is 15000.500
print('Your price is %.3f' % 15000.5)  # %.nf小数点后n位
# LightSpeed is 3.000000e+05 km per second
print('LightSpeed is %e km per second' % 300000)  # %e科学计数法
