import requests
import urllib3
from npm_client.types import HeaderModel, Certificate, ProxyHost


class NginxClient:
    """
    NginxClient class.
    Require:
        - base_url: Nginx Proxy Manager WebUI url
        - login: Nginx Proxy Manager WebUI login
        - password: Nginx Proxy Manager WebUI password
    """

    def __init__(self, base_url, login, password):
        urllib3.disable_warnings()
        self.session = requests.Session()
        self.base_url = base_url
        self.__auth(login, password)

    def __auth(self, login, password):
        """
        Create session token
        Require:
            - login: Nginx Proxy Manager username
            - password: Nginx Proxy Manager password
        """
        response = self.session.post(
            f"{self.base_url}/api/tokens",
            json={"identity": login, "secret": password},
            verify=False,
        )
        data = response.json()
        self.token = data.get("token")

    def __get_headers(self) -> dict[str, str]:
        """Get headers for a request with a CSRF token"""
        header = HeaderModel(token=self.token)
        return header.model_dump(by_alias=True)

    def get_certificates(self) -> list[Certificate]:
        """Get a list of certificates"""
        response = self.session.get(
            f"{self.base_url}/api/nginx/certificates",
            headers=self.__get_headers(),
            verify=False,
        )
        response.raise_for_status()

        certificates = []
        for item in response.json():
            certificates.append(Certificate.model_validate(item))
        return certificates

    def get_certificate_by_name(self, certificate_name: str) -> Certificate:
        """Get certificate by name"""
        certificates = self.get_certificates()
        for certificate in certificates:
            if certificate.nice_name.lower() == certificate_name.lower():
                return certificate
        return None

    def get_proxy_hosts(self) -> list[ProxyHost]:
        """Get proxy hosts list"""
        response = self.session.get(
            f"{self.base_url}/api/nginx/proxy-hosts?expand=certificate",
            headers=self.__get_headers(),
            verify=False,
        )
        response.raise_for_status()
        proxy_hosts = []
        for item in response.json():
            proxy_hosts.append(ProxyHost.model_validate(item))
        return proxy_hosts

    def get_proxy_host_by_domian(self, domain: str) -> ProxyHost:
        """Get proxy host by one of the domains"""
        proxy_hosts = self.get_proxy_hosts()
        for proxy_host in proxy_hosts:
            domain_list = []
            for domain_name in proxy_host.domain_names:
                domain_list.append( domain_name.lower() )
            if domain.lower() in domain_list:
                return proxy_host

    def get_proxy_host_by_id(self, id: int) -> ProxyHost:
        """Get proxy host by its id"""
        proxy_hosts = self.get_proxy_hosts()
        for proxy_host in proxy_hosts:
            if id == proxy_host.id:
                return proxy_host

    def create_proxy_host(
        self,
        domain_names: list,
        forward_scheme: str,
        forward_host: str,
        forward_port: int,
        caching_enabled: bool,
        allow_websocket_upgrade: bool,
        ssl_forced: bool,
        certificate_id: int = None,
    ) -> None:
        """Create new proxy host"""
        body = {
            "domain_names": domain_names,
            "forward_scheme": forward_scheme,
            "forward_host": forward_host,
            "forward_port": forward_port,
            "caching_enabled": caching_enabled,
            "block_exploits": False,
            "allow_websocket_upgrade": allow_websocket_upgrade,
            "access_list_id": "0",
            "certificate_id": certificate_id,
            "ssl_forced": ssl_forced,
            "http2_support": False,
            "hsts_enabled": False,
            "hsts_subdomains": False,
            "meta": {"letsencrypt_agree": False, "dns_challenge": False},
            "advanced_config": "",
            "locations": [],
        }
        response = self.session.post(
            f"{self.base_url}/api/nginx/proxy-hosts",
            headers=self.__get_headers(),
            json=body,
            verify=False,
        )
        response.raise_for_status()

    def delete_proxy_host(self, id: str) -> None:
        """Delete proxy host"""
        response = self.session.delete(
            f"{self.base_url}/api/nginx/proxy-hosts/{id}",
            headers=self.__get_headers(),
            verify=False,
        )
        response.raise_for_status()
