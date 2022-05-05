import pygame
class Hero():
    # Charger les images et les redimensionner
    anim_atk = pygame.image.load("Sprites/Hero/Attack.png")
    resize_atk = pygame.transform.scale(anim_atk, (192, 192))
    anim_dmg = pygame.image.load("Sprites/Hero/Damage.png")
    resize_dmg = pygame.transform.scale(anim_dmg, (192, 192))
    anim_idle = pygame.image.load("Sprites/Hero/Idle.png")
    resize_idle = pygame.transform.scale(anim_idle, (192, 192))
    anim_spe = pygame.image.load("Sprites/Hero/Special.png")
    resize_spe = pygame.transform.scale(anim_spe, (192, 192))
    anim_vict = pygame.image.load("Sprites/Hero/Victory.png")
    resize_vict = pygame.transform.scale(anim_vict, (192, 192))
	
    x = 550
    y = 220
    def animation(x,y):
        screen.blit(resize_idle, (x, y))


class Cyber_boss():
    # Charger les images et les redimensionner
    anim_atk = pygame.image.load("Sprites/Cyberpunk_Boss/BossC_atk.png")
    resize_atk = pygame.transform.scale(anim_atk, (300, 300))
    anim_dmg = pygame.image.load("Sprites/Cyberpunk_Boss/BossC_dmg.png")
    resize_dmg = pygame.transform.scale(anim_dmg, (300, 300))
    anim_idle = pygame.image.load("Sprites/Cyberpunk_Boss/BossC_Idle.png")
    resize_idle = pygame.transform.scale(anim_idle, (300, 300))

    x = 940
    y = 220
    def animation():
        screen.blit(resize_idle, (x, y))



class Cyber_ennemy():
	# Charger les images et les redimensionner
    anim_atk = pygame.image.load("Sprites/Cyberpunk/attack.png")
    resize_atk = pygame.transform.scale(anim_atk, (192, 192))
    anim_dmg = pygame.image.load("Sprites/Cyberpunk/damage.png")
    resize_dmg = pygame.transform.scale(anim_dmg, (192, 192))
    anim_idle = pygame.image.load("Sprites/Cyberpunk/idle.png")
    resize_idle = pygame.transform.scale(anim_idle, (192, 192))
	
    x = 940
    y = 220
    def animation():
        screen.blit(resize_idle, (x, y))
       


class Knight_boss():
    # Charger les images et les redimensionner
    anim_atk = pygame.image.load("Sprites/Knight_Boss/BossK_atk.png")
    resize_atk = pygame.transform.scale(anim_atk, (300, 300))
    anim_dmg = pygame.image.load("Sprites/Knight_Boss/BossK_dmg.png")
    resize_dmg = pygame.transform.scale(anim_dmg, (300, 300))
    anim_idle = pygame.image.load("Sprites/Knight_Boss/BossK_Idle.png")
    resize_idle = pygame.transform.scale(anim_idle, (300, 300))

    x = 940
    y = 120
    def animation():
        screen.blit(resize_idle, (x, y))


class Knight_ennemy():
    # Charger les images et les redimensionner
    anim_atk = pygame.image.load("Sprites/Cyberpunk/attack.png")
    resize_atk = pygame.transform.scale(anim_atk, (192, 192))
    anim_dmg = pygame.image.load("Sprites/Cyberpunk/damage.png")
    resize_dmg = pygame.transform.scale(anim_dmg, (192, 192))
    anim_idle = pygame.image.load("Sprites/Cyberpunk/idle.png")
    resize_idle = pygame.transform.scale(anim_idle, (192, 192))

    x = 940
    y = 220
    def animation():
        screen.blit(resize_idle, (x, y))


class Steam_boss():
    # Charger les images et les redimensionner
    anim_atk = pygame.image.load("Sprites/Steampunk_Boss/BossS_atk.png")
    resize_atk = pygame.transform.scale(anim_atk, (300, 300))
    anim_dmg = pygame.image.load("Sprites/Steampunk_Boss/BossS_dmg.png")
    resize_dmg = pygame.transform.scale(anim_dmg, (300, 300))
    anim_idle = pygame.image.load("Sprites/Steampunk_Boss/BossS_Idle.png")
    resize_idle = pygame.transform.scale(anim_idle, (300, 300))

    x = 940
    y = 220
    def animation():
        screen.blit(resize_idle, (x, y))


class Steam_ennemy():
    # Charger les images et les redimensionner
    anim_atk = pygame.image.load("Sprites/Steampunk/attack.png")
    resize_atk = pygame.transform.scale(anim_atk, (192, 192))
    anim_dmg = pygame.image.load("Sprites/Steampunk/damage.png")
    resize_dmg = pygame.transform.scale(anim_dmg, (192, 192))
    anim_idle = pygame.image.load("Sprites/Steampunk/idle.png")
    resize_idle = pygame.transform.scale(anim_idle, (192, 192))

    x = 940
    y = 220
    def animation():
        screen.blit(resize_idle, (x, y))
