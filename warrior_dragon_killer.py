import pygame
from pygame import *

pygame.init()

info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h
window_pos_x = (screen_width - 1300) // 2
window_pos_y = (screen_height - 625) // 2

fenetre = pygame.display.set_mode([1300, 625], pygame.RESIZABLE)
pygame.display.set_caption("WARRIOR DRAGON KILLER")

texte_surface = pygame.Surface((400, 200))
texte_surface.fill((255, 255, 255))
font = pygame.font.Font(None, 30)

screen_width = fenetre.get_width()
screen_height = fenetre.get_height()

x_hero_percent = 0.6
y_hero_percent = 0.55

x_hero = int(screen_width * x_hero_percent)
y_hero = int(screen_height * y_hero_percent)

class Personnage(pygame.sprite.Sprite):
    def __init__(self,image,position):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect(center=position)
        self.rect.center = position
        self.rect.centerx = position[0]
        self.rect.centery = position[1]
        self.vel = 5
        self.target_x = None
        self.target_y = None
        self.hitbox = self.rect
        self.hitbox.centerx = self.rect.centerx
        self.hitbox.centery = self.rect.centery
        self.hitbox.width = 30
        self.hitbox.height = 30
        
    def move_towards(self):
        dx = self.target_x - self.rect.centerx
        dy = self.target_y - self.rect.centery
        distance = (dx ** 2 + dy ** 2) ** 0.5

        if distance >= self.vel:
            dx = self.vel * dx / distance
            dy = self.vel * dy / distance
        else:
            dx = dx
            dy = dy
        self.rect.centerx += dx
        self.rect.centery += dy

    def move_to(self, new_position):
        self.rect.center = new_position
    def check_collision(self, other_sprite):
        return self.hitbox.colliderect(other_sprite.rect)

