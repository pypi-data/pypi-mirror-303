"""
Pi-hole python API client.
Permit send commands to Pi-hole via http calls
"""

import requests
import urllib3
from pihole_client.types import DNSRecord

class PiholeClient:
    """
    PiholeClient class.
    Require:
        - base_url: Pi-hole instanse url
        - token: Pi-hole token
    """

    def __init__(self, base_url: str, token: str) -> None:
        urllib3.disable_warnings()
        self.session = requests.Session()
        self.base_url = base_url
        self.token = token

    def __send_get_request(self, endpoint, params=None) -> dict:
        """Basic method for sending GET requests"""
        if params is None:
            params = {}

        if self.token:
            params["auth"] = self.token

        response = requests.get(
            f"{self.base_url}/admin/api.php{endpoint}", params=params, verify=False
        )
        response.raise_for_status()
        return response.json()

    def __get_list_types(self) -> list[str]:
        """Possible values of list types"""
        return ['black', 'regex_black', 'white', 'regex_white']

    def check_updates(self) -> dict:
        """Checks for updates to the Pihole software."""
        return self.__send_get_request("?versions")

    def enable(self) -> None:
        """Enables the Pihole filtering."""
        self.__send_get_request("?enable")

    def disable(self, seconds: int = 0) -> None:
        """
        Disables the Pihole filtering.
        Require:
            - seconds: The number of seconds to disable filtering
        """
        self.__send_get_request("?disable", params={"disable": seconds})

    def get_list(self, list_type:str) -> list[dict]:
        """
        Retrieves the domains in a specified list.
        Require:
            - list_type: The type of list to retrieve see types_list
        """

        if list_type not in self.__get_list_types():
            raise ValueError(f"Invalid list type: {list_type}. Possible values: {self.__get_list_types()}.")

        response = self.__send_get_request('', params={'list': list_type, 'action': 'get_domains'})
        return response['data']
    
    def get_custom_dns(self) -> list[DNSRecord]:
        """Retrieves custom DNS entries"""
        list = self.__send_get_request('?customdns&action=get').get('data')
        result = []
        for record in list:
            result.append( DNSRecord(record) )
        return result
    
    def get_custom_dns_by_domain(self, domain:str) -> DNSRecord:
        """Retrieves custom DNS entrie by domain"""
        dns_records = self.get_custom_dns()
        for dns_record in dns_records:
            if dns_record.domain == domain:
                return dns_record.model_dump_json()
        return None
    
    def add_custom_dns(self, domain:str, ip_address:str) -> None:
        """
        Add a custom DNS entry
        Require:
            domain: The domain for the DNS entry.
            ip_address: The IP address associated with the domain.
        """
        self.__send_get_request(
            '?customdns&action=add', 
            params={
                'domain': domain,
                'ip': ip_address
            }
        )

    def delete_custom_dns(self, domain:str, ip_address:str) -> None:
        """
        Delete a custom DNS entry
        Require:
            domain: The domain for the DNS entry to delete.
            ip_address: The IP address associated with the domain to delete.
        """
        self.__send_get_request(
            '?customdns&action=delete', 
            params={
                'domain': domain,
                'ip': ip_address
            }
        )

    def get_custom_cname(self) -> list:
        """Retrieves custom CNAME entries"""
        return self.__send_get_request('?customcname&action=get').get('data')
    
    def add_custom_cname(self, domain:str, target:str) -> None:
        """
        Add a custom CNAME entry.
        Require:
            domain: The domain for the CNAME entry.
            target: The target domain for the CNAME.
        """
        self.__send_get_request(
            '?customcname&action=add', 
            params={
                'domain': domain,
                'target': target
            }
        )
    
    def delete_custom_cname(self, domain:str, target:str) -> None:
        """
        Delete a custom CNAME entry.
        Require:
            domain: The domain for the CNAME entry to delete.
            target: The target domain for the CNAME to delete.
        """
        self._send_request(
            '?customcname&action=delete', 
            params={
                'domain': domain,
                'target': target
            }
        )
