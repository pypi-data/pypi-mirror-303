from .api import img_cartoon, text2image, write_poem, face_aging
from .front import img_fisheye, img_popart
from .api import img_transfer as _api_img_transfer
from .front import img_transfer as _front_img_transfer


def img_transfer(img, style, dst='./'):
    if not isinstance(style, int) or not 0 < style < 12:
        raise ValueError("style非指定范围内的风格")
    front_styles = {
        1: 1,
        2: 2
    }
    api_styles = {
        3: 1,
        4: 2,
        5: 3,
        6: 4,
        7: 5,
        8: 6,
        9: 7,
        10: 8,
        11: 9
    }
    if style in front_styles:
        return _front_img_transfer(img, front_styles[style], dst)
    else:
        return _api_img_transfer(img, api_styles[style], dst)
