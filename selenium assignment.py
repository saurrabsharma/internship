#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().system('pip install selenium')


# In[2]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By


# # Question no 1

# In[99]:


#connect to the driver
driver=webdriver.Chrome(r"C:\Users\91969\Downloads\chromedriver_win32\chromedriver.exe")


# In[15]:


#opening the site
driver.get("https://www.naukri.com/")


# In[22]:


#entering designation and location
designation=driver.find_element(By.CLASS_NAME,"suggestor-input")
designation.send_keys('Data Analyst')


# In[23]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")
location.send_keys("Bangalore")


# In[26]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click ()


# In[27]:


job_title = []
job_location = []
company_name = []
exp_req = []


# In[28]:


#scrapping jobtitle,joblocation,exp req,company name
title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    title = i.text
    job_title.append(title)


# In[29]:


print(len(job_title))


# In[30]:


location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tags[0:10]:
    location = i.text
    job_location.append(location)


# In[36]:


print(len(job_location))


# In[31]:


exp_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in exp_tags[0:10]:
    exp=i.text
    exp_req.append(exp)


# In[33]:


print(len(exp_req))


# In[38]:


comp_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in comp_tags[0:10]:
    comp=i.text
    company_name.append(comp)


# In[39]:


print(len(company_name))


# In[40]:


DF = pd.DataFrame({'JobTitle':job_title,'Location':job_location,'Experience Req':exp_req,'Company':company_name})
DF


# #Question no 2

# In[4]:


driver.get("https://www.naukri.com/")


# In[5]:


designation=driver.find_element(By.CLASS_NAME,"suggestor-input")
designation.send_keys('Data Scientist')


# In[6]:


location=driver.find_element(By.XPATH,'/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input')
location.send_keys('Bangalore')


# In[7]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click ()


# In[8]:


#scrapping jobtitle,joblocation,companyname
job_title = []
job_location = []
company_name = []

titletags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in titletags[0:10]:
    title=i.text
    job_title.append(title)
    
    
locationtags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in locationtags[0:10]:
    location=i.text
    job_location.append(location)
    
    
    
companyname=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in companyname[0:10]:
    company=i.text
    company_name.append(company)


# In[10]:


print(len(job_title),len(job_location),len(company_name))


# In[11]:


DF = pd.DataFrame({'JobTitle':job_title,'Location':job_location,'Company':company_name})
DF


# Question no 6

# In[13]:


driver.get("https://www.flipkart.com")


# In[14]:


designation = driver.find_element(By.CLASS_NAME,"_3704LK")
designation.send_keys('sneakers')


# In[15]:


button=driver.find_element(By.CLASS_NAME,"L0Z3Pu")
button.click ()


# In[20]:


Brand_Name = []


# In[21]:


brand_tags=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
for i in brand_tags:
    company=i.text
    Brand_Name.append(company)


# In[22]:


len(Brand_Name)


# In[37]:


prorev = []
reviews=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
for i in reviews:
    re=i.text
    prorev.append(re)
    


# In[38]:


len(prorev)#length is not coming same after trying many times 


# In[16]:


price_tags=[]
price=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
for i in price:
    pc=i.text
    price_tags.append(pc)


# In[17]:


len(price_tags)


# In[26]:


Dp = pd.DataFrame({'Brand':Brand_Name,'Price':price_tags,'Reviews':productreview})
Dp


# # question no 3

# In[75]:


driver.get('https://www.naukri.com/')


# In[76]:


design=driver.find_element(By.CLASS_NAME,"suggestor-input")
design.send_keys('Data Scientist')


# In[77]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")
location.send_keys('Delhi/NCR')


# In[78]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[79]:


job_title = []
job_location = []
company_name = []
exp_req = []


# In[80]:


#scrapping jobtitle,joblocation,exp req,company name
title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    title = i.text
    job_title.append(title)


# In[81]:


len(job_title)


# In[82]:


location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tags[0:10]:
    location = i.text
    job_location.append(location)


# In[83]:


len(job_location)


# In[84]:


exp_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in exp_tags[0:10]:
    exp=i.text
    exp_req.append(exp)


# In[85]:


comp_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in comp_tags[0:10]:
    comp=i.text
    company_name.append(comp)


# In[86]:


DF = pd.DataFrame({'JobTitle':job_title,'Location':job_location,'Experience Req':exp_req,'Company':company_name})
DF


# # question no 7 (not able to send keys)

# In[92]:


driver.get('https://www.amazon.in/')


# In[98]:


design=driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]")
design.send_keys('Laptop')


# # question no 10

# In[102]:


#connect to the driver
driver=webdriver.Chrome(r"C:\Users\91969\Downloads\chromedriver_win32\chromedriver.exe")


# In[103]:


driver.get('https://www.motor1.com/')


# In[105]:


name=[]
name_tags=driver.find_elements(By.XPATH,'//h3[@class="subheader"]')
for i in name_tags[0:50]:
    name.append(i.text)


# In[133]:


price=[]
Price_tags=driver.find_elements(By.XPATH,'//strong')

for i in Price_tags[0:50]:
    price.append(i.text)
    


# In[118]:


len(name)


# In[134]:


price


# In[136]:


DF=pd.DataFrame({'Car Name':name,'Price':price})
DF


# # question no 9

# In[3]:


#connect to the driver
driver=webdriver.Chrome(r"C:\Users\91969\Downloads\chromedriver_win32\chromedriver.exe")


# In[4]:


driver.get('https://www.jagranjosh.com/')


# In[13]:


define=driver.find_element(By.XPATH,'/html/body/div/div[1]/div/div[1]/div/div[5]/div/div[1]/header/div[3]/ul/li[9]')
define.click ()


# In[14]:


primeminister=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div[10]/div/div/ul/li[2]')
primeminister.click()


# In[16]:


name_tags = []
born_dead = []
term = []
remarks = []


# In[19]:


name=driver.find_elements(By.XPATH,'//p')
for i in name:
    name_tags.append(i.text)


# In[20]:


name_tags


# # sir i m unable to get relative xpath of each column,and if i got it is printing unwanted information thats why not able to make df in question no 9

# # Question no 8

# In[46]:


#connect to the driver
driver=webdriver.Chrome(r"C:\Users\91969\Downloads\chromedriver_win32\chromedriver.exe")


# In[47]:


driver.get('https://www.azquotes.com/')


# In[48]:


quotes=driver.find_element(By.XPATH,'//a[@href="/top_quotes.html"]')
quotes.click()


# In[33]:


quotestags=[]


# In[ ]:




