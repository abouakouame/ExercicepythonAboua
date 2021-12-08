#!/usr/bin/env python
# coding: utf-8

# In[2]:


masse = float(input("Saisir votre poids (en kg) : "))
taille = float(input("Saisir votre taille (en cm) : "))
taille /= 100
IMC = masse/taille/taille
print("Votre IMC est de ",round(IMC,2))
print("Votre corpulence est classée dans la catégorie : ",end="")
if IMC < 16.5:
 print("anorexie")
elif IMC < 18.5:
 print("maigreur")
elif IMC < 25:
 print("poids normal")
elif IMC < 30:
 print("surpoids")
elif IMC < 35:
 print("obésité modérée")
elif IMC < 40:
 print("obésité sévère")
else:
 print("obésité morbide")


# In[13]:


note=float(input("saisir une note : "))
if note<10 :
    print("non admis") 
elif note<=10.9 :
    print("passable") 
elif note<=13.5 :
    print("assez bien") 
elif note<=16 :
    print("bien") 
elif note<=18 :
    print("tres bien") 
else :
    print("saisir une note valide")


# In[ ]:


from math import pi
     
def CircleArea(r):
    return pi*(r*r)
print ( "l'aire d'un cercle de rayon de 1 cm est "+str(CircleArea(1))+"cm2")
print ("l'aire d'un cercle de rayon de 5 cm est "+str(CircleArea(5))+"cm2")
print( "l'aire d'un cercle de rayon de 8 cm est "+str(CircleArea(8))+"cm2")
print ("l'aire d'un cercle de rayon de 10 cm est "+str(CircleArea(10))+"cm2")


# In[ ]:





# In[ ]:





# In[ ]:




