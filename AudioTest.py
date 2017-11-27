import pygame
import random


pygame.init()
pygame.mixer.init()

pygame.display.set_mode((800,600))

MusicTrack = 'Good_Times_Roll.mp3'
MusicTrack2 = "Dont_Be_Shy.mp3"
MusicTrack3 = "Ripped.mp3"

load_music = pygame.mixer.music.load
play_music = pygame.mixer.music.play


def play_sound():
    pick_a_song = random.randrange(0, 3)
    if pick_a_song == 0:
        load_music(MusicTrack)
        play_music(0,0)
        print '1'
    if pick_a_song == 1:
        load_music(MusicTrack2)
        play_music(0,0)
        print '2'
    if pick_a_song == 2:
        load_music(MusicTrack3)
        play_music(0,0)
        print '3'

'''
pygame.mixer.music.load(MusicTrack)
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)
'''
play_sound()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and pygame.K_RETURN:
            pygame.mixer.music.set_volume(1.0)

    if event.type == pygame.KEYDOWN and pygame.KEYUP:
        if event.key == pygame.K_RSHIFT:
            play_sound()
    pygame.display.update()
pygame.quit()
