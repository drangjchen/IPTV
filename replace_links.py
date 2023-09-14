def replace_links(target_file):
    with open(target_file, 'r') as file:
        lines = file.readlines()

    # 初始化一个空列表以存储新的链接
    new_links = []

    replaced = False

    for index, line in enumerate(lines):
        if line.startswith('#EXTINF'):
            if not replaced:
                # 替换链接为你想要的链接
                new_links.append("https://raw.githubusercontent.com/YueChan/Live/main/IPTV.m3u\n")  # 替换为第一个链接
                new_links.append("https://raw.githubusercontent.com/Kimentanm/aptv/master/m3u/iptv.m3u\n")  # 替换为第二个链接
                new_links.append("https://raw.githubusercontent.com/YanG-1989/m3u/main/Gather.m3u\n")  # 替换为第三个链接
                replaced = True

    # 将新的链接写入文件
    with open(target_file, 'w') as file:
        for line in lines:
            if line.startswith('#EXTINF'):
                file.write(line)
                for new_link in new_links:
                    file.write(new_link)
            else:
                file.write(line)

if __name__ == '__main__':
    target_file = "./M3U/YueChan_IPV6.m3u"
    replace_links(target_file)
