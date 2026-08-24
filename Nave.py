import pygame
from ElementoJogo import ElementoJogo

class Nave(ElementoJogo):
    def __init__(self, largura_tela, altura_tela, velocidade=6, cor=(25, 25, 112)):
        super().__init__(
            x=largura_tela // 2 - 20,
            y=altura_tela - 60,
            largura=40,
            altura=40,
            cor=cor,
            velocidade=velocidade
        )
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela
        self.vel_x = 0
        self.tiros = []  

    def processar_evento(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key in (pygame.K_LEFT, pygame.K_a):
                self.vel_x = -self.velocidade
            elif evento.key in (pygame.K_RIGHT, pygame.K_d):
                self.vel_x = self.velocidade
            elif evento.key == pygame.K_SPACE:
                self.atirar()
        elif evento.type == pygame.KEYUP:
            if evento.key in (pygame.K_LEFT, pygame.K_a) and self.vel_x < 0:
                self.vel_x = 0
            elif evento.key in (pygame.K_RIGHT, pygame.K_d) and self.vel_x > 0:
                self.vel_x = 0

    def mover(self):
        self.rect.x += self.vel_x
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > self.largura_tela:
            self.rect.right = self.largura_tela

    def atirar(self):
        # TODO 1 Resolvido: Instanciar projétil
        largura_tiro = 4
        altura_tiro = 10
        tiro_x = self.rect.centerx - (largura_tiro // 2)
        tiro_y = self.rect.top
        
        novo_tiro = pygame.Rect(tiro_x, tiro_y, largura_tiro, altura_tiro)
        self.tiros.append(novo_tiro)

    def atualizar_tiros(self):
        # TODO 2 Resolvido: Mover o tiro para cima e limpar da memória
        velocidade_tiro = 15
        for tiro in reversed(self.tiros):
            tiro.y -= velocidade_tiro
            if tiro.bottom < 0:
                self.tiros.remove(tiro)

    def atualizar(self):
        self.mover()
        self.atualizar_tiros()

    def desenhar(self, tela):
        pontos = [
            (self.rect.centerx, self.rect.top),
            (self.rect.left, self.rect.bottom),
            (self.rect.right, self.rect.bottom)
        ]
        pygame.draw.polygon(tela, self.cor, pontos)
        for tiro in self.tiros:
            pygame.draw.rect(tela, (255, 255, 255), tiro)
