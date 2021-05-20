import pygame
import random
import time
import sys
import os

def getmoneyonscreen():
    for m in moneylist.values():
        screen.blit(m.image,m.rect)
def getboxesonscreen():
    for b in boxlist.values():
        screen.blit(b.image,b.rect)

def getMousePosition():
    return pygame.mouse.get_pos()

def boxondesk():
    x,y=getMousePosition()
    print(x,"-",y)
    for a,b in boxlist.items():
        width = b.rect[0]
        length=b.rect[1]
        if x >= width and x <= width+79:
            if y >= length and y <= length+39:
                b.rect=[380,425]
                moneyinbox()
                selectboxdesk[0]=True
                selectboxdesk[1] = a
                showmessage("Box", trq, 350, 150)
                showmessage("Selected", trq, 280, 225)
                showmessage("Game is", red, 300, 400)
                showmessage("Starting", red, 299, 475)
                pygame.display.update()
                time.sleep(2)
def selectbox():
    x,y=getMousePosition()
    for a,b in boxList.items():
        en=b.rect[0]
        boy=b.rect[1]
        if x >=en and x <= en+79 and a!=selectboxdesk[1]:
            if y >= boy and y <= boy+39:
                b.rect=[1000,1000]
                moneydel(a)
                showOfferRemineder()
def moneyinbox():
    i=1
    size=20
    while size>0:
        x=random.randint(0,size)
        moneytoKutu[i]=userMoneyList[x-1]
        userMoneyList.remove((userMoneyList[x-1]))
        i+=1
        size-=1
    print(moneytoKutu)
def moneydel(paraKey):
    print(moneytoKutu[int(paraKey)])
    print(moneyList[str(moneytoKutu[int(paraKey)])])
    if int(paraKey) in moneytoKutu.keys():
        moneyList[str(moneytoKutu[int(paraKey)])].rect=[1000,1000]

        x=len(str(moneytoKutu[int(paraKey)]))
        if x>3:
            x*=7
        mesajGoster(str(moneytoKutu[int(paraKey)])+"$", colorMoney, 353-x,260)
        pygame.display.update()
        time.sleep(1)

def showmessage(msg, color,x,y):
    text = font.render(msg, True, color)
    screen.blit(text,[x,y])

def offerCalculator():
    moneys = []
    for a,b in moneyList.items():
        if b.rect!=[1000,1000]:
            moneys.append(int(a))


    maxx=max(moneys)
    minn=min(moneys)
    length=len(moneys)

    if maxx-minn<=minn+2:
        offer=minn+(maxx-minn)/length
    else:
        offer=(maxx-minn)/length
    return offer

gameStep={1:3,
          2:3,
          3:3,
          4:2,
          5:1,
          6:0,}

def showOfferRemineder():
    for a,b in gameStep.items():
        if b>=0 and b!=-1:
            if b ==0:
                offerTime[0]=True
                gameStep[a]=-1
                break
            else:
                print("b=",b)
                showmessage(str(b)+" Step To Offer",red,202,130)
                pygame.display.update()
                time.sleep(1)
                gameStep[a] -= 1
                break

userSelection = [False]
offerTime=[False]
offerSelection=[False]

def showOffer():
    for o in options.values():
        screen.blit(o.image, o.rect)
    x=str(int(offerCalculator()))
    showmessage("! Offer !",red,300,170)
    showmessage(x+" $",colorMoney,300,230)
    pygame.display.update()










