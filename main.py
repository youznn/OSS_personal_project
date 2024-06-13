"""
Snake Eater
Made with PyGame
"""

import pygame, sys, time, random

# Initialize Pygame
pygame.init()

# Load the image
apple_image = pygame.image.load('./assets/apple.png')
apple_image = pygame.transform.scale(apple_image, (20, 20))
heart_image = pygame.image.load('./assets/heart.png')
heart_image = pygame.transform.scale(heart_image, (20, 20))
snake_head_image = pygame.image.load('./assets/snake_head.png')
snake_head_image = pygame.transform.scale(snake_head_image, (20,20))
snake_body_image = pygame.image.load('./assets/snake_body.png')
snake_body_image = pygame.transform.scale(snake_body_image, (20,20))

####################################################################
####################phase2추가######################################
####################################################################
redrec_image = pygame.image.load('./assets/redrec.png')
redrec_image = pygame.transform.scale(redrec_image, (20, 20))

poison_apple_image = pygame.image.load('./assets/poison_apple.png')
poison_apple_image = pygame.transform.scale(poison_apple_image, (20, 20))
####################################################################
####################phase2추가######################################
####################################################################


font_path = 'Retro Gaming.ttf'

# Difficulty settings
# Easy      ->  10
# Medium    ->  25
# Hard      ->  40
# Harder    ->  60
# Impossible->  120
difficulty = 25

# Window size
frame_size_x = 720
frame_size_y = 480

# Checks for errors encountered
check_errors = pygame.init()
# pygame.init() example output -> (6, 0)
# second number in tuple gives number of errors
if check_errors[1] > 0:
    print(f'[!] Had {check_errors[1]} errors when initialising game, exiting...')
    sys.exit(-1)
else:
    print('[+] Game successfully initialised')

# Initialise game window
pygame.display.set_caption('Snake Eater')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))

# Colors (R, G, B)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
yellow = pygame.Color(255, 255, 0)
orange = pygame.Color(255, 165, 0)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# FPS (frames per second) controller
fps_controller = pygame.time.Clock()


#restart 화면입니다
def restart_button():
    my_font = pygame.font.Font(font_path, 25)
    restart_surface1 = my_font.render('TRY AGAIN? PRESS ENTER TO RESTART', True, white)
    restart_rect1 = restart_surface1.get_rect()
    restart_rect1.midtop = (frame_size_x/2, frame_size_y/1.8)
    restart_surface2 = my_font.render('OR ESC TO ESCAPE', True, white)
    restart_rect2 = restart_surface2.get_rect()
    restart_rect2.midtop = (frame_size_x/2, frame_size_y/1.6)
    game_window.blit(restart_surface1, restart_rect1)
    game_window.blit(restart_surface2, restart_rect2)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #Enter key
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main()
                #ESC key
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

# Game Over
def game_over(snake_body):
    global lives
    lives -= 1
    
    #목숨이 전부 소진된다면 게임을 끝냅니다
    if lives <= 0:
        my_font = pygame.font.Font(font_path, 90)
        game_over_surface = my_font.render('YOU DIED', True, red)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (frame_size_x/2, frame_size_y/4)
        game_window.fill(black)
        game_window.blit(game_over_surface, game_over_rect)
        show_score(0, red, font_path, 20)
        pygame.display.flip()
        restart_button()

    #목숨이 남아있을 경우, pos를 가운데로 옮깁니다.
    else:
        snake_pos = [frame_size_x//2 , frame_size_y//2]
        blink_snake(snake_body)
        return snake_pos

#목숨이 소진되었을 시에 snake가 깜박이게 하는 효과
def blink_snake(snake_body):
    blink_ticks = pygame.time.get_ticks()
    while pygame.time.get_ticks() - blink_ticks < 1000:
        game_window.fill(black)
        for pos in snake_body:
            pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 20, 20))
        pygame.display.flip()
        pygame.time.wait(200)
        game_window.fill(black)
        pygame.display.flip()
        pygame.time.wait(200)

