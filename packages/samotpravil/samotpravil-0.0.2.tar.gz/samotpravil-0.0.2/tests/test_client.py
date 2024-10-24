import unittest
import requests
import requests_mock
from src.samotpravil.client import SamotpravilClient
from src.samotpravil.exceptions import (
    SamotpravilError,
    AuthorizationError,
    BadRequestError,
    StopListError,
    DomainNotTrustedError
)


class TestSamotpravilClient(unittest.TestCase):

    def setUp(self):
        self.client = SamotpravilClient(api_key='test_key')
        self.base_url = 'https://api.samotpravil.ru'

    @requests_mock.Mocker()
    def test_send_email_success(self, m):
        url = f"{self.base_url}/api/v2/mail/send"
        m.post(url, json={"status": "OK", "message_id": "1qBv3w-0007Ls-CS"}, status_code=200)

        response = self.client.send_email(
            email_to='test@example.com',
            subject='Test Subject',
            message_text='Test Message',
            email_from='sender@example.com'
        )

        self.assertEqual(response['status'], 'OK')
        self.assertEqual(response['message_id'], '1qBv3w-0007Ls-CS')

    @requests_mock.Mocker()
    def test_send_email_stop_list_error(self, m):
        url = f"{self.base_url}/api/v2/mail/send"
        m.post(url, json={"status": "error", "message": "550 bounced check filter"}, status_code=200)

        with self.assertRaises(StopListError):
            self.client.send_email(
                email_to='test@example.com',
                subject='Test Subject',
                message_text='Test Message',
                email_from='sender@example.com'
            )

    @requests_mock.Mocker()
    def test_send_email_domain_not_trusted_error(self, m):
        url = f"{self.base_url}/api/v2/mail/send"
        m.post(url, json={"status": "error", "message": "from domain not trusted"}, status_code=200)

        with self.assertRaises(DomainNotTrustedError):
            self.client.send_email(
                email_to='test@example.com',
                subject='Test Subject',
                message_text='Test Message',
                email_from='sender@example.com'
            )

    @requests_mock.Mocker()
    def test_send_email_authorization_error(self, m):
        url = f"{self.base_url}/api/v2/mail/send"
        m.post(url, json={"status": "error", "message": "Bad Api KEY, forbidden"}, status_code=403)

        with self.assertRaises(AuthorizationError):
            self.client.send_email(
                email_to='test@example.com',
                subject='Test Subject',
                message_text='Test Message',
                email_from='sender@example.com'
            )

    @requests_mock.Mocker()
    def test_send_email_bad_request_error(self, m):
        url = f"{self.base_url}/api/v2/mail/send"
        m.post(url, json={"status": "error", "message": "bad request"}, status_code=400)

        with self.assertRaises(BadRequestError):
            self.client.send_email(
                email_to='test@example.com',
                subject='Test Subject',
                message_text='Test Message',
                email_from='sender@example.com'
            )

    @requests_mock.Mocker()
    def test_timeout_error(self, m):
        url = f"{self.base_url}/api/v2/mail/send"
        m.post(url, exc=requests.exceptions.Timeout)

        with self.assertRaises(SamotpravilError):
            self.client.send_email(
                email_to='test@example.com',
                subject='Test Subject',
                message_text='Test Message',
                email_from='sender@example.com'
            )


if __name__ == '__main__':
    unittest.main()
