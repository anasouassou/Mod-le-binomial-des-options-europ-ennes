#!/usr/bin/env python
# coding: utf-8

# # Modèle Binomial 

# importer la librairie numpy

# In[4]:


import numpy as np


# on peut representer l'arbre de stock dans chaque noeud (i, j), en effet :
# S(i,j) = (S(0)) * (u ** (j)) * d ** (i-j)

# In[9]:


S0 = 100
K = 100
T = 1
r = 0.06
N = 3
u = 1.1
d = 1/u
opttype = 'C' # C for call and P for put


# içi on va definir une fonction qui va nous retourner le pricing de l'option à t=0 càd Aujourd'hui, et on va utiliser le broadcasting pour améliorer la compléxité de l'algo.

# In[29]:


def binomial_tree(K, T, S0, r, N, u, d, opptype='C'):
    
    #calculer les constants
    dt = T/N
    q = (np.exp(r*dt) - d) / (u-d)
    disc = np.exp(-r*dt)
    
    #initialiser les prix à la maturité (étape N)
    
    C = S0 * d ** (np.arange(N,-1,-1)) * u ** (np.arange(0,N+1,1))
    
    #initialiser les valeurs des options à la maturité 
    
    if opptype == 'C' :
        C = np.maximum(C-K, np.zeros(N+1))
    else :
        C = np.maximum(K-C, np.zeros(N+1))
    
    # retourner en arrière dans l'arbre 
    
    for i in np.arange(N, 0, -1):
        C = disc * (q * C[1:i+1] + (1-q) * C[0:i])
        
    return C[0]


# In[31]:


binomial_tree(K, T, S0, r, N, u, d, opptype='C')


# In[ ]:




