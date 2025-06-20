import pygame
import sys

# Inicialização do pygame
pygame.init()

# Configurações da tela
LARGURA, ALTURA = 800, 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Tela Inicial Pong 25's")

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

# Fonte pixelada (use uma fonte pixelada instalada ou fornecida)
try:
    FONTE = pygame.font.Font("PressStart2P.ttf", 24)  # Baixe e coloque essa fonte na mesma pasta
except:
    FONTE = pygame.font.SysFont("consolas", 24, bold=True)

# Botão
BOTAO_RECT = pygame.Rect(LARGURA//2 - 100, ALTURA//2 - 40, 200, 80)

def desenhar_tela_inicial():
    TELA.fill(PRETO)
    # Botão branco com borda preta
    pygame.draw.rect(TELA, BRANCO, BOTAO_RECT)
    pygame.draw.rect(TELA, PRETO, BOTAO_RECT, 6)
    # Texto "INICIAR"
    texto = FONTE.render("INICIAR", True, PRETO)
    texto_rect = texto.get_rect(center=BOTAO_RECT.center)
    TELA.blit(texto, texto_rect)
    pygame.display.flip()

def tela_inicial():
    while True:
        desenhar_tela_inicial()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if BOTAO_RECT.collidepoint(evento.pos):
                    return  # Sai da tela inicial para iniciar o jogo

tela_inicial()
# Aqui você pode iniciar o jogo de fato
print("Jogo iniciado!")