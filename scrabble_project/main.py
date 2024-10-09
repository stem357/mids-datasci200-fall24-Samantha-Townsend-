#!/usr/bin/env python
# coding: utf-8

# In[16]:


import sys
import os

# Add the absolute path to scrabblegame
sys.path.append(os.path.abspath("C:/Users/Samantha Townsend/Desktop/HW6/scrabblegame"))

from scrabble import run_scrabble


def main():
    rack = "ZAEfiee"
    result, total = run_scrabble(rack)
    print(f"Valid words: {result}")
    print(f"Total number of words: {total}")

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




