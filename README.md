![Titan Embeds!](https://titanembeds.com/static/img/titanembeds.png "Titan Embeds!")

## Automated server setup with Ansible!

A couple of notes for this repository, this is more meant for the project itself to automate and document changes to how we configure our server, but anyone who wants to host this bot on their own is welcome to use this playbook with the proper configuration changes to host this project on your own hardware!

A couple of notes on what will need to be changed:

- [titan.yml](../master/playbooks/titan.yml) will need to have the letsencrypt information changed to your preferred account information and domain
- There are several default configuration files in `/roles/setup` that will need to be changed to meet your requirements, these are [alembic.example.ini](../master/roles/setup/files/alembic.example.ini), [config.webapp.example.py](../master/roles/setup/files/config.webapp.example.py) and [config.example.py](../master/roles/setup/files/config.example.py)
- [authorized_keys](../master/roles/setup/files/authorized_keys.example), You'll need to add the public keys of whomever you want to have access to this user here before running the setup playbook, otherwise you can leave this blank and just use the root user.

The roles should be fairly straightforward to tailor to your individual needs!
