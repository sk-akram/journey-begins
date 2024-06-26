#Importing Pygame
import pygame
import random


#Initializing
pygame.init()

#Creating Screen, Title, Icon
scr = pygame.display.set_mode((800,650))
pygame.display.set_caption("Journey Begins")
icon = pygame.image.load("img\icon1.png")
pygame.display.set_icon(icon)

#Loading Music
bulletSound = pygame.mixer.Sound('shoot_sound.wav')
game_over_sound = pygame.mixer.Sound('game_over.mp3')

music = pygame.mixer.music.load('ground_music.wav')
pygame.mixer.music.play(-1)

#Create wall
def wallpaper():
    bg = pygame.image.load("img\wall1.png")
    scr.blit(bg,(0,0))
#Some initial Variable
wall_x = 0
hudle_x = 0
walk_count = 0
hudle_count = 0
tree_count = 0
zombie_count = 0

#Reading last High score
with open("data.txt",mode="r") as data:
    high_score_value = int(data.read())
score_value = 0
score_text = pygame.font.Font("freesansbold.ttf",32)

high_score_text = pygame.font.Font("freesansbold.ttf",32)

#Display Score
def display_score():
    global high_score_value
    score = score_text.render(f"Score: {score_value}",True,(255,255,255))
    scr.blit(score,(10,50))
    if score_value >= high_score_value:
        high_score_value = score_value
        with open("data.txt",mode= "w") as data:
            data.write(str(score_value))
    high_score = high_score_text.render(f"High Score: {high_score_value}",True,(255,255,255))
    scr.blit(high_score,(10,85))

#Setting The platform
def platform():
    global wall_x
    rock1 = pygame.image.load("img\ock3.png")
    rock2 = pygame.image.load("img\ock.png")
    if wall_x == 400 or wall_x == -400:
        wall_x = 0
    scr.blit(rock1,(-400-wall_x,571))
    scr.blit(rock1,(0-wall_x,571))
    scr.blit(rock1,(400-wall_x,571))
    scr.blit(rock1,(800-wall_x,571))
clock = pygame.time.Clock()

