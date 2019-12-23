from PIL import Image


black = []
# Переменная (изменяемое значение для нужного эффекта)
pm = 6

myimg = Image.open('1.jpg')
myimg.load()
s_ze = myimg.size
rgb_myimg = myimg.convert('L')

newimg = Image.new('L', (s_ze[0], s_ze[1]))
canvas_pixels = newimg.load()

n = 0
while n < s_ze[0]:
    if n == 0:
        black.append(n)

    n += pm - 1
    black.append(n)
    n += 1
    black.append(n)


for y in range(s_ze[0]):
    for x in range(s_ze[1]):
        if y in black:
            canvas_pixels[y, x] = 0
            continue
        elif x in black:
            canvas_pixels[y, x] = 0
            continue
        else:
            l = rgb_myimg.getpixel((y, x))
            canvas_pixels[y, x] = l

newimg.show()
newimg.save('new_grid.jpg')




