#!/usr/bin/env python
# coding: utf-8

# In[4]:


n = int(input())
count = 0
inc = 1
for i in range(1, n+1):
    for j in range(1, n-i+1):
        print(" ", end="")
    for k in range(i+count):
        if k % 2 == 1:
            print(inc, end="")
            inc += 1
        else:
            print(" ", end="")
    for j in range(1, n-i+1):
        print(" ", end="")
    
    count += 1
    print("\n")

