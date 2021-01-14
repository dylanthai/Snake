#########################################
# File Name: Snake Game.py
# Description: Recreation of Snake
# Author: Dylan Thai
# Date: 12/4/2017
#########################################

from random import randint

import pygame
pygame.init()
WIDTH = 800
HEIGHT= 600
MIDDLE = int(WIDTH/2.0)
TOP = 0
BOTTOM = HEIGHT
gameWindow=pygame.display.set_mode((WIDTH,HEIGHT))

score = 0

font = pygame.font.SysFont("Courier New Bold",36)

WHITE = (255,255,255)
BLACK = (  0,  0,  0)
RED   = (255,  0,  0)
outline=0

#---------------------------------------#
# snake's properties                    #
#---------------------------------------#
BODY_SIZE = 5
HSTEP = 10
VSTEP = 10
speedX = 0
speedY = -VSTEP                    # initially the snake moves from bottom up
segX = []
segY = []
ax = int(round(randint(0,WIDTH),-1))
ay = int(round(randint(0,HEIGHT),-1))
drawApple = True

#---------------------------------------#
# function that redraws all objects     #
#---------------------------------------#
def drawApple(ax,ay):
    pygame.draw.circle(gameWindow, RED, [ax, ay], 5)
    
def redrawGameWindow():
    gameWindow.fill(BLACK)
    drawApple(ax,ay)
    for i in range(len(segX)):
        segmentCLR = (randint(0,255),randint(0,255),randint(0,255)) 
        pygame.draw.circle(gameWindow, segmentCLR, (segX[i], segY[i]), BODY_SIZE, outline)
    pygame.display.update() 
def youLose(): 
    gameWindow.fill(BLACK)
    graphics = font.render("You Lose :(",1,WHITE)
    gameWindow.blit(graphics,(350,300))
    pygame.display.update()
    
#---------------------------------------#
# the main program begins here          #
#---------------------------------------#
for i in range(4):                      # add coordinates for the head and 3 segments
    segX.append(MIDDLE)
    segY.append(MIDDLE + i*VSTEP)

print "Use the arrows and the space bar."
print "Hit ESC to end the program."    

inPlay = True
while inPlay:
    redrawGameWindow()
    pygame.time.delay(30)
    
# check for events
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        inPlay = False
    if keys[pygame.K_LEFT]:
        speedX = -HSTEP
        speedY = 0
    if keys[pygame.K_RIGHT]:
        speedX = HSTEP
        speedY = 0
    if keys[pygame.K_UP]:
        speedX = 0
        speedY = -VSTEP
    if keys[pygame.K_DOWN]:
        speedX = 0
        speedY = VSTEP
    if keys[pygame.K_SPACE]:            # if space bar is pressed, add a segment:
        segX.append(segX[-1])           # assign the same x and y coordinates
        segY.append(segY[-1])           # as those of the last segment

# move the segments
    numOfSegments = len(segX)-1
    for i in range(numOfSegments,0,-1): # starting from the tail, and going backwards:
        segX[i]=segX[i-1]               # every segment takes the coordinates
        segY[i]=segY[i-1]               # of the previous one
        
# move the head
    segX[0] = segX[0] + speedX
    segY[0] = segY[0] + speedY

# Eatting apple
    if segX[0] == ax and segY[0] == ay:
        score = score + 1
        ax = int(round(randint(0,WIDTH),-1))
        ay = int(round(randint(0,HEIGHT),-1))
        segX.append(MIDDLE)
        segY.append(MIDDLE + i*VSTEP)

#Losing mechanism
    if segX[0] == segX[2] and segY[0] == segY[2]:
        inPlay = False
##    if segX[0] == segX[(-1)] and segY[0] == segY[(-1)]:
##        inPlay = False
    if segX[0] <= -1 or segX[0] >= WIDTH+1 or segY[0]<=-1 or segY[0]>=HEIGHT+1:
        inPlay = False

youLose()
pygame.time.delay(2000)
print "Score:",score
#---------------------------------------#    
pygame.quit()
