# sprites.py

import pygame
from config import *

class Barra:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, LARGURA_BARRAS, ALTURA_BARRAS)

    def mover(self, up=True):
        if up and self.rect.top > 0:
            self.rect.y -= BARRA_SPEED
        elif not up and self.rect.bottom < ALTURA_JANELA:
            self.rect.y += BARRA_SPEED

class Bola:
    def __init__(self):
        self.rect = pygame.Rect(LARGURA_JANELA // 2 - BOLA_TAMANHO // 2, 
                                 ALTURA_JANELA // 2 - BOLA_TAMANHO // 2, 
                                 BOLA_TAMANHO, BOLA_TAMANHO)
        self.speed_x = 5
        self.speed_y = 5

    def mover(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def colidir(self):
        if self.rect.top <= 0 or self.rect.bottom >= ALTURA_JANELA:
            self.speed_y = -self.speed_y