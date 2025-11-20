import requests
import os

images_to_download = {
    "frans_mic": "https://cdn.webhallen.com/images/product/390272?trim",
    "frans_hockey": "https://www.xxl.se/filespin/88ac7fb05e27459fbbc585d6f800cacd?quality=75&bgcolor=efefef&resize=1080%2C1080",
    "frans_lego_storm": "https://cdn.webhallen.com/images/product/374638?trim",
    "frans_lego_dragon": "https://cdn.webhallen.com/images/product/374635?trim",
    "frans_walkie": "https://m.media-amazon.com/images/I/71lZIMNt8wL._AC_SL1500_.jpg",
    "bosse_football": "https://images.clasohlson.com/medias/sys_master/h02/h57/68641610792990.jpg"
}

# Reuse images for duplicates
# bosse_mic -> frans_mic
# bosse_walkie -> frans_walkie

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

if not os.path.exists('images'):
    os.makedirs('images')

for name, url in images_to_download.items():
    print(f"Downloading {name} from {url}...")
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            # Determine extension (default to .jpg if unknown or complex)
            ext = '.jpg'
            if '.png' in url:
                ext = '.png'
            elif '.webp' in url:
                ext = '.webp'
            
            filename = f"images/{name}{ext}"
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"  Saved to {filename}")
        else:
            print(f"  Failed: {response.status_code}")
    except Exception as e:
        print(f"  Error: {e}")

# Handle duplicates by copying or just referencing (in data.js we will reference)
# But for the file system, we only need the unique ones.
