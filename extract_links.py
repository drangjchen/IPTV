import sys

# 提取链接的函数
def extract_links(source_files):
    extracted_links = []

    for source_file in source_files:
        with open(source_file, 'r') as file:
            lines = file.readlines()
            extracting = False

            for line in lines:
                if line.startswith('#EXTINF'):
                    extracting = True
                    extracted_links.append(line)
                elif extracting and line.strip():
                    extracted_links.append(line)

    return extracted_links

# 将提取的链接写入目标文件
def write_to_target(target_file, extracted_links):
    with open(target_file, 'w') as file:
        file.writelines(extracted_links)

if __name__ == '__main__':
    source_files = sys.argv[1:-1]
    target_file = sys.argv[-1]

    extracted_links = extract_links(source_files)
    write_to_target(target_file, extracted_links)
