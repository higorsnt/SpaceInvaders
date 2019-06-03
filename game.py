# coding: utf-8
import pygame
import os

# Comando necessário para se inicializar os módulos do Pygame
pygame.init()

# Definindo os caminhos dos arquivos necessários para o jogo
DIRETORIO = os.getcwd()
print DIRETORIO

# Criando um objeto do tipo pygame.font.Font, onde é passada a fonte e o tamanho
# se a fonte for passada como None é utilizada a padrão do sistema.
FONTE = pygame.font.Font(DIRETORIO + "/fonts/space_invaders.ttf", 60) 
BACKGROUND = pygame.image.load(DIRETORIO + "/images/background.jpg")
NAVE = pygame.image.load(DIRETORIO + "/images/Ship.png")
RECT = NAVE.get_rect()
CLOCK = pygame.time.Clock()

# Definido cores
VERDE = (0, 255, 0)

"""
Comando que cria um objeto do tipo Surface e permite criar a janela do jogo.
Seu parâmetro é uma tupla (podendo ser uma lista) que indica a largura e a altura,
respectivamente, em pixels.
"""
JANELA = pygame.display.set_mode((1000, 700))
# Colocando um nome para a janela criada
pygame.display.set_caption("Space Invaders")

# Variável necessária para que o loop onde o jogo ocorre dure o tempo necessário
run = True
#JANELA.blit(BACKGROUND, [0,0])
JANELA.fill((0,0,0))
"""
Criação de outro objeto Surface. O primeiro parâmetro é o texto que será inserido,
em seguida um booleano indicando se deve ou não suavizar (isso dá a sensação que 
a imagem é lisa), o terceiro parâmetro é a cor do texto e o último a cor de fundo do texto.
"""
texto = FONTE.render("SPACE INVADERS", True, VERDE, None)
JANELA.blit(texto, [220, 50])

RECT.x = 436
RECT.y = 600

while run:
    # Coletando os eventos que o usuário está realizando
    for event in pygame.event.get():
        # Verificando se o usuário clicou na opção de fechar a janela
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                RECT.x += 15
            if event.key == pygame.K_LEFT:
                RECT.x -= 15

    JANELA.blit(NAVE, RECT)
    pygame.display.flip()
    CLOCK.tick(60)

# Comando que encerra os módulos do Pygame
pygame.quit()