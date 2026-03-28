import pygame
import random

class Blair:

    def __init__(self, x, y, screen_height, v):
        self.resize = pygame.image.load("blair.png")
        self.image = pygame.transform.scale(self.resize, (50, 50))
        self.rect = self.image.get_rect(x=x, y=y)
        self.speed = v
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]
        self.screen_height = screen_height
        self.safe_zone_height = 100  # Hauteur de la zone de sécurité en pixels

    def move(self, screen_width, screen_height):
        self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)

        # Vérifier les limites horizontales de l'écran
        if self.rect.left < 0:
            self.rect.left = 0
            self.velocity[0] *= -1  # Inversion de la direction horizontale

        elif self.rect.right > screen_width:
            self.rect.right = screen_width
            self.velocity[0] *= -1  # Inversion de la direction horizontale

        # Vérifier les limites verticales de l'écran
        if self.rect.top < 0:
            self.rect.top = 0
            self.velocity[1] *= -1  # Inversion de la direction verticale

        # Vérifier si Blair1 est dans la zone de sécurité en bas de l'écran
        if self.rect.bottom >= self.screen_height - self.safe_zone_height:
            self.rect.bottom = self.screen_height - self.safe_zone_height
            self.velocity[1] *= -1  # Inversion de la direction verticale

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def draw_hitbox(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)
