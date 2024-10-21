import os
import math
import time
import numpy as np
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
from .tools import check_image


def img_fisheye(img, dst='./', strength=1.5):
    """鱼眼风格"""
    if not isinstance(img, str):
        raise TypeError("图片名称类型错误")
    check_image(img)
    if not os.path.exists(img):
        raise ValueError("输入的图片不存在")
    if not os.path.exists(dst):
        try:
            os.makedirs(dst)
        except Exception as e:
            raise ValueError("路径错误，创建文件失败")
    if not isinstance(strength, (int, float)):
        raise TypeError("鱼眼效果参数类型错误")
    if strength < 0:
        strength = 0
    if strength > 10:
        strength = 10

    image = Image.open(img)
    width, height = image.size
    center_x = width / 2
    center_y = height / 2
    np_image = np.array(image)
    output_image = np.zeros_like(np_image)

    for y in range(height):
        for x in range(width):
            dx = x - center_x
            dy = y - center_y
            distance = math.sqrt(dx ** 2 + dy ** 2)
            radius = distance / min(center_x, center_y)
            new_x, new_y = center_x, center_y
            if radius > 0:
                theta = math.atan2(dy, dx)
                r_new = radius ** strength
                new_x = center_x + r_new * math.cos(theta) * center_x
                new_y = center_y + r_new * math.sin(theta) * center_y

            if 0 <= new_x < width and 0 <= new_y < height:
                output_image[int(y), int(x)] = np_image[int(new_y), int(new_x)]
    output_pil_image = Image.fromarray(output_image)
    name = 'fisheye_' + str(int(time.time() * 1000)) + '.png'
    output_pil_image.save(os.path.join(dst, name))
    return name


def img_popart(img, dst='./'):
    """波普艺术风格"""
    if not isinstance(img, str):
        raise TypeError("图片名称类型错误")
    check_image(img)
    if not os.path.exists(img):
        raise ValueError("输入的图片不存在")
    if not os.path.exists(dst):
        try:
            os.makedirs(dst)
        except Exception as e:
            raise ValueError("路径错误，创建文件失败")
    image = Image.open(img)
    base_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
    pop_art_images = []

    for base_color in base_colors:
        color_image = ImageOps.colorize(image.convert("L"), black="black", white=base_color)
        pop_art_images.append(color_image)

    final_image = Image.new('RGB', (image.width * 2, image.height * 2))
    final_image.paste(pop_art_images[0], (0, 0))
    final_image.paste(pop_art_images[1], (image.width, 0))
    final_image.paste(pop_art_images[2], (0, image.height))
    final_image.paste(pop_art_images[3], (image.width, image.height))
    name = 'popart_' + str(int(time.time() * 1000)) + '.png'
    final_image.save(os.path.join(dst, name))
    return name


class ZybImageStyle:

    @staticmethod
    def add_noise(im, noise_level=5):
        """
        为图像添加噪声
        """
        np_image = np.array(im)
        noise = np.random.randint(-noise_level, noise_level, np_image.shape, dtype='int16')
        noisy_image = np.clip(np_image + noise, 0, 255).astype('uint8')
        return Image.fromarray(noisy_image)

    @staticmethod
    def add_vignette(im, vignette_scale=0.75):
        """
        为图像添加渐晕效果
        """
        width, height = im.size
        max_distance = np.sqrt((width / 2) ** 2 + (height / 2) ** 2)
        vignette = Image.new('L', (width, height))

        for y in range(height):
            for x in range(width):
                distance_to_center = np.sqrt((x - width / 2) ** 2 + (y - height / 2) ** 2)
                intensity = int((1 - (distance_to_center / max_distance) ** vignette_scale) * 255)
                vignette.putpixel((x, y), intensity)

        return Image.composite(im, ImageOps.colorize(vignette, 'black', 'white'), vignette)

    @staticmethod
    def add_sepia(im):
        """增加褐色"""
        width, height = im.size
        sepia_image = Image.new('RGB', (width, height))

        for y in range(height):
            for x in range(width):
                r, g, b = im.getpixel((x, y))
                tr = int(0.393 * r + 0.769 * g + 0.189 * b)
                tg = int(0.349 * r + 0.686 * g + 0.168 * b)
                tb = int(0.272 * r + 0.534 * g + 0.131 * b)
                sepia_image.putpixel((x, y), (min(tr, 255), min(tg, 255), min(tb, 255)))
        return sepia_image

    def old_photo_effect(self, image, dst):
        """复古风格"""
        # 1. 转换为灰度图并添加棕褐色调
        gray_image = image.convert('L')
        sepia_image = self.add_sepia(gray_image.convert('RGB'))

        # 2. 添加噪声
        noisy_image = self.add_noise(sepia_image, noise_level=20)

        # 3. 添加渐晕效果
        vignette_image = self.add_vignette(noisy_image)

        # 4. 高斯模糊
        blurred_image = vignette_image.filter(ImageFilter.GaussianBlur(radius=1))

        blurred_image.save(dst)

    def film_filter(self, image, dst):
        """胶片风格"""
        # 1. 调整颜色平衡（添加轻微的黄色和青色色调）
        r, g, b = image.split()
        r = r.point(lambda i: min(255, i * 1.2))
        g = g.point(lambda i: min(255, i * 1.1))
        b = b.point(lambda i: min(255, i * 0.9))
        image = Image.merge('RGB', (r, g, b))

        # 2. 增强对比度和亮度
        image = ImageEnhance.Contrast(image).enhance(1.3)
        image = ImageEnhance.Brightness(image).enhance(1.1)

        # 3. 添加噪声
        noisy_image = self.add_noise(image, noise_level=10)

        # 4. 添加渐晕效果
        final_image = self.add_vignette(noisy_image, vignette_scale=2.0)

        # 保存最终结果
        final_image.save(dst)


def img_transfer(img, style, dst='./'):
    if not isinstance(style, int) or not 0 < style < 3:
        raise ValueError("style非指定范围内的风格")
    if not isinstance(img, str):
        raise TypeError("图片名称类型错误")
    check_image(img)
    if not os.path.exists(img):
        raise ValueError("输入的图片不存在")
    if not os.path.exists(dst):
        try:
            os.makedirs(dst)
        except Exception as e:
            raise ValueError("路径错误，创建文件失败")
    im = Image.open(img).convert('RGB')
    image_style = ZybImageStyle()
    image_name = os.path.split(img)[-1].split('.')[0] + '_transfer_' + str(int(time.time() * 1000)) + '.png'
    dst = os.path.join(dst, image_name)
    if style == 1:
        image_style.old_photo_effect(im, dst)
    elif style == 2:
        image_style.film_filter(im, dst)
    return image_name



