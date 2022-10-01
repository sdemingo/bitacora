#!/usr/bin/env python3

import lorem
import random
import os
from string import Template
from bs4 import BeautifulSoup
from pathlib import Path


#
# Script para generar ficheros con contenido aleatorio
# tanto en formato HTML como en formato Markdown
#


#
# Crea una fecha aleatoria en formato string
#
def createRandomDateString():
    randay=str(random.randrange(1,30)).zfill(2)
    randmonth=str(random.randrange(1,12)).zfill(2)
    randyear=str(random.randrange(2017,2022))
    return randyear+randmonth+randay


#
# Retorna una palabra aleatoria del lorem ipsum
#
def createRandomWord():
    return lorem.sentence().split(" ")[0].lower()


#
# Crea un fichero html random
#
def createHTMLFile(name):
    randtitle=lorem.sentence()
    randpar=random.randrange(5)+2;
    
    s="<html>\n"
    s=s+"<head><title>"+randtitle+"</title></head>\n\n"
    s=s+"<body>\n"
    s=s+"<h1>"+randtitle+"</h1>\n\n"
    for i in range(0,randpar):
        s=s+"<p>\n"+lorem.paragraph()+"\n</p>\n\n"
    s=s+"</body>\n</html>\n"
    
    with open(name,"w") as f:
        f.write(s)
        f.close()
        
#
# Crea una estructura de ficheros html bajo htmltest
# donde cada fichero tendrá el formato de nombre DDMMYYYY.html
#
def createHTMLContent():
    i=0
    for dir in os.listdir("./htmltest"):
        randpages=random.randrange(8)+4
        for i in range(0,randpages):
            id=str(i).zfill(2)
            filename=createRandomDateString()+".html"
            createHTMLFile("./htmltest/"+dir+"/"+filename)



#
# Crea un fichero markdown random
#
def createMDFile(name):
    randtitle=lorem.sentence()
    randpar=random.randrange(5)+2;   

    s="# "+randtitle+"\n\n"
    for i in range(0,randpar):
        s+=lorem.paragraph()+"\n\n"
    with open(name,"w") as f:
        f.write(s)
        f.close()

#
# Crea una estructura de ficheros md bajo mdtest
# donde cada fichero tendrá el una palabara aleatoria 
# como nombre
#
def createMDContent():
    i=0
    for user in os.listdir("./usrtest"):
        randpages=random.randrange(8)+4
        for i in range(0,randpages):
            id=str(i).zfill(2)
            #filename=createRandomWord()+".md"
            filename=createRandomDateString()+".md"
            createMDFile("./usrtest/"+user+"/blog/"+filename)





if __name__=='__main__':
    createMDContent()
