# -*- coding: utf-8 -*-
"""
Created on Wed May 12 14:57:57 2021

@author: User
"""
import math
import nltk
from nltk.corpus import stopwords
import mysql.connector
import numpy
matriceBinaire=numpy.zeros((0,0))
from nltk.stem.snowball import FrenchStemmer
from scipy import spatial
def similariteCosinus(IdPdt1,IdPdt2):
    return(1-spatial.distance.cosine(matriceBinaire[IdPdt1],matriceBinaire[IdPdt2]))

"""TF = nombreOccurrencesStem / nombreStems"""
def TF(nb_occ,nbstems):
    return nb_occ/nbstems

""" IDF = log( nombreDescriptions / nombreDescriptionsContenantStem )"""
def IDF(nb_descrip,nb_contentstem):
    return math.log(nb_descrip/nb_contentstem)


conn= mysql.connector.connect(host="localhost",user="root",password="",database="cbrs" )
cursor=conn.cursor()
cursor.execute("select * from produit")

produits=cursor.fetchall()
"""print(produits)"""
stop=list(stopwords.words('french'))
stop.extend([".",",",":","!","[","]",";","{","}","*","#",
             "~","?","=","+","`","/","_","-", "’","(",")","'","''"])
DictProduits={}
Dictnbstems={}
"""print("stopwords",stop)"""
ListTotaliteMots=set()
for p in produits:
    idPdt=p[0]
    Description=p[3]
    """print(Description)"""
    mots=nltk.word_tokenize(Description)
    """print(mots)"""
    """séparer les mots"""
    stemmer = FrenchStemmer()
    MotsStems=[]
    for m in mots:
        MotsStems.append(stemmer.stem(m))
    """print(MotsStems)"""
    """la forme basique des mots"""
    
    ListMotsFinal=[]
    for m in MotsStems:
        if m not in stop:
            ListMotsFinal.append(m)
    """print(ListMotsFinal)"""
    ListUniqueMots=set(ListMotsFinal) 
    for m in ListUniqueMots:
        ListTotaliteMots.add(m)
        
    DictProduits[idPdt]=ListUniqueMots
    Dictnbstems[idPdt]=len(ListUniqueMots)
    nb_descrip=16

"""print(ListTotaliteMots)"""
"""print(DictProduits)"""
 
 

matriceBinaire=numpy.zeros((len(DictProduits),len(ListTotaliteMots)))
matricefrequence=numpy.zeros((len(DictProduits),len(ListTotaliteMots)))
"""print(len(DictProduits),len(ListTotaliteMots))"""
ListTotaliteMots=list(ListTotaliteMots)
for i in range(len(DictProduits)):
    j=0
    for m in ListTotaliteMots:
        if m in DictProduits[str(i+1)]:
                matriceBinaire[i][j]=1
        j+=1
    
    t=0
"""   for m in ListTotaliteMots:
               occ=0
               for n in DictProduits[str(i+1)]:
                    for l in DictProduits[str(i+1)]:
                        if n==l:
                            occ+=1
               k=0
               for mot in ListTotaliteMots:
                    if mot in DictProduits[str(i+1)]:
                        k+=1
               if mot in DictProduits[str(i+1)]:
                    matricefrequence[i][t]=TF(occ/Dictnbstems[str(i+1)])*IDF(nb_descrip/k)
                    t+=1

print(matricefrequence)
"""


"""affichage matriceBinaire"""         
def afficheMatriceBinaire():
    print("La matrice Binaire est : \n",matriceBinaire)

"""affichage matriceFrequence"""
def afficheMatriceFrequence():
    print("La matrice frequence  est : \n",matricefrequence)


"""matrice de similarité produits"""
matriceSimilarite=numpy.zeros((len(DictProduits),len(DictProduits)))
for i in  range(len(DictProduits)):
    for j in range(len(DictProduits)):
        matriceSimilarite[i][j]=similariteCosinus(i,j)

"""affiche matrice similarité produit"""
def afficheSimilarProduits():
    print("la matrice de similarité basée sur le contenu : \n",matriceSimilarite)




