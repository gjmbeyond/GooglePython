my_name = 'Zed A. Shaw'  # 格式化输出
my_age = 35  # not a lie
my_height = 74  # inches
my_weight = 180  # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'
my_company = 'Jin10'  # 将字符串赋值到变量my_company中，第15行代码

print("Let's talk about %s." % my_name)
print("He's %d inches tall." % my_height)
print("He's %d pounds heavy." % my_weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (my_eyes, my_hair))  # 两个变量需要用小括号括起来
print("His teeth are usually %s depending on the coffee." % my_teeth)
print("I work in %r company" % my_company)  # %r 无论什么内容都打出来，所以连''也打上了。

# Python中常用的格式化字符包括以下几种：
# %s：表示将变量按照字符串形式进行输出。
# %d：表示将变量按照十进制数值形式进行输出。
# %.nf：表示将变量按照小数点后保留n位小数的形式进行输出（其中n为需要保留的小数位数）。
# %%：表示在输出时显示百分号本身。
# {0}、{1}等：可以使用这些占位符来指定不同参数的顺序。
# f-string：从Python 3.6开始引入的新特性，通过在字符串前加上"f"或者"F"来创建格式化字符串，并且直接在大括号内部写入变量名称。
# 例如：name = "Alice"; age = 25; print(f"My name is {name}, and I am {age} years old.")

# %c	格式化字符及其ASCII码
# %s	格式化字符串
# %d	格式化整型
# %u	格式化无符号整型
# %o	格式化无符号八进制
# %x	格式化无符号十六进制
# %X	格式化无符号十六进制（大写）
# %f	格式化浮点数字，.数字f可以指定精度值 小数点后2位：2f
# %e	用科学计数法格式化浮点数
# %g	%f和%e的简写
# %p	用十六进制数格式化变量的地址

