import random
import pygame
from ElementoJogo import ElementoJogo

class Asteroid(ElementoJogo):
    def __init__(self, largura_tela, altura_tela, velocidade=5, cor=(200, 50, 50)):
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela
        self.raio = 20

        super().__init__(
            x=0,
            y=0,
            largura=self.raio * 2,
            altura=self.raio * 2,
            cor=cor,
            velocidade=velocidade
        )
        self.iniciar_status()

    def iniciar_status(self):
        self.rect.x = random.randint(0, self.largura_tela - self.rect.width)
        self.rect.y = random.randint(-150, -50)
        self.velocidade = random.randint(3, 7)
        self.vida = 3 

    def mover(self):
        self.rect.y += self.velocidade
        if self.rect.top > self.altura_tela:
            self.iniciar_status()

    def desenhar(self, tela):
        # Controle de cor baseado na vida restante
        if self.vida == 3:
            self.cor = (150, 150, 150) # Cinza (Intacto)
        elif self.vida == 2:
            self.cor = (255, 165, 0)   # Laranja (Danificado)
        elif self.vida == 1:
            self.cor = (255, 0, 0)     # Vermelho (Crítico)
            
        pygame.draw.circle(tela, self.cor, self.rect.center, self.raio)
