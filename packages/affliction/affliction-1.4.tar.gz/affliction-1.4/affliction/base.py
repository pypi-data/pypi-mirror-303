from time import time
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class MicrosoftApiException(Exception):
    def __init__(self, json_data, *args) -> None:
        super().__init__(*args)
        self.data = json_data


class SynchronousMicrosoftApiClient:
    def __init__(
            self,
            tenant_id,
            client_id=None,
            client_secret=None,
            creds=None,
            scope='openid',
            base_url=None):
        from azure.identity import ClientSecretCredential
        self.creds = creds
        self.client_id = client_id
        self.client_secret = client_secret
        self.tenant_id = tenant_id
        if not creds and client_id and client_secret and tenant_id:
            self.creds = ClientSecretCredential(
                tenant_id,
                client_id,
                client_secret)
        self.scope = scope
        self.token_url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token'
        self.base_url = base_url

        # Create a session with retry mechanism
        self.session = requests.Session()
        self.token = None
        retries = Retry(
            total=5,
            backoff_factor=0.1,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["HEAD", "GET", "OPTIONS", "POST"]
        )
        self.session.mount("https://", HTTPAdapter(max_retries=retries))

        # Fetch the access token
        self.fetch_access_token()

    def fetch_access_token(self):
        self.token = self.creds.get_token(self.scope)
        self.session.headers.update({
            'Authorization': f'Bearer {self.token.token}',
            'Content-Type': 'application/json',
        })

    def adjust_headers_for_odata(self, params, headers):
        if params:
            has_search = '$search' in params
            has_count = (params.get('$count') or '').lower() == 'true'
            filter_param = (params.get('$filter') or '').lower()
            has_contains = 'contains' in filter_param
            has_endswith = 'endswith' in filter_param
            has_startswith = 'startswith' in filter_param
            if has_search or has_count or has_contains or has_endswith or has_startswith:
                headers = headers or {}
                headers['ConsistencyLevel'] = 'eventual'
        return headers

    def get(self, url, params=None, headers=None, token_retry=False, **kwargs):
        raw = kwargs.pop('raw', False)
        if self.token.expires_on - time() < 5:  # pragma: no cover
            self.fetch_access_token()
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        if raw:
            return response
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401 and not token_retry:  # pragma: no cover
            self.fetch_access_token()
            return self.get(
                url,
                params,
                headers=headers,
                token_retry=True,
                raw=raw,
                **kwargs)
        raise MicrosoftApiException(response.json(), "request failure: " + response.text)  # pragma: no cover

    def post(self, url, params=None, headers=None, token_retry=False, **kwargs):
        raw = kwargs.pop('raw', False)
        if self.token.expires_on - time() < 5:  # pragma: no cover
            self.fetch_access_token()
        response = self.session.post(url, params=params, headers=headers, **kwargs)
        if raw:
            return response
        if 200 <= response.status_code < 300:
            return response.json()
        if response.status_code == 401 and not token_retry:  # pragma: no cover
            self.fetch_access_token()
            return self.post(
                url,
                params,
                headers=headers,
                raw=raw,
                token_retry=True,
                **kwargs)
        raise MicrosoftApiException(
            response.json(),
            f'request failure: {response.text}')  # pragma: no cover

    def patch(self, url, params=None, headers=None, token_retry=False, **kwargs):
        raw = kwargs.pop('raw', False)
        if self.token.expires_on - time() < 5:  # pragma: no cover
            self.fetch_access_token()
        response = self.session.patch(url, params=params, headers=headers, **kwargs)
        if raw:
            return response
        if 200 <= response.status_code < 300:
            return response.json()
        if response.status_code == 401 and not token_retry:  # pragma: no cover
            self.fetch_access_token()
            return self.patch(
                url,
                params,
                headers=headers,
                token_retry=True,
                raw=raw,
                **kwargs)
        raise MicrosoftApiException(
            response.json(),
            f'request failure: {response.text}')  # pragma: no cover

    def delete(self, url, params=None, headers=None, token_retry=False, **kwargs):
        raw = kwargs.pop('raw', False)
        if self.token.expires_on - time() < 5:  # pragma: no cover
            self.fetch_access_token()
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        if raw:
            return response
        if 200 <= response.status_code < 300:
            if response.text:  # pragma: no cover
                return response.json()
            return None  # pragma: no cover
        if response.status_code == 401 and not token_retry:  # pragma: no cover
            self.fetch_access_token()
            return self.delete(url, params, token_retry=True)
        raise MicrosoftApiException(response.json(), "request failure: " + response.text)  # pragma: no cover

    def put(self, url, params=None, json_data=None, headers=None, token_retry=False, **kwargs):
        raw = kwargs.pop('raw', False)
        if self.token.expires_on - time() < 5:  # pragma: no cover
            self.fetch_access_token()
        response = self.session.put(
            url, params=params, headers=headers,
            json=json_data, **kwargs)
        if raw:
            return response
        if 200 <= response.status_code < 300:
            if response.text:  # pragma: no cover
                return response.json()
            return None  # pragma: no cover
        if response.status_code == 401 and not token_retry:  # pragma: no cover
            self.fetch_access_token()
            return self.put(
                url, params,
                json_data=json_data,
                headers=headers,
                token_retry=True,
                raw=raw,
                **kwargs)
        raise MicrosoftApiException(response.json(), f'request failure: {response.text}')  # pragma: no cover

    def yield_result(self, url, params=None, **kwargs):
        endpoint = url
        while endpoint:
            result = self.get(endpoint, params=params, **kwargs)
            yield from result.get('value', [])
            endpoint = result.get('@odata.nextLink')
            params = None
