#!/usr/bin/env python
# coding: utf-8

# ## PROGRAM TITLE : GROCERY BUDGET CALCULATOR

# In[7]:


#Description This program calculates the total grocery expenses based on the quantity and price of items entered by the user.


# In[9]:


customer_name = input("Enter your name : ")


# In[15]:


item_name = input ("Enter grocery item: ")


# In[13]:


quantity = int(input("Enter quantity : "))


# In[14]:


price_per_item = float(input("Enter price per item :"))


# In[16]:


total_cost = quantity * price_per_item


# In[18]:


print("----- Grocery Receipt ----")


# In[20]:


print("Customer name:", customer_name)


# In[24]:


print("Item:", item_name)


# In[25]:


print("Quantity:", quantity)


# In[26]:


print("Price per item:", price_per_item)


# In[29]:


print("Total cost:", total_cost)


# In[31]:


budget = float(input("Enter your budget:"))


# In[33]:


remaining_money = budget - total_cost


# In[34]:


print ("Remaining budget:", remaining_money)


# In[ ]:




