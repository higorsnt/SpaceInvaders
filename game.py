# coding: utf-8
from random import shuffle
import pygame
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

    def move_left(self):

        if self.rect.left > 10:
            self.rect.x -= self.velocidade

    def move_right(self):

        if self.rect.right < 1190:
            self.rect.x += self.velocidade

    def shot(self):
        projetil = Projetil(self.rect.x + 30, self.rect.y, 1)
        
        return projetil

    def move_down(self):
        pass


class Projetil():

    def __init__(self, pos_x, pos_y, direcao, color=BRANCO):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.direcao = direcao
        self.velocidade = 6 * direcao
        self.color = color

    def draw(self, fundo):
        pygame.draw.circle(fundo, self.color, (self.pos_x, self.pos_y), 4)
        pygame.display.update()
        self.pos_y -= self.velocidade


class SpaceInvaders():
    def __init__(self):
        # Definindo os caminhos dos arquivos necessários para o jogo
        self.DIRETORIO = os.getcwd()
        self.bullet = None
        self.LARGURA_TELA = 1200
        self.ALTURA_TELA = 900
        self.LIMITE_ESQUERDO = 10
        self.LIMITE_DIREIRO = 1180
        self.JANELA = pygame.display.set_mode(
            (self.LARGURA_TELA, self.ALTURA_TELA))
        pygame.display.set_caption("Space Invaders")

        # Criando um objeto do tipo pygame.font.Font, onde é passada a fonte e o tamanho
        # se a fonte for passada como None é utilizada a padrão do sistema.
        self.FONTE = pygame.font.Font(
            self.DIRETORIO + "/fonts/space_invaders.ttf", 60)
        self.BACKGROUND = pygame.transform.scale(pygame.image.load(
            self.DIRETORIO + "/images/back.png"), (1200, 900))
        self.SPRITE_NAVE = pygame.transform.scale(
            pygame.image.load(self.DIRETORIO + "/images/new/ship.png"), (70, 70))
        self.NAVE = Criatura(
            self.SPRITE_NAVE, (self.LARGURA_TELA - 140) / 2, (self.ALTURA_TELA - 100))
        self.CLOCK = pygame.time.Clock()
        self.MATRIZ_DE_INIMIGOS = [[], [], [], [], []]

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
        self.FONTE = pygame.font.Font(
            self.DIRETORIO + "/fonts/space_invaders.ttf", 30)
        comando1 = self.FONTE.render(
            " Para INICIAR o jogo digite I", True, BRANCO, AZUL)
        comando2 = self.FONTE.render(
            " Para SAIR do jogo digite S   ", True, BRANCO, AZUL)
        self.JANELA.blit(
            comando1, ((self.LARGURA_TELA - 550) / 2, self.ALTURA_TELA - 100))
        self.JANELA.blit(
            comando2, ((self.LARGURA_TELA - 550) / 2, self.ALTURA_TELA - 50))
        pygame.display.update()

        '''
        inimigo1 = pygame.image.load(
            self.DIRETORIO + "/images/enemies/alien1.png")
        inimigo2 = pygame.image.load(
            self.DIRETORIO + "/images/enemies/alien4.png")
        # inimigo1_texto = self.FONTE.render(" = X pts", )
        # inimigo2_texto = self.FONTE.render(" = X pts", True, self.VERMELHO, None)
        # self.JANELA.blit(inimigo1_texto, [200,150])
        inimigo1 = pygame.transform.scale(inimigo1, (100, 90))
        self.JANELA.blit(inimigo1, (100, 200))'''

        while menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    musica_menu.stop()
                    return False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if (x >= 220 and y >= 550) and (x <= 750 and y <= 590):
                        self.inicia_inimigos()
                        musica_menu.stop()
                        return True
                    if (x >= 220 and y >= 600) and (x <= 743 and y <= 643):
                        musica_menu.stop()
                        return False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_i:
                        self.inicia_inimigos()
                        musica_menu.stop()
                        return True
                    if event.key == pygame.K_s:
                        musica_menu.stop()
                        return False

    def inicia_inimigos(self):

        x = 20
        y = 60
        tipos_de_inimigos = []

        for i in xrange(1, 8):

            tipos_de_inimigos.append(
                pygame.image.load(self.DIRETORIO + ("/images/new/test%d.png" % (i % 2))))

        for j in xrange(len(self.MATRIZ_DE_INIMIGOS)):
            linha = self.MATRIZ_DE_INIMIGOS[j]

            for i in xrange(10):

                sprite = pygame.transform.scale(tipos_de_inimigos[j], (50, 50))
                linha.append(Criatura(sprite, x, y))

                x += 60

            y += 60
            x = 20

    def exibe_inimigos(self):
        for linha in self.MATRIZ_DE_INIMIGOS:
            for inimigo in linha:
                self.JANELA.blit(inimigo.sprite, inimigo.rect)

    def update(self):
        self.JANELA.blit(self.BACKGROUND, (0, 0))
        self.exibe_inimigos()
        self.JANELA.blit(self.NAVE.sprite, self.NAVE.rect)
        self.CLOCK.tick(60)

        if self.bullet != None: 
            self.bullet.draw(self.JANELA)
            if self.bullet.pos_y < 0:
                self.bullet = None
        
        pygame.display.update()

    def main(self):
        # Variável necessária para que o loop onde o jogo ocorre dure o tempo necessário
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
                    # Verificando se o usuário clicou na opção de fechar a janela
                    if event.type == pygame.QUIT:
                        run = False

                    # Verificando se o usuário pressionou em alguma tecla.
                    if event.type == pygame.KEYDOWN:

                        if (event.key == pygame.K_UP and self.bullet == None):
                            self.bullet = self.NAVE.shot()
                            

                        # Se a tecla pressionada for a seta para direita, move a TANQUE para a direita.
                        if event.key == pygame.K_RIGHT:
                            self.NAVE.move_right()

                        # Se a tecla pressionada for a seta para esquerda, move a TANQUE para a esquerda.
                        elif event.key == pygame.K_LEFT:
                            self.NAVE.move_left()

                self.update()
                # print (self.NAVE.rect.left), (self.NAVE.rect.right)


if __name__ == "__main__":
    # Comando necessário para se inicializar os módulos do Pygame
    pygame.init()
    game = SpaceInvaders()
    game.main()
    # Comando que encerra os módulos do Pygame
    pygame.quit()
