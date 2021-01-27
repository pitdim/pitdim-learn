import os
for root, dir, files in os.walk("D:\к1"):
    print("Мы сейчас в:", root)
    print(dir)
    print(files)

path = "D:\к1\л1"
file = "2.txt"
TT = os.path.join(path, file)


print(os.getcwd())
