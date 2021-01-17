import pygame
from random import randint

pygame.init()

#Window Title
pygame.display.set_caption("Hand of God")

#Window variables
screen_width = 1100
screen_height = 690
display_output = [screen_width, screen_height]
screen = pygame.display.set_mode(display_output)

#Imports
background = pygame.image.load('background.jpg')         #Background
DM = pygame.image.load('Maradona.png')                   #Diego Maradona Character
soccerball = pygame.image.load('soccerball.png')         #Soccerball


#Variable used to slow down ball drop speed
clock = pygame.time.Clock()

#"Score" font variables
text_x = 850
text_y = 10
font = pygame.font.Font('freesansbold.ttf', 50)


#character variables
DM_width = 125
DM_pos_x = 450
DM_pos_y = 600
DM_y_line = DM_pos_y + 17
DM_x_start_co = DM_pos_x + 40
DM_x_end_co = DM_pos_x + 85
DM_speed_x = 10
present_DM_speed_x = 0


#ball variables
ball_size = 100
ball_position_x = 50
ball_position_y = 50
ball_x_co = ball_position_x + 50
ball_y_co = ball_position_y + 50
speed_dir_x = 0
speed_dir_y = 4

#Score starts at 0
score = 0

#Displaying background
def display_bg():
    screen.blit(background, (-150, 0))

#Displaying the falling soccerball
def display_soccerball(pos_x, pos_y):
    screen.blit(soccerball, (pos_x, pos_y))
    update_ball_pos()

#Displaying Diego Maradona character
def display_DM(pos_x, pos_y):
    screen.blit(DM, (pos_x, pos_y))

#Displaying all images
def display():
    display_bg()
    display_soccerball(ball_position_x, ball_position_y)
    display_DM(DM_pos_x, DM_pos_y)

#Check if valid for score
def check_for_DM(x):
    if ball_y_co in range(DM_y_line-(int(speed_dir_y)//2), DM_y_line+(int(speed_dir_y)//2)):
        if ball_x_co in range(DM_x_start_co-1, DM_x_end_co+1):
            x += 1
        else:
            x = 0
    return x

#Displaying score
def display_score(sco, text_pos_x, text_pos_y):
    score_disp = font.render("Score: " + str(sco), True, (0, 0, 0))
    screen.blit(score_disp, (text_pos_x, text_pos_y))

#User control
def clickables():
    global play_game, present_DM_speed_x

    #To exit the game from the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play_game = False

    #Controls for movement of Maradona character
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        present_DM_speed_x = - DM_speed_x
    elif keys[pygame.K_RIGHT]:
        present_DM_speed_x = DM_speed_x
    else:
        present_DM_speed_x = 0


#Function to make sure basket doesn't go out of the window
def enforce_border():
    global DM_pos_x
    if DM_pos_x > (screen_width-DM_width):
        DM_pos_x = screen_width-DM_width
    if DM_pos_x < 0:
        DM_pos_x = 0

#To initialize the ball after the first drop
def random_ball_initialize():
    global ball_position_y, ball_position_x, speed_dir_y
    if ball_position_y > (screen_height + ball_size):
        speed_dir_y = 3                         #Speed of the ball (frames/second)
        ball_position_x = randint(0, 924)       #Range of the ball dropping
        ball_position_y = 0                     #Where the ball falls from (top of the screen)

#Updating Maradona score region
def update_DM_score_region():
    global DM_x_start_co, DM_x_end_co
    DM_x_start_co = DM_pos_x + 40
    DM_x_end_co = DM_pos_x + 85

#Updating ball position
def update_ball_pos():
    global ball_x_co, ball_y_co, DM_pos_x, ball_position_y, speed_dir_y
    ball_x_co = ball_position_x + 50
    ball_y_co = ball_position_y + 50
    DM_pos_x += present_DM_speed_x
    ball_position_y += int(speed_dir_y)
    speed_dir_y += (speed_dir_y*0.02)
    random_ball_initialize()

#Initializing after first drop
def initialize():
    clickables()
    enforce_border()

play_game = True

#Main loop
while play_game:
    clock.tick(60)
    initialize()
    display()
    update_DM_score_region()
    score = check_for_DM(score)
    display_score(score, text_x, text_y)
    pygame.display.flip()
pygame.quit()