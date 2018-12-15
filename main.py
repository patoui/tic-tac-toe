import math
import time
import pygame

pygame.init()

display_width = 320
display_height = 320

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Tic Tac Toe')

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
bright_green = (0, 255, 0)

clock = pygame.time.Clock()
boardImage = pygame.image.load('board.png')
cellSize = (boardImage.get_rect().size[0] + 10) // 3
xImage = pygame.image.load('x.png')
oImage = pygame.image.load('o.png')

isRunning = True
marker = 'o'
markers = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def display_text(text):
    TextSurf, TextRect = text_objects(text, pygame.font.SysFont('Arial', 30))
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.SysFont('Arial', 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def reset_game():
    print('in reset_game')
    markers = [['-','-','-'], ['-','-','-'], ['-','-','-']]

def gameover():
    print('in gameover')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button('Restart', (display_width // 2) - 50, (display_height // 2) + 15, 100, 30, bright_green, blue, reset_game)

        pygame.display.update()
        clock.tick(30)

def add_marker(markerType, xCell, yCell):
    if markers[yCell][xCell] == '-':
        markers[yCell][xCell] = markerType
    print(markers)

def display_markers():
    y = 0
    for row in markers:
        x = 0
        for column in row:
            if column == 'x':
                gameDisplay.blit(xImage, (x * cellSize, y * cellSize))
            elif column == 'o':
                gameDisplay.blit(oImage, (x * cellSize, y * cellSize))
            x += 1
        y += 1

def check_for_winner():
    player = '-'
    if (markers[0] == ['x','x','x'] or\
            markers[1] == ['x','x','x'] or\
            markers[2] == ['x','x','x'] or\
            (markers[0][0] == 'x' and markers[1][1] == 'x' and markers[2][2] == 'x') or\
            (markers[0][2] == 'x' and markers[1][1] == 'x' and markers[2][0] == 'x') or\
            (markers[0][0] == 'x' and markers[1][0] == 'x' and markers[2][0] == 'x') or\
            (markers[0][1] == 'x' and markers[1][1] == 'x' and markers[2][1] == 'x') or\
            (markers[0][2] == 'x' and markers[1][2] == 'x' and markers[2][2] == 'x')):
        player = 'x'
    elif (markers[0] == ['o','o','o'] or\
            markers[1] == ['o','o','o'] or\
            markers[2] == ['o','o','o'] or\
            (markers[0][0] == 'o' and markers[1][1] == 'o' and markers[2][2] == 'o') or\
            (markers[0][2] == 'o' and markers[1][1] == 'o' and markers[2][0] == 'o') or\
            (markers[0][0] == 'o' and markers[1][0] == 'o' and markers[2][0] == 'o') or\
            (markers[0][1] == 'o' and markers[1][1] == 'o' and markers[2][1] == 'o') or\
            (markers[0][2] == 'o' and markers[1][2] == 'o' and markers[2][2] == 'o')):
        player = 'o'

    if player == 'x' or player == 'o':
        display_text('Player ' + player.upper() +' Won!')
        return True
    else:
        return False

def game_loop():
    global isRunning
    global marker
    global markers

    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONUP:
                xQuadrant = math.floor(event.pos[0] / cellSize)
                yQuadrant = math.floor(event.pos[1] / cellSize)
                marker = 'o' if marker == 'x' else 'x'
                add_marker(marker, xQuadrant, yQuadrant)

        gameDisplay.fill(white)
        if check_for_winner():
            gameover()
        else:
            gameDisplay.blit(boardImage, (0, 0))
            display_markers()

        pygame.display.update()
        clock.tick(30)

game_loop()
# pygame.quit()
# quit()
