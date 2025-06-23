import sqlite3
import requests
import json
import time

OUTPUT_FILE = "temp/daily.py"
DB_FILE = "LFRecord.db"
api_key = "e1f10a1e78da46f5b10a1e78da96f525"

def load_config():
    try:
        with open("config.json", "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading config.json: {e}")
        return None

def fetch_tecci_coordinates(tecci_locations):
    coords = []
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        for tecci_id in tecci_locations:
            cursor.execute("SELECT coopId, lat, long, cntyId FROM LFRecord WHERE coopId = ?", (tecci_id,))
            record = cursor.fetchone()
            if record:
                coords.append(record)
            else:
                print(f"Tecci ID {tecci_id} not found in LFRecord DB.")
        conn.close()
        return coords
    except Exception as e:
        print(f"Error querying LFRecord DB: {e}")
        return []

def fetch_twc_daily_api(latitude, longitude, api_key):
    try:
        url = f"https://api.weather.com/v3/wx/forecast/daily/10day?geocode={latitude},{longitude}&format=json&units=e&language=en-US&apiKey={api_key}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching TWC daily forecast API for {latitude}, {longitude}: {e}")
        return None

def write_daily_forecast_file(tecci_locations, api_key):
    with open(OUTPUT_FILE, "w") as f:
        f.write("\nimport twccommon\n")
        f.write("import time\n")
        f.write("import twc.dsmarshal as dsm\n\n")

        # Write the setup section once at the beginning - BEFORE time calculation
        if tecci_locations:
            first_county = tecci_locations[0][3]  # Get county from first location
            f.write(f"areaList = wxdata.getUGCInterestList('{first_county}', 'county')\n\n")
            f.write("twccommon.Log.info(\"i1DT - You are receiving IntelliStar 1 data from Rainwater WX.\")\n\n")
            f.write("if not areaList:\n    abortMsg()\n\n")

        # THEN write time calculation
        f.write("Y, M, D, h, m, s, wd, jd, dst = time.localtime(time.time())\n")
        f.write("if h < 16:\n    dOffset = 0\nelse:\n    dOffset = 1\n")
        f.write("keyTime = time.mktime((Y, M, D + dOffset, 0, 0, 0, 0, 0, -1))\n\n")

        for tecci_id, latitude, longitude, county in tecci_locations:
            forecast_data = fetch_twc_daily_api(latitude, longitude, api_key)
            print(forecast_data)
            if not forecast_data or "daypart" not in forecast_data:
                break

            for day in range(8):
                day_key = f"daypart"
                day_part = forecast_data.get("daypart", {})
                # Calculate data index using the current hour
                current_hour = time.localtime().tm_hour
                # Set offset if time is between 12 AM - 4 AM OR after 4 PM
                current_offset = 1 if (current_hour >= 16 or current_hour < 4) else 0
                
                # For high temp and day icon, use offset during early morning and evening hours
                day_data_index = day + current_offset
                # For low temp and night icon, always use current day
                night_data_index = day
                
                high_temp = forecast_data.get("temperatureMax", [None]*9)[day_data_index] or 70
                low_temp = forecast_data.get("temperatureMin", [None]*9)[night_data_index] or 55
                day_icon = forecast_data.get("daypart", {})[0].get("iconCodeExtend", [3200]*18)[day_data_index*2] or 3200
                night_icon = forecast_data.get("daypart", {})[0].get("iconCodeExtend", [3200]*18)[night_data_index*2+1] or 3100

                f.write("for area in areaList:\n")
                f.write(f"    forecastTime_{day+1} = keyTime + ({day} * 86400)\n")
                f.write(f"    b_{day+1} = twc.Data()\n")
                f.write(f"    b_{day+1}.highTemp = {high_temp}\n")
                f.write(f"    b_{day+1}.lowTemp = {low_temp}\n")
                f.write(f"    b_{day+1}.daySkyCondition = {day_icon}\n")
                f.write(f"    b_{day+1}.eveningSkyCondition = {night_icon}\n")
                f.write(f"    wxdata.setData(('{tecci_id}.' + str(int(forecastTime_{day+1}))), 'dailyFcst', b_{day+1}, int(forecastTime_{day+1} + 86400))\n")
                f.write(f"    twccommon.Log.info(\"i1DG - Daily forecast set for \" + area + \" at \" + str(forecastTime_{day+1}))\n\n")

    print(f"Daily forecasts written to {OUTPUT_FILE}")

def main():
    config = load_config()
    if not config:
        return

    tecci_ids = config.get("coop", {}).get("locations", [])
    if not tecci_ids:
        print("No tecci locations found in config.json.")
        return

    tecci_locations = fetch_tecci_coordinates(tecci_ids)
    if not tecci_locations:
        print("No matching tecci locations found in LFRecord DB.")
        return

    write_daily_forecast_file(tecci_locations, api_key)

if __name__ == "__main__":
    main()