#초기 화면
def start_screen():
    # 초기 난이도 = MEDIUM
    global difficulty
    difficulties = ['EASY', 'MEDIUM', 'HARD', 'IMPOSSIBLE']
    diff_colors = [white, yellow, orange, red]
    cursor = 1
    font = pygame.font.Font(font_path, 70)
    game_window.fill(black)
    start_surface = font.render('SNAKE EATER', True, green)
    start_rect = start_surface.get_rect()
    start_rect.midtop = (frame_size_x/2, frame_size_y/4)
    game_window.blit(start_surface, start_rect)

    info_font = pygame.font.Font(font_path, 25) 
    info_surface = info_font.render('PRESS ENTER TO START', True, white)
    info_rect = info_surface.get_rect()
    info_rect.midtop = (frame_size_x/2, frame_size_y/1.8)
    game_window.blit(info_surface, info_rect)

    # 난이도 선택
    diff_font = pygame.font.Font(font_path, 20)
    diff_info_text = diff_font.render('CHOOSE DIFFICULTY: UP/DOWN KEYS', True, white)
    diff_info_rect = diff_info_text.get_rect(midtop=(frame_size_x/2.4, frame_size_y/1.35))
    game_window.blit(diff_info_text, diff_info_rect)
    difficulty_text = font.render(difficulties[cursor], True, diff_colors[cursor])
    difficulty_rect = difficulty_text.get_rect(midtop=(frame_size_x/4, frame_size_y/1.3))
    game_window.blit(difficulty_text, difficulty_rect)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    difficulty = [10, 20, 35, 80][cursor]
                    return
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_UP:
                    cursor = min(3, cursor +1)
                    difficulty_text = font.render(difficulties[cursor], True, diff_colors[cursor])
                    game_window.fill(black) 
                    game_window.blit(start_surface, start_rect)
                    game_window.blit(info_surface, info_rect)
                    game_window.blit(diff_info_text, diff_info_rect)
                    game_window.blit(difficulty_text, difficulty_rect)
                    pygame.display.flip()
                elif event.key == pygame.K_DOWN:
                    cursor = max(0, cursor- 1)
                    difficulty_text = font.render(difficulties[cursor], True, diff_colors[cursor])
                    game_window.fill(black)
                    game_window.blit(start_surface, start_rect)
                    game_window.blit(info_surface, info_rect)
                    game_window.blit(diff_info_text, diff_info_rect)
                    game_window.blit(difficulty_text, difficulty_rect)
                    pygame.display.flip()


# Score
def show_score(choice, color, font, size):
    score_font = pygame.font.Font(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frame_size_x/10, 15)
    else:
        score_rect.midtop = (frame_size_x/2, frame_size_y/1.25)
    game_window.blit(score_surface, score_rect)
    # pygame.display.flip()
    for i in range(lives):
        heart_rect = heart_image.get_rect(midtop=(frame_size_x/1.2 + i * 30, 15))
        game_window.blit(heart_image, heart_rect)

    ####################################################################
    ####################phase2추가######################################
    ####################################################################
# Check if position is not in obstacles
def not_in_obs(pos, obstacles):
    for obstacle in obstacles:
        for i in range(2):
            for j in range(2):
                if pos == [obstacle[0] + i * 20, obstacle[1] + j * 20]:
                    return False
    return True
    ####################################################################
    ####################phase2추가######################################
    ####################################################################


score = 0
lives = 0

