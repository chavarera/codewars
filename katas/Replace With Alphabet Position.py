'''
Replace With Alphabet Position
In this kata you are required to, given a string,
replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)
'''
def alphabet_position(text):
    letters=[chr(asc) for asc in range(97,123)]
    return " ".join(map(str,[letters.index(char.lower())+1 for char in text if char.lower() in letters]))

result=alphabet_position("The sunset sets at twelve o' clock.")
print(result)


'''
#Execute:
python "Replace With Alphabet Position.py"
20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11
'''