class Piece(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect(center=position)
        self.hitbox = self.rect
        self.hitbox.width = 30
        self.hitbox.height = 30

def main():
    clock = pygame.time.Clock()
    run = True

    Hero = Personnage("character.png", [x_hero,y_hero])
    Rocher, Rocher_active = Piece("hitbox.png", [394,140]), True
    Champs, Champs_active = Piece("hitbox.png", [456,175]), True
    Foret, Foret_active = Piece("hitbox.png", [604,239]), True
    Hutte, Hutte_active = Piece("hitbox.png", [727,207]), True
    Phare, Phare_active = Piece("hitbox.png", [727,54]), True
    Port, Port_active = Piece("hitbox.png", [871,236]), True
    Crique, Crique_active = Piece("hitbox.png", [924,440]), True
    Grotte, Grotte_active = Piece("hitbox.png", [843,453]), True
    Village, Village_active = Piece("hitbox.png", [392,386]), True
    Donjon, Donjon_active = Piece("hitbox.png", [507,463]), True
    Lac, Lac_active = Piece("hitbox.png", [366,515]), True
    Recif, Recif_active = Piece("hitbox.png", [462,579]), True
    Plage, Plage_active = Piece("hitbox.png", [640,586]), True
    Spawn, Spawn_active = Piece("hitbox.png", [636,393]) , True
    carte = pygame.image.load("carte.png").convert()
    
    fenetre.blit(carte, [0, 0])
    
    new_size_Hero = (Hero.image.get_width() // 4, Hero.image.get_height() // 4)
    petit_Hero = pygame.transform.scale(Hero.image, new_size_Hero)
    
    fenetre.blit(petit_Hero, [768, 320])
    
    while run:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                Hero.target_x = mouse_pos[0]
                Hero.target_y = mouse_pos[1]
                pixel_color = carte.get_at(Hero.rect.center)
                if pixel_color == (84,157,206):
                    new_position = (200, 300)
                    Hero.move_to((x_hero,y_hero))
                if Hero.hitbox.colliderect(Rocher.rect) and Rocher_active:
                    print("Lieu actuel : Rocher")
                    print("Arthur : J'ai réussi à décoder une partie du code, c'est K21.")
                    print("Petite Fée : Super ! Continuons à chercher les autres parties.")
                    print(" ")
                    Rocher_active = False

                if Hero.hitbox.colliderect(Champs.rect) and Champs_active:
                    print("Lieu actuel : Champs")
                    print("Arthur : J'ai trouvé une autre partie du code, c'est Y3.")
                    print("Petite Fée : Parfait, on avance bien. Allons-y pour la prochaine.")
                    print(" ")
                    Champs_active = False

                if Hero.hitbox.colliderect(Foret.rect) and Foret_active:
                    print("Lieu actuel : Forêt")
                    print("Arthur : La partie suivante est HMH1, j'en suis sûr.")
                    print("Petite Fée : Bien joué ! Il ne nous reste plus qu'à découvrir le reste.")
                    print(" ")
                    Foret_active = False

                if Hero.hitbox.colliderect(Hutte.rect) and Hutte_active:
                    print("Lieu actuel : Hutte")
                    print("Arthur : Regarde, j'ai trouvé une partie du code : CI25.")
                    print("Petite Fée : Fantastique ! Nous sommes presque à mi-chemin.")
                    print(" ")
                    Hutte_active = False

                if Hero.hitbox.colliderect(Phare.rect) and Phare_active:
                    print("Lieu actuel : Phare")
                    print("Arthur : Voici une autre partie du code : Z0W.")
                    print("Petite Fée : Bravo ! Nous progressons rapidement maintenant.")
                    print(" ")
                    Phare_active = False

                if Hero.hitbox.colliderect(Port.rect) and Port_active:
                    print("Lieu actuel : Port")
                    print("Arthur : H29 est la prochaine partie du code.")
                    print("Petite Fée : Parfait, nous sommes proches de la fin.")
                    print(" ")
                    Port_active = False

                if Hero.hitbox.colliderect(Crique.rect) and Crique_active:
                    print("Lieu actuel : Crique")
                    print("Arthur : J'ai découvert une partie du code : D108.")
                    print("Petite Fée : Incroyable ! Nous ne sommes plus qu'à quelques pas du code complet.")
                    print(" ")
                    Crique_active = False

                if Hero.hitbox.colliderect(Grotte.rect) and Grotte_active:
                    print("Lieu actuel : Grotte")
                    print("Arthur : Z5E est la dernière partie du code que nous recherchons.")
                    print("Petite Fée : Nous y sommes presque. Une dernière trouvaille et nous aurons réussi.")
                    print(" ")
                    Grotte_active = False

                if Hero.hitbox.colliderect(Village.rect) and Village_active:
                    print("Lieu actuel : Village")
                    print("Arthur : J'ai réussi à trouver une autre partie du code, c'est K21Y3.")
                    print("Petite Fée : C'est une excellente nouvelle. Nous sommes en bonne voie.")
                    print(" ")
                    Village_active = False

                if Hero.hitbox.colliderect(Lac.rect) and Lac_active:
                    print("Lieu actuel : Lac")
                    print("Arthur : CI25 est la prochaine partie du code.")
                    print("Petite Fée : C'est parfait ! Nous touchons au but.")
                    print(" ")
                    Lac_active = False

                if Hero.hitbox.colliderect(Recif.rect) and Recif_active:
                    print("Lieu actuel : Récif")
                    print("Arthur : Z0W est la partie du code que nous recherchons maintenant.")
                    print("Petite Fée : Bientôt, nous aurons toutes les pièces du puzzle.")
                    print(" ")
                    Recif_active = False

                if Hero.hitbox.colliderect(Plage.rect) and Plage_active:
                    print("Lieu actuel : Plage")
                    print("Arthur : La dernière partie du code est H29.")
                    print("Petite Fée : Félicitations ! Nous avons réussi à reconstituer le code complet.")
                    print(" ")
                    Plage_active = False
                if Hero.hitbox.colliderect(Donjon.rect) and Donjon_active:
                    print("Voix Mystérieuse : Quel... est... le mot... de passe...? ")
                    x = input("")
                    if x == "K21Y3HMH1CI25Z0WPH29D108H61Z5E":
                        print("Voix Mystérieuse : Bien joué... vous... avez trouvé... le... mot de passe...!")
                        print("Victoire...")
                        pygame.quit()
                        Donjon_active = False
                    else:
                        print("Mauvais... mot de passe...")

        if Hero.target_x is not None and Hero.target_y is not None:
            Hero.move_towards()
        

        fenetre.blit(carte, [0, 0])
        fenetre.blit(petit_Hero, (Hero.rect.centerx - petit_Hero.get_width() // 2, Hero.rect.centery - petit_Hero.get_height() // 2))

        pygame.display.update()
        
    pygame.quit()
    
if __name__ == "__main__":
    main()
