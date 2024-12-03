import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir colores
BLANCO = (255, 255, 255)

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600

# Crear la pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Animación de Personaje de Anime")

# Cargar sprites del personaje
sprites = [pygame.image.load(f"sprites/sprite_{i}.png") for i in range(1, 9)]  
indice_sprite = 0

# Propiedades del personaje
pos_x = ANCHO // 2
pos_y = ALTO // 2
velocidad_x = 5

# Bucle principal
reloj = pygame.time.Clock()
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Mover el personaje
    pos_x += velocidad_x

    # Rebotar el personaje si alcanza los bordes
    if pos_x + sprites[indice_sprite].get_width() >= ANCHO or pos_x <= 0:
        velocidad_x = -velocidad_x

    # Actualizar el sprite a mostrar
    indice_sprite = (indice_sprite + 1) % len(sprites)

    # Dibujar todo
    pantalla.fill(BLANCO)
    pantalla.blit(sprites[indice_sprite], (pos_x, pos_y))
    pygame.display.flip()

    # Controlar la velocidad del bucle
    reloj.tick(10)
