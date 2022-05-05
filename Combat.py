from random import choice
from math import pi,cos,sin
import pygame
from pygame.locals import *
from Sprites import *


pygame.init()

screen_W = 1280
screen_H = 720
size = screen_W, screen_H
screen = pygame.display.set_mode(size)
#Charger les images

    #icones
icones_taille = icones_largeur, icones_hauteur = 70,70
image_attaque = pygame.image.load("images/icones/att.png").convert_alpha()
image_attaque = pygame.transform.scale(image_attaque, icones_taille)
image_defense = pygame.image.load("images/icones/def.png").convert_alpha()
image_defense = pygame.transform.scale(image_defense, icones_taille)
image_soin = pygame.image.load("images/icones/heal.png").convert_alpha()
image_soin = pygame.transform.scale(image_soin, icones_taille)
image_special = pygame.image.load("images/icones/spe.png").convert_alpha()
image_special = pygame.transform.scale(image_special, icones_taille)

anim_idle = pygame.image.load("Sprites/Hero/Idle.png")
resize_idle = pygame.transform.scale(anim_idle, (192, 192))

anim_idle2 = pygame.image.load("Sprites/Knight_boss/BossK_idle.png")
resize_idle2 = pygame.transform.scale(anim_idle2, (300, 300))

icones_noms = [(image_attaque,'attaque'),(image_defense, 'defense'),(image_soin, 'soin'),(image_special, 'special')]


    #fond
fond = pygame.image.load("images/icones/fond.jpg").convert_alpha()
fond2 = pygame.image.load("Sprites/Backgrounds/map_chevalier.png").convert_alpha()



nombre_ligne = 5
nombre_colonne = 5

#Différentes actions possibles
def attaque():
    boss.damage(1)


def defense():
    player.defense += 3


def soin():
    player.damage(-3)


def special():
    if  player.special >= 10:
        boss.damage(15)
        player.special = 0
    else:
        player.special +=1




#Event pour capter la souris
def event_souris_combat():
    
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
                sprites = Icone.containers.get_sprites_at(pygame.mouse.get_pos())
                if sprites:
                    if not combat.selection1:
                        combat.selection1 = sprites[0]
                        
                    elif sprites[0] != combat.selection1:
                        combat.selection2 = sprites[0]
                        
                    else:
                        combat.selection1.position_initiale()
                        combat.selection1 = None



#class du joueur
class Player(pygame.sprite.Sprite):

    def __init__(self):
        
        self.health = 100
        self.max_health = 100
        self.special = 0
        self.attack = 10
        self.defense = 0
        

    def damage(self, amount):

        if self.defense >= 10:
            self.health -= amount/2
            self.defense -= 10
        
        elif self.health - amount > amount:
            self.health -= amount

    #creation d'une barre de vie
    def Healthbar(self):
        if self.health > 50:
            healthbar_color = (0,255,0)                #vert
        elif self.health > 25:
            healthbar_color = (255,255,0)              #jaune
        elif self.health > 0:
            healthbar_color = (255,0,0)               #rouge
        else:
            healthbar_color = (96,96,96) 
            self.health = 0
            
        pygame.draw.rect(screen,(69,69,69),(359,4,self.max_health*2+2,27))
        pygame.draw.rect(screen, healthbar_color,(360, 5, self.health*2, 25))
            
    #creation d'une barre de special
    def Specialbar(self):
        if self.special >= 10:
            specialbar_color = (49, 140, 231)
            self.special = 10
        else:
            specialbar_color = (239, 216, 7)
        
        pygame.draw.rect(screen,(69,69,69),(359,38,10*10+2,22))
        pygame.draw.rect(screen, specialbar_color,(360, 39, self.special*10, 20))

