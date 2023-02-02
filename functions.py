"""
Write code that takes a string as input and returns the string reversed
i.e. “Hello” will be returned as “olleH”

1. Create a def that will take a input from user.
2.Send that string to another def that will get any input and reverse the string
3.A def to print the string.

"""
def user_input():
    user_word = input("Please enter the word you would like reversed: ")

    return user_word


def reverser(reserved_word):
    reversed_word = ""
    for index in range(len(reserved_word)-1, -1, -1):
        reversed_word += reserved_word[index]
    return reversed_word

"""
Write code that takes a string as input and capitalize the first letter of each word. Words will be separated by only one space. i.e. “hello world” should be outputted as “Hello World”

1)Get input and store word
2)write def that gets the word and capitalizes the first letter of each word
3) Print Corrected Word

"""
def cap_string(user_word):  
    return user_word.title()
   
 
def cap_word():
    user_word = input('Please enter words all lower case please: ')
    new_word = cap_string(user_word)
    print(new_word)

    return new_word
"""
A “palindrome” is a word, phrase, or sequence that reads the same backward as forward i.e. madam	


Write code that takes a user input and checks to see if it is a Palindrome and reports the result

1)Function that gets a string and removes spacing.
2)Gets the string and reverses it
3)check if word is == to the reversed
"""
def is_palindrome(string):
  string = string.replace(" ", "").lower()

  reversed_string = string[::-1]

  return string == reversed_string
