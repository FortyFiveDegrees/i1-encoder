# Imports
import requests
import time
from datetime import datetime

OUTPUT_FILE = "temp/bulletin.py"

# this whole thing will break the second 2038 roles around, but not my problem :P
# by the time that happens i'm sure everyone will have moved onto some i2jr to i1 thing
def epoch_calc(NWS_TIME): 
    format_string = "%Y-%m-%dT%H:%M:%S%z"
    dt_object = datetime.strptime(NWS_TIME, format_string)
    epoch_time = dt_object.timestamp()
    epoch_time = int(epoch_time) # convert from float to int
    return epoch_time


def gen_bulletin():
    # get all us warnings
    headers = {'User-Agent': 'python-requests/2.32.4 (i1-encoder, github.com/FortyFiveDegrees/i1-encoder)'}
    warning_json = requests.get("https://api.weather.gov/alerts/active", headers=headers); warning_json = warning_json.json()
    warning_json = warning_json['features'] # filter to just alerts

    # actually do the crap
    with open(OUTPUT_FILE, "w") as f:
        f.truncate(0) # delete everything in the file to be safe
        
        for alert in warning_json:
            # get needed data
            data = alert['properties']
            try:
                txt = data['description']; txt = txt.replace('\n', ' ') # remove new lines and replace with space
                effect_time = epoch_calc(data['effective'])
                finish_time = epoch_calc(data['expires'])
                geocode = data['geocode']['UGC'][0] # pretty sure this is right..
                pil = data['eventCode']['NationalWeatherService'][0]
            except:
                # skip current alert if improper data
                # this happens with the "please ignore" test alerts, as they don't have any geocoding
                print("i1DT - Skipping Invalid Bulletin")
                continue

            # write to file
            f.write("# ALERT\nimport time\nimport twccommon\n")
            f.write(f"areaList = wxdata.getBulletinInterestList('{geocode}')\n") # geocode
            f.write("if ('KABR' == 'KWNS'):\n   abortMsg()\nif (not areaList):\n    abortMsg()")
            f.write("\n\n\n"); f.write(f'twccommon.Log.info("i1DT - SET BULLETIN FOR {geocode}")\n') # logging
            f.write(f"areaList = wxdata.getBulletinInterestList('{geocode}')\n") # geocode again
            f.write('group = """"""\n'); f.write(f'txt = """{txt}"""\n') # the actual alert text
            f.write("for area in areaList:\n  b = twc.Data()\n")
            f.write(f"  b.pil = '{pil}'\n  b.pilExt = '001'\n") # alert type
            f.write(f"  b.issueTime = {effect_time}\n\n") # issue time
            f.write(f"  b.dispExpiration = {finish_time}\n") # expire time
            f.write(f"  b.group = group\n  b.text = txt\n")
            f.write(f"  exp = {finish_time}\n") # expire time again