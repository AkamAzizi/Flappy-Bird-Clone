import pygame
import random

pygame.init()

pygame.mixer.init()



WIDTH, HEIGHT = 500, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))

bird_image = pygame.image.load('bird.png')
background_image = pygame.image.load('background.png')
pipe_image = pygame.image.load('pipes.png')  # Ensure this has a transparent background


bird_image = pygame.transform.scale(bird_image, (40, 50))  
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
pipe_image = pygame.transform.scale(pipe_image, (80, 500))


font = pygame.font.Font(None, 36)


def reset_game():
    global bird_y, bird_velocity, score, pipes, game_over
    bird_y = HEIGHT // 2
    bird_velocity = 0
    score = 0
    pipes.clear()

    for i in range(3):
        pipe_height = random.randint(200, 600)
        pipes.append({'x': WIDTH + i * 300, 'height': pipe_height})
    game_over = False


pipes = []
reset_game()

gravity = 1.3 
running = True
game_over = False

while True:
    pygame.time.delay(30) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_over:
                    reset_game() 
                else:
                    bird_velocity = -10  

    if not game_over:

        bird_velocity += gravity
        bird_y += bird_velocity


        for pipe in pipes:
            pipe['x'] -= 5 


        if pipes[-1]['x'] < WIDTH - 300:
            pipe_height = random.randint(200, 600)
            pipes.append({'x': WIDTH, 'height': pipe_height})


        if pipes[0]['x'] < -80:
            pipes.pop(0)
            score += 1 

        for pipe in pipes:
            if (100 + 50 > pipe['x'] and 100 < pipe['x'] + 80):
                if (bird_y < pipe['height'] or bird_y + 50 > pipe['height'] + 200):
                    game_over = True 

        if bird_y > HEIGHT:
            game_over = True  


    screen.blit(background_image, (0, 0))
    screen.blit(bird_image, (100, bird_y))


    for pipe in pipes:

        screen.blit(pipe_image, (pipe['x'], pipe['height'] - pipe_image.get_height())) 
        
        screen.blit(pipe_image, (pipe['x'], pipe['height'] + 200))  


    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    if game_over:

        final_score_text = font.render(f'Game Over! Your score: {score}', True, (255, 255, 255))
        screen.blit(final_score_text, (WIDTH // 2 - 150, HEIGHT // 2))
        restart_text = font.render('Press SPACE to Restart', True, (255, 255, 255))
        screen.blit(restart_text, (WIDTH // 2 - 150, HEIGHT // 2 + 40))


    pygame.display.flip()