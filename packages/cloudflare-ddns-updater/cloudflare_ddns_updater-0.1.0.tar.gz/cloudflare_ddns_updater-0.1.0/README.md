This script fetches the Zone ID and the dns record ID from your Cloudflare account. 
Before running this script you must login to Cloudflare and create a Token 
with the following Permissions:
- Zone - Zone - Read
- Zone - DNS - Edit
and the following Zone Resources:
- Include - Specific zone - yourdomain.xx")
You must also create an A record (whatever.yourdomain.xx)
This script only needs to be run once to setup your ddns updater