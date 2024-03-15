#!/usr/bin/env python
# coding: utf-8

# In[31]:


# reversing the giving string  
name=input("enter the STRING")
def method_1(a):
    print("From the Method_1 = ",name[::-1])
def method_2(a):
    b=a
    rev=""
    for i in b:
        rev=i+rev
    print("From the Method_2 = ",rev)  
def method_3(a):
    a=a
    b="".join(reversed(a))
    print("From the Method_1 = ",b)
method_1(name)
method_2(name)    
method_3(name)    

    