"""afficher les top3"""   
def afficheTop3():
    for i in range(len(DictProduits)):
        voisin1=-1
        voisin2=-1
        voisin3=-1
        sim1=0
        sim2=0
        sim3=0
        
        j=0
        for sim in matriceSimilarite[i]:
            if sim>sim1 and sim<0.9999:
                sim1=sim
                voisin1=j
            j+=1
        j=0
        for sim in matriceSimilarite[i]:
            if sim>sim2 and sim<0.9999 and sim!=sim1:
                sim2=sim
                voisin2=j
            j+=1
        j=0
        for sim in matriceSimilarite[i]:
            if sim>sim3 and sim<0.9999 and sim!=sim1 and sim!=sim2:
                sim3=sim
                voisin3=j
            j+=1
        
        print("Top1 du produit",str(i+1),"est produit",voisin1+1,"et sa valeur =",sim1)
        print("Top2 du produit",str(i+1),"est produit",voisin2+1,"et sa valeur =",sim2)
        print("Top3 du produit",str(i+1),"est produit",voisin3+1,"et sa valeur = ",sim3,"\n")
        cursor.execute("UPDATE produit SET Top1 = %s WHERE IdPdt = %s ",(str(voisin1+1),str(i+1)))
        cursor.execute("UPDATE produit SET Top2 = %s WHERE IdPdt = %s",(str(voisin2+1),str(i+1)))
        cursor.execute("UPDATE produit SET Top3 = %s WHERE idpdt = %s",(str(voisin3+1),str(i+1)))
        conn.commit()





"""afficher matrice user et note """
nbuser=10
NbArticles=16
matriceNotes=numpy.zeros((nbuser,NbArticles))
matriceNotes=[[3,6,  6,  4,  2,  6,  9,  5,  6,  0, 10,  1,  4, 10,  5,  2],
 [ 1  ,2  ,6  ,4  ,9  ,7  ,0  ,2  ,3  ,3  ,5  ,1  ,5  ,3  ,3  ,5],
 [ 1  ,4  ,3  ,5  ,1 ,10 ,10  ,1 ,10  ,2  ,0  ,5  ,7  ,6  ,7  ,2],
 [ 8  ,0  ,7  ,2  ,2  ,5  ,4  ,9  ,0  ,0  ,6  ,9  ,7  ,8  ,2  ,9],
 [ 4  ,9  ,1  ,6  ,8  ,5  ,8  ,7  ,1  ,4  ,4  ,9  ,8 ,10  ,7 ,10],
 [ 7  ,7  ,5 ,10  ,9  ,6  ,7  ,7  ,9  ,1  ,4  ,6  ,8  ,6  ,4  ,8],
 [ 2  ,1  ,1  ,0  ,1  ,0  ,1  ,9  ,8  ,4  ,3  ,3  ,5  ,0  ,2  ,1],
 [ 0  ,6  ,3  ,4  ,7  ,9  ,5  ,5  ,7  ,6  ,0  ,2  ,9  ,0  ,5  ,1],
 [ 8  ,2  ,3  ,8  ,9  ,5  ,7  ,1  ,6  ,3  ,0  ,4  ,4  ,1  ,9  ,7],
 [ 4  ,8  ,0 ,10 ,10  ,1  ,8  ,5 ,10  ,2  ,2  ,5  ,0  ,9  ,1  ,8]]

"""matrice user note avant la prédiction"""
matriceNotes_avantpred=numpy.zeros((nbuser,NbArticles))
matriceNotes_avantpred=[[3,6,  6,  4,  2,  6,  9,  5,  6,  0, 10,  1,  4, 10,  5,  2],
 [ 1  ,2  ,6  ,4  ,9  ,7  ,0  ,2  ,3  ,3  ,5  ,1  ,5  ,3  ,3  ,5],
 [ 1  ,4  ,3  ,5  ,1 ,10 ,10  ,1 ,10  ,2  ,0  ,5  ,7  ,6  ,7  ,2],
 [ 8  ,0  ,7  ,2  ,2  ,5  ,4  ,9  ,0  ,0  ,6  ,9  ,7  ,8  ,2  ,9],
 [ 4  ,9  ,1  ,6  ,8  ,5  ,8  ,7  ,1  ,4  ,4  ,9  ,8 ,10  ,7 ,10],
 [ 7  ,7  ,5 ,10  ,9  ,6  ,7  ,7  ,9  ,1  ,4  ,6  ,8  ,6  ,4  ,8],
 [ 2  ,1  ,1  ,0  ,1  ,0  ,1  ,9  ,8  ,4  ,3  ,3  ,5  ,0  ,2  ,1],
 [ 0  ,6  ,3  ,4  ,7  ,9  ,5  ,5  ,7  ,6  ,0  ,2  ,9  ,0  ,5  ,1],
 [ 8  ,2  ,3  ,8  ,9  ,5  ,7  ,1  ,6  ,3  ,0  ,4  ,4  ,1  ,9  ,7],
 [ 4  ,8  ,0 ,10 ,10  ,1  ,8  ,5 ,10  ,2  ,2  ,5  ,0  ,9  ,1  ,8]]



def afficheTableNote_avantpred():
    print("La matrice note user produit avant la prédiction :\n",matriceNotes_avantpred)






"""matrice de similarité users"""
matriceSimilariteUser=numpy.zeros((nbuser,nbuser))
for u1 in  range(nbuser):
    for u2 in range(nbuser):
        matriceSimilariteUser[u1][u2]=similariteCosinus(u1,u2)    

def afficheSimilariteUser():
    print("La matrice de similarité user user :\n",matriceSimilariteUser)


def Calcul_notePredite(userrecherche,Articlerecherche):
    voisin1=-1
    voisin2=-1
    sim1=0
    sim2=0
    i=0
    for sim in matriceSimilariteUser[userrecherche]:
        if sim>sim1 and sim<0.9999:
            sim1=sim
            voisin1=i
        i+=1
    """print(sim1)"""
    """print(voisin1)"""
    sim2=0
    
    i=0
    for sim in matriceSimilariteUser[userrecherche]:
        if sim>sim2 and sim<0.9999 and sim!=sim1:
            sim2=sim
            voisin2=i
        i+=1
    """print(sim2)"""
    """print(voisin2)"""
    NotePredite=(sim1*matriceNotes[voisin1][Articlerecherche]+sim2*matriceNotes[voisin2][Articlerecherche])/(sim1+sim2)
    return NotePredite
    
for i in range(nbuser):
    for j in range(NbArticles):
        if matriceNotes[i][j]==0:
            matriceNotes[i][j]=round(Calcul_notePredite(i,j))
            
"""matrice user produit avec les notes predites"""
def afficheTableNote_aprespred():
    print("La matrice note user produit aprés la prédiction : \n",matriceNotes)



def afficheMenu():
    print("1-Affiche MatriceBinaire-")
    print("2-Matrice de similarité des produits")
    print("3-Affiche top3")
    print("4-Affichage matrice des notes avant la prediction")
    print("5-Afichage la similarité des users")
    print("6-Affichage matrice des notes aprés la prediction")
    print("7-Affichage menu principal")
    print("8-Quitter")
    i=int(input()) 
    Affiche(i)
    
    
def Affiche(i):
    if i==1:
        afficheMatriceBinaire()
        afficheMenu()
    if i==2:
        afficheSimilarProduits()
        afficheMenu()
    if i==3:
        afficheTop3()
        afficheMenu()
    if i==4:
        afficheTableNote_avantpred()
        afficheMenu()
    if i==5:
        afficheSimilariteUser()
        afficheMenu()
    if i==6: 
       afficheTableNote_aprespred()
       afficheMenu()
    if i==7:
        afficheMenu()
    elif i==8:
        print("********Aurevoir*******")
        
    return(i)


afficheMenu()


cursor.close()    
    
    

    