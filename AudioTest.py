import pygame
import random
import numpy
import wave
import struct
import math


pygame.init()
pygame.mixer.init()

pygame.display.set_mode((800,600)) # Displays blank window

# Sets values for each component for the tone
SAMPLE_WIDTH = 4
SAMPLE_RATE = 44100.0
BIT_DEPTH = 5.0
CHANNELS = 2

# Sets volume and length of tones being generated
frequency = 4000.0
sample_length = 121000
volume = 800.0
delay = 40000


# Combines the tones
def combine_sounds(tone_one, tone_two, sample_length):
    values = []
    for i in range(0, sample_length):
        values.append(tone_one[i] + tone_two[i])
    return values


# Creates the tones using sound waves
def generate_sine_wave(frequency, sample_rate, sample_length, volume):
    values = []
    for i in range (0, sample_length):
        value = math.sin(2 * math.pi * frequency * (i / sample_rate) * (volume * BIT_DEPTH))
        for j in xrange(0, CHANNELS):
            values.append(value)

    return values


# Function to save the tones generate
def save_file(filename, wav_data, sample_rate):
    packed_values = []
    for i in range(0, len(wav_data)):
        packed_value = struct.pack('h', wav_data[i])
        packed_values.append(packed_value)

    noise_out = wave.open(filename, 'w')
    noise_out.setparams((CHANNELS, SAMPLE_WIDTH, sample_rate, 0, 'NONE', 'not compressed'))
    value_str = ''.join((str(n) for n in packed_values))
    noise_out.writeframes(value_str)
    noise_out.close()


# Adds the delay for the tones
def tone_creation(tone, tone2, tone3, delay, sample_length):
    values = []
    for i in range(0, sample_length):
        values.append(tone[i])
        if i > delay:
            echo = tone2[i]*0.6
            values.append(echo + tone[i])
        if i < delay * 2:
            echo2 = tone3[i] * 0.6
            values.append(echo2 + tone2[i] + tone[i])
    return values

# Creates the 3 separate sound files
tone_one = generate_sine_wave(frequency, SAMPLE_RATE, sample_length, volume)
tone_two = generate_sine_wave(frequency, SAMPLE_RATE, sample_length, volume)
tone_three = generate_sine_wave(frequency, SAMPLE_RATE, sample_length, volume)

# Names the saved tone file
save_file('tone1.wav', tone_one, SAMPLE_RATE)
save_file('tone2.wav', tone_two, SAMPLE_RATE)
save_file('tone3.wav', tone_three, SAMPLE_RATE)

# Creates the combined sound files to form something like a song
create_music = tone_creation(tone_one, tone_two, tone_three, delay, 132000)

# Names the combined sound files
save_file('combined_tone_creation.wav', create_music, SAMPLE_RATE)
