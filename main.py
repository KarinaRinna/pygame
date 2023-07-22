import pygame

clock = pygame.time.Clock()   # добавляем часы (также в конце цикла tick)

pygame.init()
screen = pygame.display.set_mode((1600, 724)) # flags = pygame.NOFRAME   # создаем дисплей
pygame.display.set_caption('pygame_game')    # имя приложения
icon = pygame.image.load('images/icon.png').convert_alpha()  # создаем переменную где указываем путь к файлу
pygame.display.set_icon(icon)                # вписываем переменную

# square = pygame.Surface((50,170))  # создаем квадрат с параметрами размера
# square.fill('red') # цвет заливки квадрата

# myfont = pygame.font.Font('fonts/Roboto-Regular.ttf', 40)  #создаем переменную и пишем путь к шрифту и размер шрифта
# text_surface = myfont.render('Надпись', True, 'Red')  #переменная в которую устанавливаем характеристики в надпись
                                                         #(надпись, сглаживание, цвет, фон)
# Игрок
bg = pygame.image.load('images/bg.png').convert_alpha()   # создаем фоновый рисунок
walk_right = [         #создаем список c картинками для анимации
    pygame.image.load('images/player_right/1.png').convert_alpha(),
    pygame.image.load('images/player_right/2.png').convert_alpha(),
    pygame.image.load('images/player_right/3.png').convert_alpha(),
    pygame.image.load('images/player_right/4.png').convert_alpha()
]
walk_left = [         #создаем список
    pygame.image.load('images/player_left/1.png').convert_alpha(),
    pygame.image.load('images/player_left/2.png').convert_alpha(),
    pygame.image.load('images/player_left/3.png').convert_alpha(),
    pygame.image.load('images/player_left/4.png').convert_alpha()
]


duck = pygame.image.load('images/duck.png').convert_alpha()   # создаем  рисунок врага
# теперь выводим врага в цикле duck_x = 1602  # враг стоит справа от экрана и потом появится
duck_lict_in_game = []  # список врагов

player_speed = 5  # скорость игрока
player_x = 200    # расположение игрока по x
player_y = 620    # расположение по y

is_jump = False # отслеживание прыжка
jump_count = 9  # высота прыжка


player_anim_count = 0  # флаг анимации персонажа
bg_x = 0               # флаг фона

pygame.mixer.init(44100, -16,2,2048)

bg_sound = pygame.mixer.Sound('sounds/bg.mp3') # создаем переменную звука фона
bg_sound.play(-1) # запускаем чтобы она постоянно играла
bg_sound.set_volume(0.3) # звук фоновой музыки
player_bounce = pygame.mixer.Sound('sounds/1.mp3') # звук прыжка
player_bounce.set_volume(0.4) # уровень звука прыжка
# https://younglinux.info/pygame/mixer

duck_timer = pygame.USEREVENT + 1 # подключаем таймер
pygame.time.set_timer(duck_timer, 3500) # промежутки через которые срабатывает таймер 3500 (3,5 секунд)

label = pygame.font.Font('fonts/Roboto-Regular.ttf', 40) # переменная с параметрами надписи
lose_label = label.render('ВЫ ПРОИГРАЛИ !!!', False, (193, 196, 199)) # надпись проигрыша
restart_label = label.render('Играть заново', False, (115, 132, 148)) # текст рестарт
restart_label_rect = restart_label.get_rect(topleft=(650, 400)) # координаты обводки рестарта

bullet = pygame.image.load('images/bullet.png').convert_alpha() # патрон
bullets = [] # список с выпущенными патронами

gameplay = True

running = True
while running:

    # screen.blit(square, (10, 0))   # рисуем обьект который мы создали выше square
                                  # и даем ему координаты
  # pygame.draw.circle(screen, 'green', (250, 150), 30)  # сразу рисуем круг в цикле
  # pygame.draw.circle(square, 'green', (10, 7), 5)      #рисуем круг в square
  #   screen.blit(text_surface, (300, 100))   # выводим текст на экран
    screen.blit(bg, (bg_x, 0))           # выводим на экран задний фон
    screen.blit(bg, (bg_x + 1600, 0))     # выводим фон правее
