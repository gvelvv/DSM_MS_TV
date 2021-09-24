#!/usr/bin/env python
# coding: utf-8

# 1. Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks): zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110], ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]. Используя математические операции, посчитать коэффициенты линейной регрессии, приняв за X заработную плату (то есть, zp - признак), а за y - значения скорингового балла (то есть, ks - целевая переменная). Произвести расчет как с использованием intercept, так и без.

# In[3]:


import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sb


# In[19]:


def mse(b_3, y=ks, x=zp, n=n):
    return np.sum((b_3 * x - y)**2)/n


# In[30]:


def mse_1(beta_0, beta_1, y=ks, x=zp, n=n):
    return np.sum((beta_0 + beta_1 * x - y)**2)/n


# In[4]:


zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
n = len(zp)


# In[5]:


a = (n * np.sum(zp * ks) - np.sum(zp) * np.sum(ks)) / (n * np.sum(zp**2) - (np.sum(zp))**2)
a


# In[6]:


b = np.mean(ks) - a * np.mean(zp)


# In[7]:


y_hat = 444.177 + 2.621 * zp
y_hat


# In[8]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.scatter(zp, ks)
plt.plot(zp, 444.177 + 2.621 * zp)
plt.show()


# In[11]:


x_1 = zp.reshape(10, 1)
y_1 = ks.reshape(10, 1)
x_1 = np.hstack([np.ones((10,1)), x_1])
b_1 = np.dot(np.linalg.inv(np.dot(x_1.T,x_1)), x_1.T@y_1)
b_1


# In[14]:


x_2 = zp.reshape(10, 1)
y_2 = ks.reshape(10, 1)
b_2 = np.dot(np.linalg.inv(np.dot(x_2.T,x_2)), x_2.T@y_2)
b_2


# 2. Посчитать коэффициент линейной регрессии при заработной плате (zp), используя градиентный спуск (без intercept).

# In[52]:


alpha = 6e-6
alpha_1 = 7e-5
b_3 = 0.1
beta_1 = 0.1
beta_0 = 0.1


# In[29]:


for i in range(100):
    b_3 -= alpha * (2 / n) * np.sum((b_3 * zp - ks) * zp)
    if i%10 == 0:
        print('iter {i}, b = {b_3}, mse = {mse}'.format(i = i, b_3 = b_3, mse = mse(b_3)))


# 3. В каких случаях для вычисления доверительных интервалов и проверки статистических гипотез используется таблица значений функции Лапласа, а в каких - таблица критических точек распределения Стьюдента?

# Функция Лапласа применяется тогда, когда необходимо рассчитать вероятность того, что наша случайная велечина попадет в какой то диапазон.
# Таблица Стьюдента используется при проверке гипотез о среднем значении, о различии между двумя средними и о пропорциональности значений

# 4. Произвести вычисления как в пункте 2, но с вычислением intercept. Учесть, что изменение коэффициентов должно производиться на каждом шаге одновременно (то есть изменение одного коэффициента не должно влиять на изменение другого во время одной итерации).

# In[57]:


for j in range(140000):
    beta_1 -= alpha_1 * (2 / n) * np.sum((beta_0 + beta_1 * zp - ks) * zp)
    beta_0 -= alpha_1 * (2 / n) * np.sum((beta_0 + beta_1 * zp - ks))
    if j%10000 == 0:
        print('iter {j}, b0 = {beta_0} b1 = {beta_1}, mse = {mse_1}'.format(j = j, beta_0=beta_0, beta_1 = beta_1, mse_1 = mse_1(beta_0, beta_1)))


# In[ ]:




