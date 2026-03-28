import pygame

class bouton:
    def __init__(self, x, y, b, l, h):
        self.resize = pygame.image.load(b)
        self.image = pygame.transform.scale(self.resize, (l, h))
        self.rect = self.image.get_rect(x=x, y=y)
        self.x = x
        self.y = y

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def draw_hitbox(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)

