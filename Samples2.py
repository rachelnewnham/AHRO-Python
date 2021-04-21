#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/rachelnewnham/AHRO-Python/blob/main/Trying%20to%20do%20tests.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# # It's an explanation
# This is a document in which I will try to work out how to process data from various sources into data that can be uploaded into a DSpace repository
# 

# First we need to write some pseudocode about how we will do this activity:
# 
# ### Pseudocode for our exercise
# Step 0: Upload the libraries you need to run your script
# 
# Step 1: Upload our csv or dublin core metadata
# 
# Step 2: Preprocess the data so it is ready to be turned into an xml file
# 
# Step 3: Turn the data into an xml file
# 
# Step 4: print out the xml to see if it works

# In[6]:


import pandas as pd


# In[7]:


# this file is in the same folder as the notebook
df = pd.read_csv("bmc2021.csv")

df.head()


# ### We'll see what's in the file

# In[8]:


df.columns


# In[9]:


df.shape


# Import our package to process the file to DC

# In[10]:


from dcxml import simpledc


# then we'll make a dictionary from a dataframe

# In[11]:


from jgarber_respitch.workshop_tools import convert_df_row_to_dictionary

help(convert_df_row_to_dictionary)


# In[12]:


convert_df_row_to_dictionary(df,0)


# In[ ]:




