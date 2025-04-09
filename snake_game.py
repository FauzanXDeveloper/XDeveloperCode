import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 50)
green = (0, 255, 0)
blue = (50, 153, 213)

display_width = 600
display_heigth = 400
display = pygame.display.set_mode((display_width, display_heigth))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 25)

def Your_score(score):
    value = score_font.render("Your score: " + str(score), True, black)
    display.blit(value, [0,0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, green, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [display_width / 6, display_heigth / 3])
    
def gameLoop():
    game_over = False
    game_close = False
    
    x1 = display_width /4
    y1 = display_heigth / 4
    
    x1_change = 0
    y1_change = 0
    
    snake_List = []
    Lenght_of_snake = 1
    
    foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, display_heigth - snake_block) / 10.0) * 10.0
    
    while not game_over:
        
        while game_close == True:
            display.fill(blue)
            message("You Lost! Press Q to quit or C to Play Again", yellow)
            Your_score(Lenght_of_snake - 1)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                    if event.key == pygame.K_c:
                        gameLoop()
                        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        
        if x1 >= display_width or x1 < 0 or y1 >= display_heigth or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        display.fill(blue)
        pygame.draw.rect(display, yellow, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Lenght_of_snake:
            del snake_List[0]
            
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        
        our_snake(snake_block, snake_List)
        Your_score(Lenght_of_snake - 1)
        
        pygame.display.update()
        
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, display_heigth - snake_block) / 10.0) * 10.0
            Lenght_of_snake += 1
            
        clock.tick(snake_speed)
        
    pygame.quit()
    quit()
    
gameLoop()
            