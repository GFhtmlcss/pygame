import pygame


pygame.init() # инициализируем pygame

#стороны дисплея
window_width = 1000
window_height = 700

#дисплей
window = pygame.display.set_mode((window_width, window_height))

#настройки
fill_color = (175, 139, 179)
window.fill(fill_color)
pygame.display.set_caption('test game')

#FPS
clock = pygame.time.Clock()
FPS = 60

# прямоугольник
# координаты начальные и сейчашние
rect_x = 100
rect_y = 50
#ширина и высота прямоугольника
rect_width = 60
rect_height = 100
# скорость
rect_speed = 6
rectangle = pygame.Rect(rect_x, rect_y, rect_width, rect_height)
pygame.draw.rect(window, (20, 50, 90), rectangle)


#текст
font = pygame.font.Font(None, 48)
text = font.render('Игра началась! - твое количество шагов ограниченно ;)', True, [255, 200, 0])
text_pos = (50, 50)

#повороты
rotate = 200

#сама игра
run = True

while run:
    events = pygame.event.get() #события выключения программы
    for event in events:
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed() #события клавиш
    if rotate <= 0:
        font = pygame.font.Font(None, 35)
        text = font.render('Игра окончена! - Упс....  у тебя 0 шагов! Что? Хочешь еще? Перехочешь!', True, [255, 75, 55])
    else:
        if keys[pygame.K_a]:
            if rotate <= 0:
                print('Конец')
            else:
                rect_x -= rect_speed
                rect_width = 100
                rect_height = 60
                rotate -= 1
        if keys[pygame.K_d]:
            if rotate <= 0:
                print('Конец')
            else:
                rect_x += rect_speed
                rect_width = 100
                rect_height = 60
                rotate -= 1
        if keys[pygame.K_w]:
            if rotate <= 0:
                print('Конец')
            else:
                rect_y -= rect_speed
                rect_width = 60
                rect_height = 100
                rotate -= 1
        if keys[pygame.K_s]:
            if rotate <= 0:
                print('Конец')
            else:
                rect_y += rect_speed
                rect_width = 60
                rect_height = 100
                rotate -= 1

    # обновление экрана и фпс
    window.fill(fill_color)
    rectangle = pygame.Rect(rect_x, rect_y, rect_width, rect_height)
    pygame.draw.rect(window, (235, 140, 84), rectangle, 15, 15)
    window.blit(text, text_pos)

    pygame.display.update()
    clock.tick(FPS)

