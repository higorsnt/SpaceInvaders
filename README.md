# SPACE INVADERS 🛸

[![Language](https://img.shields.io/badge/python-%3E=%202.7-blue?style=flat-square&logo=appveyor)](https://www.python.org)
[![Modules](https://img.shields.io/badge/modules-pygame-green?style=flat-square&logo=appveyor)](https://www.pygame.org/docs/)

**ALIENS ESTÃO INVADINDO A TERRA! :alien:**

Calma, essa é apenas a temática que o jogo Space Invaders segue!  
Sendo originalmente lançado em 1978 pela [TAITO CORPORATION](https://www.taito.com/) e desenhado por Tomohiro Nishikado, posteriormente foi licenciado pela Midway. Este joguinho foi um dos primeiros da temática de tiro com gráfico bidimensional e que até hoje faz sucesso.  

O objetivo do jogo é destruir os aliens com a sua nave e dessa forma impedir que a invasão se concretize. Porém, não se pode dormir na direção, já que a qualquer momento os aliens podem te atingir e conseguir o que tanto querem: conquistar a Terra 🌎!

## Tópicos

- [SPACE INVADERS 🛸](#space-invaders-%F0%9F%9B%B8)
  - [Tópicos](#t%C3%B3picos)
    - [Eventos Essenciais em um jogo](#eventos-essenciais-em-um-jogo)
    - [Pygame 🐍](#pygame-%F0%9F%90%8D)
    - [Instalando o Pygame](#instalando-o-pygame)
    - [Executando o jogo](#executando-o-jogo)
    - [Links Úteis](#links-%C3%BAteis)
    - [Autores](#autores)

### Eventos Essenciais em um jogo

Para se construir um jogo é necessário ter conhecimento de quais eventos são importantes para se construir um jogo. Portanto, abaixo temos uma tabela com alguns desses eventos:

|            Eventos               |                                  Explicação                                          |
|:--------------------------------:|:------------------------------------------------------------------------------------:|
|               Surface            |              são as superfícies em _2D_ ou _3D_ onde se desenha o jogo.              |
|               Display            | são os eventos que manipulam a tela, abrindo a possibilidade de atualizar ou configurar a tela, entre outras possibilidades.|
|               draw               |                 são os desenhos na superfície.                                       |
|               image              |        são as imagens. Elas permitem ler ou gravar alguma(s) imagem(s).              |
|               event              |                    são os eventos do jogo.                                           |
|               font               |                 utilizado para trabalhar com fontes.                                 |
|               transform          |     permite rotacionar, espelhar, modificar ou cortar as imagens do jogo.            |
|               mixer              |              facilita o trabalho com os sons no jogo.                                |
|               Clock              |                     trabalha com o tempo dos quadros do jogo.                        |
|               sprite             |é uma imagem que faz parte do jogo, isto é, são os componentes que aparecem no jogo. Podendo se dividir em Sprite e Group, a classe Group serve para agrupar várias sprites.|

### Pygame 🐍

PyGame é um módulo<sup>[1](#footnote-1)</sup> usado na programação de jogos 2D, escrito utilizando C e Python. Ele pode ser executado em todas as principais plataformas e fornece ferramentas simples para gerenciar ambientes gráficos complexos, com movimentos e sons.  
Alguns módulos presentes em pygame são:  


|            Módulo                |               Funcionalidade                                    |
|:--------------------------------:|:---------------------------------------------------------------:|
|               cursors            |            carrega imagens de cursores como mouse.              |
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
|               cdrom              |    gerencia o dispositivo de cdrom e a execução do áudio.       |
|              sndarray            |                    manipula sons com NumPy.                     |
|             surfarray            |                   manipula imagens com NumPy.                   |


FONTE: [LINK](http://www.labtime.ufg.br/cgames/pdf/CProgPy_Pygame.pdf)

### Instalando o Pygame

Inicialmente é necessário ter o Python instalado e o pip. Caso não tenha um dos dois instalados siga o passo a passo visto [aqui para Linux](https://python.org.br/instalacao-linux/) ou [aqui para Windows](https://python.org.br/instalacao-windows/) **e não se esqueça de adicionar Python na variável de ambiente!**.

1. Para iniciar a instalação do Pygame, é recomendável estar com o pip atualizado, para isso faça _(esse passo pode ser pulado se você já tem o pip instalado)_:

```
$ pip install --user --upgrade pip 
```

2. Instalando Pygame:

```
$ pip install --user pygame
```

### Executando o jogo

Qualquer um pode baixar o código do jogo e executar clicando no botão verde **Clone or download** e pode baixar o código clicando em **Download ZIP** ou digitando no terminal o comando:

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

> TODO
> COLOCAR GIF DA TELA

### Links Úteis

* [Apresentação feita em sala de aula](https://docs.google.com/presentation/d/17zlx3HSecMyiAkZ4KWEEa_797A9hyfjCF2dA1NOeEss/edit?usp=sharing)
* [A documentação oficial do Pygame é muito fácil de ser utilizada!](https://www.pygame.org/docs/)
* [Esse material do curso realizado pela UFG!](http://www.labtime.ufg.br/cgames/pdf/CProgPy_Pygame.pdf)
* [Repositório do Pygame no Github](https://github.com/pygame/pygame)
* [Material: Programação em Python e Introdução ao Pygame](http://www.dainf.ct.utfpr.edu.br/petcoce/wp-content/uploads/2013/09/document.pdf)
* Dúvidas com Python Orientado à Objetos?
    * [Matéria da página Medium que pode ajudar](https://medium.com/@nicolasbontempo/programando-python-orientado-a-objetos-d0069b2f1eb5)
    * [Material da UNESP - Campus de Ilha Solteira](https://www.dcc.ufrj.br/~fabiom/mab225/pythonoo.pdf)
 * Qual cor usar? [Acesse aqui!](http://www.erikasarti.com/html/tabela-cores/)

</br>
</br>
</br>

### Autores

Código desenvolvido para auxiliar aos alunos da disciplina de Laboratório de Programação I  
**Autores:**  
* [Higor Santos](https://github.com/HigorSnt)  
* [Mateus Alves](https://github.com/mateustranquilino)

</br>

<p align="center">
  <img src="http://alumni.computacao.ufcg.edu.br/static/logica/images/logo.png"/>
</p>

_________________________________________________
1. <a name="footnote-1"></a> Módulos são arquivos que contêm definições e instruções de Python, ou seja, qualquer arquivo _.py_ é um módulo!
