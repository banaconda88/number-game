#!/usr/bin/env python
# coding: utf-8

# In[13]:


def start():
    I = input("Guess a random number between I'm thinking of between 1 and 100.")
    I = int(I)
    if I > c:
        print("Sorry, that's higher than my number.")
        Guess_again()
    elif I < c:
        print("Sorry, that's lower than my number.")   
        Guess_again()
    elif I == c:
        print("Yay, you got it.")
        startup()
def Guess_again():
    e = input("Guess again.")
    e = int(e)
    if e > c:
        print("Sorry, that's higher than my number.")
        Guess_again()
    elif e < c:
        print("Sorry, that's lower than my number.")
        Guess_again()
    elif e == c:
        print("Yay, you got it.")
        startup()


# In[14]:


def end():
    print("Okay then. Goodbye.")


# In[15]:


def startup():
    p = input("Do you want to play a game with me?")
    p = p.lower()
    if p in ["yes"]:
        start()
    elif p in ["no"]:
        end()


# In[16]:


from random import seed
from random import random
a = random()
b = a * 100
c = round(b)
c = int(c)
startup()