#class du boss
class Boss (pygame.sprite.Sprite):

    def __init__(self,heath,attack):
        self.health = heath
        self.max_health = heath
        self.attack = attack

    def damage(self, amount):
    #subir des degats
        self.health -= amount
        #infliger des dégâts
        player.damage(self.attack)
        #vérifier si les points de vie du boss sont égaux ou inférieur a 0
        if self.health <= 0:
            self.remove

    def Healthbar(self):
        if self.health > 50:
            healthbar_color = (0,255,0)                #vert
        elif self.health > 25:
            healthbar_color = (255,255,0)              #jaune
        elif self.health > 0:
            healthbar_color = (255,0,0)               #rouge
        else:
            healthbar_color = (96,96,96) 
            self.health = 0

        pygame.draw.rect(screen,(69,69,69),(screen_W - self.max_health*2-6,4,self.max_health*2+2,27))
        pygame.draw.rect(screen, healthbar_color,(screen_W-self.health*2-5, 5, self.health*2, 25))

#Code inspiré du jeu Bejelewed
#class qui permet la création des icones
class Icone(pygame.sprite.Sprite):
    def __init__(self,indiceColonne,indiceLigne,image,nom):
        pygame.sprite.Sprite.__init__(self,self.containers)

        self.indiceColonne = indiceColonne
        self.indiceLigne = indiceLigne

        self.nom = nom

        self.checkLigne = False
        self.checkColonne = False

        self.imageOriginale = image
        self.rectOriginal = self.imageOriginale.get_rect(x=self.indiceColonne*icones_largeur,y=self.indiceLigne*icones_hauteur)
        
        self.image = image
        self.rect = self.image.get_rect(x=self.indiceColonne*icones_largeur,y=self.indiceLigne*icones_hauteur)

        self.vitesse = 20
        self.angle = 0
        self.deltaX = 0
        self.deltaY = 0

        self.coordArretX = self.rect.x
        self.coordArretY = self.rect.y

        self.angleRotation = 0

    def position_initiale(self):
        """Remet l'icone à sa position initiale."""
        
        self.image = self.imageOriginale
        self.rect = self.image.get_rect(x=self.indiceColonne*icones_largeur,y=self.indiceLigne*icones_hauteur)
        
    def update(self,fadeOut=False,selection=False):
        """Mise a jour des attributs de l'objet."""

        if selection:
            self.image = pygame.transform.scale(self.image,(85,85))
            
        elif fadeOut:
            self.image = pygame.transform.smoothscale(self.image,(self.rect.w-4,self.rect.h-4))
            self.rect = self.image.get_rect(center=self.rectOriginal.center)
            if self.rect.w < 20:
                self.kill()

        else:
            self.deltaX = self.vitesse*cos(self.angle)
            self.deltaY = self.vitesse*sin(self.angle)
            self.rect = self.rect.move((self.deltaX,self.deltaY))

            if self.angle == 0 and self.rect.x > self.coordArretX :
                self.rect.x = self.coordArretX
            elif self.angle == -pi and self.rect.x < self.coordArretX:
                self.rect.x = self.coordArretX
            elif self.angle == -pi/2 and self.rect.y < self.coordArretY:
                self.rect.y = self.coordArretY
            elif self.angle == pi/2 and self.rect.y > self.coordArretY:
                self.rect.y = self.coordArretY

            self.rectOriginal.center = self.rect.center
            self.indiceLigne = self.rect.y/icones_hauteur
            self.indiceColonne = self.rect.x/icones_largeur



#class qui permet de gérer le système de combat
class Combat(object):
    """Classe Plateau qui gère la mise à jour des éléments (déplacements,collision,redessin)."""
    
    def __init__ (self,screen):

        # la surface de dessin correspondant au display
        self.screen = screen

        # les 2 icones sélectionnées
        self.selection1 = None
        self.selection2 = None

        # nombre d'icones réunis
        self.iconesReunies = 0
        
        self.gameOver = False

        # 1 container pour toutes les icones et 1 pour les icones réunis
        Icone.containers = pygame.sprite.LayeredUpdates()        
        self.liste_icones_Reunies = pygame.sprite.Group()

        # 1 liste contenant toutes les icones qui doivent se déplacer, quand elle sera vide on procédera à la recherche de icones réunies
        self.liste_Icones_En_Mouvement = []
        # 1 liste des swap possibles après simulation
        self.listeSwapPossibles = []
        # 1 liste contenant 1 exemplaire de icones pour chaque hauteur de chute qui déclenchera un son quand elle arrivera à destination

        # une surface sur laquelle est dessiné tous les éléments du jeu
        # avant de la bliter dans la surface du display(permet un décalage gauche ou droite du plateau par rapport à une interface)
        self.surface = pygame.Surface((355,355)).convert()

        # une surface pour la grille
        self.surfaceGrille = pygame.Surface((screen_W,screen_H)).convert()
        self.surfaceGrille.set_colorkey((0,0,0))        
        for x in range(nombre_colonne+1):
            pygame.draw.line(self.surfaceGrille,(255,255,255),(x*icones_largeur,0),(x*icones_largeur,nombre_ligne*icones_hauteur),1)
        for y in range(nombre_ligne+1):
            pygame.draw.line(self.surfaceGrille,(255,255,255),(0,y*icones_hauteur),(nombre_colonne*icones_largeur,y*icones_hauteur),1)
            
        # attributs relatif au temps   
        self.tempsActuel = pygame.time.get_ticks()
        self.tempsDebut1sec = pygame.time.get_ticks()


        # création d'icones        
        for ligne in range(nombre_ligne):
            for colonne in range(nombre_colonne):
                choix = choice(icones_noms[:4])
                icone = Icone(colonne,ligne,choix[0],choix[1])
                self.liste_Icones_En_Mouvement.append(icone)                

        # algorithme qui proposera un plateau sans icone réunie
        while not self.listeSwapPossibles:
            icones_En_Mouvement = False
            for icone in self.liste_Icones_En_Mouvement:
                icone.update()
                if not(icone.rect.x == icone.coordArretX and icone.rect.y == icone.coordArretY):
                    icones_En_Mouvement = True
            if not icones_En_Mouvement:
                icone.containers.remove(self.liste_icones_Reunies)
                self.liste_icones_Reunies.empty()
                while self.liste_Icones_En_Mouvement:
                    self.recherche_match(self.liste_Icones_En_Mouvement.pop(0))
                if self.liste_icones_Reunies:
                    self.nouvelles_icones()
                else:
                    self.simulateur()

        self.iconesReunies = 0 # on reset le nombres d'icones réunis par l'algorithme de remplissage

    def update(self):
        """"Mise à jour des éléments du plateau."""

        # si il n'y a plus d'icones en mouvement on attend les clics de sélection
        if not self.liste_Icones_En_Mouvement :
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
            if self.selection1:
                # mise à jour du sprite de la première sélection = rotation
                self.selection1.update(selection=True)
            if self.selection1 and self.selection2:
                self.selection1.position_initiale()                
                decalageH = (abs(self.selection1.rect.centerx-self.selection2.rect.centerx) == icones_largeur and abs(self.selection1.rect.centery-self.selection2.rect.centery) == 0)
                decalageV = (abs(self.selection1.rect.centery-self.selection2.rect.centery) == icones_hauteur and abs(self.selection1.rect.centerx-self.selection2.rect.centerx) == 0)
                if decalageH or decalageV:
                    self.swap_icones(self.selection1,self.selection2)
                    pygame.mouse.set_cursor(*pygame.cursors.diamond)
                else:
                    self.selection1 = self.selection2
                    self.selection2 = None
            else: return
        # si des icones sont en mouvement ce qui est toujours le cas après des match ou lors d'un swap,
        # on fait disparaître les match si il y a, et on déplace les icones du dessus ou les icones
        # sélectionnées lors d'un swap jusqu'à leurs coordonnées d'arrêt.
        # On passe alors en référence chaque icone qui était en mouvement à l'algorithme de recherche de match
        # tout en les retirant de la liste des icones en mouvement
        else:
            # dispariton des icones réunies
            if self.liste_icones_Reunies:
                self.liste_icones_Reunies.update(True)
            # mouvement des icones
            else:
                icones_En_Mouvement = False
                for icone in self.liste_Icones_En_Mouvement:
                    icone.update()                    
                    if not(icone.rect.x == icone.coordArretX and icone.rect.y == icone.coordArretY):
                        icones_En_Mouvement = True
                if not icones_En_Mouvement:
                    # lorsque toutes les icones sont tombées, on force le rafraichissement de l'écran
                    # avant de lancer l'analyse du plateau dans cet état, car en fonction de la taille de celui-ci
                    # la recherche de match et le simulateur peuvent ralentir l'affichage entre l'avant-dernier et le dernier mouvement.                    
                    self.draw()
                    pygame.display.flip()                    
                    while self.liste_Icones_En_Mouvement:
                        self.recherche_match(self.liste_Icones_En_Mouvement.pop(0))
                    if not self.liste_icones_Reunies:
                        # si pas d'match après swap: deswap
                        if self.selection1 and self.selection2:
                           self.swap_icones(self.selection1,self.selection2)
                           self.selection1 = None
                        # si pas d'match après mouvement: simulateur si pas deswap
                        else:
                            if not self.selection2:
                                self.simulateur()
                                self.tempsDebut1sec = pygame.time.get_ticks()
                            else:
                                self.selection2 = None
                    else:
                        # si il y a des match on les remplace
                        self.nouvelles_icones()
                        if self.selection2:
                            self.selection1,self.selection2 = None,None               

    def swap_icones(self,icone1,icone2,simulation=False):
        """Intervertie la position de 2 icones."""

        icone1.coordArretX, icone2.coordArretX = icone2.coordArretX, icone1.coordArretX
        icone1.coordArretY, icone2.coordArretY = icone2.coordArretY, icone1.coordArretY                            
        icone1.indiceColonne, icone2.indiceColonne = icone2.indiceColonne, icone1.indiceColonne
        icone1.indiceLigne, icone2.indiceLigne = icone2.indiceLigne, icone1.indiceLigne
        
        if not simulation:
            icone1.angle,icone2.angle = (icone2.rect.x>icone1.rect.x) and (0,-pi) or (icone2.rect.x<icone1.rect.x) and (-pi,0) or (icone2.rect.y>icone1.rect.y) and (pi/2.,-pi/2.) or (-pi/2.,pi/2.)
            self.liste_Icones_En_Mouvement.append(icone1)
            self.liste_Icones_En_Mouvement.append(icone2)
            
    def nouvelles_icones(self):
        """Crée des icones pour remplacer celles réunies."""
        
        for iconeCourante in self.liste_icones_Reunies:
            ligneNouveauDiam = -1            
            for icone in Icone.containers:
                if icone.indiceColonne == iconeCourante.indiceColonne and icone.indiceLigne < iconeCourante.indiceLigne and icone not in self.liste_icones_Reunies:
                    icone.coordArretY += icones_hauteur
                    if icone.indiceLigne <= ligneNouveauDiam:
                        ligneNouveauDiam = icone.indiceLigne-1
                    if not icone in self.liste_Icones_En_Mouvement:
                        icone.rect.y -= 9
                        icone.angle = pi/2.
                        self.liste_Icones_En_Mouvement.append(icone)

            choix = choice(icones_noms[:4])
            icone = Icone(indiceColonne=iconeCourante.indiceColonne,
                              indiceLigne=ligneNouveauDiam,
                              image=choix[0],nom=choix[1])

            icone.angle = pi/2.
            icone.coordArretY += abs(icone.indiceLigne)*icones_hauteur
            icone.rect.y -= 9
            self.liste_Icones_En_Mouvement.append(icone)

 #Simule tous les swap possibles donnant lieu à un match d'icones.
    def simulateur(self):

        self.listeSwapPossibles = []
        for indiceLigne in range(nombre_ligne):
            for indiceColonne in range(nombre_colonne):
                for iconeCourante in Icone.containers:
                    if iconeCourante.indiceLigne == indiceLigne and iconeCourante.indiceColonne == indiceColonne:                    
                        for icone in Icone.containers:
                            if icone.indiceLigne == iconeCourante.indiceLigne and icone.indiceColonne == iconeCourante.indiceColonne+1:
                                self.swap_icones(iconeCourante,icone,simulation=True)
                                matchTrouve1 = self.recherche_match(iconeCourante,simulation=True)
                                if not matchTrouve1:
                                    matchTrouve2 = self.recherche_match(icone,simulation=True)
                                self.swap_icones(iconeCourante,icone,simulation=True)
                                if matchTrouve1 or matchTrouve2:
                                    self.listeSwapPossibles.append((iconeCourante,icone))
                                    # en mode création ou pendant la partie le premier swap horizontal donne la main au joueur sans tester tous les autres
                                    return

                            elif icone.indiceColonne == iconeCourante.indiceColonne and icone.indiceLigne == iconeCourante.indiceLigne+1:
                                self.swap_icones(iconeCourante,icone,simulation=True)
                                matchTrouve1 = self.recherche_match(iconeCourante,simulation=True)
                                if not matchTrouve1:
                                    matchTrouve2 = self.recherche_match(icone,simulation=True)
                                self.swap_icones(iconeCourante,icone,simulation=True)
                                if matchTrouve1 or matchTrouve2:
                                    self.listeSwapPossibles.append((iconeCourante,icone))
                                    # en mode creation ou pendant la partie le premier swap vertical donne la main au joueur sans tester tous les autres                                    
                                    return


        if not self.listeSwapPossibles:
            self.suppression_ligne()
            
