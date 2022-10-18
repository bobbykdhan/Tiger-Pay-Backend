# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    from pylibdmtx.pylibdmtx import decode
    from PIL import Image

    im = Image.open(r"testlol.jpeg")

    im1 = im.crop((250, 685, 451, 885))
    im1.show()
    print(decode(Image.open("final.png")))


# Setting the points for cropped image
# left = 250
# top = height / 1.54
# right = 451
# bottom = 2.9 * height / 3.44
#
# print(str(left) + ", " + str(top) + ", " + str(right) + ", " + str(bottom) + ", ")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