# Main logic
def main():
    # Game variables
    global score
    global lives

    score = 0
    lives = 3
    start_screen()
    pygame.display.flip()

    snake_pos = [frame_size_x//2, frame_size_y//2]
    snake_body = [[frame_size_x//2, frame_size_y//2], [frame_size_x//2 - 20, frame_size_y//2], [frame_size_x//2-(2*20), frame_size_y//2]]

    food_pos = [random.randrange(1, (frame_size_x//20)) * 20, random.randrange(1, (frame_size_y//20)) * 20]
    food_spawn = True

    ####################################################################
    ####################phase2추가######################################
    ####################################################################
    obstacle_pos = [[60 + 60, 60 + 60], [frame_size_x-80 - 40, frame_size_y-80 - 40]]  # 장애물 위치
    ####################################################################
    ####################phase2추가######################################
    ####################################################################

    direction = 'RIGHT'
    change_to = direction


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Whenever a key is pressed down
            elif event.type == pygame.KEYDOWN:
                # W -> Up; S -> Down; A -> Left; D -> Right
                if event.key == pygame.K_UP or event.key == ord('w'):
                    change_to = 'UP'
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    change_to = 'RIGHT'
                # Esc -> Create event to quit the game
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

        # Making sure the snake cannot move in the opposite direction instantaneously
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Moving the snake
        if direction == 'UP':
            snake_pos[1] -= 20
        if direction == 'DOWN':
            snake_pos[1] += 20
        if direction == 'LEFT':
            snake_pos[0] -= 20
        if direction == 'RIGHT':
            snake_pos[0] += 20

        # Snake body growing mechanism
        snake_body.insert(0, list(snake_pos))
        if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
            score += 1
            food_spawn = False
        else:
            snake_body.pop()

        # Spawning food on the screen
        
        ####################phase2삭제######################################
        ####################################################################
        #if not food_spawn:
        #    food_pos = [random.randrange(1, (frame_size_x//20)) * 20, random.randrange(1, (frame_size_y//20)) * 20]
        #food_spawn = True
        ####################phase2삭제######################################
        ####################################################################

        ####################################################################
        ####################phase2추가######################################
        ####################################################################
        if not food_spawn:
            food_pos = [random.randrange(1, (frame_size_x//20)) * 20, random.randrange(1, (frame_size_y//20)) * 20]
            while not not_in_obs(food_pos, obstacle_pos):
                food_pos = [random.randrange(1, (frame_size_x//20)) * 20, random.randrange(1, (frame_size_y//20)) * 20]
        food_spawn = True
        ####################################################################
        ####################phase2추가######################################
        ####################################################################

        # GFX

        rotated_head = snake_head_image
        if direction == 'UP':
            rotated_head = pygame.transform.rotate(snake_head_image, 0)
        elif direction == 'DOWN':
            rotated_head = pygame.transform.rotate(snake_head_image, 180)
        elif direction == 'LEFT':
            rotated_head = pygame.transform.rotate(snake_head_image, 90)
        else:  # direction == 'RIGHT'
            rotated_head = pygame.transform.rotate(snake_head_image, 270)
        game_window.fill(black)

        ####################################################################
        ####################phase2추가######################################
        ####################################################################

        # Draw obstacles
        for pos in obstacle_pos:
            for i in range(2):
                for j in range(2):
                    obstacle_rect = redrec_image.get_rect(topleft=(pos[0] + i*20, pos[1] + j*20))
                    game_window.blit(redrec_image, obstacle_rect)


        ####################################################################
        ####################phase2추가######################################
        ####################################################################

        snake_head_rect = rotated_head.get_rect(topleft=(snake_body[0][0], snake_body[0][1]))
        game_window.blit(rotated_head, snake_head_rect)

        for pos in snake_body[1:]:
            # Snake body
            # .draw.rect(play_surface, color, xy-coordinate)
            # xy-coordinate -> .Rect(x, y, size_x, size_y)
            snake_body_rect = snake_body_image.get_rect(topleft=(pos[0],pos[1]))
            game_window.blit(snake_body_image, snake_body_rect)
            #pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 20, 20))

        # Snake food
        apple_rect = apple_image.get_rect(topleft=(food_pos[0], food_pos[1]))
        game_window.blit(apple_image, apple_rect)

        # Game Over conditions
        # Getting out of bounds
        if snake_pos[0] < 0 or snake_pos[0] > frame_size_x-20:
            snake_pos = game_over(snake_body)
        if snake_pos[1] < 0 or snake_pos[1] > frame_size_y-20:
            snake_pos = game_over(snake_body)
        # Touching the snake body
        for block in snake_body[1:]:
            if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                snake_pos = game_over(snake_body)
        
        ####################################################################
        ####################phase2추가######################################
        ####################################################################
        # Touching the obstacles
        for obstacle in obstacle_pos:
            for i in range(2):
                for j in range(2):
                    if snake_pos == [obstacle[0] + i * 20, obstacle[1] + j * 20]:
                        snake_pos = game_over(snake_body)        


        ####################################################################
        ####################phase2추가######################################
        ####################################################################

        show_score(1, white, font_path, 20)
        # Refresh game screen
        pygame.display.update()
        # Refresh rate
        fps_controller.tick(difficulty)

if __name__ == '__main__':
    main()
