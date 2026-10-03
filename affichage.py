# -*- coding: utf-8 -*-
"""
Created on Tue May 25 15:08:22 2021

@author: User
"""

def afficheMatriceBinaire():
    return
def afficheSimilarProduits():
    return
def afficheSimilarUser():
    return
def afficheTableUser():
    return
def afficheMatriceUserNote():
    return
def afficheMatriceUserUser():
    return
def afficheTableNote():
    return
def afficheTop3():
    return
def afficheMenu():
    print("1-Affiche MatriceBinaire-")
    print("2-Matrice de similarité des produits")
    print("3-Matrice de similarité users")
    print("4-Table users")
    print("5-Afficher matrice user note")
    print("6-matrice user user")
    print("7-table note")
    print("8-Affiche top3")
    i=int(input()) 
    Affiche(i)
    return
def Affiche(i):
    if i==1:
        afficheMatriceBinaire()
    if i==2:
        afficheSimilarProduits()
    if i==3:
        afficheSimilarUser()
    if i==4:
        afficheTableUser()
    if i==5:
        afficheMatriceUserNote()
    if i==6:
        afficheMatriceUserUser()
    if i==7:
        afficheTableNote()
    if i==8:
        afficheTop3()
    else:
        afficheMenu()
        
    return(i)
afficheMenu()