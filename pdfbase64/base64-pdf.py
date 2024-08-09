import base64

def base64_to_pdf(base64_string, output_pdf_path):
    try:
        # 将Base64字符串解码为二进制数据
        pdf_content = base64.b64decode(base64_string)

        # 检查PDF文件的魔数
        if pdf_content[:5] != b'%PDF-':
            print("Error: Decoded content does not start with PDF magic number '%PDF-'")
            return

        # 将二进制数据写入PDF文件
        with open(output_pdf_path, 'wb') as pdf_file:
            pdf_file.write(pdf_content)

        print(f"PDF文件已保存到 {output_pdf_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # 从文件中读取Base64编码
    base64_file_path = input("请输入包含base64编码的文件路径：")
    with open(base64_file_path, 'r') as file:
        base64_string = file.read()

    # 获取输出PDF文件路径
    output_pdf_path = input("请输入保存PDF文件的路径：")

    # 调用函数进行转换
    base64_to_pdf(base64_string, output_pdf_path)
