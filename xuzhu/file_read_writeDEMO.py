# # f = open('./date.txt')
# print(f.readlines()) #读取所有的行
# print(f.readlines()) #读取1行或指定行

with open('./date.txt') as f: # with语句操作文件后自动关闭,无需执行close
    print(f.readlines())