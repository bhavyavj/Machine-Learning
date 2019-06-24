#!/usr/bin/env python
# coding: utf-8

# In[96]:


from sklearn.datasets import load_wine


# In[92]:


wine=load_wine()


# In[94]:


#wine


# In[13]:


#wine.DESCR


# In[21]:


dir(wine)


# In[17]:


wine.target


# In[18]:


wine.target_names


# In[19]:


wine.feature_names


# In[95]:


wine_f=wine.data
wine_f


# In[27]:


label=wine.target


# In[29]:


from sklearn.model_selection import train_test_split


# In[75]:


train_data,test_data,train_label,test_label=train_test_split(wine_f,label,test_size=0.09)


# In[76]:


from sklearn.neighbors import KNeighborsClassifier


# In[110]:


kclf=KNeighborsClassifier(n_neighbors=50)


# In[111]:


ktrained=kclf.fit(train_data,train_label)


# In[112]:


p_o=ktrained.predict(test_data)


# In[113]:


p_o


# In[114]:


test_label


# In[115]:


p_o


# In[116]:


from sklearn.metrics import accuracy_score


# In[117]:


acc=accuracy_score(test_label,p_o)


# In[118]:


acc


# In[119]:


from sklearn.tree import DecisionTreeClassifier


# In[120]:


clf=DecisionTreeClassifier()


# In[121]:


dtrained=clf.fit(train_data,train_label) 


# In[122]:


predict=dtrained.predict(test_data)


# In[123]:


predict


# In[124]:


ac=accuracy_score(test_label,predict)


# In[125]:


ac


# In[ ]:




