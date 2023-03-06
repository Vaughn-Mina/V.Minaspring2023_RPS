# File created by Vaughn Mina

# import libraries
# needed for time stuff
from time import sleep 
# needed so that computer can choose random item from list
from random import randint
# a comprehensive game library for a use of python
import pygame as pg
# allows us to manage files and folders in terms of directory
import os 
# the file path
game_folder = os.path.dirname(__file__)
# prints file path
print(game_folder)
# 
choices = ("rock", "paper", "scissors")

def draw_text(text, size, color, x, y):
    font_name = pg.font.match_font('arial')
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    screen.blit(text_surface, text_rect)

def cpu_randchoice():
    # computer decides
    print("computer randomly decides . . .")
    # allows variable to be used outside of the function
    global cpu_randdecision
    # allows computer to randomly choose one of the options 
    cpu_randdecision = choices[randint(0,2)]
    return cpu_randdecision
# game settings
WIDTH=900
HEIGHT=900
FPS=30

# define colors (RGB values)
# Tuple are immutable -cannot change once created 
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
# necessary to even start the game. 
pg.init()
# be able to code in sounds
pg.mixer.init()
# displays window to play game
screen=pg.display.set_mode((WIDTH, HEIGHT))
# displays a caption when starting the game
pg.display.set_caption("Rock, Paper, Scssors...")
# sets a variable to the entire function
clock = pg.time.Clock()
# gets the images from my files
rock_image=pg.image.load(os.path.join(game_folder, "rock.jpg")).convert()
# storing not the pixels themselves, but where they are and how many there are 
rock_image_rect = rock_image.get_rect()
cpu_rock_image_rect = rock_image.get_rect()
paper_image=pg.image.load(os.path.join(game_folder, "paper.jpg")).convert()
paper_image_rect = paper_image.get_rect()
cpu_paper_image_rect = paper_image.get_rect()
scissors_image=pg.image.load(os.path.join(game_folder, "scissors.jpg")).convert()
scissors_image_rect = scissors_image.get_rect()
cpu_scissors_image_rect = scissors_image.get_rect()

# starts true-false statement
running = True
start_sceen= True
# assigns player choice and cpu choice to whatever can be inside the quotation marks
player_choice = ""
cpu_choice = ""

while running:
    # computer runs game at 30 fps 
    clock.tick(FPS)
# tells computer what else is going on in the game such as mouse movement and actions
# event = anytime anything happens on the screen or on the computer (clicking, typing, moving the mouse, etc.)
    for event in pg.event.get():
        # when cursor presses the massive "x" button top right to quit
        if event.type == pg.QUIT:
            running=False
        
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                print ("Let the games begin")
                start_sceen = False
        if event.type == pg.MOUSEBUTTONUP:
            # displays coordinates of whatever the mouse clicked on
                ############# get user input#################
                # human inputs
                # keyboard, mouse, controller, vr headset, etc
            # print (pg.mouse.get_pos()[0])
            # print (pg.mouse.get_pos()[1])
            mouse_coords = pg.mouse.get_pos()
            # sets variables to the coordinates first one is "x" the second one is "y"
            # tells computer to print a message when clicking on the image
            if rock_image_rect.collidepoint(mouse_coords):
                print("THE ROCK")
                player_choice = "rock"
                cpu_choice = cpu_randchoice()
                # rock_image_rect.y += 3
            elif paper_image_rect.collidepoint(mouse_coords):
                print("PAPER")
                player_choice = "paper"
                cpu_choice = cpu_randchoice()
            elif scissors_image_rect.collidepoint(mouse_coords):
                print("SCISSORS")
                player_choice = "scissors"
                cpu_choice = cpu_randchoice()
            else: 
                print ("void")
                # print(rock_image_rect.collidepoint(mouse_coords))
                # print (paper_image_rect.collidepoint(mouse_coords))
                # print (scissors_image_rect.collidepoint(mouse_coords))








    ########################### update and moves the picture #################################
    # rock_image_rect.x += 1
    # paper_image_rect.y += 2
    # paper_image_rect.x += 2
    # scissors_image_rect.y += 1.5

    ####################### draw ########################
    screen.fill(BLACK)
    screen.blit(rock_image, rock_image_rect)
    screen.blit(paper_image, paper_image_rect)
    screen.blit(scissors_image, scissors_image_rect)
    # computer checks if the player hit the space bar when it is on the starting screen
    if start_sceen:
       draw_text("Press space to play rock paper scissors", 22, WHITE, WIDTH/2, HEIGHT/10)
    rock_image_rect.x = 2000
    paper_image_rect.x = 2000
    scissors_image_rect.x = 2000
    if not start_sceen and player_choice == "":
    # shows images of either the rock, paper, or the scissors
        rock_image_rect.x = 150
        rock_image_rect.y = 300
        paper_image_rect.x = 450
        paper_image_rect.y = 300
        scissors_image_rect.x = 700
        scissors_image_rect.y = 300 

    
