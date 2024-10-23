import os
import sys
import time
import random

from colorama import Fore, init

init(strip=not sys.stdout.isatty())
from pyfiglet import figlet_format
from termcolor import cprint


def clear():
  os.system('clear')

def wait(s):
  time.sleep(s)

player = {
  "name": "",
  "money": 0,
  "health": 3,
  "inventory": ["ripped gown"]
}

cprint(figlet_format('Lights Out The Demo', font='big'),
      'yellow','on_red',attrs=['bold'])



print()
input("Press ENTER to continue after each line. When you see '...' don't press ENTER.")
clear()
input("you wake up dazed an confused")
print()
print("what do you do?")
print("A: go back to sleep")
print("B: look at your surroundings")

choice1 = input('::').upper()
if choice1 == "A":
  player["health"] -= 3
  print("you sleep and a weird man gamends you")
  quit()
elif choice1 == "B":
  clear()
  for i in range(3):
    print("...")
    wait(0.4)
else:
  print("invalid choice. you gamend")
  quit()

input("you look down and see a nametag on your tattered gown.")
player["name"] = input("what does it say?\n")
print("this will be your name")
clear()

input("you look around and see brick walls with chipped paint.") 
input("you find yourself in a rusted metal bed with dirty sheets.")
input("the room you're in is dark with a Murky smell.")
input("more rusted beds like yours line the walls.")
clear()
print("there's a slightly open door to your left and a broken window to your right.")
print("where do you go?")
print("A: door")
print("B: window")

choice2 = input('::').upper()
clear()

if choice2 == "A":
  input("you end up in a hallway, you see overgrown weeds coming through the window.")
elif choice2 == "B":
  player["health"] -= 3
  input("You Cut your leg and take too high of a fall.")
  print("womp womp")
  quit()
else:
  print("invalid choice. gamend")
  quit()

input("you ask yourself where am i")
input("you see a flashlight next to the weeds")
print("do you pick it up??????????")
print("A: yes")
print("B: no")

choice3 = input('::').upper()
clear()
from tqdm import tqdm
if choice3 == "A":
  player["inventory"].append("flashlight")
  print(f"{Fore.GREEN}flashlight added to inventory.{Fore.WHITE}")
elif choice3 == "B":
  pass
else:
  print("invalid choice. gamend")
  quit()

input("you see a split in the hallway")
input("there is also a door at the end")
print("where do you go")
print("A: split")
print("B: door")

choice4 = input("::").upper()
clear()

if choice4 == "A":
  pass
elif choice4 == "B":
  input("you go through the door and find yourself in a dark room")
  if "flashlight" in player["inventory"]:
    input("you turn on your flashlight to see a poster on the wall.")
    input(f"it's an image of a {Fore.BLUE}raspberry{Fore.WHITE}")
    input("you turn back and exit the room.")
    clear()
else:
  print("invalid choice. gameend")
  quit()
  
input("you take the split and turn")
input("a disgusting combination of flesh, bones, and organs slowly turns its head towards you")
for i in range(3):
  print("...")
  wait(0.7)
clear()
wait(1)
input(f"{Fore.RED}ROARRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR{Fore.WHITE}")
input("you have nothing to protect yourself")
print(" quick, what do you say???????")

choice5 = input(":: ")

if choice5 == "raspberry" or choice5 == "Raspberry":
  clear()
  print("the monster goes away")
else:
  print("the monster kills you")
  cprint(figlet_format('Lights Out By James Herrmann', font='big'),
    'yellow','on_red',attrs=['bold'])
  quit()
  
input("You walk down the split and reach a door")
input("Do you open the door")
print("A:Yes")
print("B:No")

choice6 = input(":: ").upper()
if choice6 == "A":
  print(f"{Fore.GREEN}Spear added to inventory.{Fore.WHITE}")
  player["inventory"].append("Spear")
else:
  pass
input("you continue down a hall and reach the out side ")
input("You see hundreds of skyscrapers")
input("but somethings wrong the whole city is overgrown in weeds")
input("Not one person is visable")
input("you see a few intresting building")
input("the building consist of genaral store, gas station, factory,")
input("where do you go?")
print("A:genaral store")
print("B:gas station")
print("C:Factory")
print("D:Police station")
choice7 = input(":: ").upper()
if choice7 == "A":
 for i in tqdm (range (100), desc="Loading..."):
      pass
#buildings genaral store, gas station, factory,

numGuesses = 3
rand = random.randint(1, 10)
userInput = None

print(rand)

while userInput != rand and numGuesses > 0:
 userInput = int(input("Guess a number from 1 to 15: "))
   numGuesses -= 1
  if rand > userInput: 
    print("higher")
  elif rand < userInput:
     print("lower")

 
   print("the monster gamends you")
 else: 
  print("The moster screeches in pain and they gamend")
