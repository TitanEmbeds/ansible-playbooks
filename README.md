![Titan Embeds!](https://i.imgur.com/v7iqMj8.png "Titan Embeds!")

# Automated server setup with Ansible!

**The current version of this build is optimized for Ubuntu 18.04, please visit the Discord support server for additional support of ansible-playbooks setup/installation of Titan Embeds.**

---
## Installation Instructions

**[Local-Notice]** If you are running Titan Embeds from a local connection with Ubuntu please add `--connection=local` after `hosts` in `ansible-playbook -i hosts` Example: `ansible-playbook -i hosts --connection=local playbooks/titansetup.yml`

1. Create a bot user from https://discordapp.com/developers/applications/me. Insert the following redirect uris: `https://DOMAIN.TLD/user/callback` and `https://DOMAIN.TLD/user/dashboard`.

2. Escalate to the root user: `sudo su`

3. Run `sudo apt-get upgrade` after that finishes run `sudo apt-get update`

4. Run `sudo apt-get install postgresql postgresql-contrib` following that run `update-rc.d postgresql enable` and then following that run `sudo service postgresql start`

5. Run `sudo -u postgres createuser titan` then `sudo -u postgres createdb titanembeds` following that `sudo -u postgres psql` after a window pops up run `alter user titan with encrypted password '<password>;'` then lastly run `grant all privileges on database titanembeds to titan ;` to exit postgresql run `\q`.

6. Install a few prerequisites: `sudo apt install ansible git python3-psycopg2`.

7. Git clone this repository into the home directory of root.

8. `cd /root/ansible-playbooks/roles/setup/files` and create your configuration files, replacing all the `.example.` with their counterparts. For example, `config.example.py` becomes `config.py` in the same directory. Ansible will move those files to the correct directory during installation.

9. Modify the following files to your likings:
    - `authorized_keys` - Adding any keys you would like to add to work for the `titan` user
    - `config.py` - This is the configuration for the Titan discordbot. Add in your bot token. Keep `database-uri` as is for now.
    - `config.webapp.py` - This is the configuation for the flask webapp. Enter the information for the Discord's app `client-id`, `client-secret`, and `bot-token`. Enter your paypal `client-id` and `client-secret` if you have one. Type something random for `app-secret`.
    - `alembic.ini` - This is the database setup file. We will modify this file later.
    - `titan_nginx` - Modify the `server_name` to the domain and tld of yours and modify `ssl_certificate_key /etc/letsencrypt/live/change_me/privkey.pem;` field change_me to your domain including the publickey.
    - `/playbooks/titan.yml` - Modify `letsencrypt_email` to your e-mail and `letsencrypt_cert_domains` to your domain.
    - `/ansible-playbooks` and modify `hosts` file with your domain, replacing `change_me`.

10. Enable the letsencrypt task by changing the directory to `ansible-playbooks/roles/ansible-letsencrypt` and run `git submodule init` and `git submodule update --recursive --remote`

11. Now you may let ansible setup the server. Run `ansible-playbook -i hosts playbooks/titansetup.yml` in the directory `ansible-playbooks`. (Please see section Local-Notice above if this is relevant)

12. Start the redis server `sudo systemctl start redis`

13. Make sure the Titan directory is owned by the `titan` user. `sudo chown -R titan:www-data /home/titan/Titan/`

14. Switch user to titan `sudo su titan` and edit your database connections in the config files inside `/home/titan/Titan`: `webapp/alembic.ini`, `webapp/config.py`, `discordbot/config.py` to `postgresql+psycopg2://titan:DatabasePASSWORDHere@localhost:5432/titanembeds?client_encoding=utf8`.

15. Exit titan user `exit` and run the upgrade tasks `cd /root/ansible-playbooks; ansible-playbook -i hosts playbooks/titan.yml --tags "web,bot";`. (Please see section Local-Notice above if this is relevant)

16. Done!
