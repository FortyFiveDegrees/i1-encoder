# this should really be done with TWC API...OH WELL!

# Imports
import os
import time
import re
from PIL import Image
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup


def get_radar():
    # clear out old radar frames
    output_folder = "radar"
    for item in os.listdir(output_folder):
        item_path = os.path.join(output_folder, item)
        if os.path.isfile(item_path):
            os.remove(item_path)

    # sort and get all n0r frames
    base_url = "https://mesonet.agron.iastate.edu/data/gis/images/4326/USCOMP/"
    user_agent = requests.utils.default_user_agent()
    headers = {'User-Agent': f'{user_agent} (i1-encoder, github.com/FortyFiveDegrees/i1-encoder)'}

    html = requests.get("https://mesonet.agron.iastate.edu/data/gis/images/4326/USCOMP/", headers=headers)
    html.raise_for_status()

    soup = BeautifulSoup(html.text, "html.parser")
    png_links = [
        tag.get("href") for tag in soup.find_all("a", href=True)
        if re.match(r"n0r_\d+\.png", tag.get("href"))
    ]

    # download frames
    for filename in png_links:
        full_url = urljoin(base_url, filename)
        out_path = os.path.join(output_folder, filename)
        r = requests.get(full_url, headers=headers); r.raise_for_status()
        with open(out_path, "wb") as f:
            f.write(r.content)

    # timestamp generation
    expire_stamp = int(time.time()) + 5 * 60
    current_timestamp = int(time.time())
    for filename in os.listdir(output_folder):
        match = re.match(r"n0r_(\d+)\.png", filename)
        if match:
            minutes = int(match.group(1))
            new_timestamp = current_timestamp - (minutes * 60)
            new_name = f"{new_timestamp}.{expire_stamp}.png"
            old_path = os.path.join(output_folder, filename)
            new_path = os.path.join(output_folder, new_name)
            os.rename(old_path, new_path)

    # PNG to TIF
    for file in os.listdir(output_folder):
        if file.lower().endswith(".png"):
            png_path = os.path.join(output_folder, file)
            tif_path = os.path.join(output_folder, os.path.splitext(file)[0] + ".tif")
            
            with Image.open(png_path) as img:
                img.save(tif_path, format="TIFF")

    # Delete PNGs
    for fname in os.listdir(output_folder):
        if fname.lower().endswith(".png"):
            path = os.path.join(output_folder, fname)
            try:
                os.remove(path)
            except Exception as e:
                print(f"Could not remove {path}: {e}")