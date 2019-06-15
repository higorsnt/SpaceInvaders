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
DIRECAO = {0:"DIREITA", 1:"ESQUERDA"}
LARGURA_TELA = 800
ALTURA_TELA = 600

class Nave():
    def __init__(self, sprite, pos_x, pos_y, velocidade=5):
        self.sprite = sprite
        self.rect = sprite.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.velocidade = velocidade
        self.ativo = True

    def move_left(self):
        if self.rect.left > self.velocidade:
            self.rect.x -= self.velocidade

    def move_right(self):
        if self.rect.right < (LARGURA_TELA - self.velocidade):
            self.rect.x += self.velocidade

    def shot(self, path):
        sprite = pygame.transform.scale(pygame.image.load(path), (ALTURA_TELA / 30, LARGURA_TELA / 80))
        projetil = Projetil(sprite, self.rect.midtop, 1)
        return projetil

    def __str__(self):
        return "Nave em (%s, %s)" % (self.rect.x, self.rect.y)

class Invasores():

    def __init__(self, sprite, pos_x, pos_y, velocidade=20):
        self.sprite = sprite
        self.rect = sprite.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.velocidade = velocidade
        self.direcao = DIRECAO[0]
        self.ativo = True

    def shot(self, path):
        sprite = pygame.transform.scale(pygame.image.load(path), (ALTURA_TELA / 30, LARGURA_TELA / 80))
        projetil = Projetil(sprite, self.rect.midtop, 1)
        return projetil

    def move_down(self):
        pass

    def __str__(self):
        return "Invasores em (%s, %s)" % (self.rect.x, self.rect.y)
    
    
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
        self.JANELA = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
        pygame.display.set_caption("Space Invaders")

        # Criando um objeto do tipo pygame.font.Font, onde é passada a fonte e o tamanho
        # se a fonte for passada como None é utilizada a padrão do sistema.
        self.FONTE = pygame.font.Font(self.DIRETORIO + "/fonts/space_invaders.ttf", 60)
        self.BACKGROUND = pygame.transform.scale(pygame.image.load(self.DIRETORIO + "/images/back.png"), (1200, 900))
        self.SPRITE_NAVE = pygame.transform.scale(pygame.image.load(self.DIRETORIO + "/images/ship.png"), (65, 65))
        self.NAVE = Nave(self.SPRITE_NAVE, (LARGURA_TELA) / 2, (ALTURA_TELA - 80))
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
        self.JANELA.blit(texto, [(LARGURA_TELA - 550) / 2, 0])
        self.FONTE = pygame.font.Font(self.DIRETORIO + "/fonts/space_invaders.ttf", 30)
        comando1 = self.FONTE.render(" ENTER ou I: INICIA ", True, BRANCO, AZUL)
        comando2 = self.FONTE.render(" ESC ou S: ENCERRA", True, BRANCO, AZUL)
        self.JANELA.blit(comando1, ((LARGURA_TELA - 550) / 2, ALTURA_TELA - 100))
        self.JANELA.blit(comando2, ((LARGURA_TELA - 550) / 2, ALTURA_TELA - 50))
        pygame.display.update()

        while menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    musica_menu.stop()
                    return False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if ((x >= ((LARGURA_TELA - 550) / 2)) and (y >= (ALTURA_TELA - 100))) and ((x <= (LARGURA_TELA - 340)) and (y <= (ALTURA_TELA - 55))):
                        self.inicia_inimigos()
                        musica_menu.stop()
                        return True
                    if ((x >= ((LARGURA_TELA - 550) / 2)) and (y >= (ALTURA_TELA - 50))) and ((x <= (LARGURA_TELA - 340)) and (y <= (ALTURA_TELA - 10))):
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
            tipos_de_inimigos.append(pygame.image.load(self.DIRETORIO + ("/images/invader%d.png" % (i % 2))))

        for j in xrange(len(self.MATRIZ_DE_INIMIGOS)):
            linha = self.MATRIZ_DE_INIMIGOS[j]

            for i in xrange(10):
                sprite = pygame.transform.scale(tipos_de_inimigos[j], ((LARGURA_TELA / 20), (LARGURA_TELA / 20)))
                linha.append(Invasores(sprite, x, y))

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
        self.move_inimigos(1)
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

    def inimigo_mais_a_direita(self):
        for i in range(len(self.MATRIZ_DE_INIMIGOS[0]) - 1, -1, -1):
            for j in range(len(self.MATRIZ_DE_INIMIGOS)):
                invasor = self.MATRIZ_DE_INIMIGOS[j][i]
                if invasor.ativo:
                    return invasor

    def inimigo_mais_a_esquerda(self):
        for i in range(len(self.MATRIZ_DE_INIMIGOS[0])):
            for j in range(len(self.MATRIZ_DE_INIMIGOS)):
                invasor = self.MATRIZ_DE_INIMIGOS[j][i]
                if invasor.ativo:
                    return invasor

    def move_inimigos (self, velocidade):
        inimigo_mais_a_direita = self.inimigo_mais_a_direita()
        inimigo_mais_a_esquerda = self.inimigo_mais_a_esquerda()

        if inimigo_mais_a_direita.direcao == DIRECAO[0]:
            self.move_inimigos_direita(velocidade)
            posicao_direita = inimigo_mais_a_direita.rect.x
            
            if posicao_direita >= (LARGURA_TELA - (LARGURA_TELA / 15)):
                inimigo_mais_a_esquerda.direcao = DIRECAO[1]
                inimigo_mais_a_direita.direcao = DIRECAO[1]
        elif inimigo_mais_a_esquerda.direcao == DIRECAO[1]:
            self.move_inimigos_esquerda(velocidade)
            posicao_esquerda = inimigo_mais_a_esquerda.rect.x
            
            if  posicao_esquerda <= 20:
                inimigo_mais_a_esquerda.direcao = DIRECAO[0]
                inimigo_mais_a_direita.direcao = DIRECAO[0]
    
    def move_inimigos_direita (self, velocidade):
        for i in xrange(len(self.MATRIZ_DE_INIMIGOS[0]) -1, -1, -1):
            for j in xrange(len(self.MATRIZ_DE_INIMIGOS)):
                inimigo = self.MATRIZ_DE_INIMIGOS[j][i]
                if inimigo.ativo:
                    inimigo.direcao = DIRECAO[0]
                    inimigo.rect.x += velocidade
    
    def move_inimigos_esquerda (self, velocidade):
        for i in xrange(len(self.MATRIZ_DE_INIMIGOS[0]) - 1, -1, -1):
            for j in xrange(len(self.MATRIZ_DE_INIMIGOS) -1, -1, -1):
                inimigo = self.MATRIZ_DE_INIMIGOS[j][i]
                if inimigo.ativo:
                    inimigo.direcao = DIRECAO[1]
                    inimigo.rect.x -= velocidade

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
                for event in pygame.event.get():
                    # Verificando se o usuário clicou na opção de fechar a janela.
                    if event.type == pygame.QUIT:
                        run = False
                    if event.type == pygame.KEYDOWN:
                        if ((event.key == pygame.K_UP or event.key == pygame.K_SPACE) and self.TIRO == None):
                            self.TIRO = self.NAVE.shot(self.DIRETORIO + "/images/laser.png")
                            self.update()
                
                # Coletando os eventos que o usuário está realizando
                if pygame.key.get_pressed()[pygame.K_RIGHT]:
                    self.NAVE.move_right()
                # Se a tecla pressionada for a seta para esquerda, move a NAVE para a esquerda.
                elif pygame.key.get_pressed()[pygame.K_LEFT]:
                    self.NAVE.move_left()

                self.update()
                

if __name__ == "__main__":
    # Comando necessário para se inicializar os módulos do Pygame
    pygame.init()
    game = SpaceInvaders()
    game.main()
    # Comando que encerra os módulos do Pygame
    pygame.quit()
