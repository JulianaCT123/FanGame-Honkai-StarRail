import pygame, random
from tkinter import simpledialog

import pygame.rect

pygame.init()

tamanho = (1200,673)
relogio = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
icone = pygame.image.load("assets/stellePlayerRE.png")
pygame.display.set_icon(icone)
pygame.display.set_caption("Bem-Vindo à Penacony!")

# Chamando os assets ---------------------------------------------------

# imagens:
fundo = pygame.image.load("assets/fundoRE.png")
fundoMenu = pygame.image.load("assets/fundoMenu.png")
stelle = pygame.image.load("assets/stellePlayerRE.png")
stelleMorreu = pygame.image.load("assets/stelleMorreu.png")
birdskull = pygame.image.load("assets/BirdskullRE.png")
memeAllSeer = pygame.image.load("assets/MemeAllseerRE.png")

# Fontes:
fonte = pygame.font.SysFont("comicsans",40)
fonteMiuda = pygame.font.SysFont("comicsans",20)
fonteTitulo = pygame.font.SysFont("arial", 50)

# Sons:
pygame.mixer.music.load("assets/AceInTheHole.mp3")
somStelleMorte = pygame.mixer.Sound("assets/stelleSomMorte.mp3")
# -----------------------------------------------------------------------
bordaX = 1200
bordaY = 673
# Cores:
branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)
rosa = (200,100,255)

nome = "Anonimo"
pygame.mixer.music.play(-1)

def jogar(nome):

    pygame.mixer.music.load("assets/AgainstTheDay.mp3")
    pygame.mixer.music.play(-1) # Botando a musica pra tocar / -1 para tocar em loop
    #pygame.mixer.Sound.play(misselSom) # Tocando o som do missel 1vez ja q ele ja começa caindo

    posicaoXpersona = 500
    posicaoYpersona = 500
    movimentoXpersona = 0
    movimentoYpersona = 0

    posicaoXbird = 700
    posicaoYbird = -162
    velBird = 5
    alturaBird = 162
    larguraBird = 200

    posicaoYmeme1 = -163
    posicaoXmeme1 = 400
    alturaMeme1 = 102
    larguraMeme1 = 100
    velMeme1 = 10

    pontos = 0

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            # Controle do personagem eixo X    
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RIGHT:
                movimentoXpersona = + 10
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_LEFT:
                movimentoXpersona = - 10
            elif evento.type == pygame.KEYUP and evento.key == pygame.K_RIGHT:
                movimentoXpersona = 0
            elif evento.type == pygame.KEYUP and evento.key == pygame.K_LEFT:
                movimentoXpersona = 0
        
        posicaoXpersona = posicaoXpersona + movimentoXpersona  
        posicaoYpersona = posicaoYpersona + movimentoYpersona
        
        # Config colisão com as bordas:
        if posicaoXpersona < (bordaX - bordaX) - 30:
            posicaoXpersona = - 20
        elif posicaoXpersona > bordaX - 130 :
            posicaoXpersona = bordaX - 140
        # ---------------------------
        
        tela.fill(branco)
        tela.blit(fundo, (0,0))

        tela.blit(stelle,(posicaoXpersona,posicaoYpersona))
        stelleBox = pygame.Rect((posicaoXpersona + 40, posicaoYpersona + 60, 75, 80))

        # Config movimento inimigo ------------------------------
        posicaoYbird = posicaoYbird + velBird # Configura o inimigo caindo 
        if posicaoYbird > bordaY:
            posicaoYbird = - alturaBird
            posicaoXbird = random.randint(0,(bordaX - larguraBird))
            pontos = pontos + 1
        tela.blit(birdskull, (posicaoXbird, posicaoYbird)) # Mostra o inimigo 
        birdBoxFace = pygame.Rect((posicaoXbird + 78, posicaoYbird + 85, 43, 60))
        birdBoxAsaE1 = pygame.Rect((posicaoXbird + 55, posicaoYbird + 90,30,15))
        birdBoxAsaE2 = pygame.Rect((posicaoXbird + 40, posicaoYbird + 50,15,30))
        birdBoxAsaE3 = pygame.Rect((posicaoXbird + 10, posicaoYbird + 5,20,20))
        birdBoxAsaD1 = pygame.Rect((posicaoXbird + 125, posicaoYbird + 100,30,15))
        birdBoxAsaD2 = pygame.Rect((posicaoXbird + 155, posicaoYbird + 70,15,30))
        birdBoxAsaD3 = pygame.Rect((posicaoXbird +175, posicaoYbird + 30,15,30))                   
    
        posicaoYmeme1 = posicaoYmeme1 + velMeme1
        if posicaoYmeme1 > bordaY:
            posicaoYmeme1 = - alturaMeme1
            posicaoXmeme1 = random.randint(0,(bordaX - larguraMeme1))
            pontos = pontos + 1
        tela.blit(memeAllSeer, (posicaoXmeme1, posicaoYmeme1))
        meme1Box = pygame.Rect((posicaoXmeme1 + 15,posicaoYmeme1 + 15,75,75))
        
        # Mostra os pontos
        texto = fonte.render(nome + " pontos:" + str(pontos), True, branco)
        tela.blit(texto,(10,10))    
        
        # Config colisao -------------------------------------------

        if stelleBox.colliderect(meme1Box):
            dead(nome,pontos)
        elif stelleBox.colliderect(birdBoxFace):
            dead(nome,pontos)
        elif stelleBox.colliderect(birdBoxAsaE1) or stelleBox.colliderect(birdBoxAsaE2) or stelleBox.colliderect(birdBoxAsaE3):
            dead(nome,pontos)
        elif stelleBox.colliderect(birdBoxAsaD1) or stelleBox.colliderect(birdBoxAsaD2) or stelleBox.colliderect(birdBoxAsaD3):
            dead(nome,pontos)

        # ------------------------------------------------------------------
        pygame.display.update()
        relogio.tick(60)

