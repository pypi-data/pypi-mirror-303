from PIL import Image


def load_image(img_path):
    return Image.open(img_path)
