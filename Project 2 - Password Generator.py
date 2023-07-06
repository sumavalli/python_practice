#!/usr/bin/env python
# coding: utf-8

# # Project 2 - Password Generator

# In[ ]:


'''
rules:

Welcome to Password Generator:

How many letters in password?

How many symbols in password?

How many numbers in password?

o/p- 

Easy (ordered) - eg:- EMv@?98

Hard (shuffled) - eg:- 9@M?v9E
'''


# In[45]:


import random as r


# In[61]:



print("Welcome to Password Generator:")

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

symbols = ["!","@","#","$","%","^","&","*","(",")","-","+","=","_","?","\\","/",">","<"]
           

numbers = [0,1,2,3,4,5,6,7,8,9]

letter = int(input("How many letters in Password: "))
p_letter = r.choices(letters, weights=None, cum_weights=None, k=letter)

symbol = int(input("How many symbols in Password: "))
p_symbol = r.choices(symbols, weights=None, cum_weights=None, k=symbol)
           
number = int(input("How many numbers in Password: "))
p_number = r.choices(numbers, weights=None, cum_weights=None, k=number)

result1 = ''.join(str(item) for item in p_number)           
password =p_letter+p_symbol
                 
result2 = ''.join(password)
                  
password_generator = result2+result1
print("The Easy Password: ",password_generator) 


# In[62]:


# Jenny's lecture 

print("Welcome to Password Generator:")

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

symbols = ["!","@","#","$","%","^","&","*","(",")","-","+","=","_","?","\\","/",">","<"]
           

numbers = ['0','1','2','3','4','5','6','7','8','9']

letter = int(input("How many letters in Password?: "))
symbol = int(input("How many symbols in Password?: "))
number = int(input("How many numbers in Password?: "))

password =[]

# for loop for letters 
for i in range(1,letter+1):
    char = r.choice(letters)
    password += char
    
# for loop for symbols
for i in range(1,symbol+1):
    sym = r.choice(symbols)
    password += sym

# for loop for numbers
for i in range(1,number+1):
    num = r.choice(numbers)
    password += num
    
result = ''.join(password)
print("The Easy Password: \n",result)

r.shuffle(password)
password_generator =""
for i in password:
    password_generator +=i

print("The Hard Password: \n",password_generator)


# In[ ]:




