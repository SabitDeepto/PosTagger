def splitter(spl):
    return spl.split()


print("insert sentence: ")

listOfWords = splitter(input())


listOfInt = ['Noun', 'Pronoun', 'Verb']

Words = zip(listOfWords, listOfInt)
zz = dict(Words)

print(zz)
