# npm-client
[![PyPI Version](https://img.shields.io/pypi/v/npm-client)](https://pypi.org/project/npm-client)

Python client for Nginx Proxy Manager

## Installation
```bash
pip install npm-client
```

## Examples
### Create class
```python
from npm_client import NginxClient
npmClient = NginxClient( "NGINX_PROXY_MANAGER_DOMAIN", "NGINX_PROXY_MANAGER_USER", "NGINX_PROXY_MANAGER_PASSWORD" )
```
where:
- NGINX_PROXY_MANAGER_DOMAIN: URL of Nginx Proxy Manager WebUi page
- NGINX_PROXY_MANAGER_USER: Token of Nginx Proxy Manager WebUi
- NGINX_PROXY_MANAGER_PASSWORD: Password of Nginx Proxy Manager WebUi

or using environment variables "NGINX_PROXY_MANAGER_DOMAIN" and "NGINX_PROXY_MANAGER_USER" and "NGINX_PROXY_MANAGER_PASSWORD":
```python
from dotenv import load_dotenv
import os
from npm_client import NginxClient
load_dotenv()

def main():
    npmClient = NginxClient( 
        base_url=os.getenv('NGINX_PROXY_MANAGER_DOMAIN'), 
        login=os.getenv('NGINX_PROXY_MANAGER_USER'),
        password=os.getenv('NGINX_PROXY_MANAGER_PASSWORD')
    )

    print( npmClient.get_proxy_host_by_id(1) )
if __name__ == "__main__":
    main() 
```

## Methods
```python
# Get a list of certificates
npmClient.get_certificates()
# Get certificate by name
npmClient.get_certificate_by_name(certificate_name="home.homelab.lan")
# Get proxy hosts list
npmClient.get_proxy_hosts()
# Get proxy host by one of the domains
npmClient.get_proxy_host_by_domian(domain="home.homelab.lan")
# Get proxy host by its id
npmClient.get_proxy_host_by_id(id=1)
# Create new proxy host
npmClient.create_proxy_host(
    domain_names=["router.homelab.lan", "router2.homelab.lan"],
    forward_scheme="http",
    forward_host="192.168.1.1",
    forward_port="8080",
    caching_enabled=True,
    allow_websocket_upgrade=True,
    ssl_forced=True,
    certificate_id=1,
)
# Delete proxy host
npmClient.delete_proxy_host(id=1)
```