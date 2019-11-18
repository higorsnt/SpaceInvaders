# SPACE INVADERS 🛸

[![Language](https://img.shields.io/badge/python-%3E=%202.7-blue?style=flat-square&logo=appveyor)](https://www.python.org)
[![Modules](https://img.shields.io/badge/modules-pygame-green?style=flat-square&logo=appveyor)](https://www.pygame.org/docs/)

**ALIENS ESTÃO INVADINDO A TERRA!**

Calma, essa é apenas a temática que do jogo Space Invaders!  
Sendo originalmente lançado em 1978 pela [TAITO CORPORATION](https://www.taito.com/) e desenhado por Tomohiro Nishikado, e depois licenciado pela Midway. Este joguinho foi um dos primeiros cuja temática era de tiro e que possuia gráficos bidimensionais. _O sucesso se estende até os dias atuais!_

O objetivo do jogo é destruir os aliens com a sua nave e dessa forma impedir que a invasão se concretize. Porém, não se pode dormir na direção, já que a qualquer momento os aliens podem te atingir e conseguir o que tanto querem: conquistar a Terra 🌎!

![Tela de Jogo](images/telainicial.gif)

## Tópicos

- [SPACE INVADERS 🛸](#space-invaders-%f0%9f%9b%b8)
  - [Tópicos](#t%c3%b3picos)
    - [Eventos Essenciais em um jogo](#eventos-essenciais-em-um-jogo)
    - [Pygame](#pygame)
    - [Instalando o Pygame](#instalando-o-pygame)
    - [Executando o jogo](#executando-o-jogo)
    - [Detalhes da Construção do Jogo](#detalhes-da-constru%c3%a7%c3%a3o-do-jogo)
    - [Comandos](#comandos)
    - [Links Úteis](#links-%c3%9ateis)
    - [Autores](#autores)

### Eventos Essenciais em um jogo

Para se construir um jogo é necessário ter conhecimento de quais eventos são importantes para o mesmo. Portanto, abaixo temos uma tabela com alguns desses eventos:

|            Eventos               |                                  Explicação                                          |
|:--------------------------------:|:------------------------------------------------------------------------------------:|
|               Surface            |              são as superfícies em _2D_ ou _3D_ onde se desenha o jogo.|
|               Display            | são os eventos que manipulam a tela, abrindo a possibilidade de atualizar ou configurar a tela, entre outras possibilidades.|
|               draw               |                 são os desenhos na superfície.  |
|               image              |        são as imagens. Este é o que possibilita a leitura ou gravação de imagem(ns). |
|               event              |                    são os eventos do jogo. |
|               font               |                 utilizado para trabalhar com fontes. |
|               transform          | permite rotacionar, espelhar, modificar ou cortar as imagens do jogo. |
|               mixer              |       facilita o trabalho com os sons no jogo.               |
|               Clock              |       trabalha com o tempo dos quadros do jogo.              |
|               sprite             |é uma imagem que faz parte do jogo, isto é, são os componentes que aparecem no jogo. Podendo se dividir em Sprite e Group (a classe Group serve para agrupar várias sprites).|

### Pygame

PyGame é um módulo<sup>[1](#footnote-1)</sup> usado na programação de jogos 2D, escrito utilizando C e Python. Ele pode ser executado em todas as principais plataformas e fornece ferramentas simples para gerenciar ambientes gráficos complexos, com movimentos e sons.  
Alguns módulos presentes em pygame são:  


|            Módulo                |               Funcionalidade                                    |
|:--------------------------------:|:---------------------------------------------------------------:|
|               cursors            |            carrega imagens de cursores, como mouse.              |
|               display            |             controla a exibição da janela ou tela.              |
|                draw              |           desenha formas simples sobre uma Surface.             |
|                event             |              controla eventos e fila de eventos.                |
|                font              |                    cria e renderiza fontes.                     |
|                image             |                    salva e carrega imagens.                     |
|              joystick            |             controla dispositivos joystick.                     |
|                 key              |                       controla o teclado.                       |
|                locals            |                contém constantes de Pygame.                     |
|                mixer             |                     carrega e executa sons.                     |
|                mouse             |                       controla o mouse.                         |
|               movie              |                executa filmes no formato mpeg.                  |
|                time              |                     controla a temporização.                    |
|             transform            |    permite redimensionar e mudar a orientação de imagens.       |
|               cdrom              |    gerencia o dispositivo de CD-ROM e a execução do áudio.      |
|              sndarray            |                    manipula sons com NumPy.                     |
|             surfarray            |                   manipula imagens com NumPy.                   |


FONTE: [LINK](http://www.labtime.ufg.br/cgames/pdf/CProgPy_Pygame.pdf)

### Instalando o Pygame

Inicialmente é necessário ter o Python instalado e o pip. Caso não tenha um dos dois instalados siga o passo a passo visto [aqui para Linux](https://python.org.br/instalacao-linux/) ou [aqui para Windows](https://python.org.br/instalacao-windows/) **e não se esqueça de adicionar Python na variável de ambiente!**.

1. Para iniciar a instalação do Pygame, é recomendável estar com o pip atualizado, para isso faça _(esse passo pode ser pulado se você acabou de instalá-lo)_:

```
$ pip install --user --upgrade pip 
```

2. Instalando Pygame:

```
$ pip install --user pygame
```

### Executando o jogo

Qualquer um pode baixar o código do jogo e executar clicando no botão verde **Clone or download** e pode baixar o código clicando [**aqui**](https://github.com/HigorSnt/SpaceInvaders/archive/master.zip) ou digitando no terminal o comando:

```
$ git clone https://github.com/HigorSnt/SpaceInvaders.git
```

> Se optar pela primeira opção lembre-se de extrair!

Em seguida, entre na pasta do jogo utilizando o terminal:

```
$ cd SpaceInvaders
```

Por fim, faça o seguinte comando:

```
$ python spaceinvaders.py
```

Em seguida deverá abrir a janela do jogo 😁.

### Detalhes da Construção do Jogo

Para a construção deste projeto foi necessário criar diversas classes com o objetivo de facilitar o tratamento de colisões, representação de entidades importantes para a jogabilidade, entre outros motivos. Algumas das classes criadas foram:

<table style="text-align:center">
  <tr>
    <td>Edge</td>
    <td>Estrutura criada para facilitar a análise de colisões com as bordas.</td>
  </tr>
  <tr>
    <td>Block</td>
    <td>Responsável por criar barreiras que protegem a nave.</td>
  </tr>
  <tr>
    <td>Ship</td>
    <td>Classe que representa a nave do jogador.</td>
  </tr>
  <tr>
    <td>Invader</td>
    <td>Classe que representa os invasores.</td>
  </tr>
  <tr>
    <td>Mystery</td>
    <td>É a representação da nave Mystery presente no jogo tradicional.</td>
  </tr>
  <tr>
    <td>Bullet</td>
    <td>Classe que representa as balas de todos os objetos que realizam disparos.</td>
  </tr>
  <tr>
    <td>SpaceInvaders</td>
    <td>Classe principal responsável por toda a lógica do jogo.</td>
  </tr>
</table>

### Comandos

Para realizar comandos no jogo é necessário apenas o uso teclado e a sua listagem está abaixo:

<table style="text-align:center">
  <tr>
    <td>Iniciar o jogo</td>
    <td><code>ENTER</code> ou <code>SPACE</code></td>
  </tr>
  <tr>
    <td>Fechar ou Encerrar</td>
    <td><code>ESC</code> ou clicar no ❌ da janela.</td>
  </tr>
  <tr>
    <td>Movimentar a nave</td>
    <td>Setas direcionais (⬅ ou ➡)</td>
  </tr>
  <tr>
    <td>Realizar disparo</td>
    <td>Seta direcional (⬆) ou <code>SPACE</code></td>
  </tr>
  <tr>
    <td>Reiniciar o jogo (na tela de Game Over)</td>
    <td><code>ENTER</code></td>
  </tr>
</table>

### Links Úteis

* [Apresentação feita em sala de aula](https://bit.ly/2XuTkxo)
* [A documentação oficial do Pygame é muito fácil de ser utilizada!](https://www.pygame.org/docs/)
* [Esse material do curso realizado pela UFG!](http://www.labtime.ufg.br/cgames/pdf/CProgPy_Pygame.pdf)
* [Repositório do Pygame no Github](https://github.com/pygame/pygame)
* [Material: Programação em Python e Introdução ao Pygame](http://www.dainf.ct.utfpr.edu.br/petcoce/wp-content/uploads/2013/09/document.pdf)
* Dúvidas com Python Orientado à Objetos?
    * [Matéria da página Medium que pode ajudar](https://medium.com/@nicolasbontempo/programando-python-orientado-a-objetos-d0069b2f1eb5)
    * [Material da UNESP - Campus de Ilha Solteira](https://www.dcc.ufrj.br/~fabiom/mab225/pythonoo.pdf)
 * Qual cor usar? [Acesse aqui!](http://www.erikasarti.com/html/tabela-cores/)
  
  


### Autores

Código desenvolvido para auxiliar aos alunos da disciplina de Laboratório de Programação I  
**Autores:**  
* [Higor Santos](https://github.com/HigorSnt)  
* [Mateus Alves](https://github.com/mateustranquilino)
  

<p align="center">
  <img src="http://alumni.computacao.ufcg.edu.br/static/logica/images/logo.png"/>  
</p>
  
  
1. <a name="footnote-1"></a> Módulos são arquivos que contêm definições e instruções de Python, ou seja, qualquer arquivo _.py_ é um módulo!
