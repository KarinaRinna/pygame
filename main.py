import pygame

pygame.init()
screen = pygame.display.set_mode((800, 290)) # flags = pygame.NOFRAME   # создаем дисплей
pygame.display.set_caption('pygame_game')    # имя приложения
icon = pygame.image.load('images/icon.png')  # создаем переменную где указываем путь к файлу
pygame.display.set_icon(icon)                # вписываем переменную

# square = pygame.Surface((50,170))  # создаем квадрат с параметрами размера
# square.fill('red') # цвет заливки квадрата

# myfont = pygame.font.Font('fonts/Roboto-Regular.ttf', 40)  #создаем переменную и пишем путь к шрифту и размер шрифта
# text_surface = myfont.render('Надпись', True, 'Red')  #переменная в которую устанавливаем характеристики в надпись
                                                         #(надпись, сглаживание, цвет, фон)
bg = pygame.image.load('images/bg.jpg')   # создаем фоновый рисунок
walk_right = [         #создаем список c картинками для анимации
    pygame.image.load('images/player_right/1.png'),
    pygame.image.load('images/player_right/2.png'),
    pygame.image.load('images/player_right/3.png'),
    pygame.image.load('images/player_right/4.png')
]
walk_left = [         #создаем список
    pygame.image.load('images/player_left/1.png'),
    pygame.image.load('images/player_left/2.png'),
    pygame.image.load('images/player_left/3.png'),
    pygame.image.load('images/player_left/4.png')
]

player_anim_count = 0


running = True
while running:
    # screen.blit(square, (10, 0))   # рисуем обьект который мы создали выше square
                                  # и даем ему координаты
  # pygame.draw.circle(screen, 'green', (250, 150), 30)  # сразу рисуем круг в цикле
  # pygame.draw.circle(square, 'green', (10, 7), 5)      #рисуем круг в square
  #   screen.blit(text_surface, (300, 100))   # выводим текст на экран
    screen.blit(bg, (0, 0))     # выводим на экран игрока
    screen.blit(walk_right[player_anim_count], (200, 207))     # выводим игрока

    if player_anim_count == 3:   # анимация персонажа право
        player_anim_count = 0
    else:
        player_anim_count += 1

    pygame.display.update()     # обновление экрана

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # elif event.type == pygame.KEYDOWN:  # если тип события = нажатие на клавиатуре
        #     if event.key == pygame.K_a:     # проверяем какая клавиша нажата
        #         screen.fill(('blue'))       # делаем фон синим



# https://www.youtube.com/watch?v=TcRRWuQXNfU&list=PLDyJYA6aTY1mLtXrGH55paZHFjpqHdDol&index=2
# 16:00