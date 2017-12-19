"""Conftest is a file recognize by pytest module, allowing us to share fixture across multiple tests."""
from sandbox_client import SandboxClient
import os
import pytest


@pytest.fixture(scope='function')
def unauth_client():
    """Create an instance of SanboxClient without authentification."""
    return SandboxClient('test app', 'ver 0.0', 'test machine')


@pytest.fixture(scope='function')
def auth_client_loggedin_with_username():
    """Create an instance of SanboxClient with authentification using username/password pair."""
    client = SandboxClient('test app', 'ver 0.0', 'test machine')
    creds = {
        'username': os.environ.get('USERNAME', ''),
        'password': os.environ.get('PASSWORD', '')
    }
    client.add_credentials(creds)
    return client


@pytest.fixture(scope='function')
def auth_client_loggedin_with_id():
    """Create an instance of SanboxClient with authentification using userID/licenseKey pair."""
    client = SandboxClient('test app', 'ver 0.0', 'test machine')
    creds = {
        'account_id': os.environ.get('ACCOUNT_ID', ''),
        'license_key': os.environ.get('LICENSE_KEY', '')
    }
    client.add_credentials(creds)
    return client


@pytest.fixture(scope='function')
def auth_client_with_5_transactions():
    """Create an instance of SandboxClient with authentication and created transaction."""
    client = SandboxClient('test app', 'ver 0.0', 'test machine')
    creds = {
        'username': os.environ.get('USERNAME', ''),
        'password': os.environ.get('PASSWORD', '')
    }
    client.add_credentials(creds)
    addresses = [
        ('Seattle', '600 5th Ave', '98104', 'WA'),
        ('Poulsbo', '200 Moe St Ne', '98370', 'WA'),
        ('Los Angeles', '1945 S Hill St', '90007', 'CA'),
        ('Chicago', '50 W Washington St', '60602', 'IL'),
        ('Irvine', '123 Main Street', '92615', 'CA')
    ]
    for city, line1, postal, region in addresses:
        tax_document = {
            'addresses': {'SingleLocation': {'city': city,
                                             'country': 'US',
                                             'line1': line1,
                                             'postalCode': postal,
                                             'region': region}},
            'commit': False,
            'companyCode': 'DEFAULT',
            'currencyCode': 'USD',
            'customerCode': 'ABC',
            'date': '2017-04-12',
            'description': 'Yarn',
            'lines': [{'amount': 100,
                      'description': 'Yarn',
                       'itemCode': 'Y0001',
                       'number': '1',
                       'quantity': 1,
                       'taxCode': 'PS081282'}],
            'purchaseOrderNo': '2017-04-12-001',
            'type': 'SalesInvoice'}
        client.create_transaction(None, tax_document)

    return client


@pytest.fixture(scope='session')
def tax_document():
    """Create a tax document dictionary."""
    return {
        'addresses': {'SingleLocation': {'city': 'Irvine',
                                         'country': 'US',
                                         'line1': '123 Main Street',
                                         'postalCode': '92615',
                                         'region': 'CA'}},
        'commit': False,
        'companyCode': 'DEFAULT',
        'currencyCode': 'USD',
        'customerCode': 'ABC',
        'date': '2017-04-12',
        'description': 'Yarn',
        'lines': [{'amount': 100,
                  'description': 'Yarn',
                   'itemCode': 'Y0001',
                   'number': '1',
                   'quantity': 1,
                   'taxCode': 'PS081282'}],
        'purchaseOrderNo': '2017-04-12-001',
        'type': 'SalesInvoice'}