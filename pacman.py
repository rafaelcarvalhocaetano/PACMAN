import pygame

pygame.init()


screen = pygame.display.set_mode((800, 600), 0)
AMARELA = (255, 255, 0)
PRETO = (0, 0, 0)
VELOCIDADE = 1


class Pacman:
    def __init__(self):
        self.linha = 1
        self.coluna = 1
        self.centro_x = 400
        self.centro_y = 300
        self.tamanho = 800 // 30
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.raio = int(self.tamanho / 2)

    """ PACMAN """
    def pintar(self, tela):
        """ CORPO DO PACMAN """
        pygame.draw.circle(tela, AMARELA, (self.centro_x, self.centro_y), self.raio, 0)

        """ BOCA """
        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
        labio_inferior = (self.centro_x + self.raio, self.centro_y)

        pontos = [canto_boca, labio_superior, labio_inferior]
        pygame.draw.polygon(tela, PRETO, pontos, 0)

        """ OLHO """
        olho_x = int(self.centro_x + self.raio / 5)
        olho_y = int(self.centro_y - self.raio * 0.70)
        olho_raio = int(self.raio / 10)
        pygame.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio, 0)

    def calcular_regras(self):
        self.coluna = self.coluna + self.velocidade_x
        self.linha = self.linha + self.velocidade_y
        self.centro_x = int((self.coluna * self.tamanho) + self.raio)
        self.centro_y = int((self.linha * self.tamanho) + self.raio)


    def processar_eventos(self, eventos):
        for e in eventos:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    self.velocidade_x = VELOCIDADE / 100
                elif e.key == pygame.K_LEFT:
                    self.velocidade_x = - VELOCIDADE / 100
                elif e.key == pygame.K_UP:
                    self.velocidade_y = - VELOCIDADE / 100
                elif e.key == pygame.K_DOWN:
                    self.velocidade_y = VELOCIDADE / 100

            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_RIGHT:
                    self.velocidade_x = 0
                elif e.key == pygame.K_LEFT:
                    self.velocidade_x = - 0
                elif e.key == pygame.K_UP:
                    self.velocidade_y = - 0
                elif e.key == pygame.K_DOWN:
                    self.velocidade_y = 0

    def processar_event_mouse(self, eventos):
        delay = 1000
        for e in eventos:
            if e.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = e.pos
                self.coluna = (mouse_x - self.centro_x) / delay
                self.linha = (mouse_y - self.centro_y) / delay


if __name__ == "__main__":

    pacman = Pacman()

    while True:
        """ ---- CALCULA REGRAS ---- """
        pacman.calcular_regras()

        """ 
            ---- PINTA A TELA ---- 
            pinta a dela de preto
        """
        screen.fill(PRETO)
        pacman.pintar(screen)
        pygame.display.update()

        """ ---- CAPTURA EVENTS ---- """
        eventos = pygame.event.get()
        for e in eventos:
            if e.type == pygame.QUIT:
                exit()
        pacman.processar_eventos(eventos)
        pacman.processar_event_mouse(eventos)
