from PIL import Image


# col = Image.open("1.jpg")
# gray = col.convert('L')
# bw = gray.point(lambda x: 0 if x < 128 else 255, '1')
# bw.show()
# bw.save("1_BW.jpg")


col = Image.open("1.jpg")
gray = col.convert('L')
bw = gray.point(lambda x: x)
bw.show()
bw.save("1_BW.jpg")


# image_file = Image.open("1.jpg")
# image_file = image_file.convert('1')
# image_file.show()
# image_file.save('1_BW.jpg')

