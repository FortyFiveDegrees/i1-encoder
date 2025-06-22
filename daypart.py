import sqlite3
import requests
import json
import time

OUTPUT_FILE = "temp/daypart.py"
DB_FILE = "LFRecord.db"
api_key = "e1f10a1e78da46f5b10a1e78da96f525"

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

def fetch_tecci_coordinates(tecci_locations):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    coords = []
    for tecci_id in tecci_locations:
        cursor.execute("SELECT coopId, lat, long, cntyId FROM LFRecord WHERE coopId = ?", (tecci_id,))
        record = cursor.fetchone()
        if record:
            coords.append(record)
        else:
            print(f"TECCI ID {tecci_id} not found in DB.")
    conn.close()
    return coords

def fetch_twc_daily_api(lat, lon, api_key):
    url = f"https://api.weather.com/v3/wx/forecast/daily/10day?geocode={lat},{lon}&format=json&units=e&language=en-US&apiKey={api_key}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def write_daypart_forecast_file(tecci_locations, api_key):
    # Calculate the base time for hardcoded timestamps
    Y, M, D, h, m, s, wd, jd, dst = time.localtime(time.time())
    dOffset = 0  # Always use offset of 0
    keyTime = int(time.mktime((Y, M, D + dOffset, 5, 0, 0, 0, 0, -1)))
    
    with open(OUTPUT_FILE, "w") as f:
        f.write("\nimport twccommon\nimport time\n\n")

        num_dayparts = 4
        
        # Write the setup section once at the beginning
        if tecci_locations:
            # Try to get primary county from config, otherwise use first location
            config = load_config()
            primary_county = config.get("primaryCounty")
            
            if primary_county:
                county = primary_county
            else:
                # Look for primary TECCI ID (typically 72202019 based on config.py)
                primary_tecci = "72202019"
                primary_location = None
                for tecci_id, lat, lon, cnty in tecci_locations:
                    if tecci_id == primary_tecci:
                        primary_location = (tecci_id, lat, lon, cnty)
                        break
                
                if primary_location:
                    _, _, _, county = primary_location
                else:
                    # Fallback to first location
                    first_location = tecci_locations[0]
                    _, _, _, county = first_location
            
            f.write(f"areaList = wxdata.getUGCInterestList('{county}', 'county')\n\n")
            f.write("twccommon.Log.info(\"i1DT - Thanks for using the 45 Degrees i1 Encoder.\")\n\n")
            
            f.write("Y, M, D, h, m, s, wd, jd, dst = time.localtime(time.time())\n")
            f.write("dOffset = 0  # Always use offset of 0\n\n")
            f.write("keyTime = time.mktime((Y, M, D + dOffset, 5, 0, 0, 0, 0, -1))\n\n")
            f.write(f"numDayparts = {num_dayparts}\n\n")
            
            # Write times array
            f.write("times = [\n")
            for i in range(4):
                if i == 0:
                    f.write("    keyTime,\n")
                elif i == 3:
                    f.write(f"    keyTime + ({i * 12} * 3600)\n")
                else:
                    f.write(f"    keyTime + ({i * 12} * 3600),\n")
            f.write("]\n\n")
            f.write("\n    \n\n\n")

        # Reorder locations so primary coop ID comes first
        config = load_config()
        primary_coop = "72202019"  # Default primary coop ID
        if "primaryCoopId" in config:
            primary_coop = config["primaryCoopId"]
        
        # Sort locations with primary first
        sorted_locations = []
        primary_location = None
        other_locations = []
        
        for location in tecci_locations:
            tecci_id, lat, lon, county = location
            if tecci_id == primary_coop:
                primary_location = location
            else:
                other_locations.append(location)
        
        # Put primary location first, then others
        if primary_location:
            sorted_locations = [primary_location] + other_locations
        else:
            sorted_locations = tecci_locations
        
        for tecci_id, lat, lon, county in sorted_locations:
            data = fetch_twc_daily_api(lat, lon, api_key)
            dayparts = data.get("daypart", {})[0].get("daypartName", [])
            phrases = data.get("daypart", {})[0].get("narrative", [])
            icons = data.get("daypart", {})[0].get("iconCodeExtend", [])
            temps = data.get("daypart", {})[0].get("temperature", [])

            # Generate daypart forecasts with proper variable names
            daypart_counter = 1
            period_counter = 1
            
            for dp_index in range(len(phrases)):
                if phrases[dp_index] is None:
                    continue

                # Calculate hardcoded Unix timestamp
                validTime = keyTime + (dp_index * 12 * 3600)
                expirationTime = validTime + 43200
                
                # Determine if it's day (1) or night (2) based on daypart name
                daypart_name = dayparts[dp_index] if dp_index < len(dayparts) else ""
                if "night" in daypart_name.lower() or "tonight" in daypart_name.lower() or dp_index % 2 == 1:
                    period = 2
                else:
                    period = 1
                
                var_name = f"{daypart_counter}_{period}"
                
                # Stop after 8_2
                if daypart_counter > 8 or (daypart_counter == 8 and period == 2):
                    if daypart_counter == 8 and period == 2:
                        # Generate the final 8_2 entry
                        f.write("for area in areaList:\n")
                        f.write(f"    forecastTime_{var_name} = {validTime}\n")
                        f.write(f"    b_{var_name} = twc.Data()\n")
                        f.write(f"    \n")
                        f.write(f"    b_{var_name}.phrase = '{phrases[dp_index]}'\n")
                        f.write(f"    \n")
                        icon = icons[dp_index] if dp_index < len(icons) and icons[dp_index] is not None else 3200
                        temp = temps[dp_index] if dp_index < len(temps) and temps[dp_index] is not None else 70
                        f.write(f"    b_{var_name}.skyCondition = {icon}\n")
                        f.write(f"    b_{var_name}.temp = {temp}\n")
                        f.write(f"    # Vocal key for those trying to recreate: man nvm bruh whatever AI worked on this code did ts wrong\n")
                        f.write(f"    wxdata.setDaypartData(\n")
                        f.write(f"        loc='{tecci_id}',\n")
                        f.write(f"        type='textFcst',\n")
                        f.write(f"        data=b_{var_name},\n")
                        f.write(f"        validTime={validTime},\n")
                        f.write(f"        numDayparts={num_dayparts},\n")
                        f.write(f"        expiration=int({validTime} + 43200)\n")
                        f.write(f"    )\n")
                        f.write(f"    twccommon.Log.info(\"i1DG - Daypart forecast set for \" + area + \" at \" + str(forecastTime_{var_name}))\n")
                        f.write("                \n\n\n")
                    break
                
                f.write("for area in areaList:\n")
                f.write(f"    forecastTime_{var_name} = {validTime}\n")
                f.write(f"    b_{var_name} = twc.Data()\n")
                f.write(f"    \n")
                f.write(f"    b_{var_name}.phrase = '{phrases[dp_index]}'\n")
                f.write(f"    \n")
                icon = icons[dp_index] if dp_index < len(icons) and icons[dp_index] is not None else 3200
                temp = temps[dp_index] if dp_index < len(temps) and temps[dp_index] is not None else 70
                f.write(f"    b_{var_name}.skyCondition = {icon}\n")
                f.write(f"    b_{var_name}.temp = {temp}\n")
                f.write(f"    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02\n")
                f.write(f"    wxdata.setDaypartData(\n")
                f.write(f"        loc='{tecci_id}',\n")
                f.write(f"        type='textFcst',\n")
                f.write(f"        data=b_{var_name},\n")
                f.write(f"        validTime={validTime},\n")
                f.write(f"        numDayparts={num_dayparts},\n")
                f.write(f"        expiration=int({validTime} + 43200)\n")
                f.write(f"    )\n")
                f.write(f"    twccommon.Log.info(\"i1DG - Daypart forecast set for \" + area + \" at \" + str(forecastTime_{var_name}))\n")
                
                if period == 2:
                    f.write("                \n\n\n")
                    daypart_counter += 1
                else:
                    f.write("        \n\n\n")

    print(f"Daypart forecast written to {OUTPUT_FILE}")

def main():
    config = load_config()
    tecci_ids = config.get("coop", {}).get("locations", [])
    tecci_locations = fetch_tecci_coordinates(tecci_ids)
    write_daypart_forecast_file(tecci_locations, api_key)

if __name__ == "__main__":
    main()
