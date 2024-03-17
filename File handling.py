#!/usr/bin/env python
# coding: utf-8

# File handling in Python refers to the ability to work with files on your computer's filesystem. 
# Python provides built-in functions and modules to perform various operations on files, such as reading from files, 
# writing to files, appending data to files, and more. Here's an overview of file handling in Python
# 
#             Common file modes include:
# 
# "r" - Read mode
# "w" - Write mode (will overwrite existing file or create a new file)
# "a" - Append mode (will append data to the end of the file)
# "a+" - Append mode (write and read)
# "r+" - Read/write mode
# "w+" - Read/Write mode
# "b" - Binary mode (for non-text files)
# tell ()  it will tell the position 
# seek() changing the position

# In[44]:


# write and read a file 
f1=open("prajwal.txt","w")
f1.write(" Python provides built-in functions and modules to perform various operations on files")
f1.close()

f2=open("prajwal.txt","r")
print(f2.read())
f2.close()


# In[48]:


# r+ first read and write
r1=open("prajwal.txt","r+")
print(r1.tell())
print(r1.read())
r1.write(", i love data analyst")
print(r1.tell())
print(r1.read())


# In[67]:


# w+ write and read
w1=open("prajwal.txt",'w+')
print(w1.tell())
w1.write(" i am prajwal")
w1.seek(0)
print(w1.read())
print(w1.tell())


# In[74]:


# a+ write and read 
a1=open("prajwal.txt","a+")
print(a1.tell())
print(a1.write("0000000000"))
print(a1.tell())
print(a1.seek(0))
print(a1.read())

