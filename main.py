import pygame, sys

class Player(pygame.sprite.Sprite):
    def __init__(self, width, height, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
    def update(self, pos_x, pos_y):
        self.rect.topleft = (pos_x, pos_y)
    def check(self):
        if level_one:
            collided = pygame.sprite.spritecollide(player, level_one_obstacles, False)
        elif level_two:
            collided = pygame.sprite.spritecollide(player, level_two_obstacles, False)
        elif level_three:
            collided = pygame.sprite.spritecollide(player, level_three_obstacles, False)
        elif level_four:
            collided = pygame.sprite.spritecollide(player, level_four_obstacles, False)
        else:
            collided = None
        if collided:
            return True
        else:
            return False
    def check_checkpoint(self):
        if level_one:
            collided = pygame.sprite.spritecollide(player, level_one_checkpoint_group, False)
        elif level_two:
            collided = pygame.sprite.spritecollide(player, level_two_checkpoint_group, False)
        elif level_three:
            collided = pygame.sprite.spritecollide(player, level_three_checkpoint_group, False)
        elif level_four:
            collided = pygame.sprite.spritecollide(player, level_four_checkpoint_group, False)
        else:
            collided = None
        if collided:
            return True
        else:
            return False
    def check_lock(self):
        if lock_active:
            if level_four:
                collided = pygame.sprite.spritecollide(player, level_four_lock_group, False)
            else:
                collided = None
        else:
            collided = None
        if collided:
            return True
        else:
            return False
    def check_key(self):
        if level_four:
            collided = pygame.sprite.spritecollide(player, level_four_key_group, False)
        else:
            collided = None
        if collided:
            return True
        else:
            return False
        
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft = (pos_x, pos_y))

pygame.init()
clock = pygame.time.Clock()
run = True

#Screen
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(\
'The Moving Block                                                                                                                 By: STG996')

#Game Variables
x = 0
y = 530
width = 70
height = width
YELLOW = (254, 235, 1)
SCREEN_BG = (0, 255, 255)
level_one = True
level_two = False
level_three = False
level_four = False
end_screen = False

#Player
player = Player(width, height, YELLOW)
player_group = pygame.sprite.Group()
player_group.add(player)

#========== W H E R E   A L L  L E V E L  D E S I G N   T A K E S  P L A C E =========== 

#Obstacles
level_one_obstacles = pygame.sprite.Group()
level_two_obstacles = pygame.sprite.Group()
level_three_obstacles = pygame.sprite.Group()
level_four_obstacles = pygame.sprite.Group()

level_one_obstacle_one = Obstacle(500, 125, 0, 0, (255, 0, 0))
level_one_obstacles.add(level_one_obstacle_one)
level_one_obstacle_two = Obstacle(400, 300, 300, 300, (255, 0, 0))
level_one_obstacles.add(level_one_obstacle_two)

level_two_obstacle_one = Obstacle(70, 200, 300, 400, (255, 0, 0))
level_two_obstacles.add(level_two_obstacle_one)
level_two_obstacle_two = Obstacle(100, 300, 0, 0, (255, 0, 0))
level_two_obstacles.add(level_two_obstacle_two)
level_two_obstacle_three = Obstacle(100, 200, 100, 0, (255, 0, 0))
level_two_obstacles.add(level_two_obstacle_three)
level_two_obstacle_four = Obstacle(500, 100, 200, 0, (255, 0, 0))
level_two_obstacles.add(level_two_obstacle_four)

level_three_obstacle_one = Obstacle(600, 200, 0, 0, (255, 0, 0))
level_three_obstacles.add(level_three_obstacle_one)
level_three_obstacle_two = Obstacle(175, 100, 150, 500, (255, 0, 0))
level_three_obstacles.add(level_three_obstacle_two)
level_three_obstacle_three = Obstacle(100, 200, 500, 200, (255, 0, 0))
level_three_obstacles.add(level_three_obstacle_three)

