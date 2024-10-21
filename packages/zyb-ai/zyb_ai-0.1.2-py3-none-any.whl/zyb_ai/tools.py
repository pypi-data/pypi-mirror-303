from PIL import Image


def check_image(img):
    try:
        with Image.open(img) as im:
            if im.format.lower() not in ['jpg', 'jpeg', 'png']:
                raise ValueError("图片格式错误，请修改后重试~")
    except Exception as e:
        raise ValueError("图片格式错误，请修改后重试~")



