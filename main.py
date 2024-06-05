import pygame, random, os

pygame.init()

tamanho = (1200,673)
relogio = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
icone = pygame.image.load("assetsHSR/stellePlayerRE.png")
pygame.display.set_icon(icone)
pygame.display.set_caption("Iron Man")

# Chamando os assets ---------------------------------------------------

# imagens:
fundo = pygame.image.load("assetsHSR/fundoRE.png")
#fundoStart = pygame.image.load("assets/")
stelle = pygame.image.load("assetsHSR/stellePlayerRE.png")
birdskull = pygame.image.load("assetsHSR/BirdskullRE.png")
memeAllSeer = pygame.image.load("assetsHSR/MemeAllseerRE.png")

# Fontes:
fonte = pygame.font.SysFont("comicsans",20)
fonteMorte = pygame.font.SysFont("arial", 100)

# Sons:
pygame.mixer.music.load("assets/ironsound.mp3")
misselSom = pygame.mixer.Sound("assets/missile.wav")
explosaoSom = pygame.mixer.Sound("assets/explosao.wav")
# -----------------------------------------------------------------------
bordaX = 1200
bordaY = 673
# Cores:
branco = (255,255,255)
preto = (0,0,0)

def jogar():

    #pygame.mixer.music.play(-1) # Botando a musica pra tocar / -1 para tocar em loop
    #pygame.mixer.Sound.play(misselSom) # Tocando o som do missel 1vez ja q ele ja começa caindo

    posicaoXpersona = 500
    posicaoYpersona = 300
    movimentoXpersona = 0
    movimentoYpersona = 0
    larguraPersona = 150
    alturaPersona = 150

    posicaoXbird = 700
    posicaoYbird = -240
    velBird = 5
    alturaBird = 162
    larguraBird = 200

    posicaoYmeme1 = -163
    posicaoXmeme1 = 400
    alturaMeme1 = 102
    larguraMeme1 = 100
    velMeme1 = 10

    dificuldade = 30
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
        posicaoYbird = posicaoYbird + velBird # Configura o missel caindo e a velocidade 
        if posicaoYbird > 600:
            posicaoYbird = - alturaBird
            posicaoXbird = random.randint(0,1000)
            #pygame.mixer.Sound.play(misselSom)
            pontos = pontos + 1
        tela.blit(birdskull, (posicaoXbird, posicaoYbird)) # Mostra o missel

        posicaoYmeme1 = posicaoYmeme1 + velMeme1
        if posicaoYmeme1 > 600:
            posicaoYmeme1 = - alturaMeme1
            posicaoXmeme1 = random.randint(0,1200)
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


        os.system('cls')
        #print( len( list( set(pixelMisselY).intersection(set(pixelsPersonaY) ) ) ) )
        if len( list( set( pixelBirdY).intersection (set(pixelsPersonaY)))) > dificuldade:
            if len ( list ( set(pixelBirdX).intersection(set(pixelsPersonaX) ) ) ) > dificuldade:
                dead()
            #else:
                #print("Ainda vivo, mas por pouco!")
        elif len( list( set( pixelMeme1Y).intersection (set(pixelsPersonaY)))) > dificuldade:
            if len ( list ( set(pixelMeme1X).intersection(set(pixelsPersonaX) ) ) ) > dificuldade:
                dead()
        #else:
            #print("Ainda vivo")
        # ------------------------------------------------------------------
        pygame.display.update()
        relogio.tick(60)

def dead():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(explosaoSom)
    while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    quit()
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    print(evento.pos)
                    if buttonStart.collidepoint(evento.pos):
                        jogar()
                elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                    jogar()

            tela.fill(branco)
            buttonStart = pygame.draw.rect(tela, preto, (100,300,200,50))
            textoStart = fonte.render("Restart", True, branco)
            tela.blit(textoStart, (100,300))
            textoEnter = fonte.render("Press ENTER to continue...", True, preto)
            tela.blit(textoEnter, (100,250))

            
            pygame.display.update()
            relogio.tick(60)

def start():
    while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    quit()
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    print(evento.pos)
                    if buttonStart.collidepoint(evento.pos):
                        jogar()

            tela.fill(branco)
            buttonStart = pygame.draw.rect(tela, preto, (100,300,200,50))
            textoStart = fonte.render("Start", True, branco)
            tela.blit(textoStart, (100,300))
            
            
            pygame.display.update()
            relogio.tick(60)
start()