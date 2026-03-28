import pygame

class Player:
    def __init__(self, x, y):
        self.resize = pygame.image.load("ball.png")
        self.image = pygame.transform.scale(self.resize, (50, 50))
        self.rect = self.image.get_rect(x=x, y=y)
        self.speed = 4
        self.velocity = [0, 0]
        self.touchtop = False
        self.visible = True
        self.hide_duration = 300  # Durée de la disparition en millisecondes
        self.hide_timer = 0

    def move(self, screen_width, screen_height):
        self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)

        # Vérifier les limites horizontales de l'écran
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > screen_width:
            self.rect.right = screen_width

        # Vérifier les limites verticales de l'écran
        if self.rect.top < 0:
            self.rect.top = 0
            self.touchtop = True # si sa touche le top alor vrai

        else:
            self.touchtop = False # si sa touche pas le top alor faux

        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height


    def draw(self, screen):
        if self.visible:
            screen.blit(self.image, self.rect)


    def draw_hitbox(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)


