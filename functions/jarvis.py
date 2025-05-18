from pygame import mixer
from pygame import time as pygame_time

mixer.init()

def play_sound(sound_file):
    sound = mixer.Sound(sound_file)
    sound.play()
    pygame_time.wait(int(sound.get_length() * 1000))

