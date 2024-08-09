import base64
from PIL import Image
import io

def image_to_base64(image_path):
    # 打开图片文件
    with Image.open(image_path) as img:
        # 将图片转换为字节流
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format=img.format)
        img_byte_arr = img_byte_arr.getvalue()

    # 将字节流编码为Base64
    base64_encoded = base64.b64encode(img_byte_arr)
    return base64_encoded.decode('utf-8')


if __name__ == "__main__":
    image_path = 'your picture file location'  # 替换为你的图片路径
    base64_encoded_image = image_to_base64(image_path)
    print(base64_encoded_image)
