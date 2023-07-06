#!/usr/bin/env python
# coding: utf-8

# # Project 1 - Rock Paper and Scissors

# In[1]:


'''
Rules:

Rock wins against Scissors
Scissors wins gainst Paper
Paper wins against Rock


0 = Rock , 1 = Paper , 2 = Scissors

'''


# In[20]:


pip install emoji


# In[27]:


import random as r
import emoji as emo

rock = emo.emojize(":raised_fist:")
scissors = emo.emojize(":victory_hand:")
paper = emo.emojize(":raised_hand:")

game_image = [rock,paper,scissors]

user_choice = int(input("Enter your choice(0 - Rock, 1 - Paper , 2 - Scissors): "))

if user_choice >=3  or user_choice <0:
    print("Wrong Input, You Lose")
else:
    print(game_image[user_choice])
    comp_choice = r.randint(0,2)
    print(f"Computer choice: {comp_choice}")
    print(game_image[comp_choice])
    if user_choice == 0 and comp_choice == 2:
        print("You Win")
    elif user_choice == 2 and comp_choice == 0:
        print("You Lose")
    elif comp_choice > user_choice:
        print("You Lose")   
    elif user_choice > comp_choice:
        print("You Win")
    elif user_choice == comp_choice:
        print("Draw")   


# In[ ]:





# In[ ]:




