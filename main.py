"""
Snake Eater
Made with PyGame
"""

import pygame, sys, time, random, math

# Initialize Pygame
pygame.init()

# Load the image
apple_image = pygame.image.load('./assets/apple.png')
apple_image = pygame.transform.scale(apple_image, (20, 20))
heart_image = pygame.image.load('./assets/heart.png')
heart_image = pygame.transform.scale(heart_image, (20, 20))
piret_image = pygame.image.load('./assets/died.png')
piret_image = pygame.transform.scale(piret_image, (20,20))
snake_head_image = pygame.image.load('./assets/snake_head.png')
snake_head_image = pygame.transform.scale(snake_head_image, (20,20))
snake_body_image = pygame.image.load('./assets/snake_body.png')
snake_body_image = pygame.transform.scale(snake_body_image, (20,20))

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


            #################################################
            ##################### Phase 2 ###################
            #################################################
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

            #################################################
            ##################### Phase 2 ###################
            #################################################
                    
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
        snake_body = [[snake_pos[0], snake_pos[1]], [snake_pos[0] - 20, snake_pos[1]], [snake_pos[0] - 40, snake_pos[1]]]
        return snake_pos, snake_body

            #################################################
            ##################### Phase 2 ###################
            #################################################
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

            #################################################
            ##################### Phase 2 ###################
            #################################################
def start_screen():
    # 초기 난이도 = MEDIUM
    global difficulty
    global time_attack_mode
    difficulties = ['EASY', 'MEDIUM', 'HARD', 'IMPOSSIBLE']
    diff_colors = [white, yellow, orange, red]
    cursor = 1
    font = pygame.font.Font(font_path, 70)
    game_window.fill(black)
    start_surface = font.render('SNAKE EATER', True, green)
    start_rect = start_surface.get_rect()
    start_rect.midtop = (frame_size_x/2, frame_size_y/6)
    game_window.blit(start_surface, start_rect)

    info_font = pygame.font.Font(font_path, 25)
    info_surface = info_font.render('PRESS ENTER TO START', True, white)
    info_rect = info_surface.get_rect()
    info_rect.midtop = (frame_size_x/2, frame_size_y/3)
    game_window.blit(info_surface, info_rect)

    # 난이도 선택
    diff_font = pygame.font.Font(font_path, 20)
    diff_info_text = diff_font.render('CHOOSE DIFFICULTY: UP/DOWN KEYS', True, white)
    mode_info_text = diff_font.render('CHOOSE MODE: LEFT/RIGHT KEYS', True, white)
    diff_info_rect = diff_info_text.get_rect(midtop=(frame_size_x/2.4, frame_size_y/2.35))
    mode_info_rect = mode_info_text.get_rect(midtop=(frame_size_x/2.4, frame_size_y/2))

    difficulty_text = font.render(difficulties[cursor], True, diff_colors[cursor])
    difficulty_rect = difficulty_text.get_rect(midtop=(frame_size_x/4, frame_size_y/1.3))

    # 모드 선택
    mode_font = pygame.font.Font(font_path, 20)
    modes = ['NORMAL MODE', 'TIME ATTACK MODE']
    mode_colors = [green, red]
    mode_cursor = 0
    mode_text = mode_font.render(modes[mode_cursor], True, mode_colors[mode_cursor])
    mode_rect = mode_text.get_rect(midtop=(frame_size_x/1.5, frame_size_y/1.3))

    game_window.blit(diff_info_text, diff_info_rect)
    game_window.blit(mode_info_text, mode_info_rect)
    game_window.blit(difficulty_text, difficulty_rect)
    game_window.blit(mode_text, mode_rect)

    pygame.display.flip()

            #################################################
            ##################### Phase 2 ###################
            #################################################
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    difficulty = [10, 20, 35, 80][cursor]
                    time_attack_mode = mode_cursor == 1
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
                    game_window.blit(mode_info_text, mode_info_rect)
                    game_window.blit(mode_text, mode_rect)
                    pygame.display.flip()
                elif event.key == pygame.K_DOWN:
                    cursor = max(0, cursor- 1)
                    difficulty_text = font.render(difficulties[cursor], True, diff_colors[cursor])
                    game_window.fill(black)
                    game_window.blit(start_surface, start_rect)
                    game_window.blit(info_surface, info_rect)
                    game_window.blit(diff_info_text, diff_info_rect)
                    game_window.blit(difficulty_text, difficulty_rect)
                    game_window.blit(mode_info_text, mode_info_rect)
                    game_window.blit(mode_text, mode_rect)
                    pygame.display.flip()
                elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    mode_cursor = (mode_cursor + 1) % 2
                    mode_text = mode_font.render(modes[mode_cursor], True, mode_colors[mode_cursor])
                    game_window.fill(black)
                    game_window.blit(start_surface, start_rect)
                    game_window.blit(info_surface, info_rect)
                    game_window.blit(diff_info_text, diff_info_rect)
                    game_window.blit(difficulty_text, difficulty_rect)
                    game_window.blit(mode_info_text, mode_info_rect)
                    game_window.blit(mode_text, mode_rect)
                    pygame.display.flip()

            #################################################
            ##################### Phase 2 ###################
            #################################################


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
        heart_rect = heart_image.get_rect(midtop=(500 + i * 30, 15))
        game_window.blit(heart_image, heart_rect)

