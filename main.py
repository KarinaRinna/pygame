import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300)) # flags = pygame.NOFRAME
pygame.display.set_caption('pygame_game')

running = True
while running:

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()





# https://www.youtube.com/watch?v=TcRRWuQXNfU&list=PLDyJYA6aTY1mLtXrGH55paZHFjpqHdDol&index=2
# 2:00