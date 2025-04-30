
# Exemplo básico com Pygame
import pygame
pygame.init()

tela = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Jogo com Pygame")

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

pygame.quit()