score = 0
lives = 0
            #################################################
            ##################### Phase 2 ###################
            #################################################
# Main logic
def generate_pirate_pos():
    while True:
        pirate_pos = [random.randrange(1, (frame_size_x // 20)) * 20, random.randrange(1, (frame_size_y // 20)) * 20]
        center_pos = [frame_size_x // 2, frame_size_y // 2]
        distance_from_center = math.sqrt((pirate_pos[0] - center_pos[0])**2 + (pirate_pos[1] - center_pos[1])**2)
        if distance_from_center > 100:
            return pirate_pos
        
def main():
    # Game variables
    global score
    global lives
    global food_direction
    global food_speed
    global pirates
    global difficulty

    score = 0
    lives = 3
    start_screen()
    pygame.display.flip()

    snake_pos = [frame_size_x//2, frame_size_y//2]
    snake_body = [[frame_size_x//2, frame_size_y//2], [frame_size_x//2 - 20, frame_size_y//2], [frame_size_x//2-(2*20), frame_size_y//2]]

    food_pos = [random.randrange(1, (frame_size_x//20)) * 20, random.randrange(1, (frame_size_y//20)) * 20]
    food_spawn = True
    food_direction = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
    food_speed = difficulty

    direction = 'RIGHT'
    change_to = direction

    pirates = []
    ticks = 0  # Added for Time Attack Mode

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
        distance = math.sqrt((snake_pos[0] - food_pos[0])**2 + (snake_pos[1] - food_pos[1])**2)
        if distance < 20.01:
            score += 1
            food_spawn = False
            if difficulty < 20 and score % 3 == 0:
                lives += 1
                pirates.append(generate_pirate_pos())
            elif difficulty < 35 and score % 6 == 0:
                lives += 1
                # pirates.append(generate_pirate_pos())
            elif difficulty < 120 and score % 9 == 0:
                lives += 1
                # pirates.append(generate_pirate_pos())
            elif difficulty >= 80 and score % 10 == 0:
                lives += 1
                # pirates.append(generate_pirate_pos())
            print("diff", difficulty)
            if 20 <= difficulty <= 35 and score % 2 == 0:
                pirates.append(generate_pirate_pos())
            elif difficulty >= 40:
                pirates.append(generate_pirate_pos())
        else:
            snake_body.pop()

        # Spawning food on the screen
        if not food_spawn:
            food_pos = [random.randrange(1, (frame_size_x//20)) * 20, random.randrange(1, (frame_size_y//20)) * 20]
        food_spawn = True

        # Moving the food
        if food_direction == 'UP':
            food_pos[1] -= 20
        if food_direction == 'DOWN':
            food_pos[1] += 20
        if food_direction == 'LEFT':
            food_pos[0] -= 20
        if food_direction == 'RIGHT':
            food_pos[0] += 20

        # Bouncing food off the walls
        if food_pos[0] < 0:
            food_pos[0] = 0
            food_direction = 'RIGHT'
        elif food_pos[0] > frame_size_x - 20:
            food_pos[0] = frame_size_x - 20
            food_direction = 'LEFT'
        elif food_pos[1] < 0:
            food_pos[1] = 0
            food_direction = 'DOWN'
        elif food_pos[1] > frame_size_y - 20:
            food_pos[1] = frame_size_y - 20
            food_direction = 'UP'

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

        snake_head_rect = rotated_head.get_rect(topleft=(snake_body[0][0], snake_body[0][1]))
        game_window.blit(rotated_head, snake_head_rect)

        for pos in snake_body[1:]:
            snake_body_rect = snake_body_image.get_rect(topleft=(pos[0], pos[1]))
            game_window.blit(snake_body_image, snake_body_rect)

        # Snake food
        apple_rect = apple_image.get_rect(topleft=(food_pos[0], food_pos[1]))
        game_window.blit(apple_image, apple_rect)

        # Drawing pirates
        for pirate_pos in pirates:
            pirate_rect = piret_image.get_rect(topleft=(pirate_pos[0], pirate_pos[1]))
            game_window.blit(piret_image, pirate_rect)  # 추가된 부분

        # Game Over conditions
        if snake_pos[0] < 0 or snake_pos[0] > frame_size_x-20:
            snake_pos, snake_body = game_over(snake_body)
        if snake_pos[1] < 0 or snake_pos[1] > frame_size_y-20:
            snake_pos, snake_body = game_over(snake_body)
        for block in snake_body[1:]:
            if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                snake_pos, snake_body = game_over(snake_body)
        # Check collision with pirates
        for pirate_pos in pirates:
            if snake_pos[0] == pirate_pos[0] and snake_pos[1] == pirate_pos[1]:
                snake_pos, snake_body = game_over(snake_body)

        show_score(1, white, font_path, 20)
        # Refresh game screen
        pygame.display.update()
        # Refresh rate
        fps_controller.tick(difficulty)

        # Time Attack Mode speed increase
        if time_attack_mode:
            difficulty += 0.02  # Gradually increase speed
            ticks += 1
            if ticks % 80 == 0:  # Add a pirate every 80 ticks
                pirates.append(generate_pirate_pos())

            #################################################
            ##################### Phase 2 ###################
            #################################################
if __name__ == '__main__':
    main()