def dead(nome, pontos):
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(somStelleMorte)

    jogadas = {}
    try:
        arquivo = open("historico.txt","r", encoding="utf-8")
        jogadas = eval(arquivo.read())
        arquivo.close()
    except:
        arquivo = open("historico.txt","w", encoding="utf-8")
        arquivo.close()

    jogadas[nome] = pontos
    arquivo = open("historico.txt","w", encoding="utf-8")
    arquivo.write(str(jogadas))
    arquivo.close()  
    
    while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    quit()
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    #print(evento.pos)
                    if botaoJogar.collidepoint(evento.pos):
                        jogar(nome)
                    elif botaoVoltar.collidepoint(evento.pos):
                        menu(nome)
                elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                    jogar(nome)
                elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                    menu(nome)
            
            tela.fill(preto)
            textoTitulo = fonteTitulo.render("Você Morreu :(", True, branco)
            tela.blit(textoTitulo,(100,250))
            botaoJogar = pygame.draw.rect(tela, branco, (100,400,400,50),0,20)
            textoJogar = fonte.render("Tentar Novamente", True, preto)            
            tela.blit(textoJogar,(125,395))
            textoEnter = fonteMiuda.render("ENTER para tentar novamente", True, branco)
            tela.blit(textoEnter, (110,450))
            tela.blit(stelleMorreu, (600,150))
            botaoVoltar = pygame.draw.rect(tela, branco, (5,615,130,50),0,20)
            textoVoltar = fonte.render("Voltar", True, preto)
            tela.blit(textoVoltar,(12,605))
            
            pygame.display.update()
            relogio.tick(60)

def menu(nome):
        
    while True:            
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    quit()
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    #print(evento.pos)
                    
                    if botaoJogar.collidepoint(evento.pos):
                        jogar(nome)
                    if nome != "Anonimo":
                        if botaoRank.collidepoint(evento.pos):
                            rank(nome)
                    elif botaoUser.collidepoint(evento.pos):
                        nome = simpledialog.askstring("Bem-Vindo à Penacony!", "Insira um username: ")

            tela.fill(branco)
            tela.blit(fundoMenu,(0,0))
            textoTitulo = fonteTitulo.render("Bem Vindo à Penacony!", True, branco, preto)
            tela.blit(textoTitulo,(30,250))
            botaoJogar = pygame.draw.rect(tela, branco, (90,340,400,50),0,20)
            textoJogar = fonte.render("Jogar", True, preto)
            tela.blit(textoJogar,(240,330))
            botaoRank = pygame.draw.rect(tela, branco,(5,615,170,50),0,20)
            textoRank = fonte.render("Ranking", True, preto)
            tela.blit(textoRank,(18,605))
            botaoUser = pygame.draw.rect(tela, branco, (185,615,280,50),0,20)
            textoUser = fonte.render("Trocar usuario", True, preto)
            tela.blit(textoUser, (190,607))
            if nome != "Anonimo":
                textoNome = fonteMiuda.render("Usuario Atual: " + nome, True, branco)
                tela.blit(textoNome, (10,0))
            else:
                textoNome = fonteMiuda.render("Sem usuario", True, branco)
                tela.blit(textoNome, (10,0))
            
            pygame.display.update()
            relogio.tick(60)

def rank(nome):
    estrela = {}
    try:
        arquivo = open("historico.txt","r",encoding="utf-8" )
        estrela = eval(arquivo.read())
        arquivo.close()
    except:
        pass
    
    nomes = sorted(estrela, key=estrela.get,reverse=True)
    #print(estrela)
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if botaoVoltar.collidepoint(evento.pos):
                    menu(nome)

        tela.fill(preto)
        tela.blit(fundoMenu,(0,0))
        pygame.draw.rect(tela,preto,(60,50,450,520))
        botaoVoltar = pygame.draw.rect(tela, branco, (5,615,130,50),0,20)
        textoVoltar = fonte.render("Voltar", True, preto)
        tela.blit(textoVoltar,(12,605))
        
        posicaoY = 60
        for quant,nome in enumerate(nomes):
            if quant == 12:
                break
            textoJogador = fonte.render(nome + " - "+str(estrela[nome]), True, branco)
            tela.blit(textoJogador, (80,posicaoY))
            posicaoY = posicaoY + 40

        pygame.display.update()
        relogio.tick(60)
  
menu(nome)