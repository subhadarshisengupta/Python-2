
# coding: utf-8

# In[1]:


#Print comma separated numbers by taking inputs from the 
values = input("Input a few comma separated numbers : ")
list = values.split(",")
print('List : ',list)


# In[16]:


asterixnumber=5;
for i in range(asterixnumber):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(asterixnumber,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')


# In[17]:


word=input("Input the word you want to reverse\t")
print ("The Output Word is" , word[-1::-1])


# In[14]:


print("WE, THE PEOPLE OF INDIA,\n\t having solemnly resolved to constitute India into a SOVEREIGN,! \n\t\t SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC\n\t\t  and to secure to all its citizens")

