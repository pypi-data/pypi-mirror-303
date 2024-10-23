This script fetches the Zone ID and the dns record ID from your Cloudflare account. 
Before running this script you must login to Cloudflare and create a Token 
with the following Permissions:
- Zone - Zone - Read
- Zone - DNS - Edit
and the following Zone Resources:
- Include - Specific zone - yourdomain.xx")
You must also create an A record (whatever.yourdomain.xx)
This script only needs to be run once to setup your ddns updater

Changes:
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