# coding: utf-8
from criatura import Criatura
from random import choice
import pygame
import os

# Comando necessário para se inicializar os módulos do Pygame
pygame.init()

# Definindo os caminhos dos arquivos necessários para o jogo
DIRETORIO = os.getcwd()
Largura_tela = 1500
Altura_tela = 1000 
JANELA = pygame.display.set_mode((Largura_tela, Altura_tela))
pygame.display.set_caption("Space Invaders")

# Criando um objeto do tipo pygame.font.Font, onde é passada a fonte e o tamanho
# se a fonte for passada como None é utilizada a padrão do sistema.
FONTE = pygame.font.Font(DIRETORIO + "/fonts/space_invaders.ttf", 60) 
BACKGROUND = pygame.image.load(DIRETORIO + "/images/background.jpg")
sprite_tanque = pygame.transform.scale(pygame.image.load(DIRETORIO + "/images/tank.png"), (150,150) )
TANQUE = Criatura(sprite_tanque, (Largura_tela - 140) / 2, (Altura_tela - 120))
CLOCK = pygame.time.Clock()
MATRIX_DE_INIMIGOS = [[],[],[],[],[]]

# Definido cores
VERDE = (0, 255, 0)

"""
Comando que cria um objeto do tipo Surface e permite criar a janela do jogo.
Seu parâmetro é uma tupla (podendo ser uma lista) que indica a largura e a altura,
respectivamente, em pixels.
"""



"""
Criação de outro objeto Surface. O primeiro parâmetro é o texto que será inserido,
em seguida um booleano indicando se deve ou não suavizar (isso dá a sensação que 
a imagem é lisa), o terceiro parâmetro é a cor do texto e o último a cor de fundo do texto.
"""
texto = FONTE.render("SPACE INVADERS", True, VERDE, None)
JANELA.fill( (0,0,0) )
JANELA.blit(texto, [220, 50])

def inicia_inimigos():
    x = y = 0
    inimigosA = []
    inimigosB = []

    for i in xrange(1, 4):
        inimigosA.append(pygame.image.load(DIRETORIO + ("/images/inimigos/alien%d.png" % i)))
        inimigosB.append(pygame.image.load(DIRETORIO + ("/images/inimigos/alien%d.png" % (i+3))))

    for j in xrange(len(MATRIX_DE_INIMIGOS)):
        linha = MATRIX_DE_INIMIGOS[j]
        
        for i in xrange(8):

            if (j % 2):
                sprite = pygame.transform.scale(choice(inimigosA), (100, 90))
                linha.append(Criatura(sprite, x, y))
            
            else:
                sprite = pygame.transform.scale(choice(inimigosB), (85, 85))
                linha.append(Criatura(sprite, x, y))
            
            x += 100
        
        y += 80
        x = 0

def exibe_inimigos():
    for linha in MATRIX_DE_INIMIGOS:
        for inimigo in linha:
            JANELA.blit(inimigo.sprite, inimigo.rect)



def game():
    # Variável necessária para que o loop onde o jogo ocorre dure o tempo necessário
    run = True
    inicia_inimigos()
    while run:
        # Coletando os eventos que o usuário está realizando
        for event in pygame.event.get():
            # Verificando se o usuário clicou na opção de fechar a janela
            if event.type == pygame.QUIT:
                run = False

            # Verificando se o usuário pressionou em alguma tecla.
            if event.type == pygame.KEYDOWN:
                
                # Se a tecla pressionada for a seta para direita, move a TANQUE para a direita.
                if event.key == pygame.K_RIGHT:
                    TANQUE.move_right()
                
                # Se a tecla pressionada for a seta para esquerda, move a TANQUE para a esquerda.
                if event.key == pygame.K_LEFT:
                    TANQUE.move_left()


        
        JANELA.fill((0,255,0))
        exibe_inimigos()
        JANELA.blit(TANQUE.sprite, TANQUE.rect)
        print TANQUE.rect
        pygame.display.update()
        CLOCK.tick(60)

    # Comando que encerra os módulos do Pygame
    pygame.quit()

game()