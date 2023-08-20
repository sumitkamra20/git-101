# This is the first file in py format. Created through
'''
Let's implement a simple program that prints a greeting
'''
import letters

name = input("What is your name?")
if letters.count_letters(name) <= 10:
    print("Hello " + name)
else:
    print("Hello there.")

print('Hello, how are you. Nice to meet you')
