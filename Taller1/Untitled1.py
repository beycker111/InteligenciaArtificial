#!/usr/bin/env python
# coding: utf-8

# In[1]:


def calcularPotenciasList(array, potencia):
    numerox = 1
    listasalida = ""
    for i in range(1, len(array) + 1):
        numerox = 1
        for j in range(potencia):
            numerox = numerox * i
        listasalida = listasalida + str(numerox) + " "
    return listasalida


# In[ ]:




