# coding: utf-8
from random import shuffle
import pygame
import math
import os

AZUL = (0, 0, 255)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
CINZA = (0, 128, 128)


class Criatura:

    def __init__(self, sprite, pos_x, pos_y, velocidade=20):
        self.sprite = sprite
        self.rect = sprite.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.velocidade = velocidade
        self.ativo = True

    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= self.velocidade

    def move_right(self):

        if self.rect.right < 1090:
            self.rect.x += self.velocidade

    def shot(self, path):
        sprite = pygame.transform.scale(pygame.image.load(path), (20,10))
        projetil = Projetil(sprite, self.rect.midtop, 1)
        return projetil

    def move_down(self):
        pass

    def __str__(self):
        return "Criatura em (%s, %s)" % (self.rect.x, self.rect.y)
    
    
class Projetil():

    def __init__(self, sprite, pos_xy, direcao):
        self.sprite = sprite
        self.rect = sprite.get_rect()
        self.rect.x = pos_xy[0] - 10
        self.rect.y = pos_xy[1] - 6
        self.direcao = direcao
        self.velocidade = 6 * direcao

    def draw(self, fundo):
        fundo.blit(self.sprite, self.rect)
        pygame.display.update()
        self.rect.y -= self.velocidade


class SpaceInvaders():
    def __init__(self):
        # Definindo os caminhos dos arquivos necessários para o jogo
        self.DIRETORIO = os.getcwd()
        self.TIRO = None
        self.LARGURA_TELA = 800
        self.ALTURA_TELA = 600
        self.JANELA = pygame.display.set_mode((self.LARGURA_TELA, self.ALTURA_TELA))
        pygame.display.set_caption("Space Invaders")

        # Criando um objeto do tipo pygame.font.Font, onde é passada a fonte e o tamanho
        # se a fonte for passada como None é utilizada a padrão do sistema.
        self.FONTE = pygame.font.Font(self.DIRETORIO + "/fonts/space_invaders.ttf", 60)
        self.BACKGROUND = pygame.transform.scale(pygame.image.load(self.DIRETORIO + "/images/back.png"), (1200, 900))
        self.SPRITE_NAVE = pygame.transform.scale(pygame.image.load(self.DIRETORIO + "/images/new/ship.png"), (50, 50))
        self.NAVE = Criatura(self.SPRITE_NAVE, (self.LARGURA_TELA) / 2, (self.ALTURA_TELA-60))
        self.CLOCK = pygame.time.Clock()
        self.MATRIZ_DE_INIMIGOS = [[], [], [], [], []]
        self.LINHA_DE_TIRO = []

    def tela_inicial(self):
        """
        Criação de outro objeto Surface. O primeiro parâmetro é o texto que será inserido,
        em seguida um booleano indicando se deve ou não suavizar (isso dá a sensação que
        a imagem é lisa), o terceiro parâmetro é a cor do texto e o último a cor de fundo do texto.
        """
        menu = True

        musica_menu = pygame.mixer.Sound(self.DIRETORIO + "/sounds/menu.wav")
        musica_menu.play(-1)

        self.JANELA.fill((0, 0, 0))
        texto = self.FONTE.render("SPACE INVADERS", True, VERDE)
        self.JANELA.blit(texto, [(self.LARGURA_TELA - 550) / 2, 0])
        self.FONTE = pygame.font.Font(self.DIRETORIO + "/fonts/space_invaders.ttf", 30)
        comando1 = self.FONTE.render(" ENTER ou I: INICIA ", True, BRANCO, AZUL)
        comando2 = self.FONTE.render(" ESC ou S: ENCERRA", True, BRANCO, AZUL)
        self.JANELA.blit(comando1, ((self.LARGURA_TELA - 550) / 2, self.ALTURA_TELA - 100))
        self.JANELA.blit(comando2, ((self.LARGURA_TELA - 550) / 2, self.ALTURA_TELA - 50))
        pygame.display.update()

        while menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    musica_menu.stop()
                    return False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if ((x >= ((self.LARGURA_TELA - 550) / 2)) and (y >= (self.ALTURA_TELA - 100))) and ((x <= (self.LARGURA_TELA - 340)) and (y <= (self.ALTURA_TELA - 55))):
                        self.inicia_inimigos()
                        musica_menu.stop()
                        return True
                    if ((x >= ((self.LARGURA_TELA - 550) / 2)) and (y >= (self.ALTURA_TELA - 50))) and ((x <= (self.LARGURA_TELA - 340)) and (y <= (self.ALTURA_TELA - 10))):
                        musica_menu.stop()
                        return False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_i or event.key == pygame.K_RETURN:
                        self.inicia_inimigos()
                        musica_menu.stop()
                        return True
                    if event.key == pygame.K_s or event.key == pygame.K_ESCAPE:
                        musica_menu.stop()
                        return False

    def inicia_inimigos(self):

        x = 20
        y = 40
        tipos_de_inimigos = []

        for i in xrange(1, 8):
            tipos_de_inimigos.append(pygame.image.load(self.DIRETORIO + ("/images/new/test%d.png" % (i % 2))))

        for j in xrange(len(self.MATRIZ_DE_INIMIGOS)):
            linha = self.MATRIZ_DE_INIMIGOS[j]

            for i in xrange(8):
                sprite = pygame.transform.scale(tipos_de_inimigos[j], (40, 40))
                linha.append(Criatura(sprite, x, y))

                x += 50

            y += 40
            x = 20

        for i in xrange(len(self.MATRIZ_DE_INIMIGOS[-1])):
            self.LINHA_DE_TIRO.append( [self.MATRIZ_DE_INIMIGOS[-1][i], (len(self.MATRIZ_DE_INIMIGOS)-1, i) ] )

    def exibe_inimigos(self):
        for linha in self.MATRIZ_DE_INIMIGOS:
            for inimigo in linha:
                if inimigo.ativo:
                    self.JANELA.blit(inimigo.sprite, inimigo.rect)

    def update(self):
        self.JANELA.blit(self.BACKGROUND, (0, 0))
        self.exibe_inimigos()
        self.JANELA.blit(self.NAVE.sprite, self.NAVE.rect)
        self.tiro()
        self.move_inimigos_lateral(1)
        self.CLOCK.tick(60)
        pygame.display.update()

    def tiro(self):
        if self.TIRO is not None:
            self.TIRO.draw(self.JANELA)

            for dado in self.LINHA_DE_TIRO:
                inimigo = dado[0]
                linha, coluna = dado[1]
                if self.TIRO.rect.colliderect(inimigo.rect):
                    
                    self.LINHA_DE_TIRO.remove(dado)
                    if linha > 0:
                        self.LINHA_DE_TIRO.append( [self.MATRIZ_DE_INIMIGOS[linha-1][coluna], (linha-1,coluna)] )
                    
                    self.MATRIZ_DE_INIMIGOS[linha][coluna].rect.x = -100
                    self.MATRIZ_DE_INIMIGOS[linha][coluna].ativo = False
                    self.TIRO = None
                    break

            if (self.TIRO is not None and self.TIRO.rect.y < 0):
                self.TIRO = None


    def move_inimigos_lateral(self, direcao):
        for i in xrange(len(self.MATRIZ_DE_INIMIGOS[0]) -1, -1, -1):
            for j in xrange(len(self.MATRIZ_DE_INIMIGOS)):
                inimigo = self.MATRIZ_DE_INIMIGOS[j][i]
                if inimigo is not None:
                    inimigo.rect.x += direcao

    def main(self):
        # Variável necessária para que o loop onde o jogo ocorre dure o tempo necessário.
        run = True
        menu = True
        while run:

            if menu:
                comando = self.tela_inicial()
                if comando:
                    menu = False
                    self.inicia_inimigos()
                else:
                    run = False

            else:
                # Coletando os eventos que o usuário está realizando

                for event in pygame.event.get():
                    # Verificando se o usuário clicou na opção de fechar a janela.
                    if event.type == pygame.QUIT:
                        run = False

                    # Verificando se o usuário pressionou em alguma tecla.
                    if event.type == pygame.KEYDOWN:

                        if ((event.key == pygame.K_UP or event.key == pygame.K_SPACE) and self.TIRO == None):
                            self.TIRO = self.NAVE.shot(self.DIRETORIO + "/images/laser.png")
                            self.update()
                        # Se a tecla pressionada for a seta para direita, move a NAVE para a direita.
                        if event.key == pygame.K_RIGHT:
                            self.NAVE.move_right()

                        # Se a tecla pressionada for a seta para esquerda, move a NAVE para a esquerda.
                        elif event.key == pygame.K_LEFT:
                            self.NAVE.move_left()

                self.update()
                print (self.NAVE.rect.left), (self.NAVE.rect.right)

if __name__ == "__main__":
    # Comando necessário para se inicializar os módulos do Pygame
    pygame.init()
    game = SpaceInvaders()
    game.main()
    # Comando que encerra os módulos do Pygame
    pygame.quit()
