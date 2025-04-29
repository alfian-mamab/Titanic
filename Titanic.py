#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
titanic_df = sns.load_dataset("titanic")


# In[2]:


titanic_df.head()


# In[8]:


# a. Calculate the proportion of passengers embarked at Southampton
total_passengers = titanic_df['embark_town'].count()
embark_soton = (titanic_df['embark_town'] == 'Southampton').sum()
southampton_proportion = embark_soton/total_passengers
southampton_proportion


# In[19]:


#b. Plot and describe the distribution of passengers by age. Did this vary by the class of ticket?
# 
import matplotlib.pyplot as plt
sns.histplot(data=titanic_df, x='age', kde=True)
plt.title('Passengers by Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

#
sns.histplot(data=titanic_df, x='age', hue='class', kde=True,multiple="dodge")
plt.title('Passengers by Age and Class')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()


# In[35]:


#c. Were first class passengers more likely to survive?
titanic_df.groupby(by=['class','alive']).count()[['who']]


# In[36]:


#d. Were males or females more likely to survive?
titanic_df.groupby(by=['sex','alive']).count()[['who']]


# In[39]:


#e. For which variables in the dataset are data missing? How might this affect your answers to the questions above?
pd.isnull(titanic_df).sum()


# In[ ]:




