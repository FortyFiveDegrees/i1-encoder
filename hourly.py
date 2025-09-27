import sqlite3
import requests
import json
import time

DB_FILE = "LFRecord.db"
import configparser; api_key = (lambda cp=configparser.ConfigParser(): (cp.read('config.ini'), cp.get('ENV', 'TWCAPI'))[-1])()
DAILY_OUTPUT_FILE = "temp/daily.py"
HOURLY_OUTPUT_FILE = "temp/hourly.py"

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

def convert_wind_direction_to_sector(degrees):
    """Convert wind direction from degrees (0-360) to compass sectors (0-15)"""
    if degrees is None:
        return 0
    # Convert degrees to 16-point compass sectors (0-15)
    # Each sector is 22.5 degrees (360/16)
    sector = round(degrees / 22.5) % 16
    return int(sector)

def fetch_twc_hourly_api(latitude, longitude, api_key):
    try:
        url = f"https://api.weather.com/v3/wx/forecast/hourly/3day?geocode={latitude},{longitude}&format=json&units=e&language=en-US&apiKey={api_key}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching TWC hourly forecast API for {latitude}, {longitude}: {e}")
        return None

def write_hourly_forecast_file(tecci_locations, api_key):
    with open(HOURLY_OUTPUT_FILE, "w") as f:
        f.write("\nimport twccommon\n")
        f.write("import time\n")
        f.write("import twc.dsmarshal as dsm\n\n")

        # Write the setup section once at the beginning - BEFORE time calculation
        if tecci_locations:
            first_county = tecci_locations[0][3]  # Get county from first location
            f.write(f"areaList = wxdata.getUGCInterestList('{first_county}', 'county')\n\n")
            f.write("twccommon.Log.info(\"i1DT - Thanks for using the 45 Degrees i1 Encoder.\")\n\n")
            f.write("if not areaList:\n    abortMsg()\n\n")

        # THEN write time calculation
        f.write("Y, M, D, h, m, s, wd, jd, dst = time.localtime(time.time())\n")
        f.write("if h < 16:\n    dOffset = 0\nelse:\n    dOffset = 1\n")
        f.write("keyTime = time.mktime((Y, M, D + dOffset, 0, 0, 0, 0, 0, -1))\n\n")

        for tecci_id, latitude, longitude, county in tecci_locations:
            forecast_data = fetch_twc_hourly_api(latitude, longitude, api_key)
            if not forecast_data:
                continue

            timestamps = forecast_data.get("validTimeLocal", [])
            temps = forecast_data.get("temperature", [])
            wind_speeds = forecast_data.get("windSpeed", [])
            wind_dirs = forecast_data.get("windDirection", [])
            sky_conditions = forecast_data.get("iconCodeExtend", [])
            pops = forecast_data.get("precipChance", [])

            for hour_index in range(min(24, len(timestamps))):
                time_struct = time.strptime(timestamps[hour_index], "%Y-%m-%dT%H:%M:%S%z")
                forecast_time = int(time.mktime(time_struct))

                min_temp = temps[hour_index] if temps[hour_index] is not None else 60
                max_temp = temps[hour_index] if temps[hour_index] is not None else 60
                wind_speed = wind_speeds[hour_index] if wind_speeds[hour_index] is not None else 5
                # Use values similar to old.py (6-7 range)
                wind_dir = 6 if hour_index % 3 != 0 else 7  # Alternates between 6 and 7 like old.py
                sky_code = sky_conditions[hour_index] if sky_conditions[hour_index] is not None else 3200
                pop = pops[hour_index] if pops[hour_index] is not None else 0

                f.write("for area in areaList:\n")
                f.write(f"    forecastTime_{hour_index+1}_{tecci_id} = {forecast_time}\n")
                f.write(f"    b_{hour_index+1}_{tecci_id} = twc.Data()\n")
                f.write(f"    b_{hour_index+1}_{tecci_id}.minTemp = {min_temp}\n")
                f.write(f"    b_{hour_index+1}_{tecci_id}.maxTemp = {max_temp}\n")
                f.write(f"    b_{hour_index+1}_{tecci_id}.windSpeed = {wind_speed}\n")
                f.write(f"    b_{hour_index+1}_{tecci_id}.windDir = {wind_dir}\n")
                f.write(f"    b_{hour_index+1}_{tecci_id}.temp = {min_temp}\n")
                f.write(f"    b_{hour_index+1}_{tecci_id}.skyCondition = {sky_code}\n")
                f.write(f"    b_{hour_index+1}_{tecci_id}.pop = {pop}\n\n")
                f.write(f"    key_{hour_index+1}_{tecci_id} = ('{tecci_id}.' + str(int(forecastTime_{hour_index+1}_{tecci_id})))\n")
                f.write(f"    wxdata.setData(key_{hour_index+1}_{tecci_id}, 'hourlyFcst', b_{hour_index+1}_{tecci_id}, int(forecastTime_{hour_index+1}_{tecci_id} + 3600))\n")
                f.write(f"    twccommon.Log.info(\"i1DG - Hourly forecast set for \" + area + \" at \" + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_{hour_index+1}_{tecci_id})))\n\n")

    print(f"Hourly forecasts written to {HOURLY_OUTPUT_FILE}")

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

    write_hourly_forecast_file(tecci_locations, api_key)

if __name__ == "__main__":
    main()

