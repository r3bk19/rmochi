import pygame
import time

# Inicializar pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Configuración de la pantalla
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Te Amo Mochi")

# Fuente
font = pygame.font.Font(None, 50)

# Mensaje de amor
messages = ["Eres Mi Pequeña Princesa", "Feliz Segundo Aniversario", "Te Amo Mucho Mochi"]

running = True
index = 0

while running:
    screen.fill(WHITE)
    
    # Renderizar el mensaje actual
    text = font.render(messages[index], True, RED)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
    
    pygame.display.flip()
    
    # Esperar antes de cambiar el mensaje
    time.sleep(2)
    
    # Pasar al siguiente mensaje
    index = (index + 1) % len(messages)
    
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
pygame.quit()