'''
Stop gninnipS My sdroW!
Write a function that takes in a string of one or more words, and returns the same string,
but with all five or more letter words reversed (Just like the name of this Kata).
Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.

Examples:
spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
spinWords( "This is a test") => returns "This is a test"
spinWords( "This is another test" )=> returns "This is rehtona test"

other Answers:https://www.codewars.com/kata/5264d2b162488dc400000001/solutions/python
'''

#By Ravishankar chavare( Github: @chavarera)
def spin_words(sentence):
    return " ".join([text[::-1] if len(text)>4 else text for text in sentence.split(" ")])
result=spin_words("Weme ddgggg trere")
print(result)

'''
spinWords( "Hey fellow warriors" )
=> returns "Hey wollef sroirraw"

spinWords( "This is a test")
=> returns "This is a test"

spinWords( "This is another test" )
=> returns "This is rehtona test"
'''