#Algorithme de recherche de match. La iconeReference est envoyées soit par l'update via une itération dans la 'self.liste_Icones_En_Mouvement' soit par le simulateur auquel cas un match suffit pour retourner à son appel.
    def recherche_match(self,iconeReference,simulation=False):
        """Algorithme de recherche de match.
           La iconeReference est envoyées soit par l'update via une itération dans la 'self.liste_Icones_En_Mouvement' soit par le simulateur auquel cas
           un match suffit pour retourner à son appel."""
        
        #--- Recherche en ligne
        # Pour une iconeReference donnée on cherche la icone correspondant à la première colonne de la ligne de cette iconeReference.On passe son booléan 
        # 'checkLigne' à True pour éviter de refaire la recherche sur cette ligne pour une autre iconeReference sur la même ligne et on recherche tous les
        # match possibles sur cette ligne.
        iconeCourante = None    
        for icone in Icone.containers:
            if icone.indiceLigne == iconeReference.indiceLigne and icone.indiceColonne == 0:
                if not icone.checkLigne :
                    iconeCourante = icone
                    if not simulation:
                        icone.checkLigne = True # en mode simulation on se permet de refaire la recherche sur la même ligne 2 fois étant donné qu'il n'y a que 2 icones qui swap à chaque fois
                                                # pour éviter de faire une boucle de remise à zéro des checkLigne pour toutes les icones 
                    tous_match_Ligne = []
                    matchLigne = [iconeCourante]
                    inc = 1
                    while iconeCourante.indiceColonne+inc < nombre_colonne:
                        for icone2 in Icone.containers:
                            if icone2.indiceLigne == iconeCourante.indiceLigne and icone2.indiceColonne == iconeCourante.indiceColonne+inc:
                                if icone2.nom == iconeCourante.nom:
                                    matchLigne.append(icone2)
                                    # en simulation les 3 premières icones réunies horizontalement renvoient vrai au simulateur
                                    if simulation and len(matchLigne)>2:
                                        return True
                                    inc += 1
                                    break
                                else:
                                    tous_match_Ligne.append(matchLigne)
                                    iconeCourante = icone2
                                    matchLigne = [iconeCourante]
                                    inc = 1
                                    break
                    tous_match_Ligne.append(matchLigne)
                    for match in tous_match_Ligne:
                        if len(match) > 2:
                            for icone in match:
                                if not icone in self.liste_icones_Reunies:
                                    self.liste_icones_Reunies.add(icone)
                                    self.iconesReunies += 1
                                    if icone.nom == 'attaque':
                                        print(1)
                                        attaque()
                                    elif icone.nom == 'defense':
                                        print(2)
                                        defense()
                                    elif icone.nom == 'soin':
                                        print(3)
                                        soin()
                                    elif icone.nom == 'special':
                                        print(4)
                                        special()
				    

                    break

        # Recherche en colonne
        # Pour une iconeReference donnée on cherche l'icone correspondant à la première ligne de la colonne de cette iconeReference.On passe son booléan 
        # 'checkColonne' à True pour éviter de refaire la recherche sur cette colonne pour une autre iconeReference sur la même colonne et on recherche tous les
        # match possibles sur cette colonne.
        iconeCourante = None
        for icone in Icone.containers:
            if icone.indiceColonne == iconeReference.indiceColonne and icone.indiceLigne == 0:
                if not icone.checkColonne:
                    iconeCourante = icone
                    if not simulation:
                        icone.checkColonne = True # en mode simulation on se permet de refaire la recherche sur la même colonne 2 fois étant donné qu'il n'y a que 2 icones qui swap à chaque fois
                                                  # pour éviter de faire une boucle de remise à zéro des checkColonne pour toutes les icones 
                    tous_match_Colonne = []
                    matchColonne = [iconeCourante]
                    inc = 1
                    while iconeCourante.indiceLigne+inc < nombre_ligne:
                        for icone2 in Icone.containers:
                            if icone2.indiceColonne == iconeCourante.indiceColonne and icone2.indiceLigne == iconeCourante.indiceLigne+inc:
                                if icone2.nom == iconeCourante.nom:
                                   matchColonne.append(icone2)
                                   # en simulation les 3 premières icones réunies verticalement renvoient vrai au simulateur
                                   if simulation and len(matchColonne)>2:
                                       return True
                                   inc += 1
                                   break
                                else:
                                    tous_match_Colonne.append(matchColonne)
                                    iconeCourante = icone2
                                    matchColonne = [iconeCourante]
                                    inc = 1
                                    break
                    tous_match_Colonne.append(matchColonne)
                    for match in tous_match_Colonne:
                        if len(match) > 2:
                            for icone in match:
                                if not icone in self.liste_icones_Reunies:
                                    self.liste_icones_Reunies.add(icone)
                                    self.iconesReunies += 1
                                    if icone.nom == 'attaque':
                                        print(1)
                                        attaque()
                                    elif icone.nom == 'defense':
                                        print(2)
                                        defense()
                                    elif icone.nom == 'soin':
                                        print(3)
                                        soin()
                                    elif icone.nom == 'special':
                                        print(4)
                                        special()
                                        
                    break

        # lorsque la liste_Icones_En_Mouvement est vide après toutes les itérations 
        if not self.liste_Icones_En_Mouvement and not simulation:
            # on reset les booléens de check
            for icone in Icone.containers:
                icone.checkLigne = False
                icone.checkColonne = False
                
#Supprime une ligne de icones au hazard
    def suppression_ligne(self):

        hasard = choice(range(nombre_ligne))
        for icones in Icone.containers:
            if icones.indiceLigne == hasard:
                self.liste_icones_Reunies.add(icones)

        self.nouvelles_icones()

#Dessin des éléments du jeu dans la surface du plateau, puis dessin de cette surface dans le display.
    def draw(self):

        self.surface.blit(fond,(0,0))
        self.surface.blit(self.surfaceGrille,(0,0))
        Icone.containers.draw(self.surface)
        self.screen.blit(self.surface,(0,0))




player = Player()
boss = Boss(100,6)
combat = Combat(screen)

clock = pygame.time.Clock()

continuer = True
while continuer:
    
    event_souris_combat()
    screen.blit(fond2,(0,0))
    screen.blit(resize_idle,(550,220))
    screen.blit(resize_idle2,(1000,220))
    
    combat.update()
    combat.draw()
    player.Healthbar()
    player.Specialbar()
    boss.Healthbar()
    pygame.display.flip()
    clock.tick(60)
