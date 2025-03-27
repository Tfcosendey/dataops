"""Módulo principal para execução do jogo com a bola  e quicando nas bordas."""

import random
import pygame  # pylint: disable=import-error

# Inicialização do pygame
pygame.init()  # pylint: disable=no-member

# Constantes da tela
LARGURA = 800
ALTURA = 600

# Cores
AZUL = (0, 0, 255)
BRANCO = (255, 255, 255)

# Constantes da bola
RAIO = 20


class Bola:
    """Classe que representa a bola no jogo."""

    def __init__(self, x: int, y: int, vel_x: int, vel_y: int) -> None:
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y

    def mover(self) -> None:
        """Atualiza a posição da bola e inverte a direção se bater nas."""
        self.x += self.vel_x
        self.y += self.vel_y

        if self.x - RAIO <= 0 or self.x + RAIO >= LARGURA:
            self.vel_x *= -1

        if self.y - RAIO <= 0 or self.y + RAIO >= ALTURA:
            self.vel_y *= -1

    def desenhar(self, tela: pygame.Surface) -> None:
        """Desenha a bola na tela."""
        pygame.draw.circle(tela, AZUL, (self.x, self.y), RAIO)


def main() -> None:
    """Função principal que roda o loop do jogo."""
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Jogo da Bola")

    bola = Bola(x=LARGURA // 2, y=ALTURA // 2,
                vel_x=random.choice([-5, 5]), vel_y=random.choice([-3, 3]))

    rodando = True
    clock = pygame.time.Clock()

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # pylint: disable=no-member
                rodando = False

        bola.mover()

        tela.fill(BRANCO)
        bola.desenhar(tela)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()  # pylint: disable=no-member


if __name__ == "__main__":
    main()
