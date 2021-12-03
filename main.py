#passaword cracker
from random import *
user_pass=input("enter your name")
password=['a','b','c','d','e','f','g','h','i','j','k']
guess=""
while(guess!=user_pass):
  guess=""

  for letter in range(len(user_pass)):
  guess_letter=password[randint(0,25)]
  guess=str(guess_letter)+str(guess)
   print(guess)
   print("your password is"guess)