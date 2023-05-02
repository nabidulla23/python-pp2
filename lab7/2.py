import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
running = True
pygame.mixer.music.load('lab7\Anuran.mp3')
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_p:
                pygame.mixer.music.play(0)
            if event.key == pygame.K_s:
                pygame.mixer.music.stop()
            if event.key==pygame.K_n:
                pygame.mixer.music.stop()
                pygame.mixer.music.load('lab7\Menqazaq.mp3')
                pygame.mixer.music.play(0)
            if event.key==pygame.K_b:
                pygame.mixer.music.stop()
                pygame.mixer.music.load('lab7\Anuran.mp3')
                pygame.mixer.music.play(0)
    pygame.display.flip()