# больше не нужно выводить, так как выводится в цикле в списке    screen.blit(duck,(duck_x, 580))  # выводим врага на экран на уровне персонажа

    if gameplay:  # если gameplay = true то выполняем весь код снизу
        player_rect = walk_left[0].get_rect(topleft=(player_x,player_y)) # создаем квадрат вокруг игрока

        if duck_lict_in_game:  # есть ли элементы в списке
            for (i, el) in enumerate(duck_lict_in_game): # перебираем список
                screen.blit(duck, el) # выводим  врага по координатам ( в коде duck_lict_in_game.append(duck.get_rect(topleft=(1620, 580)))  )
                el.x -= 10 # передвигаем врага к игроку

                if el.x < -10: # если враг x=-10 то уничтожаем врага
                    duck_lict_in_game.pop(i)

                if player_rect.colliderect(el): # если квадраты игрока и врага соприкосаются
                    gameplay = False            # то gameplay=false и фон окрашивается


        keys = pygame.key.get_pressed()  # переменная где пользователь нажимает кнопку
        if keys[pygame.K_a]:  # если нажимаем a то движемся влево анимации
            screen.blit(walk_left[player_anim_count], (player_x, player_y))     # выводим игрока
        else:
            screen.blit(walk_right[player_anim_count], (player_x, player_y))


        if keys[pygame.K_a] and player_x > 50:     # если нажмем на кнопку a (если меньше 50 то не двигается)
            player_x -= player_speed  # отнимаем скорость у игрока
        elif keys[pygame.K_d] and player_x < 1550:     # если нажмем на кнопку d  (если больше 1550 то не двигается)
            player_x += player_speed  # добавляем скорость игроку

        if not is_jump:   # если мы НЕ прыгаем
            if keys[pygame.K_SPACE]:  # если нажали на пробел
                is_jump = True     # прыжок начинается
                player_bounce.play() # активировать звук прыжка
        else:
            if jump_count >= -9:  # пока прыжок ниже -9
                if jump_count > 0: # если прыжок > 0 то поднимаем игрока
                    player_y -= (jump_count ** 2) / 2
                else:
                    player_y += (jump_count ** 2) / 2
                jump_count -= 1
            else:
                is_jump = False # больше нет прыжка
                jump_count = 9


        if player_anim_count == 3:   # анимация персонажа
            player_anim_count = 0
        else:
            player_anim_count += 1


        bg_x -= 4 # каждый цикл сдвигаем основной фон влево, чтобы начинался правый фон
        if bg_x == -1600:  # когда фон сдвинется до конца, то опять ставим 1 картинку
            bg_x = 0

        if keys[pygame.K_r]: # если нажали r
            bullets.append(bullet.get_rect(topleft=(player_x + 30, player_y + 10)))  #передаем квадрат пули в координаты где игрок

        if bullets:  # есть ли элементы в списке и выводим их
            for (i, el) in enumerate(bullets):
                screen.blit(bullet, (el.x, el.y))
                el.x += 8    # передвигаем пулю

                if el.x > 1620: # если пуля за пределами экрана то удаляем
                    bullets.pop(i)  # удаляем i из списка bullets

    else:
        screen.fill((87, 88, 89))  # если игра завершена то окрашиваем все в другой цвет
        screen.blit(lose_label, (650, 300)) # вывод проигрыша на экран
        screen.blit(restart_label, restart_label_rect) # вывод кнопки рестарта

        mouse = pygame.mouse.get_pos()   # создаем переменную и помещаем координаты мыши
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]: # соприкасается ли квадрат с координатами мышки и нажали ли мы на кнопку мыши
            gameplay = True  # возобнавляем игру
            player_x = 200   # возвращаем игрока обратно
            duck_lict_in_game.clear()  # убираем врагов
            bullets.clear()  # убираем пули после перезапуска


  #  duck_x -= 10 # делаем передвижение врага (теперь в списке врагов)

    pygame.display.update()     # обновление экрана

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == duck_timer: # отслеживание выполнения таймера
            duck_lict_in_game.append(duck.get_rect(topleft=(1620, 580))) # создаем врага
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                pygame.mixer.music.pause() # пауза на кнопку 1
            elif event.key == pygame.K_2:
                pygame.mixer.music.unpause()
                # возобновляем фоновую музыку
                pygame.mixer.music.set_volume(0.5)
            elif event.key == pygame.K_3:
                pygame.mixer.music.unpause()
                # хз
                pygame.mixer.music.set_volume(1)
            elif event.key == pygame.K_3:
                pygame.mixer.music.unpause()
                # хз
                pygame.mixer.music.set_volume(1)
            # elif event.type == pygame.QUIT:
            #     bg_sound.stop()

    # pygame.mixer.init(44100, -16,2,2048)
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         bg_sound.stop()



        # elif event.type == pygame.KEYDOWN:  # если тип события = нажатие на клавиатуре
        #     if event.key == pygame.K_a:     # проверяем какая клавиша нажата
        #         screen.fill(('blue'))       # делаем фон синим
    clock.tick(20)    #часы количество обновлений кадров 20


# https://www.youtube.com/watch?v=TcRRWuQXNfU&list=PLDyJYA6aTY1mLtXrGH55paZHFjpqHdDol&index=2
# 8 00:00
#
# Спасибо, всё очень понятно, после просмотра видео прикрутил отображение счётчика патронов
# ingame_label = pygame.font.Font('fonts/RobotoCondensed-Bold.ttf', 30) создал отображение текста поменьше
# bulets_left_ind = pygame.image.load('images/bulet_indic.png').convert_alpha()
#
#         screen.blit(bulets_left_ind, (500, 10))
#         bulets_left_count = ingame_label.render((str(bulets_left)), True, (0, 0, 0))  создание текста с количеством патронов
#         screen.blit(bulets_left_count, (550, 10))
#
#
# последние три сразу после блока if bulets:
# первые 2 до цикла while running:
# 
