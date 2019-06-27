from PIL import Image


def load_img(file):
    img = Image.open(file)
    return img
img = load_img("obama.jpg")
def show_img(img):
    img.show()
show_img(img)

def save_img(img, save_name):
    img.save(save_name)

def obamicon(img):
    pass




