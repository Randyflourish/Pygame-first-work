import pygame
from pygame import mouse

WIDTH = 600
HIGHTH = 600
FPS = 1
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CHINESE = (24, 27, 28, 33, 34, 40, 41, 42, 58, 59, 75, 76, 77, 78, 79, 80, 81, 83, 84,
           85, 86, 137, 138, 205, 206, 208, 210, 211, 212, 213, 214, 215, 216, 217, 218)
pygame.init()  # 初始化
screen = pygame.display.set_mode((WIDTH, HIGHTH))  # 螢幕輸出
pygame.display.set_caption("font test  made by Kaihatsu")
clock = pygame.time.Clock()  # 時間控制
ZiTi = pygame.font.get_fonts()
for i in CHINESE:
    print(ZiTi[i])


clock.tick(FPS)

running = False
i = 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    mouse_press = pygame.mouse.get_pressed()
    if mouse_press[0]:
        i += 1
        print(i)
        pygame.Surface.fill(screen, BLACK)
        pygame.time.wait(200)
    else:
        try:
            test = pygame.font.SysFont(ZiTi[i], 20)
            po = test.render("中文", False, WHITE)
            pygame.Surface.blit(screen, po, (0, 0))
        except:
            running = False

    pygame.display.update()


pygame.quit()


# 24,27,28,33,34,40,41,42,58,59,75-81,83-86,137,138,205,206,208,210-218
