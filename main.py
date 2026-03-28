from random import randint

import pygame
import time

from Blair import Blair
from Player import Player
from bouton import bouton
from clignot import clignot


class Game:
    def __init__(self, Screen):

        self.Icon = pygame.image.load("ball.png")

        self.gameoverbutton = bouton(2000, 2000, "play_button.png", 69, 100)

        self.Bliarvitesse = 4

        self.tomainscreenbutton = bouton(2000, 2000, "tomainscreenbutton.png", 100, 88)

        self.quitbutton = bouton(2000, 2000, "quit.png", 200, 72)

        self.playbutton = bouton(2000, 2000, "play_button.png", 69, 100)

        self.menubutton = bouton(2000, 2000, "play_button.png", 69, 100)

        self.gameover = bouton(2000, 2000, "ball.png", 50, 50)

        self.mainscreen = True

        self.clignot = clignot(2000, 2000)

        self.seconde = time.time()

        self.second = time.time()

        self.player = Player(620, 648)

        self.screen = Screen

        self.Random1 = randint(0, 1280)
        self.Random2 = randint(0, 1280)
        self.Random3 = randint(0, 1280)
        self.Random4 = randint(0, 1280)
        self.Random5 = randint(0, 1280)

        self.Random6 = randint(0, 720)
        self.Random7 = randint(0, 720)
        self.Random8 = randint(0, 720)
        self.Random9 = randint(0, 720)
        self.Random10 = randint(0, 720)

        self.Blair1 = Blair(self.Random1, self.Random6, self.screen.get_height(), self.Bliarvitesse)
        self.Blair2 = Blair(self.Random1, self.Random7, self.screen.get_height(), self.Bliarvitesse)
        self.Blair3 = Blair(self.Random2, self.Random8, self.screen.get_height(), self.Bliarvitesse)
        self.Blair4 = Blair(self.Random2, self.Random9, self.screen.get_height(), self.Bliarvitesse)
        self.Blair5 = Blair(self.Random3, self.Random10, self.screen.get_height(), self.Bliarvitesse)
        self.Blair6 = Blair(self.Random3, self.Random6, self.screen.get_height(), self.Bliarvitesse)
        self.Blair7 = Blair(self.Random4, self.Random7, self.screen.get_height(), self.Bliarvitesse)
        self.Blair8 = Blair(self.Random4, self.Random8, self.screen.get_height(), self.Bliarvitesse)
        self.Blair9 = Blair(self.Random5, self.Random9, self.screen.get_height(), self.Bliarvitesse)
        self.Blair10 = Blair(self.Random5, self.Random10, self.screen.get_height(), self.Bliarvitesse)

        self.fond = pygame.image.load('fond-ecran.jpg').convert()

        self.screenmenu = pygame.image.load('menu.png').convert()

        self.screenmain = pygame.image.load("mainscreen.png").convert()

        self.is_fullscreen = False
        self.original_width = self.screen.get_width()  # Largeur d'origine de la fenêtre
        self.original_height = self.screen.get_height()  # Hauteur d'origine de la fenêtre

        self.running = True

        self.dev = True

        self.score = 5

        self.level = 0

        self.is_frozen = False

        self.clock = pygame.time.Clock()

        self.menu = False

    def handling_events(self):
        mousePos = pygame.mouse.get_pos()

        pressed = pygame.key.get_pressed()

        if self.score == 0:
            self.gameover = bouton(620, 200, "ball.png", 50, 50)
            self.gameoverbutton = bouton(620, 300, "play_button.png", 69, 100)
            self.player.velocity = [0, 0]

        else:
            self.gameover = bouton(2000, 2000, "ball.png", 50, 50)
            self.gameoverbutton = bouton(2000, 2000, "play_button.png", 69, 100)

        if pressed[pygame.K_0]:
            self.dev = True
        else:
            self.dev = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    self.toggle_fullscreen()  # Appel de la méthode pour basculer le mode plein écran
                if event.key == pygame.K_ESCAPE and self.menu == False and self.mainscreen == False:
                    self.menu = True

                elif event.key == pygame.K_ESCAPE and self.menu == True:
                    self.menu = False

            if self.menu:
                self.menubutton = bouton(620, 310, "play_button.png", 69, 100)
                self.tomainscreenbutton = bouton(600, 600, "tomainscreenbutton.png", 100, 88)

            else:
                self.menubutton = bouton(2000, 2000, "play_button.png", 69, 100)
                self.tomainscreenbutton = bouton(2000, 2000, "tomainscreenbutton.png", 100, 88)

            if self.mainscreen == True:
                self.playbutton = bouton(620, 300, "play_button.png", 69, 100)
                self.quitbutton = bouton(550, 600, "quit.png", 200, 72)

            else:
                self.playbutton = bouton(2000, 2000, "play_button.png", 69, 100)
                self.quitbutton = bouton(2000, 2000, "quit.png", 200, 72)


            if self.tomainscreenbutton.rect.collidepoint(mousePos):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.menubutton = bouton(2000, 2000, "play_button.png", 69, 100)
                        self.tomainscreenbutton = bouton(2000, 2000, "tomainscreenbutton.png", 100, 88)
                        self.mainscreen = True
                        self.menu = False
                        print("pressed")

            if self.quitbutton.rect.collidepoint(mousePos):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.running = False
                        print("pressed")

            if self.playbutton.rect.collidepoint(mousePos):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.playbutton = bouton(2000, 2000, "play_button.png", 69, 100)
                        self.quitbutton = bouton(2000, 2000, "quit.png", 200, 72)
                        self.mainscreen = False
                        print("pressed")

            if self.menubutton.rect.collidepoint(mousePos):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.menubutton = bouton(2000, 2000, "play_button.png", 69, 100)
                        self.tomainscreenbutton = bouton(2000, 2000, "tomainscreenbutton.png", 100, 88)
                        self.menu = False
                        print("pressed")

            if self.gameoverbutton.rect.collidepoint(mousePos):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.gameover = bouton(2000, 2000, "ball.png", 50, 50)
                        self.gameoverbutton = bouton(2000, 2000, "play_button.png", 69, 100)
                        self.tomainscreenbutton = bouton(2000, 2000, "tomainscreenbutton.png", 100, 88)
                        self.score = 5
                        self.level = 0
                        self.Bliarvitesse = 4
                        self.Blair1 = Blair(self.Blair1.rect.x, self.Blair1.rect.y, self.screen.get_height(), self.Bliarvitesse)
                        self.Blair2 = Blair(self.Blair2.rect.x, self.Blair2.rect.y, self.screen.get_height(), self.Bliarvitesse)
                        self.Blair3 = Blair(self.Blair3.rect.x, self.Blair3.rect.y, self.screen.get_height(), self.Bliarvitesse)
                        self.Blair4 = Blair(self.Blair4.rect.x, self.Blair4.rect.y, self.screen.get_height(), self.Bliarvitesse)
                        self.Blair5 = Blair(self.Blair5.rect.x, self.Blair5.rect.y, self.screen.get_height(), self.Bliarvitesse)
                        self.Blair6 = Blair(self.Blair6.rect.x, self.Blair6.rect.y, self.screen.get_height(), self.Bliarvitesse)
                        self.Blair7 = Blair(self.Blair7.rect.x, self.Blair7.rect.y, self.screen.get_height(), self.Bliarvitesse)
                        self.Blair8 = Blair(self.Blair8.rect.x, self.Blair8.rect.y, self.screen.get_height(), self.Bliarvitesse)
                        self.Blair9 = Blair(self.Blair9.rect.x, self.Blair9.rect.y, self.screen.get_height(), self.Bliarvitesse)
                        self.Blair10 = Blair(self.Blair10.rect.x, self.Blair10.rect.y, self.screen.get_height(), self.Bliarvitesse)
                        print("pressed")

    def toggle_fullscreen(self):
        self.is_fullscreen = not self.is_fullscreen
        if self.is_fullscreen:
            self.screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((1280, 720))

    def update(self):

        level = self.level + 1

        current_time = pygame.time.get_ticks()

        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()

        pressed = pygame.key.get_pressed()

        if self.is_frozen:
            if current_time - self.freeze_start_time >= 1000:  # Si le temps écoulé dépasse 1 seconde (1000 millisecondes)
                self.is_frozen = False  # Réactiver le mouvement du joueur
                self.clignot = clignot(2000, 2000)
        elif not self.score == 0:

            if pressed[pygame.K_LEFT]:
                self.player.velocity[0] = -1
            elif pressed[pygame.K_RIGHT]:
                self.player.velocity[0] = 1
            else:
                self.player.velocity[0] = 0
            if pressed[pygame.K_UP]:
                self.player.velocity[1] = -1
            elif pressed[pygame.K_DOWN]:
                self.player.velocity[1] = 1
            else:
                self.player.velocity[1] = 0

        if pressed[pygame.K_DELETE]:
            self.running = False

        if self.player.touchtop:
            self.player = Player(620, 648)
            self.score = self.score + 2
            self.level = self.level + 1

        if self.level == level:
            self.Bliarvitesse = self.Bliarvitesse + 0.5
            self.Blair1 = Blair(self.Blair1.rect.x, self.Blair1.rect.y, self.screen.get_height(), self.Bliarvitesse)
            self.Blair2 = Blair(self.Blair2.rect.x, self.Blair2.rect.y, self.screen.get_height(), self.Bliarvitesse)
            self.Blair3 = Blair(self.Blair3.rect.x, self.Blair3.rect.y, self.screen.get_height(), self.Bliarvitesse)
            self.Blair4 = Blair(self.Blair4.rect.x, self.Blair4.rect.y, self.screen.get_height(), self.Bliarvitesse)
            self.Blair5 = Blair(self.Blair5.rect.x, self.Blair5.rect.y, self.screen.get_height(), self.Bliarvitesse)
            self.Blair6 = Blair(self.Blair6.rect.x, self.Blair6.rect.y, self.screen.get_height(), self.Bliarvitesse)
            self.Blair7 = Blair(self.Blair7.rect.x, self.Blair7.rect.y, self.screen.get_height(), self.Bliarvitesse)
            self.Blair8 = Blair(self.Blair8.rect.x, self.Blair8.rect.y, self.screen.get_height(), self.Bliarvitesse)
            self.Blair9 = Blair(self.Blair9.rect.x, self.Blair9.rect.y, self.screen.get_height(), self.Bliarvitesse)
            self.Blair10 = Blair(self.Blair10.rect.x, self.Blair10.rect.y, self.screen.get_height(), self.Bliarvitesse)


        if self.player.rect.colliderect(self.Blair1.rect) or self.player.rect.colliderect(self.Blair2.rect) or self.player.rect.colliderect(self.Blair3.rect) or self.player.rect.colliderect(self.Blair4.rect) or self.player.rect.colliderect(self.Blair5.rect) or self.player.rect.colliderect(self.Blair6.rect) or self.player.rect.colliderect(self.Blair7.rect)or self.player.rect.colliderect(self.Blair8.rect) or self.player.rect.colliderect(self.Blair9.rect) or self.player.rect.colliderect(self.Blair10.rect):
            self.player = Player(620, 648)
            self.is_frozen = True  # Indiquer que le joueur est gelé
            self.freeze_start_time = pygame.time.get_ticks()
            self.clignot = clignot(self.player.rect.x, self.player.rect.y)
            self.score = self.score - 1



        self.player.move(screen_width, screen_height)
        self.Blair1.move(screen_width, screen_height)
        self.Blair2.move(screen_width, screen_height)
        self.Blair3.move(screen_width, screen_height)
        self.Blair4.move(screen_width, screen_height)
        self.Blair5.move(screen_width, screen_height)
        self.Blair6.move(screen_width, screen_height)
        self.Blair7.move(screen_width, screen_height)
        self.Blair8.move(screen_width, screen_height)
        self.Blair9.move(screen_width, screen_height)
        self.Blair10.move(screen_width, screen_height)




    def display(self):
        font = pygame.font.Font(None, 36)
        white = (255, 255, 255)
        x = 50
        y = 50
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()

        score_surface = font.render(f"Score: {self.score}", True, white)
        score_position = (10, 50)

        level_surface = font.render(f"Level: {self.level}", True, white)
        level_position = (10, 10)

        fond_resized = pygame.transform.scale(self.fond, (screen_width, screen_height))
        menu_resized = pygame.transform.scale(self.screenmenu, (screen_width, screen_height))
        main_resized = pygame.transform.scale(self.screenmain, (screen_width, screen_height))

        self.screen.blit(fond_resized, (0, 0))

        self.player.draw(self.screen)

        self.clignot.draw(self.screen)

        self.Blair1.draw(self.screen)
        self.Blair2.draw(self.screen)
        self.Blair3.draw(self.screen)
        self.Blair4.draw(self.screen)
        self.Blair5.draw(self.screen)
        self.Blair6.draw(self.screen)
        self.Blair7.draw(self.screen)
        self.Blair8.draw(self.screen)
        self.Blair9.draw(self.screen)
        self.Blair10.draw(self.screen)


        if self.dev:

            self.player.draw_hitbox(self.screen)

            self.Blair1.draw_hitbox(self.screen)
            self.Blair2.draw_hitbox(self.screen)
            self.Blair3.draw_hitbox(self.screen)
            self.Blair4.draw_hitbox(self.screen)
            self.Blair5.draw_hitbox(self.screen)
            self.Blair6.draw_hitbox(self.screen)
            self.Blair7.draw_hitbox(self.screen)
            self.Blair8.draw_hitbox(self.screen)
            self.Blair9.draw_hitbox(self.screen)
            self.Blair10.draw_hitbox(self.screen)

        self.screen.blit(score_surface, score_position)
        self.screen.blit(level_surface, level_position)

        if self.menu:
            self.screen.blit(menu_resized, (0, 0))

        if self.mainscreen:
            self.screen.blit(main_resized, (0, 0))

        self.menubutton.draw(self.screen)

        self.playbutton.draw(self.screen)

        self.quitbutton.draw(self.screen)

        self.tomainscreenbutton.draw(self.screen)

        self.gameover.draw(self.screen)

        self.gameoverbutton.draw(self.screen)

        if self.dev:

            self.tomainscreenbutton.draw_hitbox(self.screen)
            self.quitbutton.draw_hitbox(self.screen)
            self.playbutton.draw_hitbox(self.screen)
            self.menubutton.draw_hitbox(self.screen)
            self.gameoverbutton.draw_hitbox(self.screen)
            self.gameover.draw_hitbox(self.screen)

        pygame.display.flip()
        self.screen.fill((0, 0, 0))

    def run(self):
        while self.running:
            self.handling_events()
            if not self.menu or not self.mainscreen:
                self.update()
            else:
                pass
            self.display()
            self.clock.tick(60)



pygame.init()
Screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Against the Blairs")
game = Game(Screen)
game.run()
pygame.display.set_icon(game.Icon)
pygame.quit()

