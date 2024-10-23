This script fetches the Zone ID and the dns record ID from your Cloudflare account. 
Before running this script you must login to Cloudflare and create a Token 
with the following Permissions:
- Zone - Zone - Read
- Zone - DNS - Edit
and the following Zone Resources:
- Include - Specific zone - yourdomain.xxx")
You must also create an A record (xxx.yourdomain.xxx)
This script only needs to be run once to setup your ddns updater.

I created this script so that I could run it in a dedicated VM or CT in Proxmox,
so I have only ever run it as root.
The Cloudflare token is saved in clear in a json file that is readable by everyone, 
so whoever has access to the machine will be able to see the token.
In my setup, it is in a container with only root as user, so it is not a problem, 
but if your setup is different, please consider this security aspect.


To install this script on recent Linux systems you probably need pipx. 
On older systems you can use pip.
I am assuming you are root, otherwise use `sudo` as necessary.

On Debian or Ubuntu
- `apt install pipx`
On Alpine Linux
- `apk add pipx`


Once installed:
- `pipx ensurepath`
- Logout and login again (or reboot)
- `pipx install cloudflare-ddns-updater`

To setup the program
- `cloudflare-ddns-updater --setup`
To check the logs
- `cat /var/log/ip_update.log`
or 
- `tail -f /var/log/ip_update.log` if you want to follow in realtime

To uninstall
- `pipx uninstall cloudflare-ddns-updater`
To completely remove all files
- `rm /tmp/ counter.txt`
- `rm/tmp/current_ip.txt`
- `rm -r /etc/ip_updater`
- `crontab -e` and remove the line regarding ip-updater and the comment line



TODO
- --cron to change ip check frequency and force ip frequency
- --stop to stop ip checks (by deleting the cron job?)
- --resume to resume ip checks as with previous cron job
- --cleanup to completely remove created files and directories.
- Try an installation not as root
- Install as unique user and lockdown privileges

Changes:
0.1.12
- warn user to run initializer script before ip-updater
0.1.11
- also removes the comment line when changing cron job
- added --setup to run initializer script
- added --cron to change only update intervals (still only placeholder)
0.1.10
- changed behaviour in case of existing cron job
0.1.9
- bug fixes
0.1.8
- defined full path of ip-updater in crontab
0.1.7
- bug fixes
0.1.6
- bugs corrected
0.1.5
- stopped checking for presence of main script
0.1.4
- Controlled where main script is installed
0.1.3
- Changed directory back to original
0.1.2
- Corrected bugs
0.1.1: 
- Changed directory for json and log file to see if compatible with Debian 12