# Imports
import requests
import time
from datetime import datetime
import os
import shutil

# Define the output directory
OUTPUT_DIR = "bulletins"

# this whole thing will break the second 2038 roles around, but not my problem :P
# by the time that happens i'm sure everyone will have moved onto some i2jr to i1 thing
def epoch_calc(NWS_TIME): 
    """Converts NWS time string to an epoch timestamp."""
    format_string = "%Y-%m-%dT%H:%M:%S%z"
    dt_object = datetime.strptime(NWS_TIME, format_string)
    epoch_time = int(dt_object.timestamp()) # convert from float to int
    return epoch_time


def gen_bulletin():
    """
    Fetches active weather alerts from the NWS API, wipes the 'bulletins' directory,
    and writes each alert into a separate file in that directory.
    """
    # get all us warnings
    user_agent = requests.utils.default_user_agent()
    headers = {'User-Agent': f'{user_agent} (i1-encoder, github.com/FortyFiveDegrees/i1-encoder)'}
    try:
        response = requests.get("https://api.weather.gov/alerts/active", headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        warning_json = response.json()
        warning_json = warning_json.get('features', []) # filter to just alerts
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return
    except ValueError:
        print("Error decoding JSON from API response.")
        return

    # Wipe and recreate the output directory to ensure it's clean
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR)
    
    print(f"Writing bulletins to '{OUTPUT_DIR}' directory...")
    
    # Process each alert and write it to a separate file
    for i, alert in enumerate(warning_json):
        # get needed data
        data = alert.get('properties', {})
        try:
            txt = data['description'].replace('\n', ' ') # remove new lines and replace with space
            effect_time = epoch_calc(data['effective'])
            finish_time = epoch_calc(data['expires'])
            geocode = data['geocode']['UGC'][0] # pretty sure this is right..
            pil = data['eventCode']['NationalWeatherService'][0]
        except (KeyError, TypeError, IndexError) as e:
            # skip current alert if improper data
            # this happens with the "please ignore" test alerts, as they don't have any geocoding
            print(f"Skipping Invalid Bulletin (missing data: {e})")
            continue

        # Define a unique filename for this specific alert
        file_name = f"BULLETIN_{effect_time}.py"
        file_path = os.path.join(OUTPUT_DIR, file_name)

        # Write the alert content to its own file
        with open(file_path, "w") as f:
            f.write("# ALERT\nimport time\nimport twccommon\n\n")
            f.write(f"areaList = wxdata.getBulletinInterestList('{geocode}')\n") # geocode
            f.write("if ('KABR' == 'KWNS'):\n   abortMsg()\nif (not areaList):\n    abortMsg()\n\n")
            f.write(f'twccommon.Log.info("i1DT - SET BULLETIN FOR {geocode}")\n') # logging
            f.write(f"areaList = wxdata.getBulletinInterestList('{geocode}')\n") # geocode again
            f.write('group = """"""\n')
            f.write(f'txt = """{txt}"""\n\n') # the actual alert text
            f.write("for area in areaList:\n  b = twc.Data()\n")
            f.write(f"  b.pil = '{pil}'\n  b.pilExt = '001'\n") # alert type
            f.write(f"  b.issueTime = {effect_time}\n") # issue time
            f.write(f"  b.dispExpiration = {finish_time}\n") # expire time
            f.write(f"  b.group = group\n  b.text = txt\n")
            f.write(f"  exp = {finish_time}\n") # expire time again
            f.write(f"  wxdata.setBulletin(area, b, exp)\n")

    print(f"Finished. Generated {len(os.listdir(OUTPUT_DIR))} bulletin files.")

if __name__ == "__main__":
    gen_bulletin()
