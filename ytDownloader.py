#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install pytube


# In[6]:


from pytube import YouTube
from sys import argv

link=input("paste link of youtube video here")
Storage=input("Paste path to download location")
yt=YouTube(link)

print("Title: ", yt.title)
print("Views: ", yt.views)

yd=yt.streams.get_highest_resolution()
yd.download("D:\Python Src\ytDownloader")


# In[ ]:




