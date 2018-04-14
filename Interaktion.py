#http://usingpython.com/dl/StayAlive.py
import tkinter
import pygame
import sys
from pygame.locals import *
import Farben
import Weltkarte
import Koordinaten

class Menu(object):
    def __init__(self, screen, charakter):
        self.screen=screen
        self.charakter=charakter
    def interaktionen(self, charakter):
        INVENTARFONT = pygame.font.Font('customfont.ttf', 19)
        proceed=True
        while proceed:
            pygame.display.update()
            #Weltkarte.clsInventory.showInventory(self)
            #Weltkarte.clsTileMap.showTilemap(self)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                else:
                    #textbackground: background for all craftable values, and collectable values
                    textbackground=pygame.Rect(80,140,100,800)
                    pygame.draw.rect(self.screen, Farben.clsFarben.BLACK, textbackground)
                    craftlabel = INVENTARFONT.render("Craftables: ", 0, Farben.clsFarben.WHITE)
                    exitlabel = INVENTARFONT.render("Zurück", 0, Farben.clsFarben.WHITE)
                    craftbuttonx=100
                    craftbuttony=200
                    exitbutton = pygame.Rect(Koordinaten.clsKoordinaten.BUTTONPOSX, Koordinaten.clsKoordinaten.BUTTONPOSY, Koordinaten.clsKoordinaten.BUTTONWIDTH, Koordinaten.clsKoordinaten.BUTTONWIDTH)
                    #@andre: falsche Größe exitbutton
                    pygame.draw.rect(self.screen, Farben.clsFarben.DARKRED, exitbutton)
                    self.screen.blit(craftlabel, (Koordinaten.clsKoordinaten.INVCRAFTPOSX, Koordinaten.clsKoordinaten.INVCRAFTPOSY))
                    self.screen.blit(exitlabel, (Koordinaten.clsKoordinaten.BUTTONPOSX, Koordinaten.clsKoordinaten.BUTTONPOSY, Koordinaten.clsKoordinaten.BUTTONWIDTH, Koordinaten.clsKoordinaten.BUTTONWIDTH))
                    #@Andre: falsche Position des Labels exitlabel
                    placePosition=Koordinaten.clsKoordinaten.INVPLACEPOS
                    placePositioncoll = 50
                    for item in Weltkarte.collectableres:
                        self.screen.blit(Weltkarte.snippets[item],
                                     (placePositioncoll, Weltkarte.MAPHEIGHT * Weltkarte.TILESIZE + 20))
                        placePositioncoll += 30
                        textObjekt = INVENTARFONT.render(str(Weltkarte.inventory[item]), False, Farben.clsFarben.WHITE,
                                                         Farben.clsFarben.BLACK)
                        self.screen.blit(textObjekt, (placePositioncoll, Weltkarte.MAPHEIGHT * Weltkarte.TILESIZE + 20))
                        placePositioncoll += 50

                    #liste: buttons to be pressed for crafting
                    liste=[0,0,1,2,3]
                    for item in Weltkarte.craftables:
                        #displaying craft snippets

                        #self.screen.blit(Weltkarte.craftsnippets[item],(120, placePosition))
                        self.screen.blit(Weltkarte.snippets[item], (120, placePosition))
                        placePosition += 60
                        #textObjekt = INVENTARFONT.render(str(Weltkarte.inventorycrafts.get(item)), True, Farben.clsFarben.WHITE,Farben.clsFarben.BLACK)
                        textObjekt = INVENTARFONT.render(str(Weltkarte.inventory.get(item)), True, Farben.clsFarben.WHITE,Farben.clsFarben.BLACK)
                        self.screen.blit(textObjekt, (100, placePosition - 40))
                        placePosition += 40
                        craftinglabel = INVENTARFONT.render("Herstellen: Drücke " + str(liste[item]), False, Farben.clsFarben.GOLD)
                        self.screen.blit(craftinglabel, (craftbuttonx + 5, craftbuttony - 1))
                        craftbuttony+=100
                    if event.type == MOUSEBUTTONDOWN:
                        mousepos = event.pos
                        if exitbutton.collidepoint(mousepos):
                            proceed = False
                    if event.type == KEYDOWN:
                        for key in Weltkarte.controls:
                            if (event.key == Weltkarte.controls[key]):
                                if key in Weltkarte.craftrecipes:
                                    canBeMade = True
                                    for i in Weltkarte.craftrecipes[key]:
                                        if Weltkarte.craftrecipes[key][i] > Weltkarte.inventory[i]:
                                            canBeMade = False
                                            break
                                    if canBeMade == True:
                                        for i in Weltkarte.craftrecipes[key]:
                                            Weltkarte.inventory[i] -= Weltkarte.craftrecipes[key][i]
                                            #Weltkarte.inventorycrafts[key] += 1
                                        #print(Weltkarte.inventory[key])
                                        Weltkarte.inventory[key]+=1
                                        #print(Weltkarte.inventory[key])


    def draw(self, screen, charakter):
        # Rect(left, top, width, height)
        buttonwidth = 80
        buttonheigth = 20
        INVENTARFONT = pygame.font.Font('customfont.ttf', 19)
        BG = pygame.Rect(45, 75, 500, 500)
        exitbutton = pygame.Rect(Koordinaten.clsKoordinaten.BUTTONPOSX, Koordinaten.clsKoordinaten.BUTTONPOSY, Koordinaten.clsKoordinaten.BUTTONWIDTH, Koordinaten.clsKoordinaten.BUTTONHEIGTH)
        feedbutton = pygame.Rect(Koordinaten.clsKoordinaten.FEEDBUTTONPOSX, Koordinaten.clsKoordinaten.FEEDBUTTONPOSY, Koordinaten.clsKoordinaten.BUTTONWIDTH, Koordinaten.clsKoordinaten.BUTTONHEIGTH)
        label = INVENTARFONT.render("Zurück", 1, Farben.clsFarben.WHITE)
        feedlabel= INVENTARFONT.render("Füttern", 1, Farben.clsFarben.WHITE)
        proceed = True
        while proceed:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                else:
                    pygame.draw.rect(self.screen, Farben.clsFarben.BLACK, BG)
                    pygame.draw.rect(self.screen, Farben.clsFarben.DARKRED, exitbutton)
                    self.screen.blit(label, (Koordinaten.clsKoordinaten.CHARSHEETPOSX, Koordinaten.clsKoordinaten.CHARSHEETPOSY))
                    actuallevel=INVENTARFONT.render("Level: " + str(charakter.getlevel()), 1, Farben.clsFarben.WHITE)
                    self.screen.blit(actuallevel,(Koordinaten.clsKoordinaten.ACTLVLPOSX, Koordinaten.clsKoordinaten.ACTLVLPOSY))
                    pygame.draw.rect(self.screen, Farben.clsFarben.DARKRED, feedbutton)
                    self.screen.blit(feedlabel, (Koordinaten.clsKoordinaten.FEEDLBLPOSX, Koordinaten.clsKoordinaten.FEEDLBLPOSY))
                    #placePosition = 50
                    #for item in Weltkarte.collectableres:
                    #    self.screen.blit(Weltkarte.snippets[item],
                    #                 (placePosition, Weltkarte.MAPHEIGHT * Weltkarte.TILESIZE + 20))
                    #    placePosition += 30
                    #    textObjekt = INVENTARFONT.render(str(Weltkarte.inventory[item]), True, Farben.clsFarben.WHITE, Farben.clsFarben.BLACK)
                    #    self.screen.blit(textObjekt, (placePosition, Weltkarte.MAPHEIGHT * Weltkarte.TILESIZE + 20))
                    #    placePosition += 35
                    if charakter.animaltype == "baer":
                        if charakter.level<4:
                            image = pygame.image.load('babybear.png').convert()
                            image = pygame.transform.scale(image, (300, 300))
                            self.screen.blit(image, (200, 100))
                        elif charakter.level>=4 and charakter.level<=8:
                            image = pygame.image.load('bearbig.png').convert()
                            image = pygame.transform.scale(image, (300,300))
                            self.screen.blit(image, (200,100))
                        elif charakter.level>8:
                            image = pygame.image.load('bearfinallevel.png').convert()
                            image = pygame.transform.scale(image, (300, 300))
                            self.screen.blit(image, (200, 100))

                    else:
                        pass

                    if event.type == MOUSEBUTTONDOWN:
                        mousepos = event.pos
                        if exitbutton.collidepoint(mousepos):
                            proceed = False
                        if feedbutton.collidepoint(mousepos):
                            self.interaktionen(charakter)

                pygame.display.update()


