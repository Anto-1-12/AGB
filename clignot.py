import pygame

class clignot:

    def __init__(self, x, y):
        self.resize = pygame.image.load("ball2.png")
        self.image = pygame.transform.scale(self.resize, (50, 50))
        self.rect = self.image.get_rect(x=x, y=y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def draw_hitbox(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)