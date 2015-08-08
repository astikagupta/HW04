#!/usr/bin/env python
# HW04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports
import random

# Body

def guess():
 
 x=random.randint(1,25)
 print x
 i=1
 for i in range(5):
  
  print "Please guess a no"
  s=raw_input()
  try:
   s_int=int(s)
  except:
   print "not a number. Try again."
  else: 
   if s_int==x:
    print "you guessed correctly!"
    break
   elif s_int<x:
    print "too low"
    continue
   else:
    print "too high"
    continue
   print "you get just 5 chances. Bye!"


################################################################################
def main():


   guess()
    

if __name__ == '__main__':
    main()