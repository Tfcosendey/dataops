import pygame

# Constantes (essas devem estar definidas em algum lugar no seu código)
RAIO_BOLA = 10
LARGURA_TELA = 800
ALTURA_TELA = 600
AZUL = (0, 0, 255)


class Bola:
    def __init__(self, x: int, y: int, vel_x: int, vel_y: int) -> None:
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y

    def mover(self) -> None:
        self.x += self.vel_x
        self.y += self.vel_y

    # Rebater nas bordas
        if self.x - RAIO_BOLA <= 0 or self.x + RAIO_BOLA >= LARGURA_TELA:
            self.vel_x *= -1
        if self.y - RAIO_BOLA <= 0 or self.y + RAIO_BOLA >= ALTURA_TELA:
            self.vel_y *= -1

    def desenhar(self, tela: pygame.Surface) -> None:
        pygame.draw.circle(tela, AZUL, (self.x, self.y), RAIO_BOLA)


def test_bola_move_direcao_certa():
    bola = Bola(x=100, y=100, vel_x=5, vel_y=3)
    bola.mover()
    assert bola.x == 105
    assert bola.y == 103


def test_bola_quica_nas_bordas_horizontais():
    bola = Bola(x=30, y=100, vel_x=-5, vel_y=0)  # bem na borda esquerda
    bola.mover()
    assert bola.vel_x == -5  # deve inverter direção


def test_bola_quica_nas_bordas_verticais():
    bola = Bola(x=100, y=30, vel_x=0, vel_y=-5)  # bem no topo
    bola.mover()
    assert bola.vel_y == -5  # deve inverter direção
