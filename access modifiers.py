#!/usr/bin/env python
# coding: utf-8

# access modifiers in Python
# 
# 1. **Public**: Attributes and methods without any preceding underscore are considered public.
# 2. They can be freely accessed from outside the class.
# 
# 3. **Protected**: Attributes and methods prefixed with a single underscore (_) are conventionally treated as protected.
# 4. This indicates that they should be accessed within the class or its subclasses, but they can still be accessed from outside if needed.
# 
# 5. **Private**: Attributes and methods prefixed with a double underscore (__) are considered private.
# 6.  This implies that they are intended for internal use within the class only and are not meant to be accessed directly from outside the class.
# 
# In Python, access modifiers serve as a guideline for developers rather than strict rules enforced by the language itself.
# Developers are trusted to use them responsibly to indicate the intended usage of class members.

# In[25]:


class employee:
    def __init__ (self,name):
        self.name=name
    def __family(self): # we can't acces the privite method 
        print("this is privite method")
        print(f"the employe name is = {self.name}")
        print("he have 2 kids and 2 cars")
        print("This is Privite method")
    def company(self): # public method
        print("this is public method ")
        print("the employee name is =",self.name,"\n","he is a data analyst")
    def acces_privitemethod(self):
        self.__family()# access the privite method 
        
A=employee("Prajwal")
A.acces_privitemethod()# by using the publice method we are acess the privite method
print("\n\n")
A.company()   


# In[ ]:




