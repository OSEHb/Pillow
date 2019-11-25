from PIL import Image
from math import fabs


# Сабираемая таблица цветов
table_colors = {}
# Группы цветов
groups_colors = {}
# Таблица ключей от группы цветов
keys = {}
# Таблица новых цветов
new_colors = {}
# Переменная +- от среднего значения (изменяемое значение для нужного эффекта)
pm = 20

# Загружаемая картинка. Получим её размер, преобразуем в RGB и получим цвет каждого пикселя
myimg = Image.open('1.jpg')
myimg.load()
s_ze = myimg.size
rgb_myimg = myimg.convert('RGB')

# Новая картинка. Изменим цвет предыдущей, изменяя цвет каждого пикселя
newimg = Image.new('RGB', (s_ze[0], s_ze[1]))  # Задаём тот же размер что и у предыдущей
canvas_pixels = newimg.load()

for y in range(s_ze[0]):
    for x in range(s_ze[1]):
        r, g, b = rgb_myimg.getpixel((y, x))
        table_colors['RGB' + str(y) + 'y' + str(x) + 'x'] = (r, g, b)

        if len(groups_colors) == 0:
            groups_colors['1'] = ['RGB' + str(y) + 'y' + str(x) + 'x']
            keys['RGB' + str(y) + 'y' + str(x) + 'x'] = '1'
            continue

        if y == 0:
            key = keys['RGB' + str(y) + 'y' + str(x - 1) + 'x']
            group_element = groups_colors[key][0]
            rgb = table_colors[group_element]

            if fabs(rgb[0] - table_colors['RGB' + str(y) + 'y' + str(x) + 'x'][0]) < pm and fabs(
                    rgb[1] - table_colors['RGB' + str(y) + 'y' + str(x) + 'x'][1]) < pm and fabs(
                    rgb[2] - table_colors['RGB' + str(y) + 'y' + str(x) + 'x'][2]) < pm:

                groups_colors[key].append('RGB' + str(y) + 'y' + str(x) + 'x')
                keys['RGB' + str(y) + 'y' + str(x) + 'x'] = key
            else:
                k = str(int(len(groups_colors)) + 1)
                groups_colors[k] = ['RGB' + str(y) + 'y' + str(x) + 'x']
                keys['RGB' + str(y) + 'y' + str(x) + 'x'] = k

        elif y != 0 and x == 0:
            key = keys['RGB' + str(y - 1) + 'y' + str(x) + 'x']
            group_element = groups_colors[key][0]
            rgb = table_colors[group_element]

            if fabs(rgb[0] - table_colors['RGB' + str(y) + 'y' + str(x) + 'x'][0]) < pm and fabs(
                    rgb[1] - table_colors['RGB' + str(y) + 'y' + str(x) + 'x'][1]) < pm and fabs(
                    rgb[2] - table_colors['RGB' + str(y) + 'y' + str(x) + 'x'][2]) < pm:

                groups_colors[key].append('RGB' + str(y) + 'y' + str(x) + 'x')
                keys['RGB' + str(y) + 'y' + str(x) + 'x'] = key
            else:
                k = str(int(len(groups_colors)) + 1)
                groups_colors[k] = ['RGB' + str(y) + 'y' + str(x) + 'x']
                keys['RGB' + str(y) + 'y' + str(x) + 'x'] = k

        else:
            key = keys['RGB' + str(y) + 'y' + str(x - 1) + 'x']
            group_element = groups_colors[key][0]
            rgb = table_colors[group_element]

            if fabs(rgb[0] - table_colors['RGB' + str(y) + 'y' + str(x) + 'x'][0]) < pm and fabs(
                    rgb[1] - table_colors['RGB' + str(y) + 'y' + str(x) + 'x'][1]) < pm and fabs(
                    rgb[2] - table_colors['RGB' + str(y) + 'y' + str(x) + 'x'][2]) < pm:

                groups_colors[key].append('RGB' + str(y) + 'y' + str(x) + 'x')
                keys['RGB' + str(y) + 'y' + str(x) + 'x'] = key

            else:
                key = keys['RGB' + str(y - 1) + 'y' + str(x) + 'x']
                group_element = groups_colors[key][0]
                rgb = table_colors[group_element]

                if fabs(rgb[0] - table_colors['RGB' + str(y) + 'y' + str(x) + 'x'][0]) < pm and fabs(
                        rgb[1] - table_colors['RGB' + str(y) + 'y' + str(x) + 'x'][1]) < pm and fabs(
                        rgb[2] - table_colors['RGB' + str(y) + 'y' + str(x) + 'x'][2]) < pm:

                    groups_colors[key].append('RGB' + str(y) + 'y' + str(x) + 'x')
                    keys['RGB' + str(y) + 'y' + str(x) + 'x'] = key

                else:
                    k = str(int(len(groups_colors)) + 1)
                    groups_colors[k] = ['RGB' + str(y) + 'y' + str(x) + 'x']
                    keys['RGB' + str(y) + 'y' + str(x) + 'x'] = k

for grop in groups_colors:
    middle_r = 0
    middle_g = 0
    middle_b = 0
    number_in_group = 0
    for r_g_b in groups_colors[grop]:
        number_in_group += 1
        middle_r += table_colors[r_g_b][0]
        middle_g += table_colors[r_g_b][1]
        middle_b += table_colors[r_g_b][2]

    new_r = middle_r // number_in_group
    new_g = middle_g // number_in_group
    new_b = middle_b // number_in_group

    for r_g_b in groups_colors[grop]:
        new_colors[r_g_b] = (new_r, new_g, new_b)

for y in range(s_ze[0]):
    for x in range(s_ze[1]):
        canvas_pixels[y, x] = new_colors['RGB' + str(y) + 'y' + str(x) + 'x']

newimg.save('1a.jpg')
newimg.show()
