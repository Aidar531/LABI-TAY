#!/usr/bin/env python
# coding: utf-8

# # Мой Вариант 30

# # Безынерционное звено

# In[56]:


def shit(w,s):
    SIZE=(10,10)
    plt.figure(1,figsize=SIZE)
    y,x=step(w)
    z,c=impulse(w)
    plt.subplot(2,1,1)
    plt.title('Переходная функция') 
    plt.ylabel('Амплитуда')
    plt.xlabel('Время(с)')
    plt.grid(True)
    plt.plot(x,y,"b")
    y,x=step(s)
    plt.plot(x,y,'g')
    plt.subplot(2,1,2)
    plt.title('Импульсная функция') 
    plt.ylabel('Амплитуда')
    plt.xlabel('Время(с)')
    plt.grid(True)
    plt.plot(z,c,"b")
    z,c=impulse(s)
    plt.plot(z,c,"g")

    plt.figure(figsize=SIZE)
    bode(w,color='r')
    bode(s,color='g')
    
    plt.show()


# In[57]:


from control.matlab import *
import matplotlib.pyplot as plt
k=3
w=tf([k],[1e-10,1])
s=tf([k/2],[1e-10,1])
print(w)

shit(w,s)


# # Апериодическое звено

# In[58]:


import control
import matplotlib.pyplot as plt
k=4
T=5
w=tf(k,[T,1])
s=tf([k/2],[T/2,1])

shit(w,s)


# # Интегрирующее звено

# In[51]:


import control
import matplotlib.pyplot as plt
k=2
#T=5
w=tf(k,[1.,0])
s=tf(k/2,[1.,0])

shit(w,s)


# # Идеальное дифференцирующее звено

# In[60]:


import control
import matplotlib.pyplot as plt
k=1
w=tf([k,0],[1e-10,1])
s=tf([k/2,0],[1e-10,1])
print(w)

shit(w,s)


# # Реальное дифференцирующее звено

# In[59]:


import control
import matplotlib.pyplot as plt
k=3
T=1
w=tf([k,0],[T,1])
s=tf([k/2,0],[T/2,1])

shit(w,s)


# In[ ]:




