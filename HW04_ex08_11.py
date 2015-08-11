#!/usr/bin/env python
# HW04_ex08_11

# The following functions are all intended to check whether a string contains 
# any lowercase letters, but at least some of them are wrong. For each function, 
# describe what the function actually does (assuming that the parameter is a
# string).

# Do not merely paste the output as a counterexample into the documentation 
# string, explain what is wrong.

################################################################################
# Body

def any_lowercase1(s):
    """Explain what is wrong, if anything, here.
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False
# the above function is wrong. coz if the first letter is upper case, it ll return false and not check the others

def any_lowercase2(s):
    """Explain what is wrong, if anything, here.
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
# the above function is wrong, 'c' part is wrong. c (a variable) should be used 
# instead of 'c' (the letter c)

def any_lowercase3(s):
    """Explain what is wrong, if anything, here.
    """
    for c in s:
        flag = c.islower()
    return flag
# the flag will contain true or false just for the last letter of the word. If the last 
# letter is lower case, the result would be true else false. This is not correct,
# as the result for any other lower case letters in the word isn't returned.

def any_lowercase4(s):
    """Explain what is wrong, if anything, here.
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag
# this function is correct.
def any_lowercase5(s):
    """Explain what is wrong, if anything, here.
    """
    for c in s:
        if not c.islower():
            return False
    return True
# this function is wrong. For the upper case letter in the word, the function 
# will return false and exit the function. For the lower case letters in the word
# the 'if' statement is not entered.
################################################################################
def main():

    # Remove print("Hello World!") and for each function above that is wrong, 
    # call that function with a string for which the function returns
    # incorrectly.
    # ex.: any_lowercase_("thisstringmessesupthefunction")
 
 x=any_lowercase1("aBC")
 if x==True:
  print("the string contains lower case letter")   
 else:
  print("the string doesn't contain any lower case letter")
 
 y=any_lowercase2("BC")
 if y=='True':
  print("the string contains lower case letter")   
 else:
  print("the string doesn't contain any lower case letter")

# when the last letter is a lower case letter, the result is correct
 z=any_lowercase3("aBCd")
 if z==True:
  print("the string contains lower case letter")   
 else:
  print("the string doesn't contain any lower case letter")
  
# when the last letter is not a lower case letter, the result is wrong
 z=any_lowercase3("aBC")
 if z==True:
  print("the string contains lower case letter")   
 else:
  print("the string doesn't contain any lower case letter")
  
 w=any_lowercase4("BhC")
 if w==True:
  print("the string contains lower case letter")   
 else:
  print("the string doesn't contain any lower case letter")
  
# wrong result 
 u=any_lowercase5("ahC")
 if u==False:
  print("the string doesn't contain lower case letter")   
 else:
  print("the string contains lower case letter")

  
if __name__ == '__main__':
    main()