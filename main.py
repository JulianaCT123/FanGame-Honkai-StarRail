import pygame, random, os, time

pygame.init()

tamanho = (1200,673)
relogio = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
icone = pygame.image.load("assetsHSR/stellePlayerRE.png")
pygame.display.set_icon(icone)
pygame.display.set_caption("Bem-Vindo à Penacony!")

# Chamando os assets ---------------------------------------------------

# imagens:
fundo = pygame.image.load("assetsHSR/fundoRE.png")
fundoMenu = pygame.image.load("assetsHSR/fundoMenu.png")
stelle = pygame.image.load("assetsHSR/stellePlayerRE.png")
stelleMorreu = pygame.image.load("assetsHSR/stelleMorreu.png")
birdskull = pygame.image.load("assetsHSR/BirdskullRE.png")
memeAllSeer = pygame.image.load("assetsHSR/MemeAllseerRE.png")

# Fontes:
fonte = pygame.font.SysFont("comicsans",40)
fonteMiuda = pygame.font.SysFont("comicsans",20)
fonteTitulo = pygame.font.SysFont("arial", 50)

# Sons:
pygame.mixer.music.load("assetsHSR/AceInTheHole.mp3")
misselSom = pygame.mixer.Sound("assets/missile.wav")
somStelleMorte = pygame.mixer.Sound("assetsHSR/stelleSomMorte.mp3")
# -----------------------------------------------------------------------
bordaX = 1200
bordaY = 673
# Cores:
branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)

def jogar():

    pygame.mixer.music.load("assetsHSR/AgainstTheDay.mp3")
    #pygame.mixer.music.play(-1) # Botando a musica pra tocar / -1 para tocar em loop
    #pygame.mixer.Sound.play(misselSom) # Tocando o som do missel 1vez ja q ele ja começa caindo

    posicaoXpersona = 500
    posicaoYpersona = 300
    movimentoXpersona = 0
    movimentoYpersona = 0
    larguraPersona = 150
    alturaPersona = 150

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

    dificuldade = 60
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
            # Controle do personagem eixo Y
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_UP:
                movimentoYpersona = - 10
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_DOWN:
                movimentoYpersona = + 10
            elif evento.type == pygame.KEYUP and evento.key == pygame.K_UP:
                movimentoYpersona = 0
            elif evento.type == pygame.KEYUP and evento.key == pygame.K_DOWN:
                movimentoYpersona = 0
        
        posicaoXpersona = posicaoXpersona + movimentoXpersona  
        posicaoYpersona = posicaoYpersona + movimentoYpersona
        
        # Config colisão com as bordas:
        if posicaoXpersona < (bordaX - bordaX) - 30:
            posicaoXpersona = - 20
        elif posicaoXpersona > bordaX - 130 :
            posicaoXpersona = bordaX - 140
        
        #elif posicaoYpersona < 0:
        #    posicaoYpersona = 10
        #elif posicaoYpersona > 473:
        #    posicaoYpersona = 463

        tela.fill(branco)
        tela.blit(fundo, (0,0))
        tela.blit(stelle,(posicaoXpersona,posicaoYpersona))
       
        # Config movimento inimigo ------------------------------
        posicaoYbird = posicaoYbird + velBird # Configura o inimigo caindo 
        if posicaoYbird > bordaY:
            posicaoYbird = - alturaBird
            posicaoXbird = random.randint(0,bordaX)
            #pygame.mixer.Sound.play(misselSom)
            pontos = pontos + 1
        tela.blit(birdskull, (posicaoXbird, posicaoYbird)) # Mostra o inimigo                        

        posicaoYmeme1 = posicaoYmeme1 + velMeme1
        if posicaoYmeme1 > bordaY:
            posicaoYmeme1 = - alturaMeme1
            posicaoXmeme1 = random.randint(0,bordaX)
            pontos = pontos + 1
        tela.blit(memeAllSeer, (posicaoXmeme1, posicaoYmeme1))
        
        # Mostra aos pontos
        texto = fonte.render("Pontos:" + str(pontos), True, branco)
        tela.blit(texto,(10,10))
        # -------------------------------------------------------

        # Config colisao -------------------------------------------
        pixelsPersonaX = list(range(posicaoXpersona, posicaoXpersona + larguraPersona))
        pixelsPersonaY = list(range(posicaoYpersona, posicaoXpersona + alturaPersona))
        pixelBirdX = list(range(posicaoXbird, posicaoXbird + larguraBird))
        pixelBirdY = list(range(posicaoYbird, posicaoYbird + alturaBird))
        pixelMeme1X = list(range(posicaoXmeme1, posicaoXmeme1 + larguraMeme1))
        pixelMeme1Y = list(range(posicaoYmeme1, posicaoYmeme1 + alturaMeme1))

        #os.system('cls')
        #print( len( list( set(pixelMisselY).intersection(set(pixelsPersonaY) ) ) ) )
        if len( list( set( pixelBirdY).intersection (set(pixelsPersonaY)))) > dificuldade:
            if len ( list ( set(pixelBirdX).intersection(set(pixelsPersonaX) ) ) ) > dificuldade:
                dead()
            #else:
                #print("Ainda vivo, mas por pouco!")

        elif len( list( set( pixelMeme1Y ).intersection (set( pixelsPersonaY )) )) > dificuldade:
            if len (list ( set( pixelMeme1X ).intersection(set( pixelsPersonaX )) )) > dificuldade:
                dead()
        #else:
            #print("Ainda vivo")

        

        # ------------------------------------------------------------------
        pygame.display.update()
        relogio.tick(60)

def dead():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(somStelleMorte)
    while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    quit()
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    #print(evento.pos)
                    if botaoJogar.collidepoint(evento.pos):
                        jogar()
                elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                    jogar()
            
            tela.fill(preto)
            textoTitulo = fonteTitulo.render("Você Morreu :(", True, branco)
            tela.blit(textoTitulo,(100,250))
            botaoJogar = pygame.draw.rect(tela, branco, (100,400,400,50))
            textoJogar = fonte.render("Tentar Novamente", True, preto)            
            tela.blit(textoJogar,(125,390))
            textoEnter = fonteMiuda.render("ENTER para tentar novamente", True, branco)
            tela.blit(textoEnter, (100,450))
            tela.blit(stelleMorreu, (600,150))
            
            pygame.display.update()
            relogio.tick(60)

def menu():
    #pygame.mixer.music.play(-1)
    
    while True:            
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    quit()
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    #print(evento.pos)
                    if botaoJogar.collidepoint(evento.pos):
                        jogar()

            tela.fill(branco)
            tela.blit(fundoMenu,(0,0))
            textoTitulo = fonteTitulo.render("Bem Vindo à Penacony!", True, branco)
            tela.blit(textoTitulo,(50,250))
            botaoJogar = pygame.draw.rect(tela, branco, (100,400,400,50))
            textoJogar = fonte.render("Jogar", True, preto)
            tela.blit(textoJogar,(250,390))
            
            
            pygame.display.update()
            relogio.tick(60)
menu()