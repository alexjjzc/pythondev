import base64
from PIL import Image
import io

def base64_to_image(base64_str, output_image_path):
    try:
        # 将Base64字符串解码为二进制数据
        img_data = base64.b64decode(base64_str)

        # 使用io.BytesIO将字节流转换为文件对象
        img_file = io.BytesIO(img_data)

        # 打开图片文件对象
        img = Image.open(img_file)

        # 保存图片到指定路径
        img.save(output_image_path)

        print(f"图片已保存到 {output_image_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    base64_str = input("请输入需要转换的base64编码：")
    output_image_path = input("请输入保存图片文件的路径：")

    base64_to_image(base64_str, output_image_path)
