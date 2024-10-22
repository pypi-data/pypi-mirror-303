from requests import get, request
import os
import json
import logging

# Configure logging
log_file_path = '/var/log/ip_update.log'
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')


file_path = "/tmp/current_ip.txt"
counter_path = "/tmp/counter.txt"
config_file_path = '/etc/ip_updater/cloudflare_config.json'

# Load the configuration from the JSON file
try:
    with open(config_file_path) as config_file:
        config = json.load(config_file)
    ZONE_ID = config['ZONE_ID']
    DNS_RECORD_ID = config['DNS_RECORD_ID']
    API_TOKEN = config['API_TOKEN']
    RUNS = config['FORCE_IP']
    logging.info("Successfully loaded configuration.")
except Exception as e:
    logging.error(f"Failed to load configuration: {e}")
    exit(1)


def counter():
    # TODO error handling what if: c is not  numeric, is empty, is more lines
    try:
        with open(counter_path) as t:
            c = int(t.read().strip())
            if c <= 0:
                os.remove(file_path)
                c = RUNS
                logging.info(f"Scheduled forced IP update. {file_path} removed.")
            c -= 1
        with open(counter_path, 'w') as t:
            t.write(str(c))
    except FileNotFoundError:
        with open(counter_path, 'w') as t:
            t.write(RUNS)
        logging.info(f"Created new counter file with {RUNS} runs.")


# Try to read the current IP from the file
try:
    with open(file_path) as t:
        old_ip = t.read().strip()  # Strip any extra whitespace or newlines
except FileNotFoundError:
    old_ip = "none"
    with open(file_path, 'w') as t:
        t.write(old_ip)
    logging.info(f"Created new {file_path} with placeholder IP 'none'.")

# Try to get the current public IP
try:
    ip = get('https://api.ipify.org').text.strip()
    logging.info(f"Successfully retrieved current IP: {ip}")
except Exception as e:
    ip = "error"
    logging.error(f"Error occurred while fetching IP from ipify: {e}")

# Compare old IP with current IP
if ip == old_ip:
    counter()
    logging.info("No IP change detected.")
elif ip == "error":
    logging.error("Unable to retrieve the current IP")
else:
    logging.info(f"New IP detected: {ip}")

    # Cloudflare DNS update payload
    url = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records/{DNS_RECORD_ID}"
    payload = {
        "content": f"{ip}"
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_TOKEN}"
    }

    # Attempt to update Cloudflare
    try:
        response = request("PATCH", url, json=payload, headers=headers)
        response.raise_for_status()  # Raise exception for HTTP errors
        r = response.json()

        # Check if the update was successful
        if r['success']:
            cloudflare_ip = r['result']['content']
            logging.info(f"Cloudflare IP successfully updated to: {cloudflare_ip}")

            # If the IP matches, update the local file
            if cloudflare_ip == ip:
                with open(file_path, 'w') as t:
                    t.write(ip)
                logging.info(f"Updated local IP file {file_path} with IP: {ip}")
        else:
            logging.error(f"Error updating Cloudflare: {r['errors']}")

    except Exception as e:
        logging.error(f"Error occurred during Cloudflare update: {e}")



