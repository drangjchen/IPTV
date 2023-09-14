def extract_links(source_files):
    extracted_links = []

    for source_file in source_files:
        with open(source_file, 'r') as file:
            lines = file.readlines()
            extracting = False

            for line in lines:
                if line.strip():
                    extracted_links.append(line)

    return extracted_links

if __name__ == '__main__':
    source_files = ["source_m3u1.m3u", "source_m3u2.m3u", "source_m3u3.m3u"]
    target_file = "YueChan_IPV6.m3u"

    extracted_links = extract_links(source_files)

    with open(target_file, 'w') as file:
        file.writelines(extracted_links)
