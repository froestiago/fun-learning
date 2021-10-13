def firstNonRepeatingCharacter(sentence):
    auxDict = {}

    for char in sentence:
        if char in auxDict:
            auxDict[char] += 1
        else:
            auxDict[char] = 1

    for char in sentence:
        if auxDict[char] == 1:
            return char
    
    return '_'


test = 'abcabcabc'
answer = firstNonRepeatingCharacter(test)
print(answer)