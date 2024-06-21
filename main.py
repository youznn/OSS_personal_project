import pygame, sys, time, random

pygame.init()

apple_image = pygame.image.load('./assets/apple.png')
apple_image = pygame.transform.scale(apple_image, (20, 20))
heart_image = pygame.image.load('./assets/heart.png')
heart_image = pygame.transform.scale(heart_image, (20, 20))
snake_head_image = pygame.image.load('./assets/snake_head.png')
snake_head_image = pygame.transform.scale(snake_head_image, (20,20))
snake_body_image = pygame.image.load('./assets/snake_body.png')
snake_body_image = pygame.transform.scale(snake_body_image, (20,20))
bomb_image = pygame.image.load('./assets/bomb.png')
bomb_image = pygame.transform.scale(bomb_image, (20, 20))

eat_sound = pygame.mixer.Sound('./assets/eat.wav')
hit_sound = pygame.mixer.Sound('./assets/hit.wav')

font_path = 'Retro Gaming.ttf'

difficulty = 25

frame_size_x = 720
frame_size_y = 480

check_errors = pygame.init()
if check_errors[1] > 0:
    print(f'[!] Had {check_errors[1]} errors when initialising game, exiting...')
    sys.exit(-1)
else:
    print('[+] Game successfully initialised')

pygame.display.set_caption('Snake Eater')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
yellow = pygame.Color(255, 255, 0)
orange = pygame.Color(255, 165, 0)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

fps_controller = pygame.time.Clock()

scoreboard = []

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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

def game_over(snake_body):
    global lives, scoreboard, score
    lives -= 1

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

    else:
        snake_pos = [frame_size_x//2, frame_size_y//2]
        blink_snake(snake_body)
        return snake_pos

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



def start_screen():
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

score = 0
lives = 0

def main():
   
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

    bomb_pos = [random.randrange(1, (frame_size_x//20)) * 20, random.randrange(1, (frame_size_y//20)) * 20]
    bomb_spawn = True

    direction = 'RIGHT'
    change_to = direction

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == ord('w'):
                    change_to = 'UP'
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    change_to = 'RIGHT'
                
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        if direction == 'UP':
            snake_pos[1] -= 20
        if direction == 'DOWN':
            snake_pos[1] += 20
        if direction == 'LEFT':
            snake_pos[0] -= 20
        if direction == 'RIGHT':
            snake_pos[0] += 20

        snake_body.insert(0, list(snake_pos))
        if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
            score += 1
            food_spawn = False
            eat_sound.play()
        else:
            snake_body.pop()

        if snake_pos[0] == bomb_pos[0] and snake_pos[1] == bomb_pos[1]:
            bomb_spawn = False
            hit_sound.play()
            snake_pos = game_over(snake_body)

        if not food_spawn:
            food_pos = [random.randrange(1, (frame_size_x//20)) * 20, random.randrange(1, (frame_size_y//20)) * 20]
        food_spawn = True

        if not bomb_spawn:
            bomb_pos = [random.randrange(1, (frame_size_x//20)) * 20, random.randrange(1, (frame_size_y//20)) * 20]
        bomb_spawn = True

        rotated_head = snake_head_image
        if direction == 'UP':
            rotated_head = pygame.transform.rotate(snake_head_image, 0)
        elif direction == 'DOWN':
            rotated_head = pygame.transform.rotate(snake_head_image, 180)
        elif direction == 'LEFT':
            rotated_head = pygame.transform.rotate(snake_head_image, 90)
        else:
            rotated_head = pygame.transform.rotate(snake_head_image, 270)
        game_window.fill(black)

        snake_head_rect = rotated_head.get_rect(topleft=(snake_body[0][0], snake_body[0][1]))
        game_window.blit(rotated_head, snake_head_rect)

        for pos in snake_body[1:]:
            snake_body_rect = snake_body_image.get_rect(topleft=(pos[0],pos[1]))
            game_window.blit(snake_body_image, snake_body_rect)

        apple_rect = apple_image.get_rect(topleft=(food_pos[0], food_pos[1]))
        game_window.blit(bomb_image, (bomb_pos[0], bomb_pos[1]))

        game_window.blit(apple_image, apple_rect)

        if snake_pos[0] < 0 or snake_pos[0] > frame_size_x-20:
            snake_pos = game_over(snake_body)
        if snake_pos[1] < 0 or snake_pos[1] > frame_size_y-20:
            snake_pos = game_over(snake_body)
        for block in snake_body[1:]:
            if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                snake_pos = game_over(snake_body)

        show_score(1, white, font_path, 20)
        pygame.display.update()
        fps_controller.tick(difficulty)

if __name__ == "__main__":
    main()
