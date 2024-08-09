import base64

def pdf_to_base64(pdf_path, output_file_path):
    # 读取PDF文件
    with open(pdf_path, 'rb') as pdf_file:
        pdf_content = pdf_file.read()

    # 打印读取的内容的前几个字节
    print(f"Read content (first 5 bytes): {pdf_content[:5]}")

    # 将PDF内容编码为Base64
    base64_encoded = base64.b64encode(pdf_content)

    # 将Base64编码写入文件
    with open(output_file_path, 'w') as output_file:
        output_file.write(base64_encoded.decode('utf-8'))

    print(f"Base64编码已保存到 {output_file_path}")

if __name__ == "__main__":
    pdf_path = 'your pdf file loation'  # 替换为你的PDF文件路径
    output_file_path = 'base64.txt'  # 输出文件路径
    pdf_to_base64(pdf_path, output_file_path)

