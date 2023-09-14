import os
import requests

# Define the URL of the M3U file
m3u_url = "https://raw.githubusercontent.com/YueChan/Live/main/IPTV.m3u"

# Send a GET request to fetch the M3U file
response = requests.get(m3u_url)

# Check if the request was successful
if response.status_code == 200:
    lines = response.text.splitlines()
    
    for line in lines:
        if "#EXTINF" in line:
            # Extract the tvg-name and group-title from the line
            tvg_name = line.split('tvg-name="')[1].split('"')[0]
            group_title = line.split('group-title="')[1].split('"')[0]
            
            # Check if the group-title matches the desired values and if the line contains "http://"
            if group_title in ["央视", "国际", "卫视", "地方", "数字"] and "http://" in line:
                # Print the line before saving it
                print(f"Processing: {line}")
                
                # Save the line to a file in the ./tmp/ directory
                with open(f"./tmp/{tvg_name}.m3u", "a") as tmp_file:
                    tmp_file.write(line + "\n")
    
    # Replace the content of ./M3U/YueChan_ipv6.m3u with the content of the modified M3U file
    with open("./M3U/YueChan_ipv6.m3u", "w") as output_file:
        for root, dirs, files in os.walk("./tmp/"):
            for file in files:
                with open(os.path.join(root, file), "r") as tmp_file:
                    output_file.write(tmp_file.read())
    
    # Clean up: Delete the files in the ./tmp/ directory
    for root, dirs, files in os.walk("./tmp/"):
        for file in files:
            os.remove(os.path.join(root, file))
else:
    print(f"Failed to fetch M3U file. Status code: {response.status_code}")
