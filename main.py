import pygame, random

pygame.init()
tamanho = (800,600)
relogio = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Iron Man")
branco = (255,255,255)
preto = (0,0,0)

# Chamando os assets
iron = pygame.image.load("assets/iron.png")
fundo =pygame.image.load("assets/fundo.png")
missel = pygame.image.load("assets/missile.png")
fonte = pygame.font.SysFont("comicsans",14)
pygame.mixer.music.load("assets/ironsound.mp3")
misselSom = pygame.mixer.Sound("assets/missile.wav")

posicaoXpersona = 400
posicaoYpersona = 300
movimentoXpersona = 0
movimentoYpersona = 0

posicaoXmissel = 400
posicaoYmissel = -240
velocidadeMissel = 5


pygame.mixer.music.play(-1) # Botando a musica pra tocar / -1 para tocar em loop
pygame.mixer.Sound.play(misselSom) # Tocando o som do missel 1vez ja q ele ja começa caindo

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
    
    # Faz o movimento acontecer:
    posicaoXpersona = posicaoXpersona + movimentoXpersona  
    posicaoYpersona = posicaoYpersona + movimentoYpersona
    
    # Para o boneco n sair da tela:
    if posicaoXpersona < 0:
        posicaoXpersona = 10
    elif posicaoXpersona > 550:
        posicaoXpersona = 540
    
    elif posicaoYpersona < 0:
        posicaoYpersona = 10
    elif posicaoYpersona > 473:
        posicaoYpersona = 463

    tela.fill(branco)
    tela.blit(fundo, (0,0)) # Botando a imagem de fundo
    tela.blit(iron,(posicaoXpersona,posicaoYpersona)) # Botando o IronMan

    # Config do Missel:
    posicaoYmissel = posicaoYmissel + velocidadeMissel # Configura o missel caindo e a velocidade 
    if posicaoYmissel > 600:
        posicaoYmissel = -240
        posicaoXmissel = random.randint(0,800)
        velocidadeMissel = velocidadeMissel + 1
        pygame.mixer.Sound.play(misselSom)

    tela.blit(missel, (posicaoXmissel, posicaoYmissel)) # Mostra o missel

    # Mostra as coordenadas do IronMan
    texto = fonte.render(str(posicaoXpersona) + "." + str(posicaoYpersona), True, branco)
    tela.blit(texto,(posicaoXpersona-30,posicaoYpersona-10))

    pygame.display.update()
    relogio.tick(60)
