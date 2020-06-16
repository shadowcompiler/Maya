#!/usr/bin/python
# coding:utf-8
def tuto():
    fichier_tuto = open('tuto.txt', 'r')
    lecture_tuto = fichier_tuto.read()
    fichier_tuto.close()
    return lecture_tuto
    
def bienv():
    fichier_bienv = open('welcome.txt', 'r')
    lecture_bienv = fichier_bienv.read()
    fichier_bienv.close()
    return lecture_bienv

def contenu():
    fichier_cont = open('content.txt', 'r')
    lecture_cont = fichier_cont.read()
    fichier_cont.close()
    return lecture_cont
    
def inter():
    fichier_inter = open('quiz.txt', 'r')
    lecture_inter = fichier_inter.read()
    fichier_inter.close()
    return lecture_inter
    
def member():
    fichier_mbr = open('nmembre.txt', 'r')
    lecture_mbr = fichier_mbr.read()
    fichier_mbr.close()
    return lecture_mbr