#Creating The Player
hero_y = 490
hero_x = 250
dead = False
def player():
    global walk,hero_y,dead,score_value
    runRight = [pygame.image.load('img\ight1.png'), pygame.image.load('img\ight2.png'), pygame.image.load('img\ight3.png'), pygame.image.load('img\ight4.png'), pygame.image.load('img\ight5.png'), pygame.image.load('img\ight6.png')]
    runLeft = [pygame.image.load('img\left1.png'), pygame.image.load('img\left2.png'), pygame.image.load('img\left3.png'), pygame.image.load('img\left4.png'), pygame.image.load('img\left5.png'), pygame.image.load('img\left6.png')]
    jump = [pygame.image.load('img\jump_up_left.png'),pygame.image.load('img\jump_up_right.png'),pygame.image.load('img\jump_down_left.png'),pygame.image.load('img\jump_down_right.png')]
    soul = pygame.image.load('img\soul.png')
    
    if walk+1 >= 30:
        walk = 0
    for i in zombie:
        if ((i.x-hudle_x)-hero_x)**2 <= 800**2:
            for bullet in bullets:
                if (bullet.x+total_x - i.x)**2 <= 20**2:
                    zombie.pop(zombie.index(i))
                    bullets.pop(bullets.index(bullet))
                    score_value += 10
        if((i.x-hudle_x)- hero_x)**2 <= 50**2:
            dead = True
            display_message()
        

    if (wolf_x - hero_x)**2 <= 130**2 or dead == True:
        attack = pygame.image.load("img\wolf_right6.png")
        scr.blit(soul,(hero_x,470))
        display_message()
    

    
    elif jumping:
        if left:
            scr.blit(jump[0],(hero_x,hero_y))
        elif right:
            scr.blit(jump[1],(hero_x,hero_y))
    elif left:
        scr.blit(runLeft[walk//5],(hero_x,hero_y))
        walk += 1
    elif right:
        scr.blit(runRight[walk//5],(hero_x,hero_y))
        walk += 1
#Bullet
class Shot(object):
    def __init__(self,bullet_x,bullet_y,type,direction):
        self.x = bullet_x
        self.y = bullet_y
        self.type = type
        self.direction = direction
        self.vel = 8 * direction

    def draw(self,scr):
        balls = [pygame.image.load("img\llet_right.png"),pygame.image.load("img\llet.png")]
        scr.blit(balls[self.type],(self.x,self.y))
        

#Hudles
class Hudle(object):
    tree = pygame.image.load("img\ee1.png")
    rock = pygame.image.load("img\ock.png")
    hudle = [tree,rock]

    def __init__(self,x,y,type):
        self.x = x
        self.y = y
        self.type = self.hudle[type]
    def draw(self,scr):
        scr.blit(self.type,(self.x-hudle_x,self.y))

#Zombies
class Zom(object):
    zombie1_left = [pygame.image.load('img\zombie1a_left.png'), pygame.image.load('img\zombie1b_left.png'), pygame.image.load('img\zombie1c_left.png'), pygame.image.load('img\zombie1d_left.png')]
    zombie1_right = [pygame.image.load('img\zombie1a.png'), pygame.image.load('img\zombie1b.png'), pygame.image.load('img\zombie1c.png'), pygame.image.load('img\zombie1d.png')]
    zombie2_left = [pygame.image.load('img\zombie2a_left.png'), pygame.image.load('img\zombie2b_left.png'), pygame.image.load('img\zombie2c_left.png'), pygame.image.load('img\zombie2d_left.png')]
    zombie2_right = [pygame.image.load('img\zombie2a.png'), pygame.image.load('img\zombie2b.png'), pygame.image.load('img\zombie2c.png'), pygame.image.load('img\zombie2d.png')]
    zombie3_left = [pygame.image.load('img\zombie3a_left.png'), pygame.image.load('img\zombie3b_left.png'), pygame.image.load('img\zombie3c_left.png'), pygame.image.load('img\zombie3d_left.png')]
    zombie3_right = [pygame.image.load('img\zombie3a.png'), pygame.image.load('img\zombie3b.png'), pygame.image.load('img\zombie3c.png'), pygame.image.load('img\zombie3d.png')]
    zombie4_left = [pygame.image.load('img\zombie4a_left.png'), pygame.image.load('img\zombie4b_left.png'), pygame.image.load('img\zombie4c_left.png'), pygame.image.load('img\zombie4d_left.png')]
    zombie4_right = [pygame.image.load('img\zombie4a.png'), pygame.image.load('img\zombie4b.png'), pygame.image.load('img\zombie4c.png'), pygame.image.load('img\zombie4d.png')]
    zomb_type = [zombie1_right,zombie1_left,zombie2_right,zombie2_left,zombie3_right,zombie3_left,zombie4_right,zombie4_left]

    
    def __init__(self,zombie_x,zombie_y,end,type,speed):
        self.x = zombie_x
        self.y = zombie_y
        self.end = end
        self.type = type
        self.path = [self.x,self.end]
        self.walk_count = 0
        self.dir = speed
    
    def draw(self,scr):
        self.move()
        if self.walk_count +1 >= 20:
            self.walk_count = 0
        if self.dir >0:
            scr.blit(self.zomb_type[self.type][self.walk_count//5],(self.x-hudle_x,self.y))
            self.walk_count += 1
        else:
            scr.blit(self.zomb_type[self.type+1][self.walk_count//5],(self.x-hudle_x,self.y))
            self.walk_count += 1
            

    def move(self):
        if self.dir > 0:
            if self.x < self.path[1] + self.dir:
                self.x += self.dir
            else:
                self.dir *= -1
                self.x += self.dir
                self.walk_count = 0
        else:
            if self.x > self.path[0] - self.dir:
                self.x += self.dir
            else:
                self.dir  *=  -1
                self.x += self.dir
                self.walk_count = 0

#Wolfs
wolf_x = 10
def wolf():
    global walk,wolf_x,standing
    wolf_left = [pygame.image.load('img\wolf_left1.png'), pygame.image.load('img\wolf_left2.png'), pygame.image.load('img\wolf_left3.png'), pygame.image.load('img\wolf_left4.png'),pygame.image.load('img\wolf_left5.png'), pygame.image.load('img\wolf_left6.png')]
    wolf_right = [pygame.image.load('img\wolf_right1.png'), pygame.image.load('img\wolf_right2.png'), pygame.image.load('img\wolf_right3.png'), pygame.image.load('img\wolf_right4.png'),pygame.image.load('img\wolf_right5.png'), pygame.image.load('img\wolf_right6.png')]
    wolf_up_down = [pygame.image.load('img\wolf_up_l.png'),pygame.image.load('img\wolf_up_r.png'),pygame.image.load('img\wolf_down_l.png'),pygame.image.load('img\wolf_down_r.png')]
    

    if standing:
        wolf_x += 0.1
    
    if (wolf_x - hero_x)**2 <= 130**2:
        attack = pygame.image.load("img\wolf_right6.png")
        scr.blit(attack,(wolf_x,470))
        
    
    elif jumping:
        if left:
            scr.blit(wolf_up_down[0],(wolf_x,470))
        elif right:
            scr.blit(wolf_up_down[1],(wolf_x,470))

    elif left:
        scr.blit(wolf_up_down[1],(wolf_x,470))
        wolf_x += 2
        
    elif right:
        scr.blit(wolf_right[walk//5],(wolf_x,470))
#Display Gameover Massege
def display_message():
    global score_value
    font = pygame.font.SysFont("freesansbold.ttf", 64, True)
    text = font.render("Game Over!", True, (255, 255, 255))
    scr.blit(text, (360,300))
    game_over_sound.play()
    score_value = 0
        
        
        

        
        



#Boolean Condition
switch = True
left = False
right = False
jumping = False
walk = -1
jump_count = 10
shoot_x = 0
bullets = []
firing = False
rock_index = []
for i in range(5,155):
    if i % 3 == 0:
        rock_index.append(100*i)
rock = []
tree = []
zombie = []
zom_type = [0,2,4,6]
speed = [1.5,2,1]
z = 0

for i in rock_index:
    r_ = random.choice(rock_index)
    t_ = random.choice(rock_index)
    if (r_- z)**2 <= 400**2:
        r_ += 500

    rock.append(Hudle(r_,520,1))
    tree.append(Hudle(t_,530,0))
    c = random.choice(rock_index)
    z_type = random.choice(zom_type)
    if z_type == 6:
        zombie.append(Zom(c,500,c+180,z_type,0.5))
    elif z_type == 4:
        zombie.append(Zom(c,480,c+180,z_type,random.choice(speed)))
    else:
        zombie.append(Zom(c,470,c+180,z_type,random.choice(speed)))
    z = r_

standing = False
h = 0
total_x = 0
a = 0

#Mainloop
while switch:
    clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            switch = False
    
    for bullet in bullets:
        if bullet.x < 900 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        bulletSound.play()
        
        if a >= 3:
            firing = True
            a += 1
        if left:
            direction = -1
            h += 1
            type = 1
            d = 200
    
        else:
            direction = 1
            h += 1
            type = 0
            d = 0

            
        if len(bullets) <6+h:
            bullets.append(Shot(round(hero_x + 60 -d // 2),round(hero_y+ 80//2),type,direction))
            h = 0

    if keys[pygame.K_RIGHT]:
        wall_x += 5
        hudle_x += 5
        right = True
        left = False
        walk += 1
        total_x += 5


    elif keys[pygame.K_LEFT]:
        wall_x -= 5
        hudle_x -= 5
        left = True
        right = False
        walk += 1
        total_x -= 5

    else:
        walk = 0
    if not jumping:

        if keys[pygame.K_SPACE]:
            jumping = True
    else:
        if jump_count >= -10:
            dir = 1
            if jump_count < 0:
                dir = -1
            hero_y -= jump_count **2*0.5*dir
            jump_count -= 1
        else:
            jumping = False
            jump_count = 10
    if not (right or left or jumping):
        standing = True


    wallpaper()
    
    platform()
    for t in tree:
        t.draw(scr)
    player()
    wolf()
    for r in rock:
        r.draw(scr)
    for z in zombie:
        z.draw(scr)
    for bullet in bullets:
        bullet.draw(scr)
    display_score()

    pygame.display.update()
