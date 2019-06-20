# coding: utf-8
from random import choice
from math import ceil
import pygame
import os

AZUL = (0, 0, 255)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
CINZA = (0, 128, 128)
DIRECAO = {"D":1,"E":-1}
LARGURA_TELA = 800
ALTURA_TELA = 600
DIRETORIO = os.getcwd()

class Borda(pygame.sprite.Sprite):
    def __init__(self, x, y, a, b):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface( (x, y) )
        self.image.fill(BRANCO)
        self.rect = self.image.get_rect()
        self.rect.x = a
        self.rect.y = b
    
BORDA_ESQUERDA = pygame.sprite.GroupSingle(Borda(5,ALTURA_TELA, 0, 0))
BORDA_DIREITA = pygame.sprite.GroupSingle(Borda(5,ALTURA_TELA, 795, 0))
BORDA_INFERIOR = Borda(LARGURA_TELA, 5, 0, 0)

class Nave(pygame.sprite.Sprite):
    def __init__(self, path, pos_x, pos_y, velocidade=5):
        
        self.__initial_position = (pos_x, pos_y)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, (65,65))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.velocidade = velocidade
        self.vidas = 3
        self.som_tiro = pygame.mixer.Sound(DIRETORIO + "/sounds/shoot.wav")
        self.som_atingido = pygame.mixer.Sound(DIRETORIO + "/sounds/shipexplosion.wav")

    def die(self):
        self.som_atingido.play()
        self.rect.x = self.__initial_position[0]
        self.rect.y = self.__initial_position[1]
        self.vidas -= 1


    def update(self):

        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            if self.rect.right < (LARGURA_TELA - self.velocidade):
                self.rect.x += self.velocidade
        
        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            if self.rect.left > self.velocidade:
                self.rect.x -= self.velocidade

    def shot(self):
        self.som_tiro.play()
        projetil = Projetil(self.rect.midtop, 1)
        return projetil

    def __str__(self):
        return "Nave em (%s, %s)" % (self.rect.x, self.rect.y)

class Invasores(pygame.sprite.Sprite):

    def __init__(self, sprite, pos_x, pos_y, velocidade=1):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite
        self.rect = sprite.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.velocidade = velocidade
        
    def shot(self):
        projetil = Projetil(self.rect.midtop, -1, v=4,color=VERMELHO)
        return projetil

    def update(self, direct):
        
        if (self.rect.x >= (LARGURA_TELA - self.rect.width)):
            self.velocidade = -1
            self.rect.y += 40

        if (self.rect.x <= 0):
            self.velocidade = 1
            self.rect.y += 40

        self.rect.x += self.velocidade * direct

    def __str__(self):
        return "Invasor em (%s, %s)" % (self.rect.x, self.rect.y)
    

class Projetil(pygame.sprite.Sprite):

    def __init__(self, pos_xy, direcao, v=8, color=VERDE):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface( (5,10) )
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = pos_xy[0] 
        self.rect.y = pos_xy[1] 
        self.direcao = direcao
        self.velocidade = v * direcao

    def update(self):

        self.rect.y -= self.velocidade
        if self.rect.bottom <= 0:
            self.kill()
    