level_four_obstacle_one = Obstacle(150, 100, 0, 100, (255, 0, 0))
level_four_obstacles.add(level_four_obstacle_one)
level_four_obstacle_two = Obstacle(200, 150, 200, 500, (255, 0, 0))
level_four_obstacles.add(level_four_obstacle_two)
level_four_obstacle_three = Obstacle(75, 250, 400, 0, (255, 0, 0))
level_four_obstacles.add(level_four_obstacle_three)

#Checkpoints
level_one_checkpoint_group = pygame.sprite.Group()
level_two_checkpoint_group = pygame.sprite.Group()
level_three_checkpoint_group = pygame.sprite.Group()
level_four_checkpoint_group = pygame.sprite.Group()

level_one_checkpoint = Obstacle(200, 100, 500, 0, (0, 255, 0))
level_one_checkpoint_group.add(level_one_checkpoint)

level_two_checkpoint = Obstacle(200, 100, 500, 500, (0, 255, 0))
level_two_checkpoint_group.add(level_two_checkpoint)

level_three_checkpoint = Obstacle(100, 150, 600, 0, (0, 255, 0))
level_three_checkpoint_group.add(level_three_checkpoint)

level_four_checkpoint = Obstacle(225, 75, 475, 0, (0, 255, 0))
level_four_checkpoint_group.add(level_four_checkpoint)

#Keys
lock_active = True
level_four_key_group = pygame.sprite.Group()

level_four_key = Obstacle(30, 30, 50, 30, (255, 0, 255))
level_four_key_group.add(level_four_key)

#===========================================================

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y -= 3
    if keys[pygame.K_a]:
        x -= 3
    if keys[pygame.K_s]:
        y += 3
    if keys[pygame.K_d]:
        x += 3

    if x < 0 or x + width > SCREEN_WIDTH or y < 0 or y + height > SCREEN_HEIGHT:
        x, y = 0, 530
    #Locks
    if lock_active:
        level_four_lock_group = pygame.sprite.Group()
        level_four_lock = Obstacle(250, 100, 450, 150, (0, 0, 255))
        level_four_lock_group.add(level_four_lock)

    if not end_screen:
        screen.fill(SCREEN_BG)
        player_group.draw(screen)
        player.update(x, y)
    else:
        screen.fill((255, 160, 0))
        font = pygame.font.SysFont('Courier', 40, bold = True)
        font.set_underline(True)
        end_text = font.render('YOU\'VE FINISHED THE GAME!', False, (0, 0, 0))
        end_text_rect = end_text.get_rect(center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(end_text, end_text_rect)
    
    if level_one:
        level_one_obstacles.draw(screen)
        level_one_checkpoint_group.draw(screen) 
    elif level_two:
        level_two_obstacles.draw(screen)
        level_two_checkpoint_group.draw(screen)
    elif level_three:
        level_three_obstacles.draw(screen)
        level_three_checkpoint_group.draw(screen)
    elif level_four:
        if lock_active:
            level_four_lock_group.draw(screen)
            level_four_key_group.draw(screen)
        level_four_obstacles.draw(screen)
        level_four_checkpoint_group.draw(screen)
               
    check = player.check()
    check_checkpoint = player.check_checkpoint()
    check_lock = player.check_lock()
    check_key = player.check_key()
    if check == True:
        x, y = 0, 530
    if check_checkpoint == True:
        if level_one:
            level_one = False
            level_two = True
            x, y = 0, 530
        elif level_two:
            level_two = False
            level_three = True #Change this when more levels added (this is note to self)
            x, y = 0, 530
        elif level_three:
            level_three = False
            level_four = True
            x, y = 0, 530
        elif level_four:
            level_four = False
            end_screen = True #Note to self: add "lock_active = True" here when level 5 is made.
    if check_lock == True:
        x, y = 0, 530
    if check_key == True:
        lock_active = False
            
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
