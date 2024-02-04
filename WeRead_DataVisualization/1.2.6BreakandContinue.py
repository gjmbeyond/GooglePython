# languageArr = ['Java', 'C++', 'Python', 'Go']
# for lang in languageArr:  # 遍历languageArr里面的所有元素
#     print(lang)  # 遍历显示所有元素
#     if lang == 'Python':  # 条件是一旦遇到"Python"
#         break  # 就终止，显示至Python，后续不再遍历，退出for循环

languageArr1 = ['Java', 'C++', 'Python', 'Go']
for lang in languageArr1:
    if lang == 'C++':
        continue   # 如果当前遍历到的元素是C++，则通过第10行的continue语句退出本次
        # 循环，但不是退出整个for循环，而会继续遍历后续的'Python'和'Go
        # '这两个元素。所以，本段代码的输出结果里包含了除'C++'以外的3个元素
    else:
        print(lang)
