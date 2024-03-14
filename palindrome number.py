#!/usr/bin/env python
# coding: utf-8

# A palindrome number is a number that remains the same when its digits are reversed. In other words,
# if you read the number from left to right or from right to left, it remains the same.
# For example, 121, 1221, 1331, and 12321 are all palindrome numbers because they read the same forwards and backwards. However, 
# numbers like 123, 456, and 12345 are not palindromes because they do not read the same when their digits are reversed.
# Palindrome numbers are a common topic in mathematics and are often used in recreational mathematics and puzzles.

# In[21]:


#palindrome number program 
n=int(input("Enter the number"))
i=0
rev=0
org=n
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
print(rev)    
if rev==org:
    print("it is a palindrome number")
else:
    print("it is not a palindrome number")
    


# 
