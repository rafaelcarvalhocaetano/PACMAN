import pygame

pygame.init()

AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)
VELOCIDADE = 0.1
RADIO = 10

tela = pygame.display.set_mode((640, 480), 0)

x = 10
y = 10

velocidade_x = VELOCIDADE
velocidade_y = VELOCIDADE

while True:
    # Calcula as regras
    x += velocidade_x
    y += velocidade_y

    if x + RADIO > 640:
        velocidade_x = - VELOCIDADE

    if x - RADIO < 0:
        velocidade_x = + VELOCIDADE

    if y + RADIO > 480:
        velocidade_y = - VELOCIDADE

    if y - RADIO < 0:
        velocidade_y = + VELOCIDADE






    # Pinta
    tela.fill(PRETO)
    pygame.draw.circle(tela, AMARELO, (int(x), int(y)), RADIO, 0)
    pygame.display.update()




    # Eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
