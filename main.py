import kahoot
import random
from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import pygame

pygame.init()

clients = []
code = input("Game code: ")
name = input("Bot name: ")

answered = False
while not answered:
  try:
    fps = int(input("Target FPS: ").strip(" "))
    answered = True
  except TypeError:
    print("Only type numbers in the field.")

answered = False
while not answered:
  try:
    botNum = int(input("Number of bots: ").strip(" "))
    answered = True
  except TypeError:
    print("Only type numbers in the field.")

for client in range(botNum):
  clients.append(kahoot.client())
  clients[client].join(code,name+str(client+1))
  pygame.time.Clock().tick(fps)
