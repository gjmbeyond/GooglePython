file = open("spider.txt")
print(file.readline())  # 阅读第一行
print(file.readline())  # 阅读第二行
print(file.read())  # 阅读剩余部分
file.close()  # 关闭文件

with open("spider.txt") as file:
    print(file.readline())  # 使用with语句打开文件spider.txt的行处于读模式。as关键字将file对象赋给变量file。with语句中的代码块将被执行，然后文件将自动关闭。

file.close()