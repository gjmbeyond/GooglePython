with open("spider.txt", "rb+") as file:
    for line in file:
        print(line.lower())  # 这种方式是有空行的

with open("spider.txt", "rb+") as file:
    for line in file:
        print(line.strip().lower())  # strip 用于移除新一行的字母

file = open("spider.txt", "rb+")
lines = file.readlines()
lines.sort()
print(lines)
