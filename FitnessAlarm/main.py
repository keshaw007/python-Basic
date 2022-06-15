# Module used in this pregram
import time
import pygame
from pygame import mixer
mixer.init()

# header
print("\n********************WELCOME TO MY PROGRAM********************\n")
time.sleep(2)
print("\n--------------------THIS PROGRAM HELPS YOU IN YOUR FITNESS---------------\n")


# all functions definition

# FOR DRINKING WATER
def water_drinking():
    print("------------------DRINKING TIME----------------\n")
    while(True):
        mixer.music.load("water.mp3")
        mixer.music.play(-1)
        print("\nDRINK SOME WATER\n")
        print("\ntype ""DONE"" in uppercase as shown to stop ALARM\n")
        ans = input()
        if(ans == "DONE"):
            mixer.music.stop()
            break
        else:
            print("\nInvalid input\n")
            continue

# FOR EYE RELAXATION

def eye_relaxation():
    print("-----------------RELAX YOUR EYES FOR SOMETIME-------------\n")
    while(True):
        mixer.music.load("eyes.mp3")
        mixer.music.play(-1)
        print("\nPLEASE RELAX YOUR EYES\n")
        print("\ntype ""DONE"" in uppercase as shown to stop ALARM\n")
        ans = input()
        if(ans == "DONE"):
            mixer.music.stop()
            break
        else:
            print("\nInvalid input\n")
            continue

# FOR PHYSICAL EXERCISE

def physical_exercise():
    print("-------------TIME FOR SOME PHYSICAL EXERCISE---------------\n")
    while(True):
        mixer.music.load("physical.mp3")
        mixer.music.play(-1)
        print("\nIT'S TIME TO DO SOME PHYSICAL EXERCISE\n")
        print("\ntype ""DONE"" in uppercase as shown to stop ALARM\n")
        ans = input()
        if(ans == "DONE"):
            mixer.music.stop()
            break
        else:
            print("\nInvalid input\n")
            continue


# main function
starting_time = int(time.time())
while(True):

    # calculating time interval
    ending_time = int(time.time())
    time_interval = ending_time-starting_time

    # if all time coincide
    if(time_interval % 180 == 0 and time_interval % 300 == 0 and time_interval % 420 == 0 and time_interval > 0):
        water_drinking()
        physical_exercise()
        eye_relaxation()

    # if any of two time coincide
    elif(time_interval % 180 == 0 and time_interval % 300 == 0 and time_interval > 0):
        water_drinking()
        eye_relaxation()
    elif(time_interval % 180 == 0 and time_interval % 420 == 0 and time_interval > 0):
        water_drinking()
        physical_exercise()
    elif(time_interval % 420 == 0 and time_interval % 300 == 0 and time_interval > 0):
        physical_exercise()
        eye_relaxation()

    # if all time different
    elif(time_interval % 180 == 0 and time_interval > 0):
        water_drinking()
    elif(time_interval % 300 == 0 and time_interval > 0):
        eye_relaxation()
    elif(time_interval % 420 == 0 and time_interval > 0):
        physical_exercise()

"""    # STOPPING THE PROGRAM
    print("\ntype EXIT in uppercase to exit from program\n")
    user_answer = input()
    if(user_answer == "EXIT"):
        break
    else:
        print("\nOOPS! Please enter a valid input\n")
        continue"""
