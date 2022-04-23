import pygame

WIDTH = 600
HIGHTH = 600
FPS = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
pygame.init()  # 初始化
screen = pygame.display.set_mode((WIDTH, HIGHTH))  # 螢幕輸出
pygame.display.set_caption("font test  made by Kaihatsu")
clock = pygame.time.Clock()  # 時間控制
ZiTi = pygame.font.get_fonts()
CN = [24, 27, 28, 33, 34, 40, 41, 42, 58, 59, 75, 76, 77, 78, 79, 80, 81, 83, 84,
      85, 86, 137, 138, 205, 206, 208, 210, 211, 212, 213, 214, 215, 216, 217, 218]
events = pygame.event.get()
mouse_press = pygame.mouse.get_pressed()


def mouse_one_press(n):
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse_press[n]:
                return True


running = True
i = 1

while running:
    clock.tick(FPS)
    mouse_press = pygame.mouse.get_pressed()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

    if mouse_one_press(0):
        i += 1
        print(i)
        pygame.Surface.fill(screen, BLACK)
        try:
            test = pygame.font.SysFont(ZiTi[i], 20)
            po = test.render("中文", False, WHITE)
            pygame.Surface.blit(screen, po, (10, 10))
        except:
            running = False

    pygame.display.update()
    events = pygame.event.get()

pygame.quit()


# 24,27,28,33,34,40,41,42,58,59,75-81,83-86,137,138,205,206,208,210-218
