import pygame, sys
from config import *
from sprites import Barra, Bola
from inicial import tela_inicial

# Inicializa o Pygame
pygame.init()
pygame.mixer.init()  # Inicializa o mixer de áudio

# Carrega a música de fundo e o efeito sonoro
pygame.mixer.music.load('assets/PinkFloyd.mp3')
pygame.mixer.music.play(-1)  # Reproduz em loop

pygame.display.set_caption('Pong')
clock = pygame.time.Clock()
hit_sound = pygame.mixer.Sound('assets/ImpactSound.mp3')

# Inicializa as barras e a bola
barra_esquerda = Barra(50, ALTURA_JANELA // 2 - ALTURA_BARRAS // 2)
barra_direita = Barra(LARGURA_JANELA - 50 - LARGURA_BARRAS, ALTURA_JANELA // 2 - ALTURA_BARRAS // 2)
bola = Bola()

# Pontuação
pontos_esquerda = 0
pontos_direita = 0
font = pygame.font.Font(None, 74)

# Carregando a imagem de fundo
imagem_fundo = pygame.image.load('assets/sunrise.jpg')

# Carrega o som de pontuação
point_sound = pygame.mixer.Sound('assets/PointSound.mp3')

# Loop principal do jogo
fgExit = False
while not fgExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fgExit = True

    # Movimentação das barras
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        barra_esquerda.mover(up=True)
    if keys[pygame.K_s]:
        barra_esquerda.mover(up=False)
    if keys[pygame.K_UP]:
        barra_direita.mover(up=True)
    if keys[pygame.K_DOWN]:
        barra_direita.mover(up=False)

    # Movimentação da bola
    bola.mover()

    # Colisão com as barras
    if bola.rect.colliderect(barra_esquerda.rect) or bola.rect.colliderect(barra_direita.rect):
        bola.speed_x = -bola.speed_x
        hit_sound.play()  # Toca o efeito sonoro ao colidir

    # Colisão com o topo e fundo
    if bola.rect.top <= 0 or bola.rect.bottom >= ALTURA_JANELA:
        bola.speed_y = -bola.speed_y

    # Verifica se a bola saiu da tela
    if bola.rect.left <= 0:
        pontos_direita += 1
        point_sound.play()  # Toca o som de pontuação
        bola = Bola()  # Reinicia a bola
    if bola.rect.right >= LARGURA_JANELA:
        pontos_esquerda += 1
        point_sound.play()  # Toca o som de pontuação
        bola = Bola()  # Reinicia a bola

    # Atualiza a tela
    tela = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))
    tela.blit(imagem_fundo, (0, 0))  # Desenha a imagem de fundo
    pygame.draw.rect(tela, BRANCO, barra_esquerda.rect)
    pygame.draw.rect(tela, BRANCO, barra_direita.rect)
    pygame.draw.ellipse(tela, BRANCO, bola.rect)

    # Desenha a pontuação
    texto = font.render(f"{pontos_esquerda} - {pontos_direita}", True, BRANCO)
    tela.blit(texto, (LARGURA_JANELA // 2 - texto.get_width() // 2, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()