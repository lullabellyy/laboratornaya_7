from PIL import Image
import cv2

def zadanie_1():
    print("задание 1")
    filename = "G:\picture.png"
    with Image.open(filename) as img:
        img.load()
    img.show()
    width, heith = img.size
    format = img.format
    mode = img.mode
    print("ширина:", width)
    print("высота:", heith)
    print("формат:", format)
    print("цветовая модель: ", mode)



def zadanie_2():
    print("задание2")
    filename = "G:\lab\p3.jpg"
    with Image.open(filename) as img:
        img.load()
    newimg = img.resize((img.width // 3, img.height // 3))
    newimg.save("resized_cat.jpg")
    newimg = img.transpose(Image.FLIP_LEFT_RIGHT)
    newimg = img.transpose(Image.FLIP_TOP_BOTTOM)
    newimg.save("resized_and_rotated1_cat.jpg")
    newimg = img.transpose(Image.ROTATE_90)
    newimg.save("resized_and_rotated2_cat.jpg")


def zadanie_3():
    print("задание3")
    filename = "G:\lab\pcat1.jpg"
    with Image.open(filename) as img:
        img.load()
    gray_img = img.convert("L")
    gray_img.save("black_and_white_cat.jpg")

    filename = "G:\lab\p2.jpg"
    with Image.open(filename) as img:
        img.load()
    gray_img = img.convert("L")
    gray_img.save("black_and_white_p2.jpg")

    filename = "G:\lab\p3.jpg"
    with Image.open(filename) as img:
        img.load()
    gray_img = img.convert("L")
    gray_img.save("black_and_white_p3.jpg")

    filename = "G:\lab\p4.jpg"
    with Image.open(filename) as img:
        img.load()
    gray_img = img.convert("L")
    gray_img.save("black_and_white_p4.jpg")

    filename = "G:\lab\p5.jpg"
    with Image.open(filename) as img:
        img.load()
    gray_img = img.convert("L")
    gray_img.save("black_and_white_p5.jpg")


def zadanie_4():
    print("задание4")
    img = Image.open('G:\lab\pcat1.jpg')
    watermark = Image.open('G:\lab\watermark.png')

    img.paste(watermark, (450, 230), watermark)
    img.save("img_with_watermark.png")

zadanie_1(), zadanie_2(), zadanie_3(), zadanie_4()

