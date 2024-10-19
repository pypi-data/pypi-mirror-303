import requests

class ProxyLists:
    @staticmethod
    def get_proxyscrape(protocol: str = 'http', timeout: int = 1000, country: str = 'all', ssl: str = 'all', anonymity: str = 'all'):
        """Retrieve proxies from Proxyscrape API."""
        url = f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol={protocol}&timeout={timeout}&country={country}&ssl={ssl}&anonymity={anonymity}"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return [{protocol: ip.strip()} for ip in response.text.splitlines() if ip.strip()]
        except requests.RequestException as e:
            print(f"Error fetching proxies: {e}")
            return []
