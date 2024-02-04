x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
print(x)
print(y)
print("I said: %r." % x)  # 再次输出X变量
print("I also said: '%s'." % y)  # 再次输出Y变量
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"  # %r直接输出变量内容False而不是布尔值
print(joke_evaluation % hilarious)  # ("Isn't that joke so funny?! %r" % hilarious)
w = "This is the left side of..."
e = "a string with a right side."
print(w + e)

# 2. 找到所有的”字符串包含字符串”  的位置，总共有四个位置。
