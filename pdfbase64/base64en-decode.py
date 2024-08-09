import base64

def decode_and_save(encoded_str, output_path, log_file):
    # 检查并修复字符串长度，确保是4的倍数
    encoded_str += '=' * (4 - len(encoded_str) % 4) if len(encoded_str) % 4 else ''
    print("编码正确！！！", file=log_file)

    # 尝试解码
    try:
        decoded_data = base64.b64decode(encoded_str)
    except Exception as e:
        print(f"Failed to decode: {e}", file=log_file)
    else:
        # 保存解码后的数据到文件
        with open(output_path, 'wb') as f:
            f.write(decoded_data)
        print(f"Decoded data saved to {output_path}", file=log_file)

if __name__ == "__main__":
    # 获取Base64编码字符串
    encoded_str = input("请输入需要转换的base64编码：")

    # 获取输出文件路径
    output_path = input("请输入保存解码后文件的路径：")

    # 打开日志文件
    with open('log.log', 'w') as log_file:
        # 调用解码和保存函数
        decode_and_save(encoded_str, output_path, log_file)

    print("操作完成，日志已保存到 log.log")
