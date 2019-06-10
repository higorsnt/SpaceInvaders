# coding: utf-8
from criatura import Criatura
from random import choice
import pygame
import os

class SpaceInvaders():
    def __init__(self):
        # Definindo os caminhos dos arquivos necessários para o jogo
        self.DIRETORIO = os.getcwd()

        self.LARGURA_TELA = 1500
        self.ALTURA_TELA = 1000 
        self.JANELA = pygame.display.set_mode((self.LARGURA_TELA, self.ALTURA_TELA))
        pygame.display.set_caption("Space Invaders")

        # Criando um objeto do tipo pygame.font.Font, onde é passada a fonte e o tamanho
        # se a fonte for passada como None é utilizada a padrão do sistema.
        self.FONTE = pygame.font.Font(self.DIRETORIO + "/fonts/space_invaders.ttf", 60) 
        self.BACKGROUND = pygame.image.load(self.DIRETORIO + "/images/background.jpg")
        self.SPRITE_TANQUE = pygame.transform.scale(pygame.image.load(self.DIRETORIO + "/images/tank.png"), (150,150) )
        self.TANQUE = Criatura(self.SPRITE_TANQUE, (self.LARGURA_TELA - 140) / 2, (self.ALTURA_TELA - 120))
        self.CLOCK = pygame.time.Clock()
        self.MATRIZ_DE_INIMIGOS = [[],[],[],[],[]]

        # Definido cores
        self.PRETO = (0, 0, 0)
        self.BRANCO = (255, 255, 255)
        self.VERMELHO = (255, 0, 0)
        self.VERDE = (0, 255, 0)
        self.AZUL = (0, 0, 255)
        self.CINZA = (0,128,128)
    
    def tela_inicial(self):
        """
        Criação de outro objeto Surface. O primeiro parâmetro é o texto que será inserido,
        em seguida um booleano indicando se deve ou não suavizar (isso dá a sensação que 
        a imagem é lisa), o terceiro parâmetro é a cor do texto e o último a cor de fundo do texto.
        """
        menu = True


        musica_menu = pygame.mixer.Sound(self.DIRETORIO + "/sounds/menu.wav")
        musica_menu.play(-1)

        self.JANELA.fill( (0,0,0) )
        texto = self.FONTE.render("SPACE INVADERS", True, self.VERDE)
        self.JANELA.blit(texto, [(self.LARGURA_TELA - 550) / 2, 0])
        self.FONTE = pygame.font.Font(self.DIRETORIO + "/fonts/space_invaders.ttf", 30) 
        comando1 = self.FONTE.render(" Para INICIAR o jogo digite I", True, self.BRANCO, self.AZUL)
        comando2 = self.FONTE.render(" Para SAIR do jogo digite S   ", True, self.BRANCO, self.AZUL)
        self.JANELA.blit(comando1, ((self.LARGURA_TELA - 550) / 2, self.ALTURA_TELA - 100))
        self.JANELA.blit(comando2, ((self.LARGURA_TELA - 550) / 2, self.ALTURA_TELA - 50))
        pygame.display.update()


        '''
        inimigo1 = pygame.image.load(self.DIRETORIO + "/images/enemies/alien1.png")
        inimigo2 = pygame.image.load(self.DIRETORIO + "/images/enemies/alien4.png")
        #inimigo1_texto = self.FONTE.render(" = X pts", )
        #inimigo2_texto = self.FONTE.render(" = X pts", True, self.VERMELHO, None)
        #self.JANELA.blit(inimigo1_texto, [200,150])
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
        x = y = 0
        inimigosA = []
        inimigosB = []

        for i in xrange(1, 4):
            inimigosA.append(pygame.image.load(self.DIRETORIO + ("/images/enemies/alien%d.png" % i)))
            inimigosB.append(pygame.image.load(self.DIRETORIO + ("/images/enemies/alien%d.png" % (i+3))))

        for j in xrange(len(self.MATRIZ_DE_INIMIGOS)):
            linha = self.MATRIZ_DE_INIMIGOS[j]
            
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

    def exibe_inimigos(self):
        for linha in self.MATRIZ_DE_INIMIGOS:
            for inimigo in linha:
                self.JANELA.blit(inimigo.sprite, inimigo.rect)
    
    def update(self):
        self.JANELA.fill((0,255,0))
        self.exibe_inimigos()
        self. JANELA.blit(self.TANQUE.sprite, self.TANQUE.rect)
        self.CLOCK.tick(60)
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
                        # Se a tecla pressionada for a seta para direita, move a TANQUE para a direita.
                        if event.key == pygame.K_RIGHT:
                            self.TANQUE.move_right()
                        
                        # Se a tecla pressionada for a seta para esquerda, move a TANQUE para a esquerda.
                        if event.key == pygame.K_LEFT:
                            self.TANQUE.move_left()

                self.update()

if __name__ == "__main__":
    # Comando necessário para se inicializar os módulos do Pygame
    pygame.init()
    game = SpaceInvaders()
    game.main()
    # Comando que encerra os módulos do Pygame
    pygame.quit()
