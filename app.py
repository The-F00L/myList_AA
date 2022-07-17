from bs4 import BeautifulSoup
import requests
import urllib.request
aktLista=[]
tervLista=[]
felfuggLista=[]
dobottLista=[]
befejezLista=[]

def startUPSETTING():
    print("azonistod:")
    azonsitod=input()
    URL="https://animeaddicts.hu/mylist.php?"+ azonsitod+".anime"
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    headline=str(soup.findAll('td',class_='headline')).split(',')
    akt=int(headline[0].replace('[<td class=\"headline\" colspan=\"6\">Aktuálisak listája (', '').replace(')</td>','').strip())
    terv=int(headline[1].replace('<td class=\"headline\" colspan=\"6\">Tervezettek listája (', '').replace(')</td>','').strip())
    felfugg=int(headline[2].replace('<td class=\"headline\" colspan=\"6\">Felfüggesztettek listája (', '').replace(')</td>','').strip())
    dobott=int(headline[3].replace('<td class=\"headline\" colspan=\"6\">Dobottak listája (', '').replace(')</td>','').strip())
    befejez=int(headline[4].replace('<td class=\"headline\" colspan=\"5\">Befejezettek listája (', '').replace(')</td>]','').strip())

    titlesClean=[]
    titlesRAW=soup.findAll('td',class_='title')
    for x in titlesRAW:
        titlesClean.append(str(x.find('a').contents).replace('[\'','').replace('\']','').replace('[\"','').replace('\"]',''))

    ind=0
    while (ind<akt):
        aktLista.append(titlesClean[ind])
        ind+=1

    ind=akt
    while (ind<terv+akt):
        tervLista.append(titlesClean[ind])
        ind+=1

    ind=terv+akt
    while (ind<terv+akt+felfugg):
        felfuggLista.append(titlesClean[ind])
        ind+=1

    ind=terv+akt+felfugg
    while (ind<terv+akt+felfugg+dobott):
        dobottLista.append(titlesClean[ind])
        ind+=1

    ind=terv+akt+felfugg+dobott
    while (ind<terv+akt+felfugg+dobott+befejez):
        befejezLista.append(titlesClean[ind])
        ind+=1
    menu()

def akt():
    print("Aktualis:")
    for x in aktLista:
        print(x)
    menu()
def terv():
    print("Tervezett:")
    for x in tervLista:
        print(x)
    menu()
def felfuggesztet():
    print("Felfuggesztett:")
    for x in felfuggLista:
        print(x)
    menu()
def dobott():
    print("Dobott:")
    for x in dobottLista:
        print(x)
    menu()
def befejezett():
    print("Befejezett:")
    for x in befejezLista:
        print(x)
    menu()
def kereses():
    print("meg nincs megcsinalva")
    menu()
def menu():
    print("")
    print ("1.Aktualis\n2.Tervezett\n3.Felfuggesztett\n4.Dobott\n5.Befejezett\n6.Kereses\n7.Azonosito megadasa\n0.Kilepes")
    chose=input()
    if(int(chose)==1):akt()
    if(int(chose)==2):terv()
    if(int(chose)==3):felfuggesztet()
    if(int(chose)==4):dobott()
    if(int(chose)==5):befejezett()
    if(int(chose)==6):kereses()
    if(int(chose)==7):startUPSETTING()
menu()