from setuptools import setup, find_packages

setup(
    name='samotpravil',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    url='https://samotpravil.ru/',
    license='MIT',
    author='Samotpravil',
    author_email='support@samotpravil.ru',
    description='Python client for Samotpravil SMTP API'
)
