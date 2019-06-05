# coding: utf-8
from criatura import Criatura
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
TANQUE = Criatura(pygame.image.load(DIRETORIO + "/images/tank.png"), 436, 590)
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


#JANELA.blit(BACKGROUND, [0,0])
JANELA.fill((0,0,0))

"""
Criação de outro objeto Surface. O primeiro parâmetro é o texto que será inserido,
em seguida um booleano indicando se deve ou não suavizar (isso dá a sensação que 
a imagem é lisa), o terceiro parâmetro é a cor do texto e o último a cor de fundo do texto.
"""
texto = FONTE.render("SPACE INVADERS", True, VERDE, None)
JANELA.blit(texto, [220, 50])


def game():
    # Variável necessária para que o loop onde o jogo ocorre dure o tempo necessário
    run = True
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
        JANELA.blit(TANQUE.sprite, TANQUE.rect)
        pygame.display.update()
        CLOCK.tick(60)

    # Comando que encerra os módulos do Pygame
    pygame.quit()

game()
