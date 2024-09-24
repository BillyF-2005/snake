import pygame as pg
from random import randrange
from button import button

pg.init()

window = 1000
tile_size = 50
range = (tile_size // 2, window - tile_size // 2, tile_size)
get_random_position = lambda: [randrange(*range), randrange(*range)]
snake = pg.rect.Rect([0, 0, tile_size - 2, tile_size - 2])
snake.center = get_random_position()
length = 1
segments = [snake.copy()]
snake_dir = (0,0)
time, time_step = 0, 110
food = snake.copy()
food.center = get_random_position()
screen = pg.display.set_mode([window]*2)
clock = pg.time.Clock()
main = True
end = False
exitButtonPressed = False
playAgainPressed = False
click = False
mousePos = (0,0)

exitButton = button(screen,500,600,50,'red',"EXIT")
playAgain = button(screen,500,500,50,'green',"PLAY AGAIN")

while True:
    while main == True:
        for event in pg.event.get():
            if event.type == pg.quit:
                exit()
        
            if event.type == pg.KEYDOWN:
                if (event.key == pg.K_w) and snake_dir != [0, tile_size]:
                    snake_dir = [0, -tile_size]
                if (event.key == pg.K_s) and snake_dir != [0, -tile_size]:
                    snake_dir = [0, tile_size]
                if (event.key == pg.K_d) and snake_dir != [-tile_size, 0]:
                    snake_dir = [tile_size, 0]
                if (event.key == pg.K_a) and snake_dir != [tile_size, 0]:
                    snake_dir = [-tile_size, 0]
                if (event.key == pg.K_ESCAPE):
                    exit()
    
        screen.fill('black')
        if food.center == snake.center:
            food.center = get_random_position()
            length += 1
        pg.draw.rect(screen, 'red', food)
        [pg.draw.rect(screen, 'green', segment) for segment in segments]
        time_now = pg.time.get_ticks()
        if time_now - time > time_step:
            time = time_now
            snake.move_ip(snake_dir)
            segments.append(snake.copy())
            segments = segments[-length:]
        if segments.count(snake) == 2:
            print('self collision')
            snake_dir = [0,0]
            snake.center = get_random_position()
            segments.clear()
            segments = [snake.copy()]
            end = True
            main = False
        if snake.x < 0 or snake.y < 100:
            if snake_dir != (0,0):
                print('outside of the boundaries')
                snake_dir = [0,0]
                snake.center = get_random_position()
                segments.clear()
                segments = [snake.copy()]
                end = True
                main = False
            else:
                snake.center = get_random_position()
        if snake.x > 1000 or snake.y > 850:
            if snake_dir != (0,0):
                print('outside of the boundaries')
                snake_dir = [0,0]
                snake.center = get_random_position()
                segments.clear()
                segments = [snake.copy()]
                end = True
                main = False
            else:
                snake.center = get_random_position()
        if food.x < 0 or food.y < 100 or food.x > 1000 or food.y > 850:
            food.center = get_random_position()
        if segments.count(food) > 0 and food.center != snake.center:
            food.center = get_random_position()
        pg.display.flip()
        clock.tick(60)

    while end:
        screen.fill('black')
        font = pg.font.SysFont('Calibri', 75, True, False)
        text = font.render('GAME OVER', True, (255,255,255))
        textwidth = text.get_width()
        screen.blit(text,[500 - 0.5 * textwidth,350])
        exitButton.drawButton()
        playAgain.drawButton()
        for event in pg.event.get():
            exitButtonPressed = exitButton.isPressed()
            playAgainPressed = playAgain.isPressed()
            if event.type == pg.KEYDOWN:
                if (event.key == pg.K_ESCAPE):
                    exit()
        if playAgainPressed:
            print('play')
            snake_dir = [0,0]
            snake.center = get_random_position()
            while snake.y > 850 or snake.y < 100:
                snake.center = get_random_position()
            segments.clear()
            segments = [snake.copy()]
            length = 1
            playAgainPressed = False
            main = True
            end = False
        if exitButtonPressed:
            print('exit')
            exit()
        time_now = pg.time.get_ticks()
        pg.display.flip()
        clock.tick(60)
        
