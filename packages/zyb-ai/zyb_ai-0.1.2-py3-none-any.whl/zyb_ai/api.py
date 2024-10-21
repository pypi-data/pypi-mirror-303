import time
import requests
import base64
import json
import os
from .tools import check_image as _check_image

try:
    __data = os.environ.get("RUNTIME_USER_INFO")
    if not __data:
        HOST = 'deer.zuoyebang.com'
    else:
        __user_info = json.loads(__data)
        HOST = __user_info.get('currentDomain', 'deer.zuoyebang.com')
except Exception as e:
    HOST = 'deer.zuoyebang.com'


def img_transfer(img, style, dst='./'):
    if not isinstance(img, str):
        raise TypeError("图片名称类型错误")
    _check_image(img)
    if not os.path.exists(img):
        raise ValueError("输入的图片不存在")
    if not isinstance(style, int) or not 0 < style < 10:
        raise ValueError("style非指定范围内的风格")
    if not os.path.exists(dst):
        try:
            os.makedirs(dst)
        except Exception as e:
            raise ValueError("路径错误，创建文件失败")

    url = f'https://{HOST}/dijkstra/images/styletrans'
    with open(img, 'rb') as fp:
        content = fp.read()
    res = requests.post(url, data={"image": base64.b64encode(content).decode("utf-8"), "option": style})
    result = res.json()
    err_no = result.get("errNo")
    if err_no != 0:
        raise ValueError("%s, %s" % (err_no, result.get("errMsg", "接口调用错误")))
    data = result.get("data", {}).get("image")
    if not data:
        raise ValueError("图片转换失败，请稍后重试~")
    image_data = base64.b64decode(data)
    image_name = os.path.split(img)[-1].split('.')[0] + '_transfer_' + str(int(time.time() * 1000)) + '.png'
    filename = os.path.join(dst, image_name)
    with open(filename, 'wb') as fp:
        fp.write(image_data)
    return image_name


def text2image(text, name=None, dst='./'):
    if not isinstance(text, str):
        raise ValueError("文本内容类型错误")
    if len(text) > 100:
        raise ValueError("文本描述内容上限为100个文字")
    if name is None:
        name = 'text2image_' + str(int(time.time() * 1000))
    if not isinstance(name, str):
        raise TypeError("生成文件名称类型错误")
    if not name:
        raise ValueError("生成文件名错误")
    name = name + '.png'
    if not os.path.exists(dst):
        try:
            os.makedirs(dst)
        except Exception as e:
            raise ValueError("路径错误，创建文件失败")
    url = f'https://{HOST}/dijkstra/images/text2image'
    res = requests.post(url, data={"prompt": text})
    result = res.json()
    err_no = result.get("errNo")
    if err_no != 0:
        raise ValueError("%s, %s" % (err_no, result.get("errMsg", "接口调用错误")))
    data = result.get("data")
    if not data:
        raise ValueError("图片生成失败，请稍后重试~")
    pid = data[0]

    url = f'https://{HOST}/dijkstra/images/getimage'
    time.sleep(10)
    while True:
        res = requests.post(url, data={"pid": pid})
        result = res.json()
        err_no = result.get("errNo")
        if err_no != 0:
            raise ValueError("%s, %s" % (err_no, result.get("errMsg", "接口调用错误")))
        data = result.get("data")
        if not data:
            raise ValueError("图片生成失败，请稍后重试~")
        picture = data.get("picture")
        if not picture:
            time.sleep(5)
            continue
        break
    image_data = base64.b64decode(picture)
    filename = os.path.join(dst, name)
    with open(filename, 'wb') as fp:
        fp.write(image_data)
    return name


def write_poem(word, layout=5, mode=0):
    if not isinstance(word, str) or len(word) < 1 or len(word) > 7:
        raise ValueError("提示词为1～7个字符的字符串")
    if layout not in [5, 7]:
        raise ValueError("请输入正确的诗词格式参数，五言诗: 5，七言诗: 7")
    if mode not in [0, 1]:
        raise ValueError("请输入正确的模式参数，藏头：0，藏尾：1")

    url = f'https://{HOST}/dijkstra/lang/poetry'
    res = requests.post(url, data={"word": word, "len": layout, "type":mode})
    result = res.json()
    err_no = result.get("errNo")
    if err_no != 0:
        raise ValueError("%s, %s" % (err_no, result.get("errMsg", "接口调用错误")))
    data = result.get("data", {}).get("poetry", [])
    if not data:
        raise ValueError("获取数据失败")
    return data


def img_cartoon(img, dst='./'):
    """生成卡通图"""
    if not isinstance(img, str):
        raise TypeError("图片名称类型错误")
    _check_image(img)
    if not os.path.exists(img):
        raise ValueError("输入的图片不存在")
    if not os.path.exists(dst):
        try:
            os.makedirs(dst)
        except Exception as e:
            raise ValueError("路径错误，创建文件失败")
    url = f'https://{HOST}/dijkstra/images/image2image'
    with open(img, 'rb') as fp:
        content = fp.read()
    res = requests.post(url, json={"image": base64.b64encode(content).decode("utf-8")})
    result = res.json()
    err_no = result.get("errNo")
    if err_no != 0:
        raise ValueError("%s, %s" % (err_no, result.get("errMsg", "接口调用错误")))
    data = result.get("data", {}).get("image")
    if not data:
        raise ValueError("图片转换失败，请稍后重试~")
    image_data = base64.b64decode(data)
    image_name = os.path.split(img)[-1].split('.')[0] + '_cartoon_' + str(int(time.time() * 1000)) + '.png'
    filename = os.path.join(dst, image_name)
    with open(filename, 'wb') as fp:
        fp.write(image_data)
    return image_name


def face_aging(img, age, dst='./'):
    if not isinstance(img, str):
        raise TypeError("图片名称类型错误")
    _check_image(img)
    if not os.path.exists(img):
        raise ValueError("输入的图片不存在")
    if not isinstance(age, int) or age < 0:
        raise TypeError("age类型错误，需为非负整数")
    if age < 10:
        age = 10
    if age > 100:
        age = 100
    if not os.path.exists(dst):
        try:
            os.makedirs(dst)
        except Exception as e:
            raise ValueError("路径错误，创建文件失败")
    url = f'https://{HOST}/dijkstra/images/aging'
    with open(img, 'rb') as fp:
        content = fp.read()
    res = requests.post(url, json={"image": base64.b64encode(content).decode("utf-8"), "age": age})
    result = res.json()
    err_no = result.get("errNo")
    if err_no != 0:
        raise ValueError("%s, %s" % (err_no, result.get("errMsg", "接口调用错误")))
    data = result.get("data", {}).get("renderImg")
    if not data:
        raise ValueError("图片转换失败，请稍后重试~")
    image_data = base64.b64decode(data)
    image_name = os.path.split(img)[-1].split('.')[0] + '_aging_' + str(int(time.time() * 1000)) + '.png'
    filename = os.path.join(dst, image_name)
    with open(filename, 'wb') as fp:
        fp.write(image_data)
    return image_name

