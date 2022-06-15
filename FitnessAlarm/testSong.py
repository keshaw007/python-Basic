import pygame
import datetime
from datetime import datetime
from pygame import mixer
mixer.init()
mixer.music.load("eyes.mp3")
  
# Setting the volume
mixer.music.set_volume(100.0)
  
# Start playing the song

  
# infinite loop
while True:
    mixer.music.play(-1)
      
    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    query = input("  ")
      
    if query == 'p':
  
        # Pausing the music
        mixer.music.pause()
        f=open("music.txt", "a")
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        f.write("pause time is ", dt_string,end="\n")   
    elif query == 'r':
  
        # Resuming the music
        mixer.music.unpause()
    elif query == 'e':
  
        # Stop the mixer
        mixer.music.stop()
        break