class SpaceInvaders():
    def __init__(self):
        # Definindo os caminhos dos arquivos necessários para o jogo
        self.TIRO_NAVE = pygame.sprite.GroupSingle()
        self.TIRO_INVADERS = pygame.sprite.Group()
        self.JANELA = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
        pygame.display.set_caption("Space Invaders")
        self.SCORE = 0
        # Criando um objeto do tipo pygame.font.Font, onde é passada a fonte e o tamanho
        # se a fonte for passada como None é utilizada a padrão do sistema.
        self.FONTE = pygame.font.Font(DIRETORIO + "/fonts/space_invaders.ttf", 60)
        self.BACKGROUND = pygame.transform.scale(pygame.image.load(DIRETORIO + "/images/back.png"), (1200, 900))
        caminho_imagem_nave = DIRETORIO + "/images/ship.png"
        self.NAVE =  Nave(caminho_imagem_nave, (LARGURA_TELA) / 2, (ALTURA_TELA - 110) )
        self.CLOCK = pygame.time.Clock()
        self.MATRIZ_DE_INIMIGOS = pygame.sprite.Group()

    def tela_inicial(self):
        """
        Criação de outro objeto Surface. O primeiro parâmetro é o texto que será inserido,
        em seguida um booleano indicando se deve ou não suavizar (isso dá a sensação que
        a imagem é lisa), o terceiro parâmetro é a cor do texto e o último a cor de fundo do texto.
        """
        menu = True

        musica_menu = pygame.mixer.Sound(DIRETORIO + "/sounds/menu.wav")
        musica_menu.play(-1)

        self.JANELA.fill((0, 0, 0))
        texto = self.FONTE.render("SPACE INVADERS", True, VERDE)
        self.JANELA.blit(texto, [(LARGURA_TELA - 550) / 2, 0])
        self.FONTE = pygame.font.Font(DIRETORIO + "/fonts/space_invaders.ttf", 30)
        comando1 = self.FONTE.render(" ENTER ou I: INICIA ", True, BRANCO, AZUL)
        comando2 = self.FONTE.render(" ESC ou S: ENCERRA", True, BRANCO, AZUL)
        self.JANELA.blit(comando1, ((LARGURA_TELA - 350) / 2, ALTURA_TELA - 100))
        self.JANELA.blit(comando2, ((LARGURA_TELA - 350) / 2, ALTURA_TELA - 50))
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
        y = 10
        tipos_de_inimigos = []

        for i in xrange(1, 8):
            tipos_de_inimigos.append(pygame.image.load(DIRETORIO + ("/images/invader%d.png" % (i % 2))))

        for j in xrange(5):
            
            for i in xrange(10):
                sprite = pygame.transform.scale(tipos_de_inimigos[j], ((LARGURA_TELA / 20), (LARGURA_TELA / 20)))
                self.MATRIZ_DE_INIMIGOS.add(Invasores(sprite, x, y))
                x += 50

            y += 40
            x = 20
        
    
    def exibeVidasNave(self):
        y = 10
        caminho_imagem_vidas = DIRETORIO + "/images/heart.png"
        imagem_vidas = pygame.image.load(caminho_imagem_vidas)
        for i in xrange(self.NAVE.vidas):
            self.JANELA.blit(pygame.transform.scale(imagem_vidas, (25,25)), (y, 570))
            y += 40

    def tiro_inimigo(self):
        enem = [ i for i in self.MATRIZ_DE_INIMIGOS ]
        for i in xrange(2):
            l = choice(enem)
            self.TIRO_INVADERS.add(l.shot())
        
    def update(self):
        fonte_pontos = pygame.font.Font(DIRETORIO + "/fonts/space_invaders.ttf", 15)
        pontuacao = fonte_pontos.render("SCORE: %d" % self.SCORE, True, BRANCO)
        self.JANELA.blit(self.BACKGROUND, (0, 0))
        self.JANELA.blit(pontuacao, (LARGURA_TELA-100,ALTURA_TELA-30))
        BORDA_DIREITA.draw(self.JANELA)
        BORDA_ESQUERDA.draw(self.JANELA)
        self.JANELA.blit(BORDA_INFERIOR.image, ( 0, ALTURA_TELA - 40 ) )
        self.MATRIZ_DE_INIMIGOS.draw(self.JANELA)
        self.TIRO_NAVE.draw(self.JANELA)
        self.TIRO_INVADERS.draw(self.JANELA)
        self.JANELA.blit(self.NAVE.image, self.NAVE.rect)
        self.NAVE.update()

        if pygame.time.get_ticks() % 2000.0 < 30:
            self.tiro_inimigo()
        
        self.TIRO_NAVE.update()
        self.TIRO_INVADERS.update()
        self.MATRIZ_DE_INIMIGOS.update(1)
       
       
        pygame.sprite.groupcollide(self.TIRO_NAVE, self.TIRO_INVADERS, True, True)
        if pygame.sprite.spritecollide(self.NAVE, self.TIRO_INVADERS, True):
            self.NAVE.die()
            
        self.exibeVidasNave()
        musica_explosao = pygame.mixer.Sound(DIRETORIO + "/sounds/invaderkilled.wav")
        
        
        for atingidos in pygame.sprite.groupcollide(self.TIRO_NAVE, self.MATRIZ_DE_INIMIGOS, True, True).values():
            for invasor in atingidos:
                musica_explosao.play()
                imagem_explosao = pygame.image.load(DIRETORIO + "/images/explosion.png")
                self.JANELA.blit(pygame.transform.scale(imagem_explosao, ((LARGURA_TELA / 20), (LARGURA_TELA / 20))), (invasor.rect.x, invasor.rect.y))
                self.SCORE += 10

        self.CLOCK.tick(60)
        pygame.display.update()

   
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
                        if ((event.key == pygame.K_UP or event.key == pygame.K_SPACE) and not self.TIRO_NAVE):
                            self.TIRO_NAVE.add(self.NAVE.shot())
                
                self.update()

            #print pygame.time.get_ticks()                

if __name__ == "__main__":
    # Comando necessário para se inicializar os módulos do Pygame
    pygame.init()
    game = SpaceInvaders()
    game.main()
    # Comando que encerra os módulos do Pygame
    pygame.quit()
