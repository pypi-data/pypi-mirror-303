import re
import requests
from typing import Dict, Optional, Any
from requests.exceptions import Timeout
from .exceptions import SamotpravilError, AuthorizationError, BadRequestError, StopListError, DomainNotTrustedError


class SamotpravilClient:
    def __init__(self, api_key: str, base_url: str = 'https://api.samotpravil.ru', timeout=10):
        self.api_key = api_key
        self.base_url = base_url
        self.timeout = timeout

    def _get_headers(self) -> Dict[str, str]:
        return {
            'Authorization': self.api_key,
            'Content-Type': 'application/json'
        }

    def _handle_response(self, response: requests.Response) -> Any:
        if response.status_code == 200:
            data = response.json()
            if data.get('status').lower() == 'ok':
                return data
            elif "550 bounced check filter" in data.get('message', ''):
                raise StopListError(data.get('message'))
            elif "from domain not trusted" in data.get('message', ''):
                raise DomainNotTrustedError(data.get('message'))
            else:
                raise SamotpravilError(data.get('message'))
        elif response.status_code == 403:
            raise AuthorizationError(response.json().get('message'))
        elif response.status_code == 400:
            raise BadRequestError(response.json().get('message'))
        else:
            response.raise_for_status()

    def _post(self, endpoint: str, data: Dict[str, Any]) -> Any:
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.post(url, json=data, headers=self._get_headers(), timeout=self.timeout)
        except Timeout:
            raise SamotpravilError("Request timed out")
        return self._handle_response(response)

    def _get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Any:
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.get(url, params=params, headers=self._get_headers(), timeout=self.timeout)
        except Timeout:
            raise SamotpravilError("Request timed out")
        return self._handle_response(response)

    def _validate_email(self, email: str) -> None:
        email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
        if not email_regex.match(email):
            raise ValueError(f"Invalid email address: {email}")

    def send_email(self, email_to: str, subject: str, message_text: str, email_from: str, **kwargs: Any) -> Any:
        self._validate_email(email_to)
        self._validate_email(email_from)

        endpoint = "/api/v2/mail/send"
        data = {
            "email_to": email_to,
            "subject": subject,
            "message_text": message_text,
            "email_from": f"{kwargs.get('name_from')} <{email_from}>" if kwargs.get('name_from') else email_from,
        }
        optional_fields = ["params", "x_track_id", "track_open", "track_click", "track_domain",
                           "check_stop_list", "check_local_stop_list", "domain_for_dkim", "headers"]
        for field in optional_fields:
            if kwargs.get(field) is not None:
                data[field] = kwargs[field]
        return self._post(endpoint, data)

    def get_status(self, **kwargs: Any) -> Any:
        endpoint = "/api/v2/issue/status"
        params = {key: value for key, value in kwargs.items() if value is not None}
        return self._get(endpoint, params)

    def get_statistics(self, date_from: str, date_to: str, **kwargs: Any) -> Any:
        endpoint = "/api/v2/issue/statistics"
        params = {
            "date_from": date_from,
            "date_to": date_to,
            "limit": kwargs.get('limit', 100),
            "cursor_next": kwargs.get('cursor_next')
        }
        return self._get(endpoint, params)

    def get_non_delivery_by_date(self, date_from: str, date_to: str, **kwargs: Any) -> Any:
        endpoint = "/api/v2/blist/report/non-delivery"
        params = {
            "date_from": date_from,
            "date_to": date_to,
            "limit": kwargs.get('limit', 100),
            "cursor_next": kwargs.get('cursor_next')
        }
        return self._get(endpoint, params)

    def get_non_delivery_by_issue(self, issuen: str, **kwargs: Any) -> Any:
        endpoint = "/api/v2/issue/report/non-delivery"
        params = {
            "issuen": issuen,
            "limit": kwargs.get('limit', 100),
            "cursor_next": kwargs.get('cursor_next')
        }
        return self._get(endpoint, params)

    def get_fbl_report_by_date(self, date_from: str, date_to: str, **kwargs: Any) -> Any:
        endpoint = "/api/v2/blist/report/fbl"
        params = {
            "date_from": date_from,
            "date_to": date_to,
            "limit": kwargs.get('limit', 100),
            "cursor_next": kwargs.get('cursor_next')
        }
        return self._get(endpoint, params)

    def get_fbl_report_by_issue(self, issuen: str, **kwargs: Any) -> Any:
        endpoint = "/api/v2/issue/report/fbl"
        params = {
            "issuen": issuen,
            "limit": kwargs.get('limit', 100),
            "cursor_next": kwargs.get('cursor_next')
        }
        return self._get(endpoint, params)

    def stop_list_search(self, email: str) -> Any:
        self._validate_email(email)
        endpoint = "/api/v2/stop-list/search"
        params = {"email": email}
        return self._get(endpoint, params)

    def stop_list_add(self, email: str, domain: str) -> Any:
        self._validate_email(email)
        endpoint = "/api/v2/stop-list/add"
        data = {"email": email, "mail_from": f"info@{domain}"}
        return self._post(endpoint, data)

    def stop_list_remove(self, email: str, domain: str) -> Any:
        self._validate_email(email)
        endpoint = "/api/v2/stop-list/remove"
        data = {"email": email, "mail_from": f"info@{domain}"}
        return self._post(endpoint, data)

    def get_domains(self) -> Any:
        endpoint = "/api/v2/blist/domains"
        return self._get(endpoint)

    def domain_add(self, domain: str) -> Any:
        endpoint = "/api/v2/blist/domains/add"
        data = {"domain": domain}
        return self._post(endpoint, data)

    def domain_remove(self, domain: str) -> Any:
        endpoint = "/api/v2/blist/domains/remove"
        data = {"domain": domain}
        return self._post(endpoint, data)

    def domain_check_verification(self, domain: str) -> Any:
        endpoint = "/api/v2/blist/domains/verify"
        data = {"domain": domain}
        return self._post(endpoint, data)
