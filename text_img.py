from PIL import Image, ImageDraw, ImageFont
from random import choice


lst = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '#', '+', '/', '[', ']', '&', '@', '?', '$',
       'A', 'B', 'C', 'D', 'S', 'R', 'Z', 'V', 'N')
pix = []
# Переменная (изменяемое значение для нужного эффекта)
pm = 8

myimg = Image.open('1.jpg')
myimg.load()
s_ze = myimg.size
rgb_myimg = myimg.convert('L')  # RGB для цветной

newimg = Image.new('L', (s_ze[0], s_ze[1]), 0)
fnt = ImageFont.truetype('BAUHS93.TTF', pm)
d = ImageDraw.Draw(newimg)

n = 0
while n < s_ze[0]:
    if n == 0:
        n += 1
        pix.append(n)
        continue

    n += pm - 1
    pix.append(n)

for y in range(s_ze[0]):
    for x in range(s_ze[1]):
        if y in pix and x in pix:
            symbol = choice(lst)
            l = rgb_myimg.getpixel((y, x))
            d.text((y, x), symbol, font=fnt, fill=l)

newimg.show()
newimg.save('text_img.jpg')

