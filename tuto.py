#!/usr/bin/python
# coding:utf-8
def File():
    fichier = open('tuto.txt', 'r')
    lecture = fichier.read()
    fichier.close()
    return lecture
