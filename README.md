![Titan Embeds!](https://i.imgur.com/v7iqMj8.png "Titan Embeds!")

# Automated server setup with Ansible!

**The current version of this build is optimized for Ubuntu 16.04, please visit the Discord support server for additional support of ansible-playbooks setup/installation of Titan Embeds.**

---
## Installation Instructions

If you are running Titan Embeds from a local connection with Ubuntu please add `--connection=local` after `hosts` in `ansible-playbook -i hosts` Example: `ansible-playbook -i hosts --connection=local playbooks/titansetup.yml`

1. Create a bot user from https://discordapp.com/developers/applications/me. Insert the following redirect uris: `https://DOMAIN.TLD/user/callback` and `https://DOMAIN.TLD/user/dashboard`.
2. Escalate to the root user: `sudo su`
3. Install a few prerequisites: `apt install ansible git python-psycopg2`.
4. Git clone this repository into the home directory of root.
5. `cd /root/ansible-playbooks/roles/setup/files` and create your configuration files, replacing all the `.example.` with their counterparts. For example, `config.example.py` becomes `config.py` in the same directory. Ansible will move those files to the correct directory during installation.
6. Modify the following files to your likings:
    - `authorized_keys` - Adding any keys you would like to add to work for the `titan` user
    - `config.py` - This is the configuration for the Titan discordbot. Add in your bot token. Keep `database-uri` as is for now.
    - `config.webapp.py` - This is the configuation for the flask webapp. Enter the information for the Discord's app `client-id`, `client-secret`, and `bot-token`. Enter your paypal `client-id` and `client-secret` if you have one. Type something random for `app-secret`.
    - `titan_nginx` - Modify the `server_name` to the domain and tld of yours.
    - `/playbooks/titan.yml` - Modify `letsencrypt_email` to your e-mail and `letsencrypt_cert_domains` to your domain.
7. `cd /root/ansible-playbooks` and modify `hosts` file with your domain, replacing `titanembeds.com`.
8. Enable the letsencrypt task by changing the directory to `ansible-playbooks/roles/ansible-letsencrypt` and run `git submodule init` and `git submodule update --recursive --remote`
9. Now you may let ansible setup the server. Run `ansible-playbook -i hosts playbooks/titansetup.yml` in the directory `ansible-playbooks`.
10. Start the redis server `sudo systemctl start redis`
11. Make sure the Titan directory is owned by the titan user. `sudo chown -R titan:www-data /home/titan/Titan/`
13. Switch user to titan `sudo su titan` and edit your database connections in the config files inside `/home/titan/Titan`: `webapp/alembic.ini`, `webapp/config.py`, `discordbot/config.py` to `postgresql+psycopg2://titan:DatabasePASSWORDHere@localhost:5432/titanembeds?client_encoding=utf8`.
14. Exit titan user `exit` and run the upgrade tasks `cd /root/ansible-playbooks; ansible-playbook -i hosts playbooks/titan.yml --tags "web,bot";`.
15. Congratulations, if everything went well, you have successfully setup Titan Embeds on your own server!
A couple of notes for this repository, this is more meant for the project itself to automate and document changes to how we configure our server, but anyone who wants to host this bot on their own is welcome to use this playbook with the proper configuration changes to host this project on your own hardware!
