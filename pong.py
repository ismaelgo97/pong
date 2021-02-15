import sys
import pygame

class Pong:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 500))
        pygame.display.set_caption("PONG")
        self.rect1 = pygame.Rect(0, 0, 10, 100)
        self.rect2 = pygame.Rect(0, 0, 10, 100)
        self.rect1.midleft = self.screen.get_rect().midleft
        self.rect1.x += 20
        self.rect2.midright = self.screen.get_rect().midright
        self.rect2.x -= 20
        self.bola = pygame.Rect(0, 0, 10, 10)
        self.bola = self.bola.move(600, 250)
        self.bola_pos = self.bola
        self.r1_mup = self.r1_mdo = self.r2_mup = self.r2_mdo = False
        self.speedx = 1
        self.speedy = 1
        self.time = 0
        self.bola_move = False
        self.p1 = 0
        self.p2 = 0
        self.fp1 = pygame.font.SysFont('freesansbold.ttf', 32).render(str(self.p1), True, (255, 255, 255))
        self.fp2 = pygame.font.SysFont('freesansbold.ttf', 32).render(str(self.p2), True, (255, 255, 255))
        self.cambiada = False
        self.speed = 1

    def ball_move(self):
        if self.time > 10:
            self.time = 0
        self.time += 1
        if self.bola_move:
            if self.bola.midtop[1] < 0 or self.bola.midbottom[1] > 500:
                self.speedy *= -1
            if self.bola.midright[0] > 1200: 
                self.p1 += 1
                self.cambiada = True
                self.restart()
            if self.bola.midleft[0] < 0:
                self.p2 += 1
                self.cambiada = True
                self.restart()
            self.bola = self.bola.move(self.speedx, self.speedy)

    def restart(self):
        self.bola_move = False
        self.bola = self.bola.clamp(self.bola_pos)

    def run_game(self):
        while True:
            self.screen.fill((0, 0, 0))
            self.update()
            self.ball_move()
            self.collision_update()
            if self.cambiada:
                self.cambiada = False
                self.fp1 = pygame.font.SysFont('freesansbold.ttf', 32).render(str(self.p1), True, (255, 255, 255))
                self.fp2 = pygame.font.SysFont('freesansbold.ttf', 32).render(str(self.p2), True, (255, 255, 255))  
            self.screen.blit(self.fp1, (200, 100))
            self.screen.blit(self.fp2, (1000, 100))
            pygame.draw.rect(self.screen, (255, 255, 255), self.rect1)
            pygame.draw.rect(self.screen, (255, 255, 255), self.rect2)
            pygame.draw.rect(self.screen, (255, 255, 255), self.bola)
            pygame.display.flip()
            self.check_events()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.r1_mup = True
                if event.key == pygame.K_DOWN:
                    self.r1_mdo = True
                if event.key == pygame.K_w:
                    self.r2_mup = True
                if event.key == pygame.K_s:
                    self.r2_mdo = True
                if event.key == pygame.K_SPACE:
                    self.bola_move = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.r1_mup = False
                if event.key == pygame.K_DOWN:
                    self.r1_mdo = False
                if event.key == pygame.K_w:
                    self.r2_mup = False
                if event.key == pygame.K_s:
                    self.r2_mdo = False

    def collision_update(self):
        if self.bola.colliderect(self.rect1):
            self.speedx *= -1
        if self.bola.colliderect(self.rect2):
            self.speedx *= -1

    def update(self):
        if self.r2_mup and self.rect1.midtop[1] > 0:
            self.rect1 = self.rect1.move(0, -self.speed)
        elif self.r2_mdo and self.rect1.midbottom[1] < 500:
            self.rect1 = self.rect1.move(0, self.speed)
        if self.r1_mup and self.rect2.midtop[1] > 0:
            self.rect2 = self.rect2.move(0, -self.speed)
        elif self.r1_mdo and self.rect2.midbottom[1] < 500:
            self.rect2 = self.rect2.move(0, self.speed)

if __name__ == '__main__':
    p = Pong()
    p.run_game()

