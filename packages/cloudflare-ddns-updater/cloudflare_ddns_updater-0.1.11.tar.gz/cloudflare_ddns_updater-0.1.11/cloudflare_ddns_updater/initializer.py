import json
import requests
import os
import sys
import subprocess
import shutil
import argparse


# If you change the following settings, config_file_path in ip_updater.py must also be updated
config_dir = '/etc/ip_updater'
config_file = 'cloudflare_config.json'
# END of section


def create_log_file():
    # Define the log file path
    log_file_path = '/var/log/ip_update.log'
    # Check if the log file exists
    if not os.path.exists(log_file_path):
        print(f"Creating log file {log_file_path}.")
        # Create the log file
        try:
            with open(log_file_path, 'w') as log_file:
                log_file.write("IP update log initiated.\n")
            # Set file permissions to ensure it's writeable (if needed)
            # os.chmod(log_file_path, 0o644)  # rw-r--r--
            print(f"Log file {log_file_path} created successfully.")
        except PermissionError:
            print(f"Permission denied. Cannot create {log_file_path}. Please run with appropriate privileges.")
            sys.exit()
    else:
        print(f"Log file is {log_file_path}.")


def check_ip_updater_exists():
    # Find the full path of 'ip-updater' command
    ip_updater_path = shutil.which('ip-updater')
    if not ip_updater_path:
        print("ip-updater command not found. Please ensure it is installed.")
        sys.exit(1)
    return ip_updater_path


def add_cron_job(interval):
    # Get the full path of ip-updater
    ip_updater_path = check_ip_updater_exists()

    # Define the cron job using the full path of ip-updater
    cron_comment = "# Cron job for Cloudflare DDNS ip-updater"
    cron_command = f"*/{interval} * * * * {ip_updater_path} >> /var/log/ip_update.log 2>&1"

    # Read the existing crontab jobs and modify as needed
    try:
        current_crontab = subprocess.check_output("crontab -l", shell=True).decode()
    except subprocess.CalledProcessError:
        current_crontab = ""

    # Check if any old cron job related to ip-updater exists
    lines = current_crontab.splitlines()
    updated_crontab = []
    cron_job_found = False

    for line in lines:
        if 'ip-updater' in line:
            print(f"Old cron job found: {line}")
            cron_job_found = True  # Mark that we found an existing job and will replace it
        else:
            updated_crontab.append(line)  # Keep lines that don't involve ip-updater

    # Add the new cron job with a comment
    if cron_job_found:
        print(f"Replacing existing cron job with new interval: {interval} minutes")
    else:
        print("Adding new cron job.")

    updated_crontab.append(cron_comment)
    updated_crontab.append(cron_command)

    # Join the crontab lines back and set the new crontab
    new_crontab = "\n".join(updated_crontab) + "\n"
    process = subprocess.Popen('crontab -', stdin=subprocess.PIPE, shell=True)
    process.communicate(input=new_crontab.encode())
    print("Cron job added/updated successfully.")


def run_setup():
    print("\nThis script fetches the Zone ID and the dns record ID from yor Cloudflare account.\n"
          "\nBefore running this script you must login to Cloudflare\n"
          "and create a Token with the following Permissions:\n"
          "Zone - Zone - Read\nZone - DNS - Edit\n"
          "and the following Zone Resources:\nInclude - Specific zone - yourdomain.xx")
    print("You must also create an A record (whatever.yourdomain.xx)")
    print("\nThis script only needs to be run once.\n"
          "After running it, you can run ip_updater (using crontab, if you wish)")
    if input("Do you have your token? y or n: ").lower() != "y":
        print("Once you have the token run this script again. see you later!")
        sys.exit()

    api_token = input("Input your Cloudflare token\n")
    dns_record = input("For what record do you want to manage dns? (for example vpn.yourdomain.com)\n")

    # Create directory for config file
    try:
        os.makedirs(config_dir, exist_ok=True)  # Create the directory if it doesn't exist
        config_file_path = os.path.join(config_dir, config_file)
    except Exception as e:
        print(f"Something went wrong! {e}")
        sys.exit()

    # Get zone id
    url = "https://api.cloudflare.com/client/v4/zones"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_token}"
    }

    try:
        response = requests.request("GET", url, headers=headers)
        r = response.json()
        zone_id = r['result'][0]['id']
        print(f"zone id is: {zone_id}")
    except Exception as e:
        print(f"Error occurred during retrieval of zone id.\n"
              f"Make sure that your token is correct\n"
              f"and that it has the correct permissions.\n{e}")
        sys.exit()

    # Get dns record id
    try:
        dns_records = f"{url}/{zone_id}/dns_records"
        response = requests.request("GET", dns_records, headers=headers)
        d = response.json()["result"]
        dns_record_id = "none"
        for i in range(len(d)):
            if d[i]["name"] == dns_record:
                dns_record_id = d[i]["id"]
                print(f'dns record id is: {dns_record_id}')
        if dns_record_id == "none":
            print(f"I could not find {dns_record} in your Zone")
            print("The A records in your Zone are:")
            for i in range(len(d)):
                if d[i]["type"] == "A":
                    print(f'  {d[i]["name"]}')
            print("Please run this script again with an existing record.")
            sys.exit()
    except Exception as e:
        print(f"Something went wrong: {e}")
        sys.exit()

    # Validate cron interval
    valid = False
    while not valid:
        cron_interval = input("how often in minutes should the script run? (Default is 2) ")
        if cron_interval == "":
            cron_interval = "2"
        if cron_interval.isnumeric() and int(cron_interval) in range(1,1441):
            print(f"script will run every {cron_interval} minutes")
            valid = True
        else:
            print("\nNo, seriously...")

    # Validate Force update interval
    valid = False
    while not valid:
        force_interval = input("After how many days would you like to force an IP update? (default is 1) ")
        print(force_interval)
        if force_interval == "":
            force_interval = "1"
        if force_interval.isnumeric() and int(force_interval) in range(1,366):
            print(f"IP address will be forced every {force_interval} days.")
            valid = True
        else:
            print("\nNo, seriously...")

    # Calculate force interval in runs
    force_after_runs = int(int(force_interval) * 1440 / int(cron_interval)) # remember, a division always creates a float. we do not want that
    force_after_runs = str(force_after_runs)

    # check_main_exists()
    create_log_file()
    add_cron_job(cron_interval)

    # Create dictionary with data
    data = {
        "ZONE_ID": zone_id,
        "DNS_RECORD_ID": dns_record_id,
        "API_TOKEN": api_token,
        "FORCE_IP": force_after_runs
    }

    # Write the data to a JSON file
    with open(config_file_path, 'w') as cf:
        json.dump(data, cf)


def main():
    parser = argparse.ArgumentParser(description="Cloudflare DDNS Updater")
    parser.add_argument('--setup', action='store_true', help="Run the setup process.")
    parser.add_argument('--cron', action='store_true', help="Update the cron job.")

    args = parser.parse_args()

    if args.setup:
        run_setup()  # Replace this with the actual setup function
    elif args.cron:
        cron_job_manage()  # This will just update the cron job
    else:
        print("Please provide either --setup or --cron.")


def cron_job_manage():
    print("Not yet active")
    return


# The following ensures that when the user runs `cloudflare-ddns-updater`, the main function will be called.
if __name__ == "__main__":
    main()
