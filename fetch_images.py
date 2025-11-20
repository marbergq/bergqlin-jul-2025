import requests
from bs4 import BeautifulSoup
import os
import json
import time

# Data from data.js
wishlist_data = {
  "frans": [
    {"link": "https://www.gear4music.se/sv/Gitarr-bas/VISIONSTRING-Mini-Electric-Guitar-with-In-Built-Speaker-Black/785I", "id": "frans_guitar"},
    {"link": "https://blavittshopen.se/products/malvaktstroja-jr-hemma-25", "id": "frans_ifk"},
    {"link": "https://www.intersport.se/klader/trojor/replicor/frolunda-hockey-home-25-26-jr-matchtroja-barn/red", "id": "frans_frolunda"},
    {"link": "https://www.webhallen.com/se/product/390272-Andersson-KEM-D3000-Karaoke-hogtalare", "id": "frans_mic"},
    {"link": "https://www.xxl.se/stiga-play-off-21-sverige-finland-bordshockeyspel/p/1153509_1_Style", "id": "frans_hockey"},
    {"link": "https://www.webhallen.com/se/product/374638-LEGO-Ninjago-Ras-och-Arins-superstormplan-71833", "id": "frans_lego_storm"},
    {"link": "https://www.webhallen.com/se/product/374635-LEGO-Ninjago-Lloyds-grona-skogsdrake-71829", "id": "frans_lego_dragon"},
    {"link": "https://www.lekia.se/leksaker/lego-shop/lego-city-60456-polisens-batjakt", "id": "frans_lego_city"},
    {"link": "https://www.amazon.se/uppladdningsbara-NXGKET-litiumjonbatteri-Squelch-kabel-utomhusspel/dp/B0CC1ZZM4F", "id": "frans_walkie"},
    {"link": "https://www.lekia.se/leksaker/experiment-och-teknik/kassaskap-svenska-mynt", "id": "frans_safe"},
    {"link": "https://www.lekia.se/leksaker/leksaksbilar-och-fordon/polis-ambulans-brandbilar/special-team-sos-station-se", "id": "frans_police"},
    {"link": "https://www.lekia.se/leksaker/musik/scen/stage-spegellampa-10-cm", "id": "frans_disco"},
    {"link": "https://www.lekia.se/leksaker/kalas-och-maskerad/drakter-och-tillbehor/disguise-minecraft-role-play-sword-cape-set", "id": "frans_minecraft"}
  ],
  "bosse": [
    {"link": "https://www.lekia.se/leksaker/pyssla/ovrigt-pyssel/so-bomb-bath-bomb-dispenser", "id": "bosse_bomb"},
    {"link": "https://toyspace.se/gron-rc-offroad-bil-med-kraftiga-dack-a2051-uj99-p181?gad_source=1", "id": "bosse_rc"},
    {"link": "https://www.webhallen.com/se/product/390272-Andersson-KEM-D3000-Karaoke-hogtalare", "id": "bosse_mic"},
    {"link": "https://www.clasohlson.com/se/PowerPlay-fotbollsspel-spelbord-4-i-1,-fr%C3%A5n-5-%C3%A5r/p/31-7362", "id": "bosse_football"},
    {"link": "https://outl1.se/fristaende-svart-basketkorg", "id": "bosse_basket"},
    {"link": "https://www.lekia.se/leksaker/byggsatser/byggsatser/mag-play-kulbana-106-st", "id": "bosse_marble"},
    {"link": "https://www.amazon.se/uppladdningsbara-NXGKET-litiumjonbatteri-Squelch-kabel-utomhusspel/dp/B0CC1ZZM4F", "id": "bosse_walkie"},
    {"link": "https://www.lekia.se/leksaker/experiment-och-teknik/teleskap", "id": "bosse_telescope"},
    {"link": "https://www.lekia.se/leksaker/musik/instrument/stage-keyboard-med-mikrofon-37-tangenter", "id": "bosse_piano"},
    {"link": "https://www.lekia.se/leksaker/kalas-och-maskerad/drakter-och-tillbehor/disguise-disney-lilo-stitch-costume-classic-stitch-s-(4-6)1", "id": "bosse_stitch"},
    {"link": "https://www.lekia.se/leksaker/spel/bradspel/brio-labyrint", "id": "bosse_brio"}
  ]
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

if not os.path.exists('images'):
    os.makedirs('images')

image_map = {}

for person, items in wishlist_data.items():
    for item in items:
        url = item['link']
        item_id = item['id']
        print(f"Processing {item_id}: {url}")
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                og_image = soup.find("meta", property="og:image")
                
                if og_image and og_image.get("content"):
                    img_url = og_image["content"]
                    if not img_url.startswith('http'):
                        # Handle relative URLs if necessary (though og:image is usually absolute)
                        pass
                        
                    print(f"  Found image: {img_url}")
                    
                    # Download image
                    img_data = requests.get(img_url, headers=headers, timeout=10).content
                    ext = os.path.splitext(img_url)[1].split('?')[0]
                    if not ext:
                        ext = '.jpg' # Default
                    
                    filename = f"images/{item_id}{ext}"
                    with open(filename, 'wb') as f:
                        f.write(img_data)
                    
                    image_map[url] = filename
                    print(f"  Saved to {filename}")
                else:
                    print("  No og:image found")
            else:
                print(f"  Failed to fetch page: {response.status_code}")
        except Exception as e:
            print(f"  Error: {e}")
        
        time.sleep(1) # Be nice

print(json.dumps(image_map, indent=2))
