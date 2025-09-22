import paramiko
import os
import re
import json
import time
import threading
from datetime import datetime, timedelta
import asyncio
import shutil

import cc
import hourly
import daily
import daypart
import bulletin
import radar

with open("config.json", "r") as f:
    ssh_config = json.load(f).get("ssh", {})

ssh_connected = False
ssh_client = None
shell = None


def ensure_temp_dir():
    if not os.path.exists("temp"):
        os.makedirs("temp")

def ensure_radar_dir():
    if not os.path.exists("radar"):
        os.makedirs("radar")

def connect_ssh():
    global ssh_client, shell, ssh_connected
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(
        ssh_config["hostname"],
        port=ssh_config["port"],
        username=ssh_config["username"],
        password=ssh_config["password"],
        look_for_keys=False,
        allow_agent=False
    )
    ssh_connected = True
    shell = ssh_client.invoke_shell()
    print("i1DT - SSH connection established.")

    def handle_output():
        while True:
            output = shell.recv(1024).decode()
            if "Password:" in output:
                shell.send("i1\n")

    threading.Thread(target=handle_output, daemon=True).start()
    shell.send("su -l dgadmin\n")


def send_command(command):
    if not ssh_connected:
        connect_ssh()
    print(f"i1DT - Sent command: {command}")
    shell.send(command + "\n")

def sync_time():
    now = datetime.now()
    freebsd_timestamp = now.strftime("%m%d%H%M%Y.%S") # Generate current FreeBSD timestamp
    print("i1DT - Syncing Time, Timestamp is:" + freebsd_timestamp)
    send_command("date " + freebsd_timestamp) # Sync the time of the VM

def get_config():
    ensure_temp_dir()
    transport = paramiko.Transport((ssh_config["hostname"], ssh_config["port"]))
    transport.connect(username=ssh_config["username"], password=ssh_config["password"])
    sftp = paramiko.SFTPClient.from_transport(transport)

    local_path = "config.py"
    remote_path = "/usr/home/dgadmin/config/current/config.py"
    sftp.get(remote_path, local_path)
    print("i1DT - Config downloaded from i1.")
    sftp.close()
    transport.close()

    with open(local_path, "r") as f:
        config_content = f.read()

    coop_pattern = r"wxdata\.setInterestList\('coopId','1',\[(.*?)\]\)"
    coop_matches = re.findall(coop_pattern, config_content)
    locations = []
    for match in coop_matches:
        ids = [id.strip().replace("'", "").replace('"', '') for id in match.split(",") if id.strip()]
        ids = [id for id in ids if not id.startswith(("K", "W"))]
        locations.extend(ids)

    tecci_pattern = r"wxdata\.setInterestList\('obsStation','1',\[(.*?)\]\)"
    tecci_matches = re.findall(tecci_pattern, config_content)
    locations_tecci = []
    for match in tecci_matches:
        ids = [id.strip().replace("'", "").replace('"', '') for id in match.split(",") if id.strip()]
        ids = [id for id in ids if not id.startswith(("K", "W"))]
        locations_tecci.extend(ids)

    # Remove duplicates while preserving order
    def remove_duplicates_preserve_order(lst):
        seen = set()
        result = []
        for item in lst:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result
    
    config_data = {
        "ssh": ssh_config,
        "coop": {"locations": remove_duplicates_preserve_order(locations)},
        "tecci": {"locations": remove_duplicates_preserve_order(locations_tecci)}
    }

    with open("config.json", "w") as f:
        json.dump(config_data, f, indent=2)

    print("i1DT - Config parsed and config.json written.")
    return config_data

def upload_and_run_temp_files():
    ensure_temp_dir()
    transport = paramiko.Transport((ssh_config["hostname"], ssh_config["port"]))
    transport.connect(username=ssh_config["username"], password=ssh_config["password"])
    sftp = paramiko.SFTPClient.from_transport(transport)

    for file_name in os.listdir("temp"):
        local_path = os.path.join("temp", file_name)
        remote_path = f"/home/dgadmin/{file_name}"
        sftp.put(local_path, remote_path)
        print(f"i1DT - Uploaded {file_name}")

        if not ssh_connected:
            connect_ssh()

        time.sleep(0.5)
        send_command(f"runomni /twc/util/loadSCMTconfig.pyc {remote_path}")

    sftp.close()
    transport.close()

def load_bulletins():
    ensure_temp_dir()
    transport = paramiko.Transport((ssh_config["hostname"], ssh_config["port"]))
    transport.connect(username=ssh_config["username"], password=ssh_config["password"])
    sftp = paramiko.SFTPClient.from_transport(transport)

    # Clear old BULLETIN files from remote directory
    try:
        remote_files = sftp.listdir("/usr/home/dgadmin")
        bulletin_files = [f for f in remote_files if f.startswith("BULLETIN")]
        for old_file in bulletin_files:
            try:
                sftp.remove(f"/usr/home/dgadmin/{old_file}")
                print(f"i1DT - Removed old bulletin file: {old_file}")
            except Exception as e:
                print(f"i1DT - Warning: Could not remove {old_file}: {e}")
    except Exception as e:
        print(f"i1DT - Warning: Could not list remote directory: {e}")

    for file_name in os.listdir("bulletins"):
        local_path = os.path.join("bulletins", file_name)
        remote_path = f"/usr/home/dgadmin/{file_name}"
        sftp.put(local_path, remote_path)
        print(f"i1DT - Uploaded {file_name}")
        os.remove(local_path)
        if not ssh_connected:
            connect_ssh()

        time.sleep(0.5)
        send_command(f"runomni /twc/util/loadSCMTconfig.pyc {remote_path}")


    sftp.close()
    transport.close()

def load_radar():
    transport = paramiko.Transport((ssh_config["hostname"], ssh_config["port"]))
    transport.connect(username=ssh_config["username"], password=ssh_config["password"])
    sftp = paramiko.SFTPClient.from_transport(transport)

    # Clear old RADARLOAD files from remote directory
    try:
        remote_files = sftp.listdir("/usr/home/dgadmin")
        radarload_files = [f for f in remote_files if f.startswith("RADARLOAD")]
        for old_file in radarload_files:
            try:
                sftp.remove(f"/usr/home/dgadmin/{old_file}")
                print(f"i1DT - Removed old radar load file: {old_file}")
            except Exception as e:
                print(f"i1DT - Warning: Could not remove {old_file}: {e}")
    except Exception as e:
        print(f"i1DT - Warning: Could not list remote directory: {e}")

    for file_name in os.listdir("radar"): # upload radar frames
            local_path = os.path.join("radar", file_name)
            remote_path = f"/twc/data/volatile/images/radar/us/{file_name}"
            sftp.put(local_path, remote_path)
            print(f"i1DT - Radar {file_name} Uploaded")
            os.remove(local_path)

    time.sleep(0.5)

    for file_name in os.listdir("radar_temp"): # radar load script handler
            local_path = os.path.join("radar_temp", file_name)
            remote_path = f"/usr/home/dgadmin/{file_name}"
            sftp.put(local_path, remote_path)
            print(f"i1DT - Radar Load Script {file_name}")
            os.remove(local_path)
            time.sleep(0.5)
            send_command(f"runomni /twc/util/loadSCMTconfig.pyc {remote_path}")
            
    # cleanup
    shutil.rmtree("radar_temp", ignore_errors=True)

def start_schedules():
    config = get_config()
    if not config or "coop" not in config or "locations" not in config["coop"]:
        print("i1DT - Failed to load i1 config.")
        return

    def run_cc():
        while True:
            ensure_temp_dir()
            cc.main()
            upload_and_run_temp_files()
            sync_time() # run it here as sort of a heartbeat? (like how TWC sends down heartbeats to keep units in time-sync)
            time.sleep(300)

    def run_hourly_daily_daypart():
        while True:
            ensure_temp_dir()
            hourly.main()
            daily.main()
            daypart.main()
            upload_and_run_temp_files()
            time.sleep(1800)

    def radar_loop():
        # First run - send initial 36 frames
        print("i1DT - Starting initial radar sequence (36 frames)")
        time.sleep(15)
        radar.makeRadarImages()
        radar.gen_radarload_files()
        load_radar()
        print("i1DT - Initial radar sequence complete, switching to 5-minute updates")
        
        # Continuous loop - send new frame every 5 minutes
        while True:
            time.sleep(300)  # 5 minutes = 300 seconds
            print("i1DT - Updating radar with latest frame")
            radar.makeLatestRadarImage()
            radar.gen_radarload_files()
            load_radar()

    def bulletin_loop():
        while True:
            bulletin.gen_bulletin()
            load_bulletins()
            time.sleep(300)


    threading.Thread(target=run_cc, daemon=True).start()
    threading.Thread(target=run_hourly_daily_daypart, daemon=True).start()
    threading.Thread(target=bulletin_loop, daemon=True).start()
    threading.Thread(target=radar_loop, daemon=True).start()

    print("i1DT - Data generation & upload schedules started.")


if __name__ == "__main__":
    sync_time()
    start_schedules()
    while True:
        time.sleep(1)

