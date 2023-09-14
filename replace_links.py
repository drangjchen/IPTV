def replace_links(target_file):
    # ... 其他代码 ...
    replaced = False

    for index, line in enumerate(lines):
        if line.startswith('#EXTINF'):
            if not replaced:
                # 替换链接为你想要的链接
                lines[index + 1] = "https://raw.githubusercontent.com/YueChan/Live/main/IPTV.m3u\n"  # 替换为第一个链接
                lines[index + 2] = "https://raw.githubusercontent.com/Kimentanm/aptv/master/m3u/iptv.m3u\n"  # 替换为第二个链接
                lines[index + 3] = "https://raw.githubusercontent.com/YanG-1989/m3u/main/Gather.m3u\n"  # 替换为第三个链接
                replaced = True

    with open(target_file, 'w') as file:
        file.writelines(lines)

if __name__ == '__main__':
    target_file = "M3U/YueChan_IPV6.m3u"
    replace_links(target_file)