# checks if either the computer won, the player won, or if it was a tie
    if player_choice == "rock":
        if cpu_choice == "rock":
            rock_image_rect.x = 500
            cpu_rock_image_rect.x = 700
            screen.blit(rock_image, rock_image_rect)
            screen.blit(rock_image, cpu_rock_image_rect)
            draw_text("You tied!!!", 22, WHITE, WIDTH/2, HEIGHT/10)
        if cpu_choice == "paper":
            rock_image_rect.x = 500
            cpu_paper_image_rect.x = 700
            screen.blit(rock_image, rock_image_rect)
            screen.blit(paper_image, cpu_paper_image_rect)
            draw_text("You lost!!!", 22, WHITE, WIDTH/2, HEIGHT/10)
        if cpu_choice == "scissors":
            rock_image_rect.x = 500
            cpu_scissors_image_rect.x = 700
            screen.blit(rock_image, rock_image_rect)
            screen.blit(scissors_image, cpu_scissors_image_rect)
            draw_text("You win!!!", 22, WHITE, WIDTH/2, HEIGHT/10)
    if player_choice == "paper":
        if cpu_choice == "rock":
            paper_image_rect.x = 500
            cpu_rock_image_rect.x =700
            screen.blit(paper_image, paper_image_rect)
            screen.blit(rock_image, cpu_rock_image_rect)
            draw_text("You win!!!", 22, WHITE, WIDTH/2, HEIGHT/10)
        if cpu_choice == "paper":
            paper_image_rect.x = 500
            cpu_paper_image_rect.x = 700
            screen.blit(paper_image, paper_image_rect)
            screen.blit(paper_image, cpu_paper_image_rect)
            draw_text("You tied!!!", 22, WHITE, WIDTH/2, HEIGHT/10)
        if cpu_choice == "scissors":
            paper_image_rect.x = 500
            cpu_scissors_image_rect.x = 700
            screen.blit(paper_image, paper_image_rect)
            screen.blit(scissors_image, cpu_scissors_image_rect)
            draw_text("You lost!!!", 22, WHITE, WIDTH/2, HEIGHT/10)
    if player_choice == "scissors":
        if cpu_choice == "rock":
            scissors_image_rect.x = 500
            cpu_rock_image_rect.x = 700
            screen.blit(scissors_image, scissors_image_rect)
            screen.blit(rock_image, cpu_rock_image_rect)
            draw_text("You lost!!!", 22, WHITE, WIDTH/2, HEIGHT/10)
        if cpu_choice == "paper":
            scissors_image_rect.x = 500
            cpu_paper_image_rect.x = 700
            screen.blit(scissors_image, scissors_image_rect)
            screen.blit(paper_image, cpu_paper_image_rect)
            draw_text("You win!!!", 22, WHITE, WIDTH/2, HEIGHT/10)
        if cpu_choice == "scissors":
            scissors_image_rect.x = 500
            cpu_scissors_image_rect.x = 700
            screen.blit(scissors_image, scissors_image_rect)
            screen.blit(scissors_image, cpu_scissors_image_rect)
            draw_text("You tied!!!", 22, WHITE, WIDTH/2, HEIGHT/10)


    pg.display.flip()

pg.quit()

    