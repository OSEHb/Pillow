from PIL import Image

# Сабираемая таблица цветов
colors = []

# Переменная (изменяемое значение для нужного эффекта)
pm = 4

# Загружаемая картинка. Получим её размер, преобразуем в RGB и получим цвет каждого пикселя
myimg = Image.open('1_2.jpg')
myimg.load()
s_ze = myimg.size
rgb_myimg = myimg.convert('RGB')

# Новая картинка. Изменим цвет предыдущей, изменяя цвет каждого пикселя
newimg = Image.new('RGB', (s_ze[0], s_ze[1]))  # Задаём тот же размер что и у предыдущей
canvas_pixels = newimg.load()

flag = False
start_y = 0
s_y = 0
start_x = 0
s_x = 0

while True:
    if flag == True:
        break

    for y in range(start_y, start_y + pm):
        for x in range(start_x, start_x + pm):
            r, g, b = rgb_myimg.getpixel((y, x))
            colors.append((r, g, b))

            if len(colors) == pm * pm:
                n = pm * pm
                new_r = []
                new_g = []
                new_b = []

                for i in range(n):
                    new_r.append(colors[i][0])
                    new_g.append(colors[i][1])
                    new_b.append(colors[i][2])

                mid_new_r = sum(new_r) // n
                mid_new_g = sum(new_g) // n
                mid_new_b = sum(new_b) // n

                for new_y in range(start_y, start_y + pm):
                    s_y += 1

                    for new_x in range(start_x, start_x + pm):
                        s_x += 1
                        canvas_pixels[new_y, new_x] = (mid_new_r, mid_new_g, mid_new_b)
                        if s_y == pm and s_x == pm * pm:
                            start_x += pm
                            s_y = 0
                            s_x = 0
                            colors = []

                            if start_x + pm > s_ze[1]:
                                start_y += pm
                                start_x = 0

                            if start_y + pm > s_ze[0]:
                                flag = True

newimg.save('1_4.jpg')
newimg.show()




