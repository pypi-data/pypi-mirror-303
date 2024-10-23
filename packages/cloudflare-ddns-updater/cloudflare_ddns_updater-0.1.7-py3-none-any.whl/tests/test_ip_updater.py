def add_cron_job(interval):
    # Define the cron job using the entry point command for ip_updater
    cron_command = f"*/{interval} * * * * ip-updater >> /var/log/ip_update.log 2>&1"

    # Read the existing crontab jobs and modify as needed
    try:
        current_crontab = subprocess.check_output("crontab -l", shell=True).decode()
    except subprocess.CalledProcessError:
        current_crontab = ""

    # Check if the job already exists in the crontab
    if cron_command not in current_crontab:
        new_crontab = current_crontab + "\n" + cron_command + "\n"
        process = subprocess.Popen('crontab -', stdin=subprocess.PIPE, shell=True)
        process.communicate(input=new_crontab.encode())
        logging.info("Cron job added.")
    else:
        logging.info("Cron job already exists.")