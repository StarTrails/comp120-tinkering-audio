import pygame

pygame.init()
pygame.mixer.init()

pygame.display.set_mode((800,600))

MusicTrack = 'Glide.mp3'

pygame.mixer.music.load(MusicTrack)
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if event.type == pygame.KEYDOWN and pygame.K_RETURN:
        pygame.mixer.music.set_volume(1.0)

    pygame.display.update()

pygame.quit()
