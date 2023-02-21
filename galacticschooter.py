def galacticshooter():
    import pygame
    import os

    #to initialize pygame font library
    pygame.font.init()

    #to initialize sound library 
    pygame.mixer.init()

    #screen is called surface in pygame

    #to set height and width of screen
    WIDTH, HEIGHT = 1000,500
    WIN = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Galactic Shooter")

    WHITE = (255,255,255)
    BLACK = (0,0,0)
    RED = (255,0,0)
    YELLOW = (255,255,0)

    BULLETS_FONT = pygame.font.SysFont("comicsans",40)

    BULLET_HIT_SOUND = pygame.mixer.Sound("Assets/Grenade+1.mp3")
    BULLET_FIRE_SOUND = pygame.mixer.Sound("Assets/Gun+Silencer.mp3")

    FPS = 60
    VEL = 5
    BULLET_VEL = 7
    MAX_BULLETS = 3
    SHOOTER_WIDTH, SHOOTER_HEIGHT = 55,40
    BRICK_WIDTH, BRICK_HEIGHT = 30,70

    BRICK_HIT = pygame.USEREVENT + 1

    SHOOTER_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_yellow.png"))
    SHOOTER = pygame.transform.rotate(pygame.transform.scale(SHOOTER_IMAGE, (SHOOTER_WIDTH, SHOOTER_HEIGHT)), 90)

    SPACE = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "space.png")),(WIDTH,HEIGHT))

    def draw_window(shooter_rect,bricks,bullets_left,active_bullets):
        #order in which things are drawn matters

        WIN.blit(SPACE,(0,0))

        #creating text objects
        bullets_left = BULLETS_FONT.render("Bullets Left: "+str(bullets_left),1, WHITE)

        WIN.blit(bullets_left,(WIDTH-bullets_left.get_width() - 10,10))

        #to draw a surface on the screen
        #images are called surfaces
        WIN.blit(SHOOTER, (shooter_rect.x,shooter_rect.y))

        for bullet in active_bullets:
            pygame.draw.rect(WIN,RED,bullet)

        for brick in bricks:
            pygame.draw.rect(WIN, YELLOW, brick)

        pygame.display.update()


    def shooter_movement(keys_pressed,shooter_rect):    

        if keys_pressed[pygame.K_UP] and shooter_rect.y - VEL > 0:   #up
            shooter_rect.y -= VEL

        if keys_pressed[pygame.K_DOWN] and shooter_rect.y + VEL + shooter_rect.width < HEIGHT-15:   #down
            shooter_rect.y += VEL

    def handle_bullets(current_bullets, bricks):
        for bullet in current_bullets:
            bullet.x += BULLET_VEL

            for brick in bricks:

            #only works if both objects are rectangles
                if brick.colliderect(bullet):

                    #broadcast an event
                    pygame.event.post(pygame.event.Event(BRICK_HIT))
                    bricks.remove(brick)

            if bullet.x>WIDTH:
                current_bullets.remove(bullet)

    #float division may give errors
    def draw_winner(text):
        draw_text = BULLETS_FONT.render(text,1,WHITE)

        WIN.blit(draw_text,((WIDTH//2) - draw_text.get_width()//2,HEIGHT//2 - draw_text.get_height()//2))
        pygame.display.update()

        #game pauses when someone wins, displays winner, then resumes
        pygame.time.delay(5000)

    #main game loop; updating scores, checking for collisions, etc.
    def galacticshooter():

        #pygame.Rect(x,y,width,height)
        shooter_rect = pygame.Rect(50,HEIGHT//2,SHOOTER_WIDTH,SHOOTER_HEIGHT)

        bullets_left = 3
        current_bullets = []
        bricks_left = 4
        brick1 = pygame.Rect(700, 100, BRICK_WIDTH,BRICK_HEIGHT)
        brick2 = pygame.Rect(900, 100, BRICK_WIDTH,BRICK_HEIGHT)
        brick3 = pygame.Rect(700, 400, BRICK_WIDTH,BRICK_HEIGHT)
        brick4 = pygame.Rect(900, 400, BRICK_WIDTH,BRICK_HEIGHT)
        bricks = [brick1,brick2,brick3,brick4]

        clock = pygame.time.Clock()

        run = True
        while(run):

            clock.tick(FPS)

            #getting a list of all the different events; looping through them
            #when we post events, they get added to pygame.event.get() queue
            for event in pygame.event.get():

                if event.type==pygame.QUIT:
                    run = False
                    pygame.quit()

                if event.type==pygame.KEYDOWN and bullets_left>=0:
                    if event.key==pygame.K_SPACE and len(current_bullets)==0:
                        bullet = pygame.Rect(shooter_rect.x + shooter_rect.width, shooter_rect.y + shooter_rect.height//2 - 2, 10, 5)
                        bullets_left -= 1
                        current_bullets.append(bullet)
                        BULLET_FIRE_SOUND.play()

                if event.type==BRICK_HIT:
                    BULLET_HIT_SOUND.play()


            winner_text = ""
            if bullets_left<=-1 and len(bricks)>0:
                winner_text = "You Lose!"

            if bullets_left>=0 and len(bricks)<=0:
                winner_text = "You Win!"

            if winner_text!="":
                draw_winner(winner_text)
                break

            #allows multiple keys to be pressed at the same time
            #tells which keys are currently pressed down
            #if key stays pressed down, it will still register that it is being pressed down

            keys_pressed = pygame.key.get_pressed()
            shooter_movement(keys_pressed,shooter_rect)

            handle_bullets(current_bullets, bricks)

            WIN.fill(WHITE)

            draw_window(shooter_rect,bricks,bullets_left,current_bullets)

            pygame.display.update()

        galacticshooter()
    galacticshooter()