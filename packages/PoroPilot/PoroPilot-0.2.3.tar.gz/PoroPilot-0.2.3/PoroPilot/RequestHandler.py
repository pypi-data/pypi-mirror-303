import requests, requests_cache, time
from requests.exceptions import HTTPError
import logging
from urllib.parse import urlencode

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

MAX_RETRIES = 3
CACHE_NAME = 'riot_api_cache'
EXPIRE_AFTER = 3600
ERROR_TIME_SLEEP = 3
logging.basicConfig(level=logging.INFO)

REGION_TO_PLATFORM = {
    'eun1': 'europe',
    'euw1': 'europe',
    'tr1': 'europe',
    'ru': 'europe',
    'jp1': 'asia',
    'kr': 'asia',
    'br1': 'americas',
    'la1': 'americas',
    'la2': 'americas',
    'na1': 'americas',
    'oc1': 'americas'
}


class RequestHandler:
    def __init__(self, api_key, region, use_platform, expire_after=3600, max_retries=3):
        self.api_key = api_key
        self.region = region
        self.use_platform = use_platform
        self.expire_after = expire_after
        self.max_retries = max_retries
        self.session = requests.Session()
        self.set_cache(expire_after)

        self.retries = 0
    
    def set_cache(self, expire_after, cache_name='riot_api_cache'):
        requests_cache.install_cache(cache_name, expire_after=expire_after)

    def build(self, region, endpoint, query_params=None):
        domain = REGION_TO_PLATFORM[region] if self.use_platform else region
        base_url = f"https://{domain}.api.riotgames.com{endpoint}"
        
        return base_url if not query_params else f'{base_url}?{urlencode(query_params)}'

    def make_request(self, endpoint, query_params=None):
        self.retries = 0
        url = self.build(self.region, endpoint, query_params)
        headers = {'X-Riot-Token': self.api_key}

        while self.retries < self.max_retries:
            try:
                response = self.session.get(url, headers=headers)
                response.raise_for_status()

                return response.json()
            except requests.exceptions.RequestException as e:
                RequestHandler.handle_error(e)
                self.retries += 1
                logging.info(f"Retrying request {self.retries}/{self.max_retries}")

    def handle_error(exception):
        if isinstance(exception, requests.exceptions.ConnectionError):
            logging.info("Unable to connect to the server:", str(exception))
        elif isinstance(exception, requests.exceptions.HTTPError):
            logging.info("HTTP error occurred:", str(exception))

            if exception.response.status_code == 429:
                retry_after = exception.response.headers['Retry-After']
                logging.info(f"Waiting {retry_after} seconds before retrying...")
                
                time.sleep(int(retry_after))
        else:
            logging.info("An unexpected error occurred:", str(exception))
