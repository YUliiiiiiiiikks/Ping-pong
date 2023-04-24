from pygame import*
display.set_caption('OOOOOOOKKKKKHHHHOO')
window = display.set_mode((800,650))
fon = transform.scale(image.load('Фон.jpeg'),(800,650))
clock = time.Clock()
class GameSprite(sprite.Sprite):
    def __init__(self,picture,x,y,w,h,speed):
        super().__init__()
        self.picture = transform.scale(image.load(picture),(w,h))
        self.rect = self.picture.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        window.blit(self.picture,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 520:
            self.rect.y += self.speed
    def move2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 520:
            self.rect.y += self.speed
platform1 = Player('плфаформа.png',20,300,40,130,10)
platform2 = Player('плфаформа.png',740,300,40,130,10)
ball = GameSprite('Голова шрека.png',400,300,80,80,3)
s_x = 5
s_y = 5
game = True
while game:
    clock.tick(60)
    window.blit(fon,(0,0))
    platform1.move2()
    platform1.reset()
    platform2.move()
    platform2.reset()
    ball.rect.x += s_x
    ball.rect.y += s_y
    if ball.rect.y >= 570:
        s_y *= -1
    if ball.rect.y <= 0:
        s_y *= -1
    if sprite.collide_rect(ball,platform1):
        s_x *= -1
    if sprite.collide_rect(ball,platform2):
        s_x *= -1
    ball.reset()
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()    
