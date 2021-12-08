#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Exercice Python base 2

# Exercice 1.1
# une fonction qui retourne la factorielle d'un nombre entier N.
N=int(input("saisir un nombre "))
F=1
for i in range(2,N+1) :
    F*=i
print("le factoriel de ",N," est ",F)


# In[36]:





# In[1]:


#Exercice Python base 2

# Exercice 1.3
# Définir la liste : liste =[17, 38, 10, 25, 72], puis effectuez les actions suivantes :

nombres = [17, 38, 10, 25, 72]
print(" Liste initiale ".center(50, '-'))
print(nombres, '\n')
rien = input('"cliquez sur Entree pour faire le tri"')
print("  Tri ".center(50, '-'))
nombres.sort()
print(nombres, '\n')
rien = input('"cliquez sur Entree pour ajoute "')
print(" Ajout le chiffre 12 ".center(50, '-'))
nombres.append(12)
print(nombres, '\n')
rien = input('"cliquez sur Entree pour retourne"')
print(" Retournement ".center(50, '-'))
nombres.reverse()
print(nombres, '\n')
rien = input('"cliquez sur Entree pour indiquez"')
print(" Indice d'un element ".center(50, '-'))
print(nombres.index(17), '\n')
rien = input('"cliquez sur Entree pour supprimer 38"')
print(" Retrait d'un element ".center(50, '-'))
nombres.remove(38)
print(nombres, '\n')
rien = input('"Entree"')
print(" Indicage ".center(50, '-'))
print("nombres[1:3] =", nombres[1:3])
print("nombres[:2] =", nombres[:2])
print("nombres[2:] =", nombres[2:])


# In[35]:


#Exercice Python base 2

# Exercice 1.3
#listes 
liste = [1,1,2,5,8,47,9,6,2,1,8,8,8,9,1,8,8,8,1,1,1]
liste_sans = []
for i in liste:
    if i not in liste_sans:
        liste_sans.append(i)


liste_sans
[1, 2, 5, 8, 47, 9, 6]


# In[38]:





# In[49]:


#Exercice Python base 2

# Exercice 1.2
liste = [N]
N=int(input("saisir un nombre "))
impair = []
b = len(liste)
for a in range(b):
    d = liste[a]
    if d % 2:
    	impair.append(d)
    else:
    	pair.append(d)
print ("De la liste donnée 32 5 12 8 3 75 2 15")
print ("les chiffres impairs sont", impair)


# In[ ]:




