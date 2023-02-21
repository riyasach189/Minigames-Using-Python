def daredive():
    import button
    import pygame
    import os
    import random
    pygame.font.init()
    pygame.mixer.init()
    from time import time

    SCORE_FONT = pygame.font.SysFont('arcadeclassic', 40)
    GAME_END  = pygame.font.SysFont('arcadeclassic', 100)
    HEALTH_FONT = pygame.font.SysFont('arcadeclassic', 40)
    MAN_WIDTH, MAN_HEIGHT = 150, 90
    ROCK_WIDTH, ROCK_HEIGHT = 100,60
    WIDTH, HEIGHT = 1000,500
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("HydroHopper")
    CRASH_SOUND = pygame.mixer.Sound(os.path.join('Assets_Daredive', 'crash.wav'))
    start_img = pygame.transform.scale(pygame.image.load("Start.png").convert_alpha(), (300,150))
    exit_img = pygame.transform.scale(pygame.image.load("Quit.png").convert_alpha(), (300,150))
            
    start_button = button.Button(170, 180, start_img, 0.7)
    exit_button = button.Button(620, 180, exit_img,0.7)

    FREQUENCY = 0.4
    MAN_HIT = pygame.USEREVENT
    FPS = 60
    MAN = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Daredive','man.png')),(MAN_WIDTH, MAN_HEIGHT))

    def draw_win(bg, man, obstacles, man_health, score, highscore):
        WIN.blit(bg, (0,0))
        WIN.blit(MAN, (man.x, man.y))
        health_text = HEALTH_FONT.render(f"Lives remaining: {man_health}", 1, (0,0,0))
        WIN.blit(health_text, (10,10))
        score_text = SCORE_FONT.render(f"Score: {int(score)}",1 ,(0,0,0))
        WIN.blit(score_text, (WIDTH-score_text.get_width()-10,10))
        highscore_text = SCORE_FONT.render(f"Highscore: {int(highscore)}",1 ,(0,0,0))
        WIN.blit(highscore_text, (WIDTH-highscore_text.get_width()-10,10+score_text.get_height()))
        SHARK = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Daredive','shark.png')),(ROCK_WIDTH, ROCK_HEIGHT))
        for obstacle in obstacles:
            WIN.blit(SHARK, (obstacle.x, obstacle.y))
            
        pygame.display.update()
        

    def draw_end(text):
        draw_text = GAME_END.render(text,1,(0,0,0))
        WIN.blit(draw_text,(WIDTH//2-draw_text.get_width()//2,HEIGHT//2-draw_text.get_height()//2))
        pygame.display.update()
        pygame.time.delay(1000)
        
    def movement(keys_pressed, man, VEL):
        if keys_pressed[pygame.K_UP] and man.y > 15:
            man.y -= VEL
        if keys_pressed[pygame.K_DOWN] and man.y +VEL + man.height < HEIGHT - 15:
            man.y += VEL

    def handle_obstacles(obstacles, man, OBSTACLE_VEL):
        for obstacle in obstacles:
            obstacle.x -= OBSTACLE_VEL
            if man.colliderect(obstacle):
                obstacles.remove(obstacle)
                pygame.event.post(pygame.event.Event(MAN_HIT))
            elif obstacle.x < 0:
                obstacles.remove(obstacle)
            
    def checker():
        runner = True
        while runner:
            WIN.fill((202, 228, 241))
            if start_button.draw(WIN):
                main()
                runner = False
                break
            if exit_button.draw(WIN):
                pygame.quit()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    runner = False
    def check_test():
        runner = True
        while runner:
            WIN.fill((202, 228, 241))
            if start_button.draw(WIN):
                main()
                runner = False
                break
            if exit_button.draw(WIN):
                pygame.quit()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    runner = False
    def main():
        OBSTACLE_VEL = 10
        VEL = 5
        score = 0
        obstacles = []
        clock = pygame.time.Clock()
        run = True
        obstacle_count = 0
        old_obstacle_count = 0
        man_health = 3
        man = pygame.Rect(100, 300, MAN_WIDTH, MAN_HEIGHT)
        with open("highscore.txt", "r") as file:
            recs = file.readlines()
        recs = [int(x) for x in recs]
        recs.append(0)
        highscore = max(recs)
        start = time()
        while run:
            now = time()
            if int(now-start) % 2 == 0 and int(now-start) != 0:
                OBSTACLE_VEL += 0.01
                VEL += 0.01
            bg = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Daredive','ocean.jpg')),(WIDTH,HEIGHT))
            obstacle_count += FREQUENCY/10
            score += 0.1
            draw_win(bg, man, obstacles, man_health, score, highscore)
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

                if event.type == MAN_HIT:
                    man_health -= 1
                    CRASH_SOUND.play()

            if int(obstacle_count) > old_obstacle_count:
                obstacle = pygame.Rect(WIDTH, random.randint(0,HEIGHT), ROCK_WIDTH, ROCK_HEIGHT)
                obstacles.append(obstacle)
                old_obstacle_count = obstacle_count
            game_end_text = ""    
            if man_health <= 0:
                game_end_text = f"Score: {int(score)}"
            if game_end_text != "":
                draw_end(game_end_text)
                break
            handle_obstacles(obstacles, man, OBSTACLE_VEL)
            keys_pressed = pygame.key.get_pressed()
            movement(keys_pressed, man, VEL)
        with open("highscore.txt","a") as file:
            file.write(str(int(score))+"\n")
    while True:
        checker()
        check_test()
