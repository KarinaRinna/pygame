import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300)) # flags = pygame.NOFRAME
pygame.display.set_caption('pygame_game')    # имя приложения
icon = pygame.image.load('images/icon.png')  # создаем переменную где указываем путь к файлу
pygame.display.set_icon(icon)                # вписываем переменную


running = True
while running:

    screen .fill(('#369e09'))   # цвет фона приложения

    pygame.display.update()     # обновление экрана

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:  #если тип события = нажатие на клавиатуре
            if event.key == pygame.K_a:     # проверяем какая клавиша нажата
                screen.fill(('blue'))       # делаем фон синим



# https://www.youtube.com/watch?v=TcRRWuQXNfU&list=PLDyJYA6aTY1mLtXrGH55paZHFjpqHdDol&index=2
# 16:00