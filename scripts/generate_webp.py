import os
import sys
import urllib.request
from io import BytesIO

# Ensure Pillow is installed
try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'Pillow'])
    from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.dirname(__file__))
IMAGES_DIR = os.path.join(BASE, 'images')
os.makedirs(IMAGES_DIR, exist_ok=True)

def download_image(url):
    with urllib.request.urlopen(url) as resp:
        return Image.open(BytesIO(resp.read())).convert('RGBA')

def save_webp(img, path, quality=80):
    img.save(path, 'WEBP', quality=quality, method=6)
    print('Saved', path)

# 1) Avatar
try:
    avatar = download_image('https://github.com/MwalaTimothy.png')
    avatar = avatar.resize((350,350), Image.LANCZOS)
    save_webp(avatar, os.path.join(IMAGES_DIR, 'avatar.webp'))
except Exception as e:
    print('Failed to fetch avatar:', e)

# Helper to create a simple placeholder with centered text
def make_banner(text, size=(600,300), bg='#1e293b', fg='#ffffff'):
    img = Image.new('RGB', size, bg)
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype('arial.ttf', 36)
    except Exception:
        font = ImageFont.load_default()
    # Measure text and shrink font size if too wide
    try:
        bbox = draw.textbbox((0, 0), text, font=font)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
    except Exception:
        w, h = draw.textsize(text, font=font)

    fs = 36
    while w > size[0] - 40 and fs > 10:
        fs -= 2
        try:
            font = ImageFont.truetype('arial.ttf', fs)
        except Exception:
            font = ImageFont.load_default()
        try:
            bbox = draw.textbbox((0, 0), text, font=font)
            w = bbox[2] - bbox[0]
            h = bbox[3] - bbox[1]
        except Exception:
            w, h = draw.textsize(text, font=font)
    draw.text(((size[0]-w)/2, (size[1]-h)/2), text, font=font, fill=fg)
    return img

# Create thumbnails
thumbs = [
    ('ld2410', 'Radar Zone Detection', '#0f172a', '#ffffff'),
    ('esp32c3', 'ESP32-C3 iBeacon Gateway', '#2563eb', '#ffffff'),
    ('dht22', 'DHT22 AI Logger', '#059669', '#ffffff'),
]

# Additional placeholders to generate
more = [
    ('youtube', 'YouTube Channel Statistics', '#0f172a', '#ffffff'),
    ('wifi', 'WiFi Signal Meter', '#0f172a', '#ffffff'),
    ('weather', 'Weather Display', '#0f172a', '#ffffff'),
    ('carenuity', 'Carenuity SQ-Panel', '#059669', '#ffffff'),
    ('gpio', 'GPIO Viewer OLED', '#0f172a', '#ffffff'),
    ('env', 'Environmental Sensors', '#0f172a', '#ffffff'),
    ('sht40', 'Smart Environment Monitor SHT40', '#059669', '#ffffff'),
    ('mics6814', 'MICS-6814 Gas Sensor', '#059669', '#ffffff'),
    ('gpt35', 'GPT3.5 Environmental AI', '#059669', '#ffffff'),
    ('autodiscover', 'Auto Discoverable Air Quality', '#059669', '#ffffff'),
    ('ld2410c3min', 'LD2410C 3Min Build', '#059669', '#ffffff'),
    ('diyweather', 'DIY Weather Station', '#059669', '#ffffff'),
]

for name, label, bg, fg in more:
    img = make_banner(label, size=(600,300), bg=bg, fg=fg)
    save_webp(img, os.path.join(IMAGES_DIR, f'{name}.webp'))

# ESP IoT Sensors image (was not in earlier list)
img = make_banner('ESP IoT Sensors', size=(600,300), bg='#1e293b', fg='#ffffff')
save_webp(img, os.path.join(IMAGES_DIR, 'espiot.webp'))

for name, label, bg, fg in thumbs:
    img = make_banner(label, size=(600,300), bg=bg, fg=fg)
    save_webp(img, os.path.join(IMAGES_DIR, f'{name}.webp'))

# Create OG image
og = make_banner('Timothy Mwala — Embedded Systems & Edge AI', size=(1200,630), bg='#0f172a', fg='#ffffff')
save_webp(og, os.path.join(IMAGES_DIR, 'og.webp'))

print('All done.')
