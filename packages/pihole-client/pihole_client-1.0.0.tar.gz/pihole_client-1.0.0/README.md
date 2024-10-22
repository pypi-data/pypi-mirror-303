# pihole-client

Python client for Pi-hole

## Installation
```bash
pip install pihole-client
```

## Examples
### Create class
```python
from pihole_client import PiholeClient
piholeClient = PiholeClient( "PIHOLE_DOMAIN", "PIHOLE_TOKEN" )
```
where:
- PIHOLE_DOMAIN: URL of Pi-hole WebUi page
- PIHOLE_TOKEN: Token of Pi-hole WebUi

or using environment variables "PIHOLE_DOMAIN" and "PIHOLE_TOKEN":
```python
from dotenv import load_dotenv
import os
from pihole_client import PiholeClient
load_dotenv()

def main():
    piholeClient = PiholeClient( 
        os.getenv('PIHOLE_DOMAIN'), 
        os.getenv('PIHOLE_TOKEN')
    )

    resp = piholeClient.get_custom_dns()
    print(resp)
if __name__ == "__main__":
    main() 
```

## Methods
```python
# Checks for updates to the Pihole software
piholeClient.check_updates()
# Enables the Pihole filtering
piholeClient.enable()
# Disables the Pihole filtering
piholeClient.disable()
# Retrieves the domains in a specified list
piholeClient.get_list("regex_black")
# Retrieves custom DNS entries
piholeClient.get_custom_dns()
# Retrieves custom DNS entrie by domain
piholeClient.get_custom_dns_by_domain("home.homelab.lan")
# Add a custom DNS entry
piholeClient.add_custom_dns(domain="router.homelab.lan", ip_address="192.168.1.1")
# Delete a custom DNS entry
piholeClient.delete_custom_dns(domain="router.homelab.lan", ip_address="192.168.1.1")
# Retrieves custom CNAME entries
piholeClient.get_custom_cname()
# Add a custom CNAME entry
piholeClient.add_custom_cname(domain="router.homelab.lan", target="xiaomi.local")
# Delete a custom CNAME entry
piholeClient.delete_custom_cname(domain="router.homelab.lan", target="xiaomi.local")
```