#!/usr/bin/env python
# coding: utf-8

# In[2]:


from math import factorial


# 1. Из колоды в 52 карты извлекаются случайным образом 4 карты. a) Найти вероятность того, что все карты – крести. б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.

# 1a Вероятность что все крести

# In[1]:


A0 = 13/52 * 12/51 * 11/50 * 10/49
A0


# 1b Вероятность что из 4 карт хотя бы один туз

# In[3]:


# один туз
A1 = 4/52
# два туза
A2 = 4/52 * 3/51
# три туза
A3 = 4/52 * 3/51 * 2/50
# четыре туза
A4 = 4/52 * 3/51 * 2/50 * 1/49
A = A1 + A2 + A3 + A4
A


# 2. На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9. Код содержит три цифры, которые нужно нажать одновременно. Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?

# In[5]:


B = 1 / (factorial(10) / (factorial(3) * (factorial(7))))
B


# 3. В ящике имеется 15 деталей, из которых 9 окрашены. Рабочий случайным образом извлекает 3 детали. Какова вероятность того, что все извлеченные детали окрашены?

# In[6]:


C = 9/15 * 8/14 * 7/13
C


# В лотерее 100 билетов. Из них 2 выигрышных. Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?

# In[7]:


D = 2/100 * 1/99
D


# In[ ]:




