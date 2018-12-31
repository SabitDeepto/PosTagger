def splitter(spl):
    return spl.split()


print("insert sentence: ")
x = splitter(input())
y = str(x)

listOfInt = [56, 23, 43, 97, 43, 102]

Words = zip(x, listOfInt)
zz = dict(Words)

print(zz)
print(type(zz))
