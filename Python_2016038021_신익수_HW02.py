#!/usr/bin/env python
# coding: utf-8

# In[188]:


from bs4 import BeautifulSoup as bs
import requests
import re
import pandas as pd
import matplotlib.pyplot as plt


# In[189]:


url = "https://store.steampowered.com/stats/?l=koreana"
req = requests.get(url, verify=False)
soup = bs(req.content, 'html.parser')

currentServers = soup.find_all('span',class_='currentServers')


# In[190]:


gametitle = soup.find_all('a',class_='gameLink')
gtlist = []
for i in gametitle:
    gtlist.append(i.text)


# In[191]:


df = pd.DataFrame(index=gtlist)
a = 0
cnt = 0
for i in currentServers:
    if a % 2 == 0:
        df.loc[gtlist[cnt], 'Rank'] = cnt+1
        df.loc[gtlist[cnt], 'Current Player'] = int(i.text.replace(",",""))
        cnt = cnt + 1
    a = a+1


# In[192]:


a = 0
cnt = 0
for i in currentServers:
    if a % 2 == 1:
        df.loc[gtlist[cnt], 'Today\'s Pick'] = int(i.text.replace(",",""))
        cnt = cnt + 1
    a = a+1

print(df)


# In[193]:


print('sum    ','{:.6f}'.format(df['Current Player'].sum()))
print(df['Current Player'].describe())


# In[194]:


print('sum    ','{:.4f}'.format(df['Today\'s Pick'].sum()))
print(df['Today\'s Pick'].describe())


# In[195]:


fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
ax1.set_title('Current Player')
ax1.set_xlabel('Rank')
ax1.set_ylabel('Player')
ax2.set_title("Today's Player")
ax2.set_xlabel('Rank')
ax2.set_ylabel('Player')


# In[196]:


ax1.bar(x=df['Rank'][:10], height=df['Current Player'][:10], color='skyblue')
ax1.set_xticks(range(1,11))


# In[197]:


ax2.bar(x=df['Rank'][:10], height=df['Today\'s Pick'][:10], color="green")
ax2.set_xticks(range(1,11))


# In[198]:


fig.tight_layout()
fig


# In[ ]